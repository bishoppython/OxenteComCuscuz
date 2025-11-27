import React from 'react';
import Chatbot from './components/Chatbot';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Nutrição Nordestina</h1>
        <p>Chatbot especializado em nutrição com receitas nordestinas</p>
      </header>
      <main>
        <Chatbot />
      </main>
    </div>
  );
}

export default App;
