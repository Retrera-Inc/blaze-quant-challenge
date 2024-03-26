import {
  Avatar,
  Box,
  Button,
  Drawer,
  DrawerBody,
  DrawerCloseButton,
  DrawerContent,
  DrawerHeader,
  DrawerOverlay,
  Input,
  Menu,
  MenuButton,
  MenuDivider,
  MenuItem,
  MenuList,
  Spinner,
  Text,
  Tooltip,
  background,
  color,
  useDisclosure,
  useToast,
} from "@chakra-ui/react";
import { BellIcon, ChevronDownIcon } from "@chakra-ui/icons";
import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import "./sideDrawer.css";

import { ChatState } from "../../context/ChatProvider";
import ProfileModal from "./ProfileModal";
import ChatLoading from "../ChatLoading";
import UserListItem from "../UserAvatar/UserListItem";
import { getSender } from "../../config/ChatLogics";
import "../../App.css";

const SideDrawer = () => {
  const [search, setSearch] = useState("");
  const [searchResult, setSearchResult] = useState([]);
  const [loading, setLoading] = useState(false);
  const [loadingChat, setLoadingChat] = useState(false);

  const {
    user,
    setSelectedChat,
    chats,
    setChats,
    notification,
    setNotification,
  } = ChatState();
  const navigate = useNavigate();
  const { isOpen, onOpen, onClose } = useDisclosure();
  const toast = useToast();

  const logoutHandler = () => {
    localStorage.removeItem("userInfo");
    navigate("/");
  };

  const handleSearch = async () => {
    if (!search) {
      return toast({
        title: "Please Enter something in search",
        colorScheme:"white",
        status: "warning",
        duration: 5000,
        isClosable: true,
        position: "bottom-left",
        variant: "solid",
      });
    }

    try {
      setLoading(true);

      const response = await fetch(`/server/api/user?search=${search}`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${user.token}`,
        },
      });
      const data = await response.json();

      setLoading(false);
      setSearchResult(data);
    } catch (error) {
      console.log(error);
      setLoading(false);
      return toast({
        title: "Error Occured!",
        description: "Failed to Load the Search Results",
        status: "error",
        duration: 5000,
        isClosable: true,
        position: "bottom-left",
        variant: "solid",
      });
    }
  };

  const accessChat = async (userId) => {
    try {
      setLoadingChat(true);

      const response = await fetch(`/server/api/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${user.token}`,
        },
        body: JSON.stringify({
          userId,
        }),
      });
      const data = await response.json();

      // If the chat already inside 'chat' state, append it
      if (!chats.find((c) => c._id === data._id)) setChats([data, ...chats]);

      setSelectedChat(data);
      setLoadingChat(false);
      onClose(); // Close the side drawer
    } catch (error) {
      setLoadingChat(false);
      return toast({
        title: "Error fetching the chat",
        description: error.message,
        status: "error",
        duration: 5000,
        isClosable: true,
        position: "bottom-left",
        variant: "solid",
      });
    }
  };
  return (
    <>
      {/* Chat Page UI */}
      <Box
        display="flex"
        justifyContent="space-between"
        alignItems="center"
        bgGradient="radial(ellipse at center, #000 0%, transparent 70%)"
        w="100%"
        p="5px 10px 5px 10px"
        borderWidth="5px"
      >
        {/* Search User Section */}
        <Tooltip label="Search users to chat" hasArrow placement="bottom-end">
          <Button variant="ghost" onClick={onOpen} _hover={{ backgroundColor: "#BF0451" }} >
            <i className="fas fa-search" />
            <Text display={{ base: "none", md: "flex"}} paddingX="2.5" className="searchButtonText">
              Search User
            </Text>
          </Button>
        </Tooltip>

        {/* App Name Section */}
        <Text fontSize="2xl" fontFamily="Orbitron" color={"white"}>
         DeFi Cosmos
        </Text>
        {/* <Link to='/chats' className="navlink">Chats</Link>
        <Link to='/home' className="navlink">Home</Link> */}
        {/* User Profile and Bell Icon Section */}
        <div>
        <Menu>
  <MenuButton p="1" className="notification-badge-container" >
    {/* Apply inline styling to make the icon pink */}
    <BellIcon fontSize="2xl" m="1" color="#ff3d61" />

    {notification.length > 0 && (
      <span className="notification-badge">
        {notification.length > 9 ? "9+" : notification.length}
      </span>
    )}
  </MenuButton>

  <MenuList>
    {!notification.length && <Text pl="2">No New Messages</Text>}
    {notification.map((notif) => (
      <MenuItem
        key={notif._id}
        onClick={() => {
          setSelectedChat(notif.chat[0]);
          setNotification(notification.filter((n) => n !== notif));
        }}
      >
        {notif.chat.isGroupChat
          ? `New Message in ${notif.chat[0].chatName}`
          : `New Message from ${getSender(
              user,
              notif.chat[0].users
            )}`}
        {/* Change chat[0] to chat from server side */}
      </MenuItem>
    ))}
  </MenuList>
</Menu>

          <Menu>
            <MenuButton as={Button} rightIcon={<ChevronDownIcon />} colorScheme={"black"}>
              <Avatar
                name={user.name}
                size="sm"
                cursor="pointer"
                src={user.pic}
              />
            </MenuButton>

            <MenuList bg={"black"}>
              <ProfileModal user={user}>
              <MenuItem bg= {"black"} color={"white"}  _hover={"pink"}
            // onMouseEnter={() => setSelectedOption("My Profile")}
            // onMouseLeave={() => setSelectedOption(null)}
          >My Profile</MenuItem>
              </ProfileModal>

              <MenuDivider />
              <MenuItem  bg={"black"} color={"white"} _hover={"pink"} onClick={logoutHandler} onMouseEnter={() => setSelectedOption("Logout")}
          onMouseLeave={() => setSelectedOption(null)}>Logout</MenuItem>
            </MenuList>
          </Menu>
        </div>
      </Box>
      <Drawer placement="left" isOpen={isOpen} onClose={onClose} className="space-background">
  {/* <DrawerOverlay /> */}
  <DrawerContent className="drawer-content">
    <DrawerCloseButton />
    <DrawerHeader className="drawer-header">Search Users</DrawerHeader>

    <DrawerBody className="drawer-body">
      {/* Search User */}
      <Box display="flex" pb="2">
        <Input
          className="drawer-input"
          placeholder="Search by name or email"
          mr="2"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <Button className="drawer-button" onClick={handleSearch} >
          Go
        </Button>
      </Box>

      {/* Populate Search Results */}
      {loading ? (
        <ChatLoading className="drawer-spinner" />
      ) : (
        searchResult?.map((user) => (
          <UserListItem
            key={user._id}
            user={user}
            handleFunction={() => accessChat(user._id)}
          />
        ))
      )}

      {/* if the chat has been created, don't show the loading */}
      {loadingChat && <Spinner className="drawer-spinner" ml="auto" d="flex" />}
    </DrawerBody>
  </DrawerContent>
</Drawer>


    </>
  );
};

export default SideDrawer;