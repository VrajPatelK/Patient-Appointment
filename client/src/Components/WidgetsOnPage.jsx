import { useTheme } from "@emotion/react";
import { Box, Typography, useMediaQuery } from "@mui/material";

import React from "react";
import NavBar from "../Pages/admin/NavBar";
import FlexBetween from "./FlexBetween";

const WidgetsOnPage = ({ title, leftComponent, rightComponent }) => {
  const theme = useTheme();
  const isNonMobileScreens = useMediaQuery("(min-width:1000px)");
  return (
    <FlexBetween flexDirection={"column"} width={"100%"}>
      {title && (
        <Box
          width={"100%"}
          p={"1rem 6%"}
          textAlign="center"
          backgroundColor={theme.palette.background}
        >
          <Typography
            fontWeight={"bold"}
            fontSize={"1.5rem"}
            color={theme.palette.neutral.main}
          >
            {title}
          </Typography>
        </Box>
      )}
      <Box
        width="100%"
        padding="2rem 6%"
        display={isNonMobileScreens ? "flex" : "block"}
        gap="2rem"
        justifyContent="center"
      >
        <Box flexBasis={isNonMobileScreens ? "30%" : undefined}>
          {leftComponent}
          <Box m="1rem 0" />
        </Box>
        <Box
          flexBasis={isNonMobileScreens ? "60%" : undefined}
          mt={isNonMobileScreens ? undefined : "2rem"}
        >
          {rightComponent}
        </Box>
      </Box>
    </FlexBetween>
  );
};

export default WidgetsOnPage;
