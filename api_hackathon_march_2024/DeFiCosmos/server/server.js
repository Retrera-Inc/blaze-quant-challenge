const express = require("express");
const dotenv = require("dotenv");
const path = require("path");

const { connectToMongoDB } = require("./config");
const { userRoutes, chatRoutes, messageRoutes, dataRoutes } = require("./routes");
const { notFound, errorHandler } = require("./middleware");
const searchController = require("./controllers/searchController");
const storeWalletController = require("./controllers/storeWalletController");
const getUserInfoAndAddress = require("./controllers/getUserInfoAddressController");
const storeScoreController = require("./controllers/storeScoreController");
const tokenCountController = require("./controllers/tokenCountController");
const portfolioValueController = require("./controllers/portfolioValueController");
const {getTop5PortfolioValues} = require("./controllers/leaderboardPortfolioValue");
const {getTop5WalletScores} = require("./controllers/leaderboardWalletScore");
const {followUser} = require("./controllers/userFollowerController");
const {getNumberOfFollowers} = require('./controllers/getNumberOfFollowersController');
const {followingUser, unfollowUser} = require("./controllers/followingController")
const app = express(); // Use express js in our app
app.use(express.json()); // Accept JSON data
dotenv.config(); // Specify a custom path if your file containing environment variables is located elsewhere
connectToMongoDB(); // Connect to Database

app.use("/api/user", userRoutes);
app.use("/api/chat", chatRoutes);
app.use("/api/message", messageRoutes);
app.use("/api/store", dataRoutes);
app.get("/api/search", searchController);
app.post("/api/storeWallet", storeWalletController);
app.get("/api/getUser/:id", getUserInfoAndAddress);
app.post("/api/storeScore", storeScoreController);
app.post("/api/storeTokenCount", tokenCountController);
app.post("/api/storePortfolioValue", portfolioValueController);
app.get("/api/leaderboardPortfolioValue", getTop5PortfolioValues);
app.get("/api/leaderboardWalletScore", getTop5WalletScores);
app.get("/api/getFollowers/:id", getNumberOfFollowers);
app.post("/api/follow", followUser);
app.post("/api/followUser", followingUser);
app.post("/api/unfollow", unfollowUser);
// --------------------------DEPLOYMENT------------------------------

if (process.env.NODE_ENV === "production") {
  app.use(express.static(path.join(__dirname, "./client/build")));

  app.get("*", (req, res) => {
    return res.sendFile(
      path.resolve(__dirname, "client", "build", "index.html")
    );
  });
} else {
  app.get("/", (req, res) => {
    res.send("API is running");
  });
}

// --------------------------DEPLOYMENT------------------------------

app.use(notFound); // Handle invalid routes
app.use(errorHandler);

const server = app.listen(process.env.PORT, () =>
  console.log(`Server started on PORT ${process.env.PORT}`)
);

const io = require("socket.io")(server, {
  cors: {
    origin: ["http://localhost:3000", "http://localhost:3001", "http://localhost:3002", "http://localhost:5173"],
  },
  pingTimeout: 60 * 1000,
});

io.on("connection", (socket) => {
  console.log("Connected to socket.io");

  socket.on("setup", (userData) => {
    socket.join(userData._id);
    socket.emit("connected");
  });

  socket.on("join chat", (room) => {
    socket.join(room);
    console.log("User joined room " + room);
  });

  socket.on("typing", (room) => socket.in(room).emit("typing"));

  socket.on("stop typing", (room) => socket.in(room).emit("stop typing"));

  socket.on("new message", (newMessageRecieved) => {
    let chat = newMessageRecieved.chat[0]; // Change it to object

    if (!chat.users) return console.log("chat.users not defined");

    chat.users.forEach((user) => {
      if (user._id === newMessageRecieved.sender._id) return;

      socket.in(user._id).emit("message recieved", newMessageRecieved);
    });
  });

  socket.off("setup", () => {
    console.log("User Disconnected");
    socket.leave(userData._id);
  });
});
