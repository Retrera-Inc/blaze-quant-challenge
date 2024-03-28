import React, { useState, useEffect } from 'react';
import "./scList.css";
function SmartContractsList({ walletAddress, lastNDays }) {
  const [allData, setAllData] = useState([]);
  const [contracts, setContracts] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [showAll, setShowAll] = useState(false);
  const [showToggle, setShowToggle] = useState(false);
  const apiKey = import.meta.env.VITE_API_KEY;
  console.log(walletAddress);
  useEffect(() => {
    const fetchContracts = async () => {
      try {
        const response = await fetch('https://dashboard.withblaze.app/api/graphql-api', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-api-key': apiKey // Replace 'API Key' with your actual API key
          },
          body: JSON.stringify({
            query: `
              query SmartContractsInteractions($walletAddress: String!, $lastNDays: Int!) {
                smartContractsInteractions(walletAddress: $walletAddress, lastNDays: $lastNDays) {
                  walletAddress
                  smartContracts
                }
              }
            `,
            variables: {
              "walletAddress": walletAddress,
              "lastNDays": lastNDays,
            }
          })
        });
        const data = await response.json();
        setAllData(data.data.smartContractsInteractions.smartContracts);
        setContracts(data.data.smartContractsInteractions.smartContracts.slice(0, 5));
        setIsLoading(false);
        if (data.data.smartContractsInteractions.smartContracts.length > 5) {
          setShowToggle(true);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
        setIsLoading(false);
      }
    };

    fetchContracts();
  }, [walletAddress, lastNDays]);

  const toggleContracts = () => {
    setShowAll(!showAll);
    if (!showAll) {
      setContracts(allData);
    } else {
      setContracts(allData.slice(0, 5));
    }
  };

  const renderContracts = () => {
    if (isLoading) {
      return <p>Loading...</p>;
    } else {
      return (
        <div>
          <ul className='list-contracts'>
            {contracts.map(contract => (
              <li className='list-contracts' key={contract}>{contract}</li>
            ))}
          </ul>
          {showToggle && <button onClick={toggleContracts}>{showAll ? 'Show Less' : 'Show More'}</button>}
        </div>
      );
    }
  };

  return (
    <div className='smartListBox' >
      <h2>Smart Contracts Interacted with by Wallet</h2>
      {renderContracts()}
    </div>
  );
}

export default SmartContractsList;
