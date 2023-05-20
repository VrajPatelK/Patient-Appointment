import { useTheme } from "@emotion/react";
import Contact from "Pages/Contact/Contact";
import Home from "Pages/Home/Home";
import MyProject from "Pages/Projects/MyProject";
import FlexBetween from "./FlexBetween";

const PageSections = () => {
  const theme = useTheme();
  return (
    <FlexBetween
      sx={{ backgroundImage: `linear-gradient(120deg,${theme.palette.background.dark},${theme.palette.background.default})` }}
      flexDirection={"column"}
    >
      <Home />
      <MyProject />
      <Contact />
    </FlexBetween>
  );
};

export default PageSections;
