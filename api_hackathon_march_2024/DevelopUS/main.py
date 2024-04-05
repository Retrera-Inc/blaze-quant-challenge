import discord
import re
from dotenv import load_dotenv
import os
from api import make_api_call

# Initialize Discord client
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

# Regular expression pattern for wallet address
wallet_address_pattern = r"\b0x[a-fA-F0-9]{40}\b"

# Dictionary to store API responses
responses = {}


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    # Check if the author of the message is the bot itself
    if message.author == client.user:
        return

    # Check if bot is mentioned
    if client.user.mentioned_in(message):
        responses[message.id] = []  # Initialize empty list to store responses
        await message.channel.send("I'm now listening to replies.")

    # Check if the message is a reply
    if message.reference:
        replied_message = await message.channel.fetch_message(message.reference.message_id)
        # Check if the replied message tags the bot
        if client.user in replied_message.mentions:
            # Check if the reply contains a wallet address
            wallet_address = re.search(wallet_address_pattern, message.content)
            if wallet_address:
                # Make API call with the wallet address
                data = make_api_call(message.content)
                if data is not None:
                    responses[replied_message.id].append(
                        {message.author.name: data})
                else:
                    await message.channel.send("Error occurred while fetching data from API")
        # Check for slash commands
        if message.content.startswith("/check"):
            # Split the message content into words
            words = message.content.split()
            # If there's a second word, use it as the option
            option = words[1] if len(words) > 1 else None

            if message.reference and message.reference.message_id in responses:
                # Send stored responses to the user who tagged the bot
                # Fetch the referenced message
                referenced_message = await message.channel.fetch_message(message.reference.message_id)
                # Get the author of the referenced message
                user = referenced_message.author
                if user:
                    response_list = responses[message.reference.message_id]
                    if option == "email":
                        # Fetch and send the emails
                        emails = [(name, response['data']['walletTraits']['emails'][0])
                                  for response in response_list for name, response in response.items() if response['data']['walletTraits']['emails']]
                        response_str = "\n".join(
                            [f"{name}: {email}" for name, email in emails])
                    elif option == "score":
                        # Fetch and send the scores
                        scores = [[name, response['data']['walletScores']['web3ReputationScore'], response['data']
                                   ['walletScores']['authenticityScore']] for response in response_list for name, response in response.items()]
                        response_str = "\n".join(
                            [f"{x[0]}: Web3 Reputation Score: {x[1]}, Authenticity Score: {x[2]}" for x in scores])
                    else:
                        # Send all stored responses
                        response_str = "\n".join(
                            [
                                f"**{name}**:\n" +
                                f"    Wallet Address: {response['data']['walletTraits']['walletAddress']}\n" +
                                f"    Emails: {', '.join(response['data']['walletTraits']['emails'])}\n" +
                                f"    Ethereum Token Portfolio Value: {response['data']['walletTraits']['ethereumTokenPortfolioValue']}\n" +
                                f"    Polygon Token Portfolio Value: {response['data']['walletTraits']['polygonTokenPortfolioValue']}\n" +
                                f"    NFT Portfolio Value: {response['data']['walletTraits']['nftPortfolioValue']}\n" +
                                f"    Last Transaction Date: {response['data']['walletTraits']['lastTransactionDate']}\n" +
                                f"    Web3 Reputation Score: {response['data']['walletScores']['web3ReputationScore']}\n" +
                                f"    Authenticity Score: {response['data']['walletScores']['authenticityScore']}"
                                for response in response_list for name, response in response.items()
                            ]
                        )
                    await user.send(f"Responses to your request:\n{response_str}")
                else:
                    await message.channel.send("Unable to send message to user.")
            else:
                await message.channel.send("No responses found for your message.")
        elif message.content.startswith('/stop'):
            # Fetch the referenced message
            referenced_message = await message.channel.fetch_message(message.reference.message_id)
            # Get the author of the referenced message
            user = referenced_message.author
            if message.reference and message.reference.message_id in responses and message.author.id == user.id:
                del responses[message.reference.message_id]
                await message.channel.send("Stopped monitoring this message.")
            else:
                await message.channel.send("You can't stop monitoring this message.")
        elif message.content.startswith('/help'):
            await message.channel.send(
                "Usage: \n"
                "/check - Get all responses to your tagged message.\n"
                "/check email - Get the emails from the responses to your tagged message.\n"
                "/check score - Get the scores from the responses to your tagged message.\n"
                "/stop - Stop monitoring a message."
            )


load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

# Run the bot
client.run(bot_token)
