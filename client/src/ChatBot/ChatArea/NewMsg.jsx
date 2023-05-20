import { Box, Button } from "@mui/material";
import React, { useEffect, useState } from "react";
import Messages from "./Messages";
import WriteMsg from "./WriteMsg";

const msgList = [
  //   {
  //     _id: 1,
  //     side: "a",
  //     message: "Hello Sir!",
  //   },
  //   {
  //     _id: 2,
  //     side: "a",
  //     message: "hello",
  //   },
];

const NewMsg = ({ id, conversationMsgs }) => {
  const [refresh, setRefresh] = useState(0);
  useEffect(() => {
    setRefresh(0);
  }, [refresh]);
  const [typing, setTyping] = useState(false);
  return (
    <>
      <Messages msgLst={conversationMsgs} />
      {typing && (
        <Box fontSize={"0.7rem"} px={1}>
          typing...
        </Box>
      )}
      {/* <FilterAsHome  typing={typing} setTyping={setTyping} /> */}
      
      <Box
        sx={{
          position: "absolute",
          bottom: 10,
        }}
      >
        <WriteMsg id={id} typing={typing} setTyping={setTyping} setRefresh={setRefresh} msgList={conversationMsgs} />
      </Box>
    </>
  );
};

export default NewMsg;
