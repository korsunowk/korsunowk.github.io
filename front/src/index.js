import React from 'react'
import ReactDOM from 'react-dom'

import {Provider} from 'react-redux'

import App from './App'
import store from './store'
import './index.css'

import registerServiceWorker from './registerServiceWorker'

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
)

store.subscribe(() => console.log('new state', store.getState()))
registerServiceWorker()