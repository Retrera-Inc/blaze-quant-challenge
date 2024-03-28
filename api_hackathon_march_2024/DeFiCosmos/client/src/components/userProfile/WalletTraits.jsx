import React, { useState, useEffect } from 'react';
import "./wallettraits.css";

function WalletTraitsComponent(props) {
    const {walletAddress} = props;
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const apiKey = import.meta.env.VITE_API_KEY;
    const storePortfolioValue = (portfolioValues) => {
        const data = {
          userInfo: localStorage.getItem("userInfo"),
          portfolioValues: portfolioValues,
        }
        console.log(data);
        fetch("/server//api/storePortfolioValue", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        })
          .then((response) => {
            if (!response.ok) {
              throw new Error("Network response was not ok");
            }
            return response.json();
          })
          .then((data) => {
            // Handle success response
            console.log("Portfolio Values updated successfully:", data);
          })
          .catch((error) => {
            // Handle error
            console.error("There was a problem updating the portfolio values:", error);
          });
      };    const dummyWallet = import.meta.env.VITE_WALLET;
    useEffect(() => {
        async function fetchData() {
            try {
                const response = await fetch('https://dashboard.withblaze.app/api/graphql-api', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'x-api-key': apiKey
                    },
                    body: JSON.stringify({
                        query: `
                        query WalletTraits($walletAddress: String!){
                            walletTraits(walletAddress: $walletAddress){
                                walletAddress
                                twitterHandles
                                emails
                                telegramHandles
                                walletTags {
                                    cex
                                    historical
                                    latestActive
                                }
                                erc20Tokens {
                                    chain
                                    tokenAddress
                                    tokenName
                                    tokenSymbol
                                }
                                erc721Tokens {
                                    chain
                                    tokenAddress
                                    tokenName
                                    tokenSymbol
                                }
                                ethereumTokenPortfolioValue
                                polygonTokenPortfolioValue
                                nftPortfolioValue
                                arbitrumTokenPortfolioValue
                                bscTokenPortfolioValue
                                baseTokenPortfolioValue
                                optimismTokenPortfolioValue
                                washCategory
                                volumeCategory
                                activityCategory
                                lastTransactionDate
                            }
                        }
                        `,
                        variables: {
                            walletAddress: dummyWallet
                        }
                    })
                });

                const responseData = await response.json();
                setData(responseData.data.walletTraits);
                const walletTraits = responseData.data.walletTraits;
                const portfolioValues = {
                    ethereumTokenPortfolioValue: walletTraits.ethereumTokenPortfolioValue,
                    polygonTokenPortfolioValue: walletTraits.polygonTokenPortfolioValue,
                    nftPortfolioValue: walletTraits.nftPortfolioValue,
                    arbitrumTokenPortfolioValue: walletTraits.arbitrumTokenPortfolioValue,
                    bscTokenPortfolioValue: walletTraits.bscTokenPortfolioValue,
                    baseTokenPortfolioValue: walletTraits.baseTokenPortfolioValue,
                    optimismTokenPortfolioValue: walletTraits.optimismTokenPortfolioValue
                }
                storePortfolioValue(portfolioValues);
                setLoading(false);
            } catch (error) {
                setError(error);
                setLoading(false);
            }
        }

        fetchData();
    }, [walletAddress, apiKey]);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;
    if (!data) return null;

    return (
        <div className="wallet-details">
            <h2 style={{ marginBottom: '10px' }}>Wallet Address: {data.walletAddress}</h2>
            {data.walletTags && Object.keys(data.walletTags).length > 0 ? (
                <div className="wallet-tags">
                    <h3>Wallet Tags:</h3>
                    <ul>
                        {Object.keys(data.walletTags).map((tagType) => (
                            <li key={tagType}>
                                <strong>{tagType}:</strong> {data.walletTags[tagType].join(', ')}
                            </li>
                        ))}
                    </ul>
                </div>
            ) : (
                <p>No wallet tags found.</p>
            )}
            <div className="portfolio-values">
                <h3>Portfolio Values:</h3>
                <ul>
                    <li>Ethereum: {data.ethereumTokenPortfolioValue}</li>
                    <li>Polygon: {data.polygonTokenPortfolioValue}</li>
                    <li>NFT: {data.nftPortfolioValue}</li>
                    <li>Arbitrum: {data.arbitrumTokenPortfolioValue}</li>
                    <li>BSC: {data.bscTokenPortfolioValue}</li>
                    <li>Base: {data.baseTokenPortfolioValue}</li>
                    <li>Optimism: {data.optimismTokenPortfolioValue}</li>
                </ul>
            </div>
        </div>
    );
}

export default WalletTraitsComponent;
