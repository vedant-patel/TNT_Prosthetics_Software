import React, { useState, useEffect } from "react";
import handImage from "./prostheticHand.png";


function Slider({ id, value, onChange, shiftDown, shiftRight }) {
  const handleChange = (event) => {
    onChange(event.target.value);
  };

  return (
    <div style={{ height: "200px", display: "flex", flexDirection: "column", marginLeft:-50+shiftRight }}>
      <input
        type="range"
        min="0"
        max="180"
        value={value}
        onChange={handleChange}
        style={{ 
          height: "100%", 
          appearance: "slider-vertical", 
          background: "auto", 
          outline: "none", 
          marginTop: shiftDown}}
      />
      <div style={{ alignSelf: "center" }}>{`${id}:`}</div>
      <div style={{ alignSelf: "center "}}>{`${value}`}</div>
    </div>
  );
}


function App() {
  const [slider1Value, setSlider1Value] = useState(180);
  const [slider2Value, setSlider2Value] = useState(180);
  const [slider3Value, setSlider3Value] = useState(180);
  const [slider4Value, setSlider4Value] = useState(180);
  const [slider5Value, setSlider5Value] = useState(180);

  const [pressedKeys, setPressedKeys] = useState({});

  useEffect(() => {
    const handleKeyDown = (event) => {
      // Ensures that neither cmd and a slider control are true at the same time
      if(event.metaKey) {
        setPressedKeys((prevState) => ({
          ...prevState,
          [event.key]: false, [event.metaKey]:true
        }));
      } else {
        setPressedKeys((prevState) => ({
          ...prevState,
          [event.key]: true, [event.metaKey]:false
        }));
      }
    };
    const handleKeyUp = (event) => {

        setPressedKeys((prevState) => ({
          ...prevState,
          [event.key]: false,
        }));
    };
    document.addEventListener("keydown", handleKeyDown); //window.addEventListener(...)?
    document.addEventListener("keyup", handleKeyUp);
    return () => {
      document.removeEventListener("keydown", handleKeyDown);
      document.removeEventListener("keyup", handleKeyUp);
    };
  }, []);

  useEffect(() => {
    const incrementSlider1 = () => {
      setSlider1Value((prevValue) => Math.min(prevValue + 1, 180));
    };
    const decrementSlider1 = () => {
      setSlider1Value((prevValue) => Math.max(prevValue - 1, 0));
    };

    const incrementSlider2 = () => {
      setSlider2Value((prevValue) => Math.min(prevValue + 1, 180));
    };
    const decrementSlider2 = () => {
      setSlider2Value((prevValue) => Math.max(prevValue - 1, 0));
    };

    const incrementSlider3 = () => {
      setSlider3Value((prevValue) => Math.min(prevValue + 1, 180));
    };
    const decrementSlider3 = () => {
      setSlider3Value((prevValue) => Math.max(prevValue - 1, 0));
    };

    const incrementSlider4 = () => {
      setSlider4Value((prevValue) => Math.min(prevValue + 1, 180));
    };
    const decrementSlider4 = () => {
      setSlider4Value((prevValue) => Math.max(prevValue - 1, 0));
    };

    const incrementSlider5 = () => {
      setSlider5Value((prevValue) => Math.min(prevValue + 1, 180));
    };
    const decrementSlider5 = () => {
      setSlider5Value((prevValue) => Math.max(prevValue - 1, 0));
    };


    const intervalId = setInterval(() => {
      if (pressedKeys.q) {
        incrementSlider4();
      } if (pressedKeys.a) {
        decrementSlider4();
      }
      
      if (pressedKeys.w) {
        incrementSlider3();
      }  if (pressedKeys.s) {
        decrementSlider3();
      }

      if (pressedKeys.e) {
        incrementSlider2();
      }  if (pressedKeys.d) {
        decrementSlider2();
      }

      if (pressedKeys.r) {
        incrementSlider1();
      }  if (pressedKeys.f) {
        decrementSlider1();
      }

      if (pressedKeys.g) {
        incrementSlider5();
      }  if (pressedKeys.v) {
        decrementSlider5();
      }
    }, 15); //this was 50 ms, I changed to 15

    return () => {
      clearInterval(intervalId);
    };
  }, [pressedKeys]);

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center"}}>
      <div style={{ display: "flex", flexDirection:"row-reverse",  marginTop:50, marginBottom:25, marginLeft:40}}>
        <Slider id={"Thumb"} value={slider5Value} onChange={setSlider5Value} shiftDown={140} shiftRight={30}/>
        <Slider id={"Index"} value={slider1Value} onChange={setSlider1Value} shiftDown={60} shiftRight={0}/>
        <Slider id={"Middle"} value={slider2Value} onChange={setSlider2Value} shiftDown={0} shiftRight={0}/>
        <Slider id={"Ring"} value={slider3Value} onChange={setSlider3Value} shiftDown={60} shiftRight={0}/>
        <Slider id={"Pinky"} value={slider4Value} onChange={setSlider4Value} shiftDown={90} shiftRight={0}/>
      </div>
      <img src={handImage} alt="hand" style={{ width: "43%", height: "auto" }} />
  </div>
  );
}

export default App;


