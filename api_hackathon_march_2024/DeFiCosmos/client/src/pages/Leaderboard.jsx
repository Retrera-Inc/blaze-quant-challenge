import React, { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import "./leaderboard.css";

function Leaderboard() {
  const [topWalletScoreUsers, setTopWalletScoreUsers] = useState([]);
  const [topPortfolioValuesUsers, setTopPortfolioValuesUsers] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTopPerformers = () => {
      // Fetch top performers based on wallet score
      fetch("/server/api/leaderboardWalletScore", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch wallet score leaderboard");
          }
          return response.json();
        })
        .then((walletScoreData) => {
          console.log(walletScoreData);
          setTopWalletScoreUsers(walletScoreData);
        })
        .catch((error) => {
          setError(error.message);
        });
    };

    const fetchTopPortfolios = () => {
      fetch("/server/api/leaderboardPortfolioValues", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch portfolio values leaderboard");
          }
          return response.json();
        })
        .then((portfolioValuesData) => {
          console.log(portfolioValuesData);
          setTopPortfolioValuesUsers(portfolioValuesData);
        })
        .catch((error) => {
          setError(error.message);
        });
    };

    fetchTopPerformers();
    fetchTopPortfolios();
  }, []);

  return (
    <div className="container">
      <div className="graph-container">
        <h2 className="graph-title">Top 5 Wallet Score Performers</h2>
        {topWalletScoreUsers.map((performer, index) => (
          <div key={index}>
            <h3 className="values">{index + 1}. {performer.userID}</h3>
            <div className="graphs">
            <Plot
              data={[
                {
                  x: ['Web3 Reputation', 'Authenticity'],
                  y: [performer.score.web3ReputationScore, performer.score.authenticityScore],
                  type: "bar",
                  marker: { color: ["blue", "green"] },
                },
              ]}
              layout={{
                width: 400,
                height: 300,
                title: "Wallet Score Distribution",
                paper_bgcolor: 'rgba(137, 113, 208, 0.1)',
                plot_bgcolor: 'rgba(137, 113, 208, 0.1)',
                font: { color: "white" }
              }}
            />
            <Plot
              data={[
                {
                  x: ['Portfolio Value'],
                  y: [performer.totalScore],
                  type: "bar",
                  marker: { color: "orange" },
                },
              ]}
              layout={{
                width: 400,
                height: 300,
                title: "Portfolio Value",
                paper_bgcolor: 'rgba(137, 113, 208, 0.1)',
                plot_bgcolor: 'rgba(137, 113, 208, 0.1)',
                font: { color: "white" }
              }}
            />
            </div>
          </div>
        ))}
        {error && <p>{error}</p>}
      </div>
    </div>
  );
  
}

export default Leaderboard;
