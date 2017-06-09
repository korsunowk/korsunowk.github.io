import React from 'react'

var words = require('../../../../words.json')

export default class RussianAlternateTranslateTest extends React.Component {
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
        <h2>Translate test</h2>
        <h3>Enter the correct translation of the displayed verb in the appropriate field.</h3>
        <div className='test-body' onKeyPress={(e) => this.EnterPress(e)}>
          <div className='test-header'>
            <span className='verb-number'>
              {this.state.current_word}.
            </span>
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
