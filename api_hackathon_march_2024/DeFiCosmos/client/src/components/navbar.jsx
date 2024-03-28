import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom"; // Import Link component
import "./navbar.css"; // Import CSS file for styling

// Navbar component
const Navbar = () => {
  const navigate = useNavigate();
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState([]);

  const handleLogout = () => {
    localStorage.removeItem("userInfo");
    localStorage.removeItem("walletAddress");
    navigate("/");
  };

  const handleSearch = async () => {
    // Your search logic here
    try {
      const response = await fetch(`/server/api/search?q=${searchQuery}`);
      const data = await response.json();
      setSearchResults(data.results);
      localStorage.setItem("searchedUser", data.results);
      console.log(data.results[0]._id);
      navigate(`/user/${data.results[0]._id}`);
      console.log(searchResults);
    } catch (error) {
      console.error("Error searching:", error);
    }
  };

  // Get user ID from localStorage
  const userInfo = JSON.parse(localStorage.getItem("userInfo"));
  const userID = userInfo ? userInfo._id : "";

  return (
    <nav className="navbar">
      <div className="nav-wrapper">
        <ul className="nav-links">
          <li>
            <Link to="/home" className="nav-link">
              Home
            </Link>
          </li>
          <li>
            <Link to="/chats" className="nav-link">
              Chats
            </Link>
          </li>
          <li>
            <div className="input-field">
              <input
                id="search"
                type="search"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                required
              />
              <button className="search-button" onClick={handleSearch}>
                Search
              </button>
              {/* <label className="label-icon" htmlFor="search"><i className="material-icons">search</i></label> */}
              <i className="material-icons">close</i>
            </div>
          </li>
          <li>
            {/* Navigate to user page with dynamic user ID */}
            <Link to={`/user/${userID}`} className="nav-link">
              User
            </Link>
          </li>
          <li>
            <a onClick={handleLogout} className="nav-link">
              Logout
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
