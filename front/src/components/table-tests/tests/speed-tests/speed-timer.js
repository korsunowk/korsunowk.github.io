import React, { Component } from 'react'

import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import store from '../../../../store'

class SpeedTimer extends Component {
  constructor () {
    super()

    this.state = {
      seconds: 30
    }
  }

  static MinusOneSecond () {
    store.dispatch({
      type: 'DEC_SEC'
    })
  }

  render () {
    return (
      <div className='timer-block'>
        Time left: {this.state.seconds}
      </div>
    )
  }

  componentWillReceiveProps (nextProps) {
    this.setState(
      nextProps.seconds
    )
  }

  shouldComponentUpdate (nextProps, nextState) {
    return this.state.seconds !== nextState.seconds
  }

  componentDidMount () {
    window.setInterval(SpeedTimer.MinusOneSecond(), 1000)
  }
}

function mapStateToProps (state) {
  return {
    seconds: state
  }
}

function mapDispatchToProps (dispatch) {
  return {
    pageActions: bindActionCreators(SpeedTimer.MinusOneSecond, dispatch)
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(SpeedTimer)
