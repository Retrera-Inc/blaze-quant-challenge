// userController.js

const User = require('../models/userFollowers');

async function followUser(req, res) {
  const { userId, followerId } = req.body;

  try {
    const user = await User.findById(userId);
    const follower = await User.findById(followerId);

    if (!user || !follower) {
      return res.status(404).json({ message: 'User or follower not found' });
    }

    if (user.followers.includes(followerId)) {
      return res.status(400).json({ message: 'You are already following this user' });
    }

    user.followers.push(followerId);
    await user.save();

    res.status(200).json({ message: 'Successfully followed user' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
}

module.exports = {
  followUser
};
