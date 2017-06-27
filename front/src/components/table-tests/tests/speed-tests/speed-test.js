import React, { Component } from 'react'
import SpeedTimer from './speed-timer'

import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import store from '../../../../store'

var words = require('../../../../words.json')

function shuffleArray (d) {
  for (var c = d.length - 1; c > 0; c--) {
    var b = Math.floor(Math.random() * (c + 1))
    var a = d[c]
    d[c] = d[b]
    d[b] = a
  }
  return d
};

class SpeedTest extends Component {
  constructor () {
    super()

    let _words = []

    for (let i = 1; i <= Object.keys(words).length; i++) {
      _words.push({
        'number': i,
        'infinitive': words[i]['infinitive'],
        'russian_translate': words[i]['russian_translate'],
        'past_simple': words[i]['past_simple'],
        'perfect': words[i]['perfect']
      })
    }

    _words = shuffleArray(_words)

    this.state = {
      _words: _words.slice(0, 20),
      current_word: 0,

      translate_error: false
    }

    this.timeIsOver = false

    this.CheckWords = this.CheckWords.bind(this)
    this.AddFocus = this.AddFocus.bind(this)
    this.changeStateToNext = this.changeStateToNext.bind(this)
    this.addErrorOnInput = this.addErrorOnInput.bind(this)
    this.cleanInputs = this.cleanInputs.bind(this)
    this.EnterPress = this.EnterPress.bind(this)
  }

  EnterPress (e) {
    if (this.props.seconds !== 0) {
      if (e.key === 'Enter') {
        this.CheckWords()
      }
    }
  }

  static ResetTimer () {
    store.dispatch({
      type: 'RESET_SEC'
    })
  }

  AddFocus (e) {
    e.target.focus()
  }

  CheckWords () {
    if (!this.timeIsOver) {
      let translate = this.refs.translate.value
      let currentWord = this.state._words[this.state.current_word]

      let valid = true

      let errors = {
        'translate_error': false
      }

      let currWord = currentWord['infinitive']
      if (currWord.trim() !== translate.toLowerCase().trim()) {
        valid = false
        errors['translate_error'] = true
      }

      if (valid) {
        this.cleanInputs()
        this.changeStateToNext()
      } else {
        this.addErrorOnInput(errors)
      }
    }
  }

  changeStateToNext () {
    let next = this.state.current_word + 1
    SpeedTest.ResetTimer()

    this.setState({
      current_word: next,
      translate_error: false
    })
  }

  cleanInputs () {
    this.refs.translate.value = ''
  }

  addErrorOnInput (errors) {
    this.setState(errors)
  }

  shouldComponentUpdate (nextProps, nextState) {
    let validTime = nextProps.seconds < 6 && nextProps.seconds >= 0
    let validTranslate = this.state.translate_error !== nextState.translate_error
    let validCurrentWord = this.state.current_word !== nextState.current_word

    if (validTime || validTranslate || validCurrentWord) {
      return true
    }
    return false
  }

  render () {
    let alert = null
    if (this.props.seconds === 0) {
      alert = ' alert'
      this.timeIsOver = true
    } else {
      alert = this.props.seconds <= 5 && this.props.seconds % 2 !== 0 ? ' alert' : ''
    }
    return (
      <div className={'test-block' + alert}>
        <div className='test-top'>
          <h2>Speed test</h2>
          <SpeedTimer />
          <span className='test-counter'>
            {this.state.current_word + 1} / {this.state._words.length}
          </span>
        </div>
        <h3>Enter the correct translation of the displayed verb in the appropriate field.</h3>
        <div className='test-body' onKeyPress={(e) => this.EnterPress(e)}>
          <div className='test-header'>
            <span className='verb-russian no-brakets'>
              {this.state._words[this.state.current_word]['russian_translate']}
            </span>
          </div>
          <hr />
          <div className='test-test'>
            <label htmlFor='translate-verb'>
                English translate:
                <input
                  type='text'
                  id='translate-verb'
                  onMouseEnter={this.AddFocus}
                  ref='translate'
                  className={alert + (this.state.translate_error ? 'error' : '')}
                />
            </label>
          </div>
          <div className={'button check' + (this.props.seconds === 0 ? ' disabled' : '') + alert} onClick={this.CheckWords}>Check</div>
        </div>
      </div>
    )
  }
}

function mapStateToProps (state) {
  return {
    seconds: state.seconds
  }
}

function mapDispatchToProps (dispatch) {
  return {
    pageActions: bindActionCreators(SpeedTest.ResetTimer, dispatch)
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(SpeedTest)
