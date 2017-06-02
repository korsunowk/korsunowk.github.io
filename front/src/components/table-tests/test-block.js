import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom'


export default class TestBlock extends React.Component {
    render () {
        return (
            <div className="test-buttons">
              <Link to="/random">
                <div className="test-button">
                  Test with randow verbs
                </div>
              </Link>
              <Link to="/alternate">
                <div className="test-button">
                  Test with alternate verbs
                </div>
              </Link>

              <Route path="/random"/>
              <Route path="/alternate"/>
            </div>
            )
    }
}