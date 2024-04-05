// followerController.js

const User = require('../models/userFollowers');

async function getNumberOfFollowers(req, res) {
  const { userId } = req.params;

  try {
    const user = await User.findById(userId);

    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }

    const numberOfFollowers = user.followers.length;

    res.status(200).json({ numberOfFollowers });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
}

module.exports = {
  getNumberOfFollowers
};
