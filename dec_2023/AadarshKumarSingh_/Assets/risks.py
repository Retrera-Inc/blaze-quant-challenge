import streamlit as st

# Set title and subheader

def r():
    st.title("Ocean Protocol: Potential Risks and Mitigation Strategies")
    st.markdown("---")
    
    # Risk Categories
    categories = ["Technology and Development", "Economic and Token", "Governance and Regulatory", "Ecosystem and Adoption"]
    
    # Risk Analysis
    for category in categories:
    
        st.subheader(category)
    
        risks = {
            "Technology and Development": ["Smart contract vulnerabilities", "Technical challenges", "Blockchain dependency"],
            "Economic and Token": ["Market volatility", "Competition", "Token distribution and inflation", "Burning mechanisms"],
            "Governance and Regulatory": ["Centralization concerns", "Evolving regulatory landscape", "Community governance risks"],
            "Ecosystem and Adoption": ["Data availability and quality", "Limited network effects", "Security and privacy concerns"],
        }
    
        for risk in risks[category]:
            st.write(f"- {risk}")
    
        mitigation = {
            "Technology and Development": ["Auditing smart contracts", "Open-source development"],
            "Economic and Token": ["Diversifying data sources"],
            "Governance and Regulatory": ["Community building and education"],
            "Ecosystem and Adoption": ["Regulatory compliance"],
        }
    
        st.write("**Mitigation Strategies:**")
    
        for strategy in mitigation[category]:
            st.write(f"- {strategy}")
    
    # Conclusion
    st.subheader("Conclusion")
    
    st.write("Despite potential risks, Ocean Protocol actively works to build a secure and sustainable ecosystem.")
    st.write("Understanding these risks and engaging responsibly contributes to the project's success and unlocks the potential of decentralized data.")
    