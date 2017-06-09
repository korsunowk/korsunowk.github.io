import {createStore} from 'redux'

function reducer (state, action) {
  switch (action.type) {
    case 'TOGGLE_TABLE':
      let _new = !state.table
      return {...state, ...{table: _new}}
    case 'DEC_SEC':
      let newSec = state.seconds - 1
      return {...state, ...{seconds: newSec}}
    default:
      return state
  }
}

const store = createStore(reducer, {
  table: true,
  seconds: 30
})

export default store
