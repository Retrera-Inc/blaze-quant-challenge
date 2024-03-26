// Import necessary modules
const { ObjectId } = require("mongoose").Types; // Import ObjectId from mongoose
const Address = require("../models/address"); // Assuming you have a User model defined
const User = require("../models/User");

const getUserInfoAndAddress = async (req, res) => {
  try {
    // Fetch user by address id
    const userInfoAndAddressObject = await Address.findOne({
      "userID": req.params.id,
    });
    const userInfoObject = await User.findOne({ _id: ObjectId(req.params.id) });

    console.log("address" + userInfoAndAddressObject);
    console.log("user info" + userInfoObject);
    if (!userInfoAndAddressObject || !userInfoObject) {
      return res
        .status(404)
        .json({ error: "User not found with the provided address ID" });
    }

    res.status(200).json({ userInfoAndAddressObject, userInfoObject });
  } catch (err) {
    console.error("Error retrieving user info and address:", err);
    res.status(500).json({ error: "Server error" });
  }
};

// Controller to retrieve user info and address
module.exports = getUserInfoAndAddress;
