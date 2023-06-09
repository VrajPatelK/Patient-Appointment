import React, { useEffect, useState } from "react";
import chatBtnImg from "./chatIcon.png";
import "./Chat.css";
import { Box, IconButton } from "@mui/material";
import ChatBox from "./ChatArea/ChatBox";
// import { getdataFromLocalStorage, setdataFromLocalStorage } from "./chatApis";

export default function ChatBtn() {
  const [ChatAreaDisplay, setChatAreaDisplay] = useState(true);

  const [conversationMsgs, setConversationMsgs] = useState([
    { bot: "Hello Sir! I can Check Status Of your Appointment" },
    { c: "Hello " },
  ]);
  // useEffect(() => {
  //   const dt = getdataFromLocalStorage();
  //   setConversationMsgs(dt);
  // }, []);

  return (
    <Box
      sx={{
        position: "fixed",
        bottom: "1rem",
        right: "1rem",
      }}
    >
      <IconButton
        sx={{
          padding: "0.2rem",
          cursor: "pointer",
        }}
        onClick={() => setChatAreaDisplay(!ChatAreaDisplay)}
      >
        <img src={chatBtnImg} style={{ width: "5rem" }} alt="" />
      </IconButton>
      {ChatAreaDisplay && (
        <>
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
          <ChatBox conversationMsgs={conversationMsgs} />
        </>
      )}
    </Box>
  );
}
