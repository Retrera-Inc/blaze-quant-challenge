const mongoose = require("mongoose");

const HoldingSchema = mongoose.Schema(
  {
    id: { type: mongoose.Schema.Types.ObjectId, ref: "User" },
    address: { type: String, unique: true },
    holdings: { type: Object, required: true }, 
  },
  { timestamps: true }
);

const Holdings = mongoose.model("Holdings", HoldingSchema);
module.exports = Holdings;
