const mongoose = require("mongoose");

const scoreSchema = new mongoose.Schema({
 userID: {
    type: String,
    ref: "User",
    required: true,
    unique: true
  },
  score: {
    type: Object,
    required: true,
  },
});

const Score = mongoose.model("Score", scoreSchema);

module.exports = Score;