import { Box } from "@mui/material";
import React, { useEffect, useState } from "react";
import Messages from "./Messages";
import WriteMsg from "./WriteMsg";

const NewMsg = ({ id, conversationMsgs }) => {
  // TO REFRESH THE CHATBOX
  const [refresh, setRefresh] = useState(0);
  useEffect(() => {
    setRefresh(0);
  }, [refresh]);
  // WHILE SERVER IS PROCCESSING TYPING VALUE WILL BE  true
  const [typing, setTyping] = useState(false);
  return (
    <>
      {/* TO DISPLAY MESSAGES  */}
      <Messages typing={typing} msgLst={conversationMsgs} />
      <Box
        sx={{
          position: "absolute",
          bottom: 10,
          width: "100%",
        }}
      >
        {/* TO WRITE A NEW MESSAGE  */}
        <WriteMsg
          id={id}
          typing={typing}
          setTyping={setTyping}
          setRefresh={setRefresh}
          msgList={conversationMsgs}
        />
      </Box>
    </>
  );
};

export default NewMsg;
