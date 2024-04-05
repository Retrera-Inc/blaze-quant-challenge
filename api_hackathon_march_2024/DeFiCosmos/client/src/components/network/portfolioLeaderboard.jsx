import React, { useState, useEffect } from "react";
import "./portfolioLeaderboard.css";
const LeaderboardCard = () => {
  const [portfolios, setPortfolios] = useState([]);
  const [showMore, setShowMore] = useState(false);
  const [expandedPortfolio, setExpandedPortfolio] = useState(null);

  useEffect(() => {
    // Fetch portfolios data from API
    const fetchPortfolios = async () => {
      try {
        const response = await fetch("/server/api/leaderBoard");
        if (!response.ok) {
          throw new Error("Failed to fetch portfolios");
        }
        const data = await response.json();
        setPortfolios(data);
      } catch (error) {
        console.error("Error fetching portfolios:", error);
      }
    };

    fetchPortfolios();
  }, []);

  const toggleShowMore = () => {
    setShowMore(!showMore);
  };

  const togglePortfolio = (index) => {
    if (expandedPortfolio === index) {
      setExpandedPortfolio(null);
    } else {
      setExpandedPortfolio(index);
    }
  };

  return (
    <div className="leaderboard-card">
      <h2 className="leaderboard-title">Top Portfolios</h2>
      <ul className="portfolio-list">
        {portfolios.slice(0, showMore ? 10 : 5).map((portfolio, index) => (
          <li key={index} className="portfolio-item">
            {portfolio.name} - {portfolio.score}
            <button
              className="portfolio-toggle"
              onClick={() => togglePortfolio(index)}
            >
              {expandedPortfolio === index
                ? "Hide Portfolio"
                : "View Portfolio"}
            </button>
            {expandedPortfolio === index && (
              <div className="portfolio-details">
                <p>Description: {portfolio.description}</p>
                {/* Add additional portfolio details here */}
              </div>
            )}
          </li>
        ))}
      </ul>
      <button className="toggle-button" onClick={toggleShowMore}>
        {showMore ? "Show Less" : "Show More"}
      </button>
    </div>
  );
};

export default LeaderboardCard;
