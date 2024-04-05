import { Routes, Route, Navigate, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import {
  Auth,
  Chat,
  WalletPage,
  Home,
  Data,
  PolygonSystem,
  EthereumSystem,
  BaseSystem,
  BSCSystem,
  OptimismSystem,
  ArbitrumSystem,
  UserProfile,
  Leaderboard,
} from "./pages";
import "./App.css";
import Navbar from "./components/navbar";

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(true);
  const location = useLocation();

  useEffect(() => {
    // Function to generate a random number between min and max (inclusive)
    function getRandomNumber(min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    // Function to generate a random color from an array of colors
    function getRandomColor(colors) {
      return colors[Math.floor(Math.random() * colors.length)];
    }

    // Function to create stars and asteroids with random colors
    function createStarsAndAsteroids(numElements) {
      const container = document.querySelector(".stars");
      const colors = ["#FFC0CB", "#FF69B4", "#FFD700", "#FFFF00", "#FFFFFF"]; // Shades of pink, yellow, and white

      for (let i = 0; i < numElements; i++) {
        const element = document.createElement("div");
        element.classList.add("element");

        // Randomize position and color
        element.style.left = `${getRandomNumber(0, container.offsetWidth)}px`;
        element.style.top = `${getRandomNumber(0, container.offsetHeight)}px`;
        element.style.backgroundColor = getRandomColor(colors);

        // Add class for differentiating between stars and asteroids
        if (Math.random() < 0.5) {
          element.classList.add("star");
        } else {
          element.classList.add("asteroid");
        }

        container.appendChild(element);
      }
    }

    // Call the function to create stars and asteroids
    createStarsAndAsteroids(50); // You can adjust the number of elements as needed
  }, []);

  const isNotHomeOrChatsRoute = location.pathname !== "/" && location.pathname !== "/chats" && location.pathname !== "/wallet";
  
  return (
    <div className="app-container stars">
      {isNotHomeOrChatsRoute && isLoggedIn && <Navbar/>}
      <div className="App">
        <Routes>
          <Route path="/" element={<Auth />} />
          <Route path="/chats" element={<Chat />} />
          <Route path="/wallet" element={<WalletPage />} />
          <Route path="/home" element={<Home />} />
          <Route path="/data" element={<Data />} />
          <Route path="/polygon" element={<PolygonSystem />} />
          <Route path="/arbitrum" element={<ArbitrumSystem />} />
          <Route path="/bsc" element={<BSCSystem />} />
          <Route path="/base" element={<BaseSystem />} />
          <Route path="/optimism" element={<OptimismSystem />} />
          <Route path="/ethereum" element={<EthereumSystem />} />
          <Route path="/user/:id" element={<UserProfile />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          {/* If the user enters an invalid path in the URL it automatically redirects them to the homepage */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </div>
  );
};

export default App;
