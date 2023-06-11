import { useTheme } from "@emotion/react";
import {
  Autocomplete,
  Box,
  Button,
  TextField,
  Tooltip,
  Typography,
} from "@mui/material";
import React from "react";
export const SelectAutoComplete = ({
  msg,
  setInputVal,
  options,
  label,
  value,
  req = true,
}) => {
  return (
    <Tooltip title={msg}>
      <Autocomplete
        sx={{ width: "100%" }}
        options={options}
        autoHighlight
        value={value}
        getOptionLabel={(option) => option}
        onInputChange={(e, newInputValue) => {
          setInputVal(newInputValue, String(label).replace(" ", ""));
        }}
        renderOption={(props, option) => (
          <Box
            component="li"
            sx={{ width: "100%" }}
            // sx={{ "& > img": { mr: 2, flexShrink: 0 } }}
            {...props}
          >
            {option}
          </Box>
        )}
        renderInput={(params) => (
          <TextField
            required={req}
            value={value}
            {...params}
            label={
              String(label).charAt(0).toUpperCase() + String(label).substring(1)
            }
          />
        )}
      />
    </Tooltip>
  );
};


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