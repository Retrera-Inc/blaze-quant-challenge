const mongoose = require("mongoose");

const tokenCountSchema = new mongoose.Schema({
 userID: {
    type: String,
    ref: "User",
    required: true,
    unique: true
  },
  tokenCount: {
    type: Object,
    required: true,
  },
});

const tokenCount = mongoose.model("tokenCount", tokenCountSchema);

module.exports = tokenCount;