import React from "react";
import "./network.css";

const BaseSystem = () => {
    const navigate = useNavigate();
    const navigateToChats = () => {
        navigate("/chats"); // Navigate to /chats route
    };
    return(
        <div className="network-body">
            <div className="base-sun"></div>
            <button className="navigate-button" onClick={navigateToChats}>Go to text channel</button>
        </div>
    );
}

export default BaseSystem;