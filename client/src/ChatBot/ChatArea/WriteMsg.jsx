import SendIcon from "@mui/icons-material/Send";
import React, { useState } from "react";
import { sendNewMsgs } from "../chatApis";
import { Box, Button, IconButton, Select, TextField } from "@mui/material";
import { MyBtn, SelectAutoComplete } from "../../Components/MyComponent";
import FlexBetween from "../../Components/FlexBetween";

const WriteMsg = ({ msgList, setRefresh, id, typing, setTyping }) => {
  const [selectList, setSelectList] = useState([]);
  const [val, setVal] = useState("");
  const handleSendMess = (e) => {
    e.preventDefault();
    if (val === "") {
      setTyping(true);
      selectList.length === 0
        ? msgList.push({ bot: "Type Message and Hit The Enter" })
        : msgList.push({ bot: "Select Option and Hit The Enter" });
      setRefresh(1);
      setTyping(false);
    } else {
      msgList.push({ c: val });
      setRefresh(1);
      setTyping(true);
      sendNewMsgs({ sender: id, message: val })
        .then((x) =>
          x.map((m) => {
            // m.text = 'Select Time ["1","2"]';
            // m.text = "Select Time ['1','2']";
            const indOfOpenSqrBrk = String(m.text).indexOf("[");
            if (indOfOpenSqrBrk === -1) {
              msgList.push({ bot: m.text });
              setSelectList([]);
            } else {
              msgList.push({
                bot: String(m.text).substring(0, indOfOpenSqrBrk),
              });
              // console.log(String(m.text).substring(indOfOpenSqrBrk));
              let tmpStr = String(m.text).substring(indOfOpenSqrBrk);
              while (tmpStr.indexOf("'") !== -1)
                tmpStr = tmpStr.replace("'", '"');
              const lst = JSON.parse(tmpStr);
              // console.log(lst);
              setSelectList(lst);
            }
          })
        )
        .catch((e) => {
          msgList.push({ bot: "Server Error" });
        })
        .finally(() => {
          setRefresh(1);
          setTyping(false);
        });
      setVal("");
    }
  };

  return (
    <>
      {selectList.length > 0 ? (
        <>
          <FlexBetween width={"97%"}>
            <SelectAutoComplete
              label={"Select"}
              value={val}
              setInputVal={setVal}
              msg={"Select From Here"}
              options={selectList}
            />
            <IconButton
              disabled={typing}
              onClick={handleSendMess}
              sx={{ borderBottomRightRadius: "0.8rem" }}
            >
              <SendIcon />
            </IconButton>
          </FlexBetween>
        </>
      ) : (
        <form
          onSubmit={handleSendMess}
          style={{
            // ,

            width: "97%",
          }}
        >
          <FlexBetween>
            <TextField
              type="text"
              sx={{
                flexGrow: "1",
                outline: "0 !important",
                border: "transparent",
                marginRight: "0.1rem",
                fontSize: "0.9rem",
                borderBottomLeftRadius: "0.8rem",
                background: "#00000079",
              }}
              disabled={typing}
              InputProps={{
                disableUnderline: true,
              }}
              placeholder="Type here..."
              onChange={(e) => setVal(e.target.value)}
              value={val}
            />
            <IconButton
              type="submit"
              disabled={typing}
              sx={{ borderBottomRightRadius: "0.8rem" }}
            >
              <SendIcon />
            </IconButton>
          </FlexBetween>
        </form>
      )}
    </>
  );
};

export default WriteMsg;
