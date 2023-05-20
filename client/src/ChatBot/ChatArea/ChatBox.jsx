import { Box, useMediaQuery } from "@mui/material";
import React, { useEffect, useRef, useState } from "react";
import NewMsg from "./NewMsg";

const ChatBox = ({ conversationMsgs }) => {
  const msgContainerRef = useRef(null);
  const [id, setId] = useState(new Date().getTime());

  const isNonMobileScreens = useMediaQuery("(min-width: 367px)");

  useEffect(() => {
    if (msgContainerRef.current) {
      const container = msgContainerRef.current;
      container.scrollTop = container.scrollHeight - container.clientHeight;
      const observer = new MutationObserver(() => {
        container.scrollTop = container.scrollHeight - container.clientHeight;
      });
      observer.observe(container, {
        attributes: true,
        childList: true,
        subtree: true,
      });
    }
  }, []);

  return (
    <Box
      sx={{
        zIndex: "25",
        position: "absolute",
        background: "rgba(187, 187, 187, 0.837)",
        bottom: "2rem",
        padding: "0.8rem",
        borderRadius: "1rem",
        border: "2px solid rgba(128, 128, 128, 0.281)",
        right: "2rem",
      }}
    >
      {/* {id ? ( */}
      <Box sx={{ overflow: "auto" }}>
        <h1
          style={{
            textDecoration: "underline",
            textAlign: "center",
            margin: "0.2rem",
            width: "100%",
          }}
        >
          Chat Bot
        </h1>
        <Box
          sx={{
            height: "25rem",
            width: isNonMobileScreens ? "17rem" : "70vw",
            overflow: "auto",
            marginBottom: "1.2rem",
          }}
          ref={msgContainerRef}
        >
          <NewMsg id={id} conversationMsgs={conversationMsgs} />
        </Box>
      </Box>
      {/* ) : ( */}
      <>{/* <Login setId={setId} /> */}</>
      {/* )} */}
    </Box>
  );
};

export default ChatBox;
