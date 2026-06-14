import { useState, useEffect, useRef } from "react";
import mermaid from "mermaid";

function App() {
  const [code, setCode] = useState("");
  const [language, setLanguage] = useState("python");
  const [result, setResult] = useState(null);

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const mermaidRef = useRef(null);

  useEffect(() => {
    mermaid.initialize({
      startOnLoad: true,
      securityLevel: "loose",
    });
  }, []);

  useEffect(() => {
    if (!result?.flowchart || !mermaidRef.current) return;

    const items = result.flowchart;

    let chart = "graph TD\n";

    for (let i = 0; i < items.length; i++) {
      chart += `N${i}["${items[i]}"]\n`;

      if (i < items.length - 1) {
        chart += `N${i} --> N${i + 1}\n`;
      }
    }

    mermaid
      .render("flowchartGraph", chart)
      .then(({ svg }) => {
        mermaidRef.current.innerHTML = svg;
      })
      .catch((err) => {
        console.error(err);
      });
  }, [result]);

  // ANALYZE CODE
  const analyzeCode = async () => {
    const res = await fetch("http://127.0.0.1:8000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        code,
        language
      }),
    });

    const data = await res.json();
    setResult(data);
  };

  // CHATBOT
  const askAI = async () => {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        question,
      }),
    });

    const data = await res.json();
    setAnswer(data.answer);
  };

  // DOWNLOAD PDF
  const downloadPDF = async () => {
    const res = await fetch("http://127.0.0.1:8000/download-pdf", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        code,
        language,
      }),
    });

    const blob = await res.blob();

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "analysis_report.pdf";

    document.body.appendChild(a);
    a.click();
    a.remove();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>🚀 AI Code Flow Mapper</h1>

      <h3>Select Language</h3>

      <select
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
      >
        <option value="python">Python</option>
        <option value="java">Java</option>
        <option value="c">C</option>
        <option value="cpp">C++</option>
      </select>

      <br />
      <br />

      <textarea
        rows="12"
        cols="80"
        value={code}
        placeholder="Paste your code here..."
        onChange={(e) => setCode(e.target.value)}
      />

      <br />
      <br />

      <button onClick={analyzeCode}>
        Analyze Code
      </button>

      <button
        onClick={downloadPDF}
        style={{ marginLeft: "10px" }}
      >
        Download PDF
      </button>

      {result && (
        <div>

          <h2>Functions</h2>

          {result.functions?.map((f, i) => (
            <div key={i}>
              👉 {f.name}
              <br />
              Parameters: {f.parameters}
              <br />
              {f.explanation}
              <br />
              <br />
            </div>
          ))}

          <h2>Classes</h2>

          {result.classes?.map((c, i) => (
            <div key={i}>
              👉 {c.name}
            </div>
          ))}

          <h2>Imports</h2>

          {result.imports?.map((imp, i) => (
            <div key={i}>
              👉 {imp}
            </div>
          ))}

          <h2>Viva Questions</h2>

          {result.viva_questions?.map((q, i) => (
            <div key={i}>
              <b>{q.question}</b>
              <br />
              Answer: {q.answer}
              <br />
              <br />
            </div>
          ))}

          <h2>Project Tree</h2>

          {result.project_tree?.map((item, i) => (
            <div key={i}>
              {item}
            </div>
          ))}

          <h2>Graphical Flowchart</h2>

          <div
            ref={mermaidRef}
            style={{
              padding: "20px",
              border: "1px solid #ccc",
              background: "#ffffff",
              marginTop: "10px",
              overflowX: "auto",
            }}
          />

          {result.complexity_analysis && (
            <>
              <h2>Code Complexity Analysis</h2>

              <p>
                Lines of Code:{" "}
                {result.complexity_analysis.lines_of_code}
              </p>

              <p>
                Functions:{" "}
                {result.complexity_analysis.functions}
              </p>

              <p>
                Classes:{" "}
                {result.complexity_analysis.classes}
              </p>

              <p>
                Imports:{" "}
                {result.complexity_analysis.imports}
              </p>

              <p>
                Complexity:{" "}
                {result.complexity_analysis.complexity}
              </p>
            </>
          )}

          {result.code_quality && (
            <>
              <h2>Code Quality Score</h2>

              <p>
                Score: {result.code_quality.score}/100
              </p>

              {result.code_quality.suggestions?.map(
                (s, i) => (
                  <div key={i}>
                    👉 {s}
                  </div>
                )
              )}
            </>
          )}
        </div>
      )}

      <hr />

      <h2>💬 AI Chatbot</h2>

      <input
        type="text"
        value={question}
        placeholder="Ask question..."
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        onClick={askAI}
        style={{ marginLeft: "10px" }}
      >
        Ask AI
      </button>

      <p>{answer}</p>
    </div>
  );
}

export default App;