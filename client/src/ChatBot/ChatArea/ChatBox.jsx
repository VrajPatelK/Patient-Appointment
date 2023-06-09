import { Box, useMediaQuery } from "@mui/material";
import React, { useEffect, useRef, useState } from "react";
import NewMsg from "./NewMsg";

const ChatBox = ({ conversationMsgs }) => {
  const msgContainerRef = useRef(null);
  const [id, setId] = useState(new Date().getTime());

  const isNonMobileScreens = useMediaQuery("(min-width: 600PX)");

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
        background: "#f1f2f6",
        padding: "0.5rem",
        borderRadius: "1rem",
        border: "2px solid rgba(128, 128, 128, 0.81)",
        bottom: "2rem",
        right: "2rem",
      }}
    >
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
            height: "70vh",
            width: isNonMobileScreens ? "35rem" : "70vw",
            overflow: "auto",
            marginBottom: "2.4rem",
          }}
          ref={msgContainerRef}
        >
          <NewMsg id={id} conversationMsgs={conversationMsgs} />
        </Box>
      </Box>
    </Box>
  );
};

export default ChatBox;
