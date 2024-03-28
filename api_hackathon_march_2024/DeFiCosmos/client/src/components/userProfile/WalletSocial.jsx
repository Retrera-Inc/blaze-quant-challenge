import React, { useState, useEffect } from 'react';
import "./walletSocial.css";

const WalletContactComponent = (props) => {
  const {walletAddress} = props;
  const [data, setData] = useState(null);
  const apiKey = import.meta.env.VITE_API_KEY;
  const dummyWallet = import.meta.env.VITE_WALLET_2;
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('https://dashboard.withblaze.app/api/graphql-api', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': apiKey
        },
        body: JSON.stringify({
          query: `
            query WalletContacts($walletAddress: String!){
              walletContacts(walletAddress: $walletAddress){
                  walletAddress
                  twitterHandle
                  email
                  telegramHandle
              }
            }
          `,
          variables: {
            walletAddress: dummyWallet
          }
        })
      });

      const responseData = await response.json();
      console.log(responseData.data.walletContacts);
      setData(responseData.data.walletContacts);
    };

    fetchData();
  }, [walletAddress, apiKey]);
  

  return (
    <div className="wallet-social-container">
      {data ? (
        <div className="bento-grid">
          <div className="remaining-info" id="item-0">
            <h3>Twitter Handle:</h3>
            <p>{data.twitterHandle ? data.twitterHandle : "None"}</p>
          </div>
          <div className="remaining-info" id="item-1">
            <h3>Email:</h3>
            <p>{data.email ? data.email : "None"}</p>
          </div>
          <div className="remaining-info" id="item-2">
            <h3>Telegram Handle:</h3>
            <p>{data.telegramHandle ? data.telegramHandle : "None"}</p>
          </div>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default WalletContactComponent;
