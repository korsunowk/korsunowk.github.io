import React from 'react';
import {NavLink} from 'react-router-dom'

import '../../styles/test-block.css';


export default class TestBlock extends React.Component {
    render () {
        return (
          <ul className="dropdown-menu">
            <NavLink to="/tests/random" activeClassName="active">
              <li className="test-button">
                Test with random verbs
              </li>
            </NavLink>
            <li role="separator" className="divider"></li>
            <NavLink to="/tests/alternate" activeClassName="active">
              <li className="test-button">
                Test with alternate verbs
              </li>
            </NavLink>
            <li role="separator" className="divider"></li>
            <NavLink to="/tests/random-translate" activeClassName="active">
              <li className="test-button">
                 Random translate test
              </li>
            </NavLink>
            <li role="separator" className="divider"></li>
            <NavLink to="/tests/alternate-translate" activeClassName="active">
              <li className="test-button">
                Alternate translate test
              </li>
            </NavLink>
            <li role="separator" className="divider"></li>
            <NavLink to="/tests/alternate-eng-translate" activeClassName="active">
              <li className="test-button">
                English translate test alternate
              </li>
            </NavLink>
            <li role="separator" className="divider"></li>
            <NavLink to="/tests/random-eng-translate" activeClassName="active">
              <li className="test-button">
                English translate test random
              </li>
            </NavLink>
          </ul>
        )
    }
}