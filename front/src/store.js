import {createStore} from 'redux'

function reducer (state, action) {
  switch (action.type) {
    case 'TOGGLE_TABLE':
      let _new = !state.table
      return {...state, ...{table: _new}}
    default:
      return state
  }
}

const store = createStore(reducer, {
  table: true
})

export default store
