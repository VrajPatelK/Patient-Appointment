import { Box, useMediaQuery } from "@mui/material";
import React, { useEffect, useRef, useState } from "react";
import NewMsg from "./NewMsg";

const ChatBox = ({ conversationMsgs }) => {
  const msgContainerRef = useRef(null);
  //  GENERATE NEW USERID FOR EVERYTIME SOMEONE START CHAT WITH CHATBOT USING MILISECOND TIME FUNCTION
  // (NOTE: IT'S ONLY FOR SENDING DATA TO BACKEND AS IT'S REQUIRED TO SEND DATA TO BACKEND. WE ARE NOT SAVING IT ANYWHERE)
  const [id, setId] = useState(new Date().getTime());
  //  TO MAKE MOBILE RESPONSIVE
  const isNonMobileScreens = useMediaQuery("(min-width: 600PX)");

  useEffect(() => {
    // FUNCTION TO SCROLL UPTO LAST MESSAGE
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
        {/* MESSAGE CONTAINER */}
        <Box
          sx={{
            height: "70vh",
            width: isNonMobileScreens ? "35rem" : "70vw",
            overflow: "auto",
            marginBottom: "2.4rem",
          }}
          ref={msgContainerRef}
        >
          {/* MESSAGE CONTAINER FOR WRITE NEW MESSAGE AND DISPLAY ALL MESSAGES */}
          <NewMsg id={id} conversationMsgs={conversationMsgs} />
        </Box>
      </Box>
    </Box>
  );
};

export default ChatBox;
