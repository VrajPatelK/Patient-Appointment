import React, { useState } from "react";
import chatBtnImg from "./chatIcon.png";
import { Box, IconButton } from "@mui/material";
import ChatBox from "./ChatArea/ChatBox";
// import { getdataFromLocalStorage, setdataFromLocalStorage } from "./chatApis";

export default function ChatBtn() {
  const [ChatAreaDisplay, setChatAreaDisplay] = useState(true);
  // eslint-disable-next-line
  const [conversationMsgs, setConversationMsgs] = useState([
    // FIRST MESSAGE HARDCODED ON CHATBOT SIDE
    {
      bot: "Hello Sir! I can check status of your appointment, cancel appointment and book appointment for you !",
    },
  ]);
  return (
    <Box
      sx={{
        position: "fixed",
        bottom: "1rem",
        right: "1rem",
      }}
    >
      {/* CHAT BUTTON ICON */}
      <IconButton
        sx={{
          padding: "0.2rem",
          cursor: "pointer",
        }}
        onClick={() => setChatAreaDisplay(!ChatAreaDisplay)}
      >
        <img src={chatBtnImg} style={{ width: "5rem" }} alt="" />
      </IconButton>
      {/* CHAT WINDOW */}
      {ChatAreaDisplay && (
        <>
          {/* CONTAINER TO CLOSE CHAT WINDOW WHEN USER CLICK ON ANYWHERE ON SCREEN INSTEAD OF CHAT WINDOW */}
          <Box
            sx={{
              height: "100vh",
              width: "100vw",
              top: 0,
              background: "rgba(0,0,0,0.25)",
              right: 0,
              zIndex: 3,
              position: "fixed",
              // border: "5px solid green",
            }}
            onClick={() => {
              setChatAreaDisplay(false);
            }}
          />
          {/* CHAT WINDOW CONTAINER */}
          <ChatBox conversationMsgs={conversationMsgs} />
        </>
      )}
    </Box>
  );
}
