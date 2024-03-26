import React from "react";
import "./network.css";
import { useNavigate } from "react-router-dom";
const ArbitrumSystem = () => {
    const navigate = useNavigate();
    const navigateToChats = () => {
        navigate("/chats"); // Navigate to /chats route
    };
    return(
        <div className="network-body">
            <div className="arbitrum-sun"></div>
            <button className="navigate-button" onClick={navigateToChats}>Go to text channel</button>
        </div>
    );
}

export default ArbitrumSystem;