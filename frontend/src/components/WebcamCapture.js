import { useState, useRef, useCallback } from "react";

const WebcamCapture = () =>{
    const webcamRef = useRef(null);
    const [imgSrc, setImgSrc] = useState(null);

    const capture = useCallback(() =>{
        const imageSrc = webcamRef.current.getScreenShoot();
        setImgSrc(imageSrc);
    }, [webcamRef, setImgSrc]);
}

export default WebcamCapture;