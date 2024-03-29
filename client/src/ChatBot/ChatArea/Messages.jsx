import { Box } from "@mui/material";
import React from "react";
import FlexBetween from "../../Components/FlexBetween";
export default function Messages({ msgLst, typing }) {
  return (
    <>
      {/* // TO DISPLAY ALL MESSAGES FROM THE OBJECT  */}
      {msgLst.map((m, i) => (
        <MsgInstace
          key={i}
          side={!m["bot"]}
          msg={m["bot"] ? m["bot"] : m["c"]}
        />
      ))}
      {/* TO DISPLAY "typing..." WHILE SERVER IS PROCCESSING ON DATA */}
      {typing && <MsgInstace side={false} msg={"typing..."} />}
    </>
  );
}

const MsgInstace = ({ side, msg }) => {
  return (
    <FlexBetween fontSize={".9rem"}>
      {side ? (
        <>
          {/* USER SIDE */}
          {/* TO DISPLAY MESSAGE ON RIGHT SIDE  */}
          <Box flexGrow={1}></Box>
          <Msg
            msg={msg}
            side={{
              float: "right",
              backgroundColor: "rgba(147, 135, 135, 0.696)",
            }}
          />
        </>
      ) : (
        <>
          {/* CHATBOT SIDE */}
          <Msg msg={msg} />
        </>
      )}
    </FlexBetween>
  );
};

const Msg = ({ msg, side }) => {
  return (
    <Box
      sx={{
        backgroundColor: "#55efc4",
        maxWidth: "80%",
        clear: "both",
        color: "#2d3436",
        margin: "0.5rem",
        padding: "0.5rem",
        borderRadius: "0.3rem",
        border: "none",
        outline: "none !important",
      }}
      style={side}
    >
      {msg}
    </Box>
  );
};
