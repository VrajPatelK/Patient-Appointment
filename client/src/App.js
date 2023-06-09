import React, { useMemo } from "react";
import { useSelector } from "react-redux";
import { Box, CssBaseline, ThemeProvider } from "@mui/material";
import { createTheme } from "@mui/material/styles";
import { themeSettings } from "./theme";
import ChatBtn from "./ChatBot/ChatBtn";
import FlexBetween from "./Components/FlexBetween";

const App = () => {
  const mode = useSelector((state) => state.mode);
  const theme = useMemo(() => createTheme(themeSettings(mode)), [mode]);

  return (
    <FlexBetween height={"100%"} sx={{ background: "#6693fc" }}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <ChatBtn />
      </ThemeProvider>
    </FlexBetween>
  );
};

export default App;
