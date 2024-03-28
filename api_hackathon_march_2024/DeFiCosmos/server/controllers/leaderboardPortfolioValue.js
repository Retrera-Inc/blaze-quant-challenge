const PortfolioValue = require('../models/portfolioValues');

async function getTop5PortfolioValues(req, res) {
  try {
    const top5PortfolioValues = await PortfolioValue.aggregate([
      {
        $project: {
          totalPortfolioValue: {
            $sum: {
              $sum: [
                "$portfolio.ethereumTokenPortfolioValue",
                "$portfolio.polygonTokenPortfolioValue",
                "$portfolio.nftPortfolioValue",
                "$portfolio.arbitrumTokenPortfolioValue",
                "$portfolio.bscTokenPortfolioValue",
                "$portfolio.baseTokenPortfolioValue",
                "$portfolio.optimismTokenPortfolioValue"
              ]
            }
          },
          userID: 1,
          portfolio: 1
        }
      },
      {
        $sort: { totalPortfolioValue: -1 }
      },
      {
        $limit: 5
      }
    ]);
    console.log(top5PortfolioValues);
    res.json(top5PortfolioValues);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
}

module.exports = {
  getTop5PortfolioValues
};
