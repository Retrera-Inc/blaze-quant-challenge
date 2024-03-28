const Address = require("../models/address");

const storeWalletController = async (req, res) => {
  try {
    const userData = req.body;
    const userInfo = JSON.parse(userData.userInfo);
    console.log(userInfo._id);
    
    // Check if the address for the user already exists
    let existingAddress = await Address.findOne({ userID: userInfo._id });

    if (existingAddress) {
      // If address exists, update it
      existingAddress.address = userData.address;
      await existingAddress.save();
      
      res.status(200).json({ message: "Address updated successfully", address: existingAddress });
    } else {
      // If address doesn't exist, create a new one
      const newAddress = new Address({
        userID: userInfo._id,
        address: userData.address,
      });

      await newAddress.save();

      res.status(201).json({ message: "Address created successfully", address: newAddress });
    }
  } catch (error) {
    console.error("Error updating/creating address:", error);
    res.status(500).json({ message: "Internal server error" });
  }
};

module.exports = storeWalletController;
