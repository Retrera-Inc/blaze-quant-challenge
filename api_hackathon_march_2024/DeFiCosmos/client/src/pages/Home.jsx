import React, { useState } from "react";
import Portfolio from "../components/portfolio/portfolio";
import Map from "../components/home/map";
import { useNavigate } from "react-router-dom";
import "./home.css";
const Home = () => {
  const navigate = useNavigate();
  const [showPortfolio, setShowPortfolio] = useState(false);

  const handleChatButton = () => {
    navigate("/chats");
  };

  const handlePortfolioButton = () => {
    setShowPortfolio((prevState) => !prevState);
  };

  return (
    <div className="home">
      <Map className='map' />
      {showPortfolio && <Portfolio className='portfolio' />}
      <button className='open-chat' onClick={handleChatButton}>Chat</button>
      <button className='open-portfolio' onClick={handlePortfolioButton}>
        {showPortfolio ? "Hide Portfolio" : "View Portfolio"}
      </button>
    </div>
  );
};

export default Home;
