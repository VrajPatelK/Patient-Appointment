import React, { useMemo } from "react";
import { useSelector } from "react-redux";
import { CssBaseline, ThemeProvider } from "@mui/material";
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
        {/* TO ADD CHAT BUTTON ON HOME SCREEN (CHAT BUTTON COMPONENT) */}
        <ChatBtn />
      </ThemeProvider>
    </FlexBetween>
  );
};

export default App;
