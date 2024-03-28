const mongoose = require("mongoose");

const portfolioValueSchema = new mongoose.Schema({
 userID: {
    type: String,
    ref: "User",
    required: true,
    unique: true
  },
  portfolio: {
    type: Object,
    required: true,
  },
});

const PortfolioValue = mongoose.model("PortfolioValue", portfolioValueSchema);

module.exports = PortfolioValue;