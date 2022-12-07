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
      <div style={{ textAlign: "left" }}>
        <h1>
          SITE CERTIFICADO, MAS NAO POR UMA ENTIDADE REAL DE CERTIFICACAO.
        </h1>
        <h2>
          Você precisa usar um nome de domínio que você controle e que seja
          válido. Isso significa que você não pode usar autoridades de
          certificação reais para:
        </h2>
      </div>
      <div style={{ fontWeight: "bold", marginBottom: 20, textAlign: "left" }}>
        <li>
          localhost e outros nomes de domínio reservados, como example ou test.
          superior que não são válidos.
        </li>
        <li>Qualquer nome de domínio que você não controla.</li>
        <li>
          Domínios de nível superior que não são válidos.{" "}
          <a href="https://www.iana.org/domains/root/db">
            Veja a lista de domínios de nível superior válidos.
          </a>
        </li>
      </div>
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
