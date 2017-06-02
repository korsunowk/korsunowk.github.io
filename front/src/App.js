import React, { Component } from 'react';

import logo from './logo.svg';
import './App.css';
import './styles/buttons.css'



class App extends Component {
  render() {
    return (
      <div className="App">
        <img src={logo} className="App-logo" alt="logo" />
        <div className="app-block">
          <h1>Welcome to Past participle helper</h1>
          <div className="buttons">
            <div className="button">Table with verbs forms</div>
            <div className="button">Test</div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
