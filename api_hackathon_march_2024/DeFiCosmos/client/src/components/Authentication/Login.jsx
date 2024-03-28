import React, { useState } from "react";
import {
  Button,
  FormControl,
  FormLabel,
  Input,
  InputGroup,
  InputRightElement,
  Stack,
  color,
  useToast,
} from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import "./login.css";

const Login = () => {
  const [show, setShow] = useState(false);
  const [loading, setLoading] = useState(false);

  const toast = useToast();
  const navigate = useNavigate();

  const [credentials, setCredentials] = useState({
    email: "",
    password: "",
  });

  const handleCredentials = (e) => {
    setCredentials({ ...credentials, [e.target.name]: e.target.value });
  };

  const submitHandler = async () => {
    setLoading(true);

    // If email or password is missing
    if (!credentials.email || !credentials.password) {
      toast({
        title: "Please Fill all the Fields",
        status: "warning",
        duration: 5000,
        isClosable: true,
        position: "bottom-right",
        variant: "left-accent",
      });
      setLoading(false);
      return;
    }

    try {
      const response = await fetch("/server/api/user/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: credentials.email,
          password: credentials.password,
        }),
      });
      const data = await response.json();
      toast({
        title: data.message,
        status: !data.success ? "error" : "success",
        duration: 5000,
        isClosable: true,
        position: "bottom-right",
        variant: !data.success ? "left-accent" : "solid",
      });

      if (data.success) {
        localStorage.setItem("userInfo", JSON.stringify(data));
        // Redirect to wallet page on successful login
        setLoading(false);
        navigate("/wallet");
      } else {
        setLoading(false);
      }
    } catch (error) {
      setLoading(false);
      return toast({
        title: "Internal server error",
        status: "error",
        duration: 5000,
        isClosable: true,
        position: "bottom-right",
        variant: "solid",
      });
    }
  };

  return (
    <div className="login-container">
      <Stack spacing="6" p="6" borderRadius="md" bg="transparent">
        <Stack spacing="5">
          <FormControl isRequired>
            <FormLabel htmlFor="email" color="yellow">
              Email
            </FormLabel>
            <Input
              type="email"
              color={"white"}
              name="email"
              value={credentials.email}
              placeholder="Enter Your Email"
              onChange={(e) => handleCredentials(e)}
            />
          </FormControl>
        </Stack>

        <Stack spacing="5">
          <FormControl isRequired>
            <FormLabel htmlFor="password" color="yellow">
              Password
            </FormLabel>
            <InputGroup>
              <InputRightElement w="4.5rem">
                <Button h="1.75rem" size="sm" onClick={() => setShow(!show)}>
                  {show ? "Hide" : "Show"}
                </Button>
              </InputRightElement>
              <Input
                type={show ? "text" : "password"}
                name="password"
                value={credentials.password}
                placeholder="Password"
                onChange={(e) => handleCredentials(e)}
                style={{color: 'white'}}
              />
            </InputGroup>
          </FormControl>
        </Stack>

        <Button
          colorScheme="pink"
          width="100%"
          style={{ marginTop: 15 }}
          onClick={submitHandler}
          isLoading={loading}
        >
          Login
        </Button>

        <Button
          variant="solid"
          colorScheme="red"
          width="100%"
          onClick={() => {
            setCredentials({
              email: "guest@example.com",
              password: "12345678",
            });
          }}
        >
          <i
            className="fas fa-user-alt"
            style={{ fontSize: "15px", marginRight: 8 }}
          />{" "}
          Get Guest User Credentials
        </Button>
      </Stack>
    </div>
  );
};

export default Login;
