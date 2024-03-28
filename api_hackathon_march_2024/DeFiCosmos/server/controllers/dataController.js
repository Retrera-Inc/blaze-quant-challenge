const Holdings = require("../models/Data");

const storePortfolio = async (req, res) => {
    try {
        // Extract data from the request body
        const { id, address, holdings } = req.body; // Update keys as per your data structure

        // Create a new document using the model constructor
        const newData = new Holdings({
            id: id,
            address: address,
            holdings: holdings,
        });
        console.log(newData);
        // Save the new data to the database
        await newData.save();

        // Respond with success message
        res.status(201).json({ message: 'Data stored successfully' });
    } catch (error) {
        // If an error occurs, respond with an error message
        console.error('Error storing data:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
}

module.exports = { storePortfolio };
