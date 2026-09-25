import { useState } from "react";
import "./App.css";

export default function App() {
  const [titulo, setTitulo] = useState("");
  const [mensagem, setMensagem] = useState("");
  const [estado, setEstado] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    const valor = titulo.trim();

    if (!valor) {
      setEstado("erro");
      setMensagem("O título é obrigatório.");
      return;
    }

    setEstado("sucesso");
    setMensagem(`Salvo: ${valor}`);
    setTitulo("");
  }

  function handleChange(event) {
    setTitulo(event.target.value);
    setMensagem("");
    setEstado("");
  }

  return (
    <main className="pagina">
      <section className="cartao" aria-labelledby="titulo-pagina">
        <p className="sobretitulo">Protótipo convertido em React</p>
        <h1 id="titulo-pagina">Registrar item</h1>
        <p>Preencha o título e salve para ver o resultado.</p>

        <form onSubmit={handleSubmit} noValidate>
          <label htmlFor="titulo">Título</label>

          <input
            id="titulo"
            name="titulo"
            type="text"
            value={titulo}
            onChange={handleChange}
            aria-invalid={estado === "erro"}
            aria-describedby={estado === "erro" ? "feedback" : undefined}
          />

          <button type="submit" data-testid="acao-principal">
            Salvar
          </button>
        </form>

        {mensagem && (
          <p
            id="feedback"
            className={`feedback feedback--${estado}`}
            role={estado === "erro" ? "alert" : "status"}
          >
            {mensagem}
          </p>
        )}
      </section>
    </main>
  );
}