import { Box } from "@mui/material";
import { styled } from "@mui/system";

const WidgetWrapper = styled(Box)(({ theme }) => ({
  padding: "1rem 1rem 1rem 1rem",
  margin: "0.5rem",
  display: "flex",
  borderRadius: "0.75rem",
  backgroundColor: theme.palette.background.alt,
  transition: "height 10s",
}));

export default WidgetWrapper;
