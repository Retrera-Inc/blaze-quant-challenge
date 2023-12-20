import streamlit as st


def team_analysis():
    st.title("Livepeer Team Analysis")
    st.header("Positive Aspects")
    st.markdown("**Experienced Leadership:** The Livepeer team boasts an experienced executive lead (CEO, COO) "
                "with a proven track record of managing multi-million dollar companies. This brings stability and "
                "expertise to the project.")
    st.markdown("**Innovative Tech Lead:** The tech lead has a rich background, having successfully managed million-dollar "
                "projects. This indicates a strong technical foundation and the ability to navigate complex development tasks.")
    st.markdown(" **Successful Project Experience:** The team's collective experience includes working on "
                "million-dollar projects, showcasing a history of successful endeavors in their respective domains.")

    st.markdown("**Community Engagement:** Livepeer is actively engaged with the community, evident in their inclusive "
                "approach to token distribution. The project aims to decentralize video broadcasting, allowing anyone to "
                "have a voice and participate in the platform.")


    st.header("Community Orientation")

    st.markdown("**Decentralization Mission:** Livepeer's mission to decentralize one-to-many live video broadcast "
                "aligns with community values. It provides a platform for direct interaction without third-party control, "
                "emphasizing inclusivity and freedom of expression.")

    st.markdown("**Fair Token Distribution:** The allocation of tokens to various stakeholders, including founders, "
                "pre-sale purchasers, crowd, grants, and a long-term project endowment, reflects a commitment to a fair and "
                "diverse distribution, fostering a sense of community ownership.")

    st.markdown("**Active Community Engagement:** The presence of social media links for advisory board members and the "
                "community-oriented approach demonstrate Livepeer's commitment to engaging with its user base.")




def utility_analysis():
    st.title("Livepeer (LPT) Token Utilities")

    st.write("""
    Livepeer (LPT) is the native token of the Livepeer network, playing a crucial role in various aspects of the decentralized video streaming protocol.

    1. **Staking:** LPT is staked as collateral by nodes (transcoders) participating in the network's proof-of-stake consensus.

    2. **Transcoding Rewards:** Transcoders earn LPT rewards for processing and transcoding video streams.

    3. **Bonding:** Token holders can bond LPT to specific transcoders, contributing to network security and earning a share of rewards.

    4. **Governance:** LPT holders actively participate in network governance, proposing and voting on protocol changes.

    5. **Protocol Fees:** LPT is used for paying fees on the Livepeer network for various services.

    6. **Community Incentives:** LPT is distributed as incentives for community contributions, fostering ecosystem growth.

    7. **Voting Power:** LPT holders possess voting power, influencing protocol direction and upgrades.

    8. **Network Security:** Stakers and holders enhance network security, aligning their interests with the network's success.

    """)


def tech_analysis():
    st.title("Technology Overview")

    st.markdown(
        """
    **1. Decentralized Video Infrastructure:** Livepeer utilizes blockchain technology to create a 
    decentralized video infrastructure, allowing users to broadcast live video streams with reduced costs 
    and increased accessibility.

    **2. Transcoding and Video Processing:** LPT employs a transcoding mechanism where nodes on the 
    network (transcoders) process and optimize video content. This enhances scalability and improves 
    the quality of the streaming experience.

    **3. Ethereum Integration:** Built on the Ethereum blockchain, Livepeer benefits from the security 
    and transparency of a well-established blockchain network. Smart contracts govern various aspects 
    of the Livepeer protocol.
    """
    )


def fundmental_analysis():


    st.title("Livepeer's Mission")

    problem_description = """
      Livepeer addresses a fundamental challenge in the world of video broadcasting, aiming to revolutionize the way 
      live video content is distributed and consumed. The project targets the one-to-many live video broadcast, or multicast,
      providing a decentralized and censorship-resistant platform for content creators and viewers alike.

      **Livepeer's Mission:**
      Livepeer envisions a future where broadcasters can connect directly with their audience, fostering a first-hand and unaltered 
      interaction. By decentralizing live video broadcasting, Livepeer aims to eliminate censorship concerns, empower content creators, 
      and provide an open and efficient platform for media distribution.  
      """
    st.image('assets/video-data.png')
    st.write(problem_description)

    tech_analysis()

    team_analysis()

    utility_analysis()








