// userController.js

const followingUserModel = require('../models/userFollowers');

async function followingUser(req, res) {
  const { userId, followingId } = req.body;

  try {
    const user = await followingUserModel.findById(userId);
    const followingUser = await followingUserModel.findById(followingId);

    if (!user || !followingUser) {
      return res.status(404).json({ message: 'User or following user not found' });
    }

    if (user.following.includes(followingId)) {
      return res.status(400).json({ message: 'You are already following this user' });
    }

    user.following.push(followingId);
    await user.save();

    res.status(200).json({ message: 'Successfully followed user' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
}

async function unfollowUser(req, res) {
  const { userId, followingId } = req.body;

  try {
    const user = await User.findById(userId);

    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }

    if (!user.following.includes(followingId)) {
      return res.status(400).json({ message: 'You are not following this user' });
    }

    user.following = user.following.filter(id => id.toString() !== followingId);
    await user.save();

    res.status(200).json({ message: 'Successfully unfollowed user' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
}

module.exports = {
  followingUser,
  unfollowUser
};
