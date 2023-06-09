export const sendNewMsgs = async (data) => {

  const res = await fetch(`${process.env.REACT_APP_RASA}`, {
  // const res = await fetch(`http://localhost:5005/webhooks/rest/webhook`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  const rs = await res.json();
  return rs;
};
