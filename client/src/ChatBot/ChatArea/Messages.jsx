import { Box } from "@mui/material";
import React from "react";
export default function Messages({ msgLst }) {
  return (
    <>
      {msgLst.map((m, i) => (
        <Box key={i} fontSize={"0.7rem"}>
          {m["c"] ? (
            <p className="mess visitor">{m["c"]}</p>
          ) : (
            <p className="mess me">{m["bot"]}</p>
          )}
        </Box>
      ))}
    </>
  );
}
