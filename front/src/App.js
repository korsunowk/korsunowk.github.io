import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  NavLink
} from 'react-router-dom'

import WordsTable from './components/table-words/table';
import TestBlock from './components/table-tests/test-block';

import RandomTest from './components/table-tests/tests/random-test/random-test';
import AlternateTest from './components/table-tests/tests/alternate-test/alternate-test';

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
                <NavLink to='/table' activeClassName="active">
                  <div className="button">Table with verbs forms</div>
                </NavLink>
                <div className="btn-group">
                  <div className="button dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Some tests <span className="caret"></span>
                  </div>
                  <TestBlock />
                </div>
              </div>

              <Route path="/tests/random" component={RandomTest} />
              <Route path="/tests/alternate" component={AlternateTest} />
              <Route path="/table" component={WordsTable}/>
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
