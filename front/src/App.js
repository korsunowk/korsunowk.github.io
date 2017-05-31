import React, { Component } from 'react';

import logo from './logo.svg';
import './App.css';

import WordsTable from './components/table-words/table';


class App extends Component {
  render() {
    return (
      <div className="App">
        <img src={logo} className="App-logo" alt="logo" />
        <WordsTable />        
      </div>
    );
  }
}

export default App;
