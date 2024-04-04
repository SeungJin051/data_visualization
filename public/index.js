const express = require("express");
const app = express();

app.get("/", function (req, res) {
  return res.send("hel2211lo world");
});

app.listen(3000, function () {
  console.log("server listening on port 3000");
});
