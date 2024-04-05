// Assuming you have mongoose and express installed
const User = require('../models/User'); // Replace 'YourModel' with the actual model name

// Define a route to handle search requests
const searchController = async (req, res) => {
  try {
    const { q } = req.query; // Assuming the search query is passed as a query parameter
    console.log(q);
    // Perform the search using Mongoose find method
    const searchResults = await User.find({ name: { $regex: new RegExp(q, 'i') } }); // Using case-insensitive regex for partial matching
    console.log(searchResults);
    res.json({ results: searchResults });
  } catch (error) {
    console.error('Error searching:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
}

module.exports = searchController;
