import React, { Component } from 'react'

import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import store from '../../../../store'

class SpeedTimer extends Component {
  constructor () {
    super()

    this.state = {
      seconds: 10
    }

    this.interval = null
    this.stopTimer = this.stopTimer.bind(this)
    this.startTimer = this.startTimer.bind(this)
  }

  stopTimer () {
    clearInterval(this.interval)
  }

  startTimer () {
    this.interval = window.setInterval(SpeedTimer.MinusOneSecond, 1000)
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
    if (nextProps.seconds >= 0) {
      this.setState({
        seconds: nextProps.seconds
      })
      if (nextProps.resetTimer) {
        this.startTimer()
      }
    } else {
      this.stopTimer()
    }
  }

  shouldComponentUpdate (nextProps, nextState) {
    return this.state.seconds !== nextState.seconds && nextState.seconds >= 0
  }

  componentDidMount () {
    this.startTimer()
  }
}

function mapStateToProps (state) {
  return {
    seconds: state.seconds
  }
}

function mapDispatchToProps (dispatch) {
  return {
    pageActions: bindActionCreators(SpeedTimer.MinusOneSecond, dispatch)
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(SpeedTimer)
