import streamlit as st
st.set_page_config(page_title="Governance Mechanisms", page_icon="🗳️")
st.title("Governance Mechanisms")
img_tag = '<img src="data:image/png;base64,{}" style="width:10%; height:10%; padding-bottom:2%" alt="Your Image">'

def display_voting_system():
    st.header("Voting System")
    st.subheader("Earning Your Say: The Power of Token Holding")
    st.markdown("At the heart of Marker's governance lies a simple yet powerful principle: the more you hold, the more you have to say. Each Marker token, affectionately called 'MKR,' serves as a miniature ballot, granting its holder the right to vote on proposals that impact the very fabric of the MakerDAO ecosystem. This weighted voting system ensures that those with a vested interest in the protocol's success hold greater sway in its direction.")
    st.image("assets/voting_system.png",width=630)

    st.subheader("Delegation: Amplifying Voices, Bridging Gaps")
    st.markdown("Recognizing the diverse nature of its community, Marker incorporates a clever mechanism called 'delegation.' Through delegation, token holders can entrust their voting power to individuals or organizations who align with their values and vision. This not only amplifies the voices of smaller holders but also fosters the emergence of specialized entities that can effectively represent the interests of specific groups within the ecosystem.")

    st.subheader("From Proposition to Action: The Journey of a Proposal")
    st.markdown("The lifeblood of Marker's governance lies in its proposals. Anyone, from seasoned veterans to enthusiastic newcomers, can submit proposals encompassing a vast spectrum of topics. These proposals might seek to tweak the protocol's parameters, allocate funds for new initiatives, or even chart the course for future development. Each proposal then embarks on a journey, open for scrutiny and debate by the entire community during a designated voting period.")

    st.subheader("Casting Your Vote: Mechanisms of Choice")
    st.markdown("The act of voting itself in Marker's governance is far from a simplistic binary choice. Different implementations employ diverse voting mechanisms, each tailored to ensure fair and informed participation. Some favor straightforward majority rule, while others utilize more intricate methods like quadratic voting, where the weight of your vote increases not just with the number of tokens you hold, but also with the intensity of your conviction.")

    st.subheader("The Verdict is Rendered: Shaping the Future Together")
    st.markdown("Once the voting period concludes, the community's voice resonates through the tally. Accepted proposals pave the way for concrete action, shaping the evolution of the MakerDAO ecosystem in accordance with the collective will. Rejected proposals, though not a dead end, offer valuable insights into the community's preferences and priorities, informing future iterations and fostering continuous refinement.")

    st.markdown("Marker's governance, a vibrant tapestry woven from token-based rights, delegation, and a diverse array of voting mechanisms, stands as a testament to the power of collective decision-making in the cryptocurrency landscape. It empowers the community to be not just passive observers but active participants in shaping the future of a revolutionary financial experiment.")

def display_onchain_voting():
    st.header("On-Chain Voting")

    st.subheader("On-Chain Voting: A Complex Tapestry for Marker's Governance")
    st.markdown("At the heart of Marker's progressive governance framework lies the innovative concept of 'on-chain voting,' an approach that immerses proposals and votes directly into the blockchain. While celebrated for its transparency and security, this methodology brings forth its own set of intricacies. Let's explore the dual facets of this intricate landscape.")

    st.subheader("Transparency Ascendant: A Chronicle of Collective Decisions")
    st.markdown("Envision an immaculate voting booth, accessible to all, where each ballot and proposal is illuminated within the unyielding realm of the blockchain. This exemplifies the essence of on-chain voting – a process meticulously documented, cultivating trust and accountability. No clandestine dealings or obscured intentions; just a public ledger chronicling communal decisions that sculpt the trajectory of Marker.")

    st.subheader("Security Bastion: Votes Engraved in the Blockchain Citadel")
    st.markdown("The blockchain serves as an indomitable bastion, shielding votes from tampering. Manipulating these votes is tantamount to attempting an Everest ascent blindfolded – an endeavor nearly insurmountable. This robust security guarantees that every voice echoed genuinely mirrors the collective will of the community, untarnished by the stratagems of malicious actors.")

    st.subheader("Engagement Amplified: From Observers to Custodians")
    st.markdown("On-chain voting transcends mere balloting; it extends an invitation to active involvement. The accessibility and transparency inherent in this process beckon even the most indifferent token holder to assume a stewardship role within the Marker ecosystem. This surge in engagement fuels lively discussions, informed proposals, and ultimately contributes to a more resilient and responsive governance system.")

    st.subheader("Challenges Emerge: The Other Side of the Coin")
    st.markdown("Yet, this utopian narrative encounters earthly challenges. Voter turnout, unfortunately, can be elusive. Complex voting mechanisms or a perceived lack of impact may leave the ballot boxes resonating with the silence of disengaged token holders.")
    st.markdown("Then arises the 'whale effect.' With voting power tethered to token holdings, a handful of influential entities may sway the vote disproportionately, potentially drowning out the voices of smaller participants. This raises questions about the true representativeness of the outcomes.")
    st.markdown("Finally, as the Marker community burgeons, scalability challenges confront on-chain voting. Processing myriad votes on the blockchain can become sluggish and costly, potentially impeding the agility and responsiveness promised by on-chain voting.")

    st.subheader("Striking the Right Balance: A Governance Odyssey")
    st.markdown("On-chain voting presents a potent tool for Marker's governance, contingent upon navigating these challenges. Streamlining voting processes, fostering inclusive dialogues, and exploring alternative scaling solutions are pivotal steps toward achieving a genuinely representative and engaged governance system. Ultimately, achieving equilibrium among transparency, security, and accessibility will determine whether on-chain voting fulfills its revolutionary potential for Marker's future.")

    st.subheader("On-Chain Voting in Action")
    st.markdown("Examples of on-chain voting systems:")
    st.markdown("**MakerDAO:** The MakerDAO platform employs a 'decentralized autonomous organization' (DAO) system, allowing DAI token holders to vote on proposals shaping the Maker protocol.")
    st.markdown("**Tezos:** The Tezos blockchain utilizes 'on-chain governance,' enabling token holders to vote on protocol-altering proposals.")
    st.markdown("**Aragon:** Aragon furnishes tools for constructing decentralized applications (dApps) with integrated on-chain governance.")
    st.subheader("Future of On-Chain Voting")
    st.markdown("While on-chain voting confronts existing challenges, its potential to reshape organizational governance is significant. As a relatively new technology, ongoing refinement and widespread adoption hinge on addressing these challenges. Nevertheless, on-chain voting is poised to play a pivotal role in shaping the future of the cryptocurrency market.")

st.sidebar.title("Navigation")

# Sidebar navigation
selected_section = st.sidebar.selectbox("Go to", ["Voting System", "On-Chain Voting","Governance stats"])

# Display content based on selected section
if selected_section == "Voting System":
    display_voting_system()
elif selected_section == "On-Chain Voting":
    display_onchain_voting()
elif selected_section == "Governance stats":
    st.subheader("Governance Stats")
    st.image("assets/governance_stats.png",width=650)
    st.markdown("In this illuminating image, numerical prowess takes center stage, revealing the essence of MakerDAO's governance landscape. Witness the delegate count, MKR delegates, and delegators count – each digit a crucial piece in the decentralized puzzle. These numbers encapsulate the active engagement of community delegates, who play a pivotal role in shaping the MakerDAO ecosystem. Delegators, too, contribute to this dynamic force, amplifying the decentralized influence. This defines the governance strength of MKR DAO tokens, where each count signifies a strategic step towards decentralized financial empowerment.")
    