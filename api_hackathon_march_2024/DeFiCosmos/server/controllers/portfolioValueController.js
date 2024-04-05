const Portfolio = require("../models/portfolioValues");

const PortfolioValueController = async (req, res) => {
  try {
    const userData = req.body;
    const userInfo = JSON.parse(userData.userInfo);
    console.log(userInfo._id);
    
    // Check if the address for the user already exists
    let existingPortfolioValue= await Portfolio.findOne({ userID: userInfo._id });

    if (existingPortfolioValue) {
      // If address exists, update it
      existingPortfolioValue.portfolioValue = userData.score;
      await existingPortfolioValue.save();
      
      res.status(200).json({ message: "Portofolio updated successfully", score: existingPortfolioValue });
    } else {
      // If address doesn't exist, create a new one
      const newPortfolioValue = new Portfolio({
        userID: userInfo._id,
        portfolioValue: userData.portfolioValue,
      });

      await newPortfolioValue.save();

      res.status(201).json({ message: "Portfolio created successfully", portfolio: newPortfolioValue });
    }
  } catch (error) {
    console.error("Error updating/creating address:", error);
    res.status(500).json({ message: "Internal server error" });
  }
};

module.exports = PortfolioValueController;