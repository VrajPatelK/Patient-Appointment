import { Box } from "@mui/material";
import React from "react";
import FlexBetween from "../../Components/FlexBetween";
export default function Messages({ msgLst, typing }) {
  return (
    <>
      {msgLst.map((m, i) => (
        <MsgInstace
          key={i}
          side={!m["bot"]}
          msg={m["bot"] ? m["bot"] : m["c"]}
        />
      ))}
      {typing && <MsgInstace side={false} msg={"typing..."} />}
    </>
  );
}

const MsgInstace = ({ side, msg }) => {
  return (
    <FlexBetween fontSize={".9rem"}>
      {side ? (
        <>
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
        <Msg msg={msg} />
      )}
    </FlexBetween>
  );
};

const Msg = ({ msg, side }) => {
  return (
    <Box
      sx={{
        backgroundColor: "#55efc4",
        /* background-color: rgba(240, 248, 255, 0.555); */
        border: "1px solid rgb(187, 187, 187)",
        width: "80%",
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
