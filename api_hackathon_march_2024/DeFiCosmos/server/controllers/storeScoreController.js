const Score = require("../models/score");

const storeScoreController = async (req, res) => {
  try {
    const userData = req.body;
    const userInfo = JSON.parse(userData.userInfo);
    console.log(userInfo._id);
    
    // Check if the address for the user already exists
    let existingScore= await Score.findOne({ userID: userInfo._id });

    if (existingScore) {
      // If address exists, update it
      existingScore.score = userData.score;
      await existingScore.save();
      
      res.status(200).json({ message: "Address updated successfully", score: existingScore });
    } else {
      // If address doesn't exist, create a new one
      const newScore = new Score({
        userID: userInfo._id,
        score: userData.score,
      });

      await newScore.save();

      res.status(201).json({ message: "Address created successfully", scores: newScore });
    }
  } catch (error) {
    console.error("Error updating/creating address:", error);
    res.status(500).json({ message: "Internal server error" });
  }
};

module.exports = storeScoreController;