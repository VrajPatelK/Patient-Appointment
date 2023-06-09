import SendIcon from "@mui/icons-material/Send";
import React, { useState } from "react";
import { sendNewMsgs } from "../chatApis";
import { Box, Button, IconButton, TextField } from "@mui/material";
import { MyBtn } from "../../Components/MyComponent";
import FlexBetween from "../../Components/FlexBetween";

const WriteMsg = ({ msgList, setRefresh, id, typing, setTyping }) => {
  const [val, setVal] = useState("");
  const handleSendMess = (e) => {
    e.preventDefault();
    setVal("");
    msgList.push({ c: val });
    setRefresh(1);
    setTyping(true);
    sendNewMsgs({ sender: id, message: val })
      .then((x) => x.map((m) => msgList.push({ bot: m.text })))
      .catch((e) => msgList.push({ bot: "Server Error" }))
      .finally(() => {
        setRefresh(1);
        setTyping(false);
      });
  };
  return (
    <>
      <form
        onSubmit={handleSendMess}
        style={{
          // ,

          width: "97%",
        }}
      >
        <FlexBetween>
          <TextField
            type="text"
            sx={{
              flexGrow: "1",
              outline: "0 !important",
              border: "transparent",
              marginRight: "0.1rem",
              fontSize: "0.9rem",
              borderBottomLeftRadius: "0.8rem",
              background: "#00000079",
            }}
            InputProps={{
              disableUnderline: true,
            }}
            placeholder="Type here..."
            onChange={(e) => setVal(e.target.value)}
            value={val}
          />
          <IconButton type="submit" sx={{ borderBottomRightRadius: "0.8rem" }}>
            <SendIcon />
          </IconButton>
        </FlexBetween>
      </form>
    </>
  );
};

export default WriteMsg;
