const mongoose = require("mongoose");

const addressSchema = new mongoose.Schema({
 userID: {
    type: String,
    ref: "User",
    required: true,
    unique: true
  },
  address: {
    type: String,
    required: true,
  },
});

const Address = mongoose.model("Address", addressSchema);

module.exports = Address;
