import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  NavLink
} from 'react-router-dom'

import WordsTable from './components/table-words/table';
import TestBlock from './components/table-tests/test-block';

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
          <Router>      
            <div>
              <div className="buttons">
                <NavLink to='/table' activeClassName="active"><div className="button">Table with verbs forms</div></NavLink>
                <NavLink to='/test' activeClassName="active"><div className="button">Test</div></NavLink>
              </div>

              <Route path="/table" component={WordsTable}/>
              <Route path="/test" component={TestBlock}/>
            </div>
          </Router>
        </div>
        {/*<footer>
          My site
        </footer>*/}
      </div>
    );
  }
}

export default App;
