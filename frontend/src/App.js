import { BrowserRouter, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import Webcam from "react-webcam";

import './App.css';
import WebcamCapture from "./components/WebcamCapture";
function App() {
  return (
    <div className="page-container">
      <div className="content-wrap">
        <>
        <Webcam
          audio={false}
          ref={WebcamCapture.webcamRef}
          screenshotFormat="image/jpeg"/>
        <button onClick={WebcamCapture.capture}>Capture photo</button>
        {WebcamCapture.imgSrc && <img src={WebcamCapture.imgSrc}/>}
        </>
      </div>
    </div>
  );
}

export default App;
