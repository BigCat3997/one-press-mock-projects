import React from 'react';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import './App.css';
import logo from './logo.svg';
import Version from './Version';

function App() {
  return (
    <Router basename="/weather-forecast">
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {process.env.REACT_APP_MESSAGE}
          </p>
        </header>
        <Routes>
          <Route path="/version" element={<Version />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;