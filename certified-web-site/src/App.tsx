import { useState } from "react";
import reactLogo from "./assets/react.svg";
import "./App.css";
import img from "../public/meme_1.png";
import img2 from "../public/meme_2.png";
import img3 from "../public/confia.jpeg";

function App() {
  const [show, setShow] = useState(false);

  const mostrarAlgo = () => {
    if (show) {
      setShow(false);
    } else {
      setShow(true);
    }
  };

  return (
    <div className="App">
      <h1>SITE CERTIFICADO, CONFIA NI MIM ALEX.</h1>
      <h2>AQUI NAO TEM PRA VIRUS E NEM HACKER MEU FI</h2>
      <button onClick={mostrarAlgo}>CLIQUE AQUI POR GENTILEZA</button>
      <h3>TU É RAQUE MEMO</h3>
      {!show ? (
        <img src={img} width={500} alt="" />
      ) : (
        <img src={img3} width={500} alt="" />
      )}
    </div>
  );
}

export default App;
