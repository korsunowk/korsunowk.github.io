import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  NavLink
} from 'react-router-dom'

import RandomTest from './tests/random-test/random-test';
import AlternateTest from './tests/alternate-test/alternate-test';

import '../../styles/test-block.css';


export default class TestBlock extends React.Component {
    render () {
        return (
          <Router>
            <div className="test-block">
              <div className="test-buttons">
                <NavLink to="/tests/random" activeClassName="active">
                  <div className="test-button">
                    Test with random verbs
                  </div>
                </NavLink>
                <NavLink to="/tests/alternate" activeClassName="active">
                  <div className="test-button">
                    Test with alternate verbs
                  </div>
                </NavLink>
              </div>

              <Route path="/tests/random" component={RandomTest} />
              <Route path="/tests/alternate" component={AlternateTest} />
            </div>
          </Router>
            
            )
    }
}