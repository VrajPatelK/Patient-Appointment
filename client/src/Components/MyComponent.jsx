import { useTheme } from "@emotion/react";
import { Button, Typography } from "@mui/material";
import React, { useMemo } from "react";

export const MyTitle = ({ title }) => {
  const theme = useTheme();
  return (
    <Typography
    width={"100%"}
      fontWeight={"bold"}
      fontSize={"1.5rem"}
      color={theme.palette.primary.main}
    >
      {title}
    </Typography>
  );
};


export const MyBtn = ({ onclickHandle, label = "x" }) => {
  const theme = useTheme();
  return (
    <Button
      fullWidth
      type="submit"
      onClick={onclickHandle}
      sx={{
        m: "1.2rem 0",
        p: "1rem",
        backgroundColor: theme.palette.primary.main,
        color: theme.palette.background.alt,
        "&:hover": { color: theme.palette.primary.main },
      }}
    >
      {label}
    </Button>
  );
};