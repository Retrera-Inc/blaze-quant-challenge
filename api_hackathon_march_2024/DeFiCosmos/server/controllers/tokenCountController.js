const TokenCount = require("../models/tokenCount");

const tokenCountController = async (req, res) => {
  try {
    const userData = req.body;
    const userInfo = JSON.parse(userData.userInfo);
    console.log(userInfo._id);

    // Check if the address for the user already exists
    let existingTokenCount = await TokenCount.findOne({ userID: userInfo._id });

    if (existingTokenCount) {
      // If address exists, update it
      existingTokenCount.portfolioValue = userData.score;
      await existingTokenCount.save();

      res
        .status(200)
        .json({
          message: "Token Count updated successfully",
          score: existingTokenCount,
        });
    } else {
      // If address doesn't exist, create a new one
      const newTokenCount = new Score({
        userID: userInfo._id,
        tokenCount: userData.TokenCount,
      });

      await newTokenCount.save();

      res
        .status(201)
        .json({
          message: "token count created successfully",
          portfolio: newTokenCount,
        });
    }
  } catch (error) {
    console.error("Error updating/creating address:", error);
    res.status(500).json({ message: "Internal server error" });
  }
};

module.exports = tokenCountController;
