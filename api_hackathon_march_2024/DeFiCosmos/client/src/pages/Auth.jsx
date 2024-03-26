import {
  Container,
  Box,
  Text,
  Tab,
  TabList,
  TabPanel,
  TabPanels,
  Tabs,
} from "@chakra-ui/react";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

import { Login, Signup } from "../components";
import "./auth.css";
const Home = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const userInfo = JSON.parse(localStorage.getItem("userInfo"));

    if (!userInfo) {
      navigate("/");
    }
  }, [navigate]);

  return (
    <Container maxWidth="xl" >
      <Box
        d="flex"
        justifyContent="center"
        p={3}
        
        w="100%"
        m="40px 0 15px 0"
        borderRadius="lg"
        borderWidth="1px"
      >
        <Text className="text-pink" fontSize="4xl" textAlign="center">
          DeFi Cosmos
        </Text>
      </Box>

      <Box w="100%" p={4} borderWidth="4px">
        <Tabs isFitted variant="soft-rounded">
          <TabList mb="1em">
            <Tab variant="solid">LOGIN</Tab>
            <Tab variant="solid">SIGN UP</Tab>
          </TabList>
          <TabPanels>
            <TabPanel>
              <Login />
            </TabPanel>
            <TabPanel>
              <Signup />
            </TabPanel>
          </TabPanels>
        </Tabs>
      </Box>
    </Container>
  );
};

export default Home;
