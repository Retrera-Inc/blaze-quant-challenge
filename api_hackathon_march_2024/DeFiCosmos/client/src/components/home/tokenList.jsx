import React, { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import "./tokenList.css"; // Import CSS file for component styles

const TokenList = (props) => {
  const {walletAddress} = props;
  const dummyWallet = import.meta.env.VITE_WALLET;
  const [portfolioData, setPortfolioData] = useState(null);
  const [walletHoldings, setWalletHoldings] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [expandedNetwork, setExpandedNetwork] = useState(null); // Track expanded network
  const apiKey = import.meta.env.VITE_API_KEY;

const storeTokenList = (tokenList) => {
    const data = {
      userInfo: localStorage.getItem("userInfo"),
      tokenCount: tokenList,
    }
    console.log(data);
    fetch("/server/api/storeTokenCount", {
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
        console.log("Token Count updated successfully:", data);
      })
      .catch((error) => {
        // Handle error
        console.error("There was a problem updating the Tokenlist:", error);
      });
  };

  const fetchWalletHoldings = async () => {
    setIsLoading(true);
    try {
      const response = await fetch(
        "https://dashboard.withblaze.app/api/graphql-api",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "x-api-key": apiKey,
          },
          body: JSON.stringify({
            query: `
            query WalletHoldings($walletAddress: String!){
              walletHoldings(walletAddress: $walletAddress){
                walletAddress
                erc20Tokens{
                  chain
                  tokenAddress
                  tokenName
                  tokenSymbol
                }
                erc721Tokens{
                  chain
                  tokenAddress
                  tokenName
                  tokenSymbol
                }
                erc1155Tokens{
                  chain
                  tokenAddress
                  tokenName
                  tokenSymbol
                }
              }
            }
          `,
            variables: {
              walletAddress: dummyWallet,
            },
          }),
        }
      );

      const responseData = await response.json();
      console.log(responseData);
      setWalletHoldings(responseData.data.walletHoldings);
      storeTokenList(responseData.data.walletHoldings)
      // const holdings = {
      //   id: localStorage.getItem('userInfo')._id,
      //   address: localStorage.getItem('walletAddress'),
      //   holdings: walletHoldings,
      // };
      // storeHoldings(holdings);
    } catch (error) {
      console.error("Error fetching wallet holdings:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleNetworkClick = (network) => {
    if (expandedNetwork === network) {
      setExpandedNetwork(null); // Collapse if already expanded
    } else {
      setExpandedNetwork(network);
    }
  };

  useEffect(() => {
    fetchWalletHoldings();
  }, []); // Fetch data on component mount

  const countTokensByTypeAndNetwork = () => {
    if (!walletHoldings) return {};
  
    const counts = {};
  
    ["erc20Tokens", "erc721Tokens", "erc1155Tokens"].forEach((tokenType) => {
      if (walletHoldings[tokenType]) {
        walletHoldings[tokenType].forEach((token) => {
          const { chain } = token;
          counts[tokenType] = counts[tokenType] || {};
          counts[tokenType][chain] = (counts[tokenType][chain] || 0) + 1;
        });
      }
    });
  
    return counts;
  };
  

  const generateChartData = () => {
    const counts = countTokensByTypeAndNetwork();
    const tokenTypes = Object.keys(counts);

    const data = tokenTypes.map((tokenType) => ({
      type: "bar",
      name: tokenType,
      x: Object.keys(counts[tokenType]),
      y: Object.values(counts[tokenType]),
    }));

    return data;
  };

  return (
    <div className="crypto-portfolio-container">
      <div className="wallet-holdings-section flip-card">
        <div
          className="flip-card-inner"
          onClick={() => handleCardFlip("wallet")}
        >
          <div className="flip-card-front">
            <h2>Wallet Holdings</h2>
            <button
              className="refresh-button"
              onClick={fetchWalletHoldings}
              disabled={isLoading}
            >
              {isLoading ? "Loading..." : "Refresh Wallet Holdings"}
            </button>
          </div>
          <div className="flip-card-back">
            {/* Content for the back of the card */}
            {walletHoldings && (
              <div>
                <p className="wallet-address">
                  Wallet Address: {walletHoldings.walletAddress}
                </p>
                {Object.entries(walletHoldings).map(([network, tokens]) => (
                  <div key={network}>
                    {Array.isArray(tokens) && tokens.length > 0 ? (
                      <>
                        <h3 className="network-tokens">
                          {network} Tokens: {tokens.length}
                        </h3>
                        <button
                          className="network-button"
                          onClick={() => handleNetworkClick(network)}
                        >
                          {expandedNetwork === network
                            ? "Hide Tokens"
                            : "Show Tokens"}
                        </button>
                        {expandedNetwork === network && (
                          <ul className="token-list">
                            {tokens.map((token) => (
                              <li key={token.tokenAddress}>
                                {token.tokenName} ({token.tokenSymbol}) - Chain:{" "}
                                {token.chain}
                              </li>
                            ))}
                          </ul>
                        )}
                      </>
                    ) : (
                      <p>No tokens found for {network}</p>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
      <div className="token-distribution-chart flip-card">
        <div
          className="flip-card-inner"
          onClick={() => handleCardFlip("distribution")}
        >
          <div className="flip-card-front">
            <h2>Token Distribution</h2>
            <button
              className="refresh-button"
              onClick={fetchWalletHoldings}
              disabled={isLoading}
            >
              {isLoading ? "Loading..." : "Refresh Wallet Holdings"}
            </button>
          </div>
          <div className="flip-card-back">
            {/* Content for the back of the card */}
            {walletHoldings && (
              <div>
                
                <Plot
                  className="plotly-chart"
                  data={generateChartData()}
                  layout={{
                    width: 450,
                    height: 400,
                    title: "Token Distribution by Type and Network",
                    barmode: "stack",
                    xaxis: { title: "Network" },
                    yaxis: { title: "Number of Tokens" },
                    plot_bgcolor: 'rgba(137, 113, 208, 0.1)',
                    paper_bgcolor: 'rgba(137, 113, 208, 0.1)',
                  }}
                  config={{ displayModeBar: false }}
                />
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default TokenList;
