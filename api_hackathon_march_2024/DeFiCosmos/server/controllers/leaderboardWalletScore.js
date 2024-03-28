const Score = require("../models/score");

async function getTop5WalletScores(req, res) {
  try {
    const top5WalletScores = await Score.aggregate([
      {
        $project: {
          totalScore: {
            $sum: [
              "$score.web3ReputationScore",
              "$score.authenticityScore"
            ]
          },
          userID: 1,
          score: 1
        }
      },
      {
        $sort: { totalScore: -1 }
      },
      {
        $limit: 5
      }
    ]);
    console.log(top5WalletScores);
    res.json(top5WalletScores);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

module.exports = {
  getTop5WalletScores
};
