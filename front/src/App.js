import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import One from './components/one'

var words = require('./words.json');

class App extends Component {
  render() {
    let rows = new Array();
    for(let i=1; i<=Object.keys(words).length; i++) {
      rows.push(
        <One russian={words[i]['russian_translate']} 
             infinitive={words[i]['infinitive']}
             past_simple={words[i]['past_simple']}
             perfect={words[i]['perfect']}
             key={i}
        />
      )
    }
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <table>
          <tbody>
           {rows}
          </tbody>
        </table>
      </div>
    );
  }
}

export default App;
