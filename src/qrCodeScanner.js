var fs = require("fs");

const qrcode = window.qrcode;

const video = document.createElement("video");
const canvasElement = document.getElementById("qr-canvas");
const canvas = canvasElement.getContext("2d");

const qrResult = document.getElementById("qr-result");
const outputData = document.getElementById("outputData");
const btnScanQR = document.getElementById("btn-scan-qr");
const statusData = document.getElementById("statusData");

let scanning = false;

qrcode.callback = (res) => {
  if (res) {
    outputData.innerText = res;
    scanning = false;

    video.srcObject.getTracks().forEach((track) => {
      track.stop();
    });

    qrResult.hidden = false;
    canvasElement.hidden = true;
    btnScanQR.hidden = false;
  }
};

btnScanQR.onclick = () => {
  navigator.mediaDevices
    .getUserMedia({ video: { facingMode: "environment" } })
    .then(function (stream) {
      scanning = true;
      qrResult.hidden = true;
      btnScanQR.hidden = true;
      canvasElement.hidden = false;
      video.setAttribute("playsinline", true); // required to tell iOS safari we don't want fullscreen
      video.srcObject = stream;
      video.play();
      tick();
      scan();
    });
};

function tick() {
  canvasElement.height = video.videoHeight;
  canvasElement.width = video.videoWidth;
  canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);

  scanning && requestAnimationFrame(tick);
}

function scan() {
  try {
    qrcode.decode();
    statusData.textContent = "Could Not Find.";
    var text = fs.readFileSync("./tokens.txt").toString("utf-8");
    var textByLine = text.split(",");
    var scanned_content = outputData.innerText;
    console.log(textByLine);
    console.log(scanned_content);
    console.log(textByLine[0]);
    console.log(scanned_content === textByLine[0]);
    for (var x in textByLine) {
      console.log(textByLine[x]);
      console.log(typeof scanned_content);
      console.log(typeof textByLine[x]);
      if (scanned_content === textByLine[x]) {
        statusData.textContent = "Token Found!";
        textByLine.splice(x, 1);
        fs.writeFile("./tokens.txt", textByLine.join(), function () {
          console.log("Removed Token");
        });
        console.log("Found!");
      }
    }
  } catch (e) {
    setTimeout(scan, 1000);
  }
}
