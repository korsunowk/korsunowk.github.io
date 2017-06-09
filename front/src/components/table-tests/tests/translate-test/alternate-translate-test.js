import React from 'react'

var words = require('../../../../words.json')

export default class AlternateTranslateTest extends React.Component {
  constructor () {
    super()

    let _words = {}
    for (let i = 1; i <= Object.keys(words).length; i++) {
      _words[i] = words[i]
    }

    this.state = {
      _words: _words,
      current_word: 1,

      translate_error: false
    }

    this.CheckWords = this.CheckWords.bind(this)
    this.AddFocus = this.AddFocus.bind(this)
    this.changeStateToNext = this.changeStateToNext.bind(this)
    this.addErrorOnInput = this.addErrorOnInput.bind(this)
    this.cleanInputs = this.cleanInputs.bind(this)
    this.EnterPress = this.EnterPress.bind(this)
  }

  EnterPress (e) {
    if (e.key === 'Enter') {
      this.CheckWords()
    }
  }

  AddFocus (e) {
    e.target.focus()
  }

  CheckWords () {
    let translate = this.refs.translate.value
    let currentWord = this.state._words[this.state.current_word]

    let valid = true

    let errors = {
      'translate_error': false
    }

    let currWord = currentWord['russian_translate'].split(', ')
    for (let i = 0; i < currWord.length; i++) {
      if (currWord[i].trim() === translate.toLowerCase().trim()) {
        valid = true
        errors['translate_error'] = false
        break
      }

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

  changeStateToNext () {
    let next = ++this.state.current_word

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

  render () {
    return (
      <div className='test-block'>
        <div className='test-top'>
          <h2>Translate test</h2>
          <span className='test-counter'>
            {this.state.current_word} / {Object.keys(this.state._words).length}
          </span>
        </div>
        <h3>Enter the correct translation of the displayed verb in the appropriate field.</h3>
        <div className='test-body' onKeyPress={(e) => this.EnterPress(e)}>
          <div className='test-header'>
            <span className='verb-infinitive'>
              {this.state._words[this.state.current_word]['infinitive']}
            </span>
            <span className='verb-simple'>
              {this.state._words[this.state.current_word]['past_simple']}
            </span>
            <span className='verb-perfect'>
              {this.state._words[this.state.current_word]['perfect']}
            </span>
          </div>
          <hr />
          <div className='test-test'>
            <label htmlFor='translate-verb'>
                Russian translate:
                <input
                  type='text'
                  id='translate-verb'
                  onMouseEnter={this.AddFocus}
                  ref='translate'
                  className={this.state.translate_error ? 'error' : ''}
                />
            </label>
          </div>
          <div className='button check' onClick={this.CheckWords}>Check</div>
        </div>
      </div>
    )
  }
}
