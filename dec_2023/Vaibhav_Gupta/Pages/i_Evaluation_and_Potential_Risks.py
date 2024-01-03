import streamlit as st
from PIL import Image



def i():
    

    st.markdown(
        """
    ## Evaluation of Potential Risks and Future Prospects :
    ### Risks and Mitigation:

    Common risks associated with GNO investments and ways to mitigate them:
    1. Market Volatility:high volatility, and significant price fluctuations.
        Mitigation: Diversify investment portfolio, and consider using risk management strategies.

    2. Regulatory Risks: Regulatory changes can impact the legality   
    Mitigation: Stay informed about regulatory developments, comply with local regulations, and consider investing in projects that prioritize regulatory compliance.

    3. Security Risks:Smart contract vulnerabilities, hacking incidents, or security breaches can impact the security of the Gnosis platform.
        Mitigation: Choose platforms and projects with a strong security track record, keep software and wallets updated, use hardware wallets for storage, and follow best practices for securing private keys.

    4. Technology Risks:Technical issues, bugs, or vulnerabilities in the underlying technology can affect the functionality and security of the Gnosis platform.
        Mitigation: Stay informed about platform updates, and be cautious about using newly released features.

    5. Competition:Increased competition may impact the adoption and value of GNO tokens.
    Mitigation: Keep track of developments in the decentralized prediction market space, assess the unique features of Gnosis, and consider the project's roadmap and community support.

    6. Liquidity Risks:Low liquidity can lead to challenges when buying or selling GNO tokens.
        Mitigation: Trade on reputable and liquid exchanges, and avoid placing large market orders that could impact prices.
    8. Governing Decisions:Governance decisions by token holders may lead to disagreements or controversial changes.
        Mitigation: Participate in governance discussions, understand the decision-making process, and diversify governance involvement to reduce concentration of power.

    9. Token Utility:Changes in the utility or use cases of GNO tokens could impact demand and value.
    Mitigation:  Stay informed about platform updates and token utility, and assess the long-term viability of the project's ecosystem.

    ### Future Prospects:
    
    - The future projections include development of the dxDAO — a decentralized governance mechanism based on the Genesis protocol, and derived from the Holographic Consensus framework. 
    This decentralized application will govern the trading protocol. Besides, the team is working on the mobile version of the Gnosis platform.

    - Gnosis Chain is currently secured by the POSDAO consensus, but this will be deprecated in the coming months as the Gnosis Chain incorporates a consensus-layer beacon chain. The Gnosis Beacon Chain mirrors the Ethereum Beacon Chain (with some important optimizations including faster blocks and epoch times). Close to 60,000 validators are already participating as the chain closes in on the merge between the Gnosis Chain EVM and the Gnosis Beacon Chain.

    - With the collaboration of GNO with the LI.FI and with xDAI chain , Gnosis Chain exists to facilitate high frequency and cost-efficient EVM-compatible transactions. Activity on Gnosis Chain is high, as the chain facilitated between 100,000–300,000 daily transactions for the month of February. As mentioned above, Gnosis Chain is home to a wide variety of crypto tooling that includes DEXs, NFT infrastructure, DAOs, gaming, and more. However, to fully unlock the potential of Gnosis Chain assets and protocols, users must be able to directly leverage tokens from other chains.

    """
    )
    image_path = "./assets/footer image.png"
    image = Image.open(image_path)
    st.image(image, caption="")
