import React, { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import './marketCap.css'; // Import CSS file for component styles

const CryptoMarketCap = () => {
  const [chain, setChain] = useState("ETHEREUM");
  const [marketCapData, setMarketCapData] = useState([]);

  const apiKey = import.meta.env.VITE_API_KEY;
  useEffect(() => {
    fetchMarketCapData();
  }, [chain]);

  const fetchMarketCapData = async () => {
    try {
      const url = new URL("https://dashboard.withblaze.app/api/chain-insights/market_cap");
      url.searchParams.append("chain", chain);
      url.searchParams.append("start_date", "2023-01-01");
      url.searchParams.append("end_date", "2023-01-31");
  
      const response = await fetch(url, {
        method: "GET",
        headers: {
          "x-api-key": '',
          "Content-Type": "application/json",
        },
      });
  
      if (!response.ok) {
        throw new Error("Failed to fetch data");
      }
  
      const data = await response.json();
      setMarketCapData(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleChangeChain = (newChain) => {
    setChain(newChain);
  };

  // Extracting date and market cap values for Plotly
  const dates = marketCapData.map((entry) => entry.date);
  const marketCaps = marketCapData.map((entry) => entry.market_cap);

  return (
    <div className="crypto-market-container">
      <h1>Crypto Market Capitalization</h1>
      <div className='graphs-buttons'>
      
      <Plot
        className="plotly-chart"
        data={{
            x: dates,
            y: marketCaps,
            type: "scatter",
            mode: "lines+markers",
            
            marker: { color: "yellow" }, // Bright color for markers
            line: { color: 'cyan' }, // Bright color for lines
            textfont: { color: 'green' }, // Bright color for text
          }}
        layout={{
          width: 800,
          height: 400,
          title:  `<span style="color: pink;">Market Cap Over Time (${chain})</span>`,
          xaxis: { title: `<span style="color: pink;">Date </span>` ,
          tickfont: { color: 'pink' }, // Set the color of x-axis labels
          gridcolor: 'yellow',},
          yaxis: { title: `<span style="color: pink;">Market Cap</span>`,
          tickfont: { color: 'pink' }, // Set the color of x-axis labels
          gridcolor: 'yellow', },
          plot_bgcolor: 'black',
          paper_bgcolor: 'black',
        }}
      />
      <div className="button-container">
        <button className="gradient-button" onClick={() => handleChangeChain("ETHEREUM")}>Ethereum</button>
        <button className="gradient-button" onClick={() => handleChangeChain("ARBITRUM")}>Arbitrum</button>
        <button className="gradient-button" onClick={() => handleChangeChain("BSC")}>BSC</button>
        <button className="gradient-button" onClick={() => handleChangeChain("POLYGON")}>Polygon</button>
        <button className="gradient-button" onClick={() => handleChangeChain("BASE")}>Base</button>
        <button className="gradient-button" onClick={() => handleChangeChain("OPTIMISM")}>Optimism</button>
      </div>
    </div>
    </div>
  );
};

export default CryptoMarketCap;
