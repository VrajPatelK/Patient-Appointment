import React, { useState } from "react";
import { sendNewMsgs } from "../chatApis";

const WriteMsg = ({ msgList, setRefresh, id, typing, setTyping }) => {
  const [val, setVal] = useState("");
  const handleSendMess = (e) => {
    e.preventDefault();
    setVal("");
    msgList.push({ c: val });
    setRefresh(1);
    setTyping(true);
    sendNewMsgs({ sender: id, message: val })
      .then((x) => x.map((m) => msgList.push({ bot: m.text })))
      .catch((e) => msgList.push({ bot: "Server Error" }))
      .finally(() => {
        setRefresh(1);
        setTyping(false);
      });
  };
  return (
    <>
      <form onSubmit={handleSendMess} className="sendMess">
        <input
          type="text"
          className="sendMessChat sendChatText"
          placeholder="Type here..."
          onChange={(e) => setVal(e.target.value)}
          value={val}
        />
        <input
          className="sendMessChat sendChatBnt"
          type="submit"
          value="Send"
        />
      </form>
    </>
  );
};

export default WriteMsg;
