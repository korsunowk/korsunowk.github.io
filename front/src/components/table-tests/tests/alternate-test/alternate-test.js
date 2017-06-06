import React from 'react';

var words = require('../../../../words.json');

export default class AlternateTest extends React.Component {
    constructor() {
        super();

        let _words = {};
        for(let i=1; i<= Object.keys(words).length; i++)
            _words[i] = words[i];
        
        this.state = {
            _words: _words,
            current_word: 1,

            past_simple_error: false,
            perfect_error: false
        };

        this.CheckWords = this.CheckWords.bind(this);
        this.AddFocus = this.AddFocus.bind(this);
        this.changeStateToNext = this.changeStateToNext.bind(this);
        this.addErrorOnInput = this.addErrorOnInput.bind(this);
        this.cleanInputs = this.cleanInputs.bind(this);
        this.EnterPress = this.EnterPress.bind(this);
    }

    EnterPress(e) {
        if (e.key === 'Enter') {
            this.CheckWords();
        }
    }

    AddFocus(e) {
        e.target.focus()
    }

    CheckWords() {
        let past_simple = this.refs.past.value;
        let perfect = this.refs.perfect.value;
        let current_word = this.state._words[this.state.current_word];

        let valid = true;

        let errors = {
            'past_simple_error': false,
            'perfect_error': false
        }

        if (current_word['past_simple'].trim() !== past_simple.toLowerCase().trim()) {
            valid = false;
            errors['past_simple_error'] = true;
        }
        
        if (current_word['perfect'].trim() !== perfect.toLowerCase().trim()) {
            valid = false;
            errors['perfect_error'] = true;
        }
        
        if (valid) {
            this.cleanInputs();
            this.changeStateToNext();        
        } else {
            this.addErrorOnInput(errors);
        }
    }

    changeStateToNext() {
        let next = ++this.state.current_word;

        this.setState({
            current_word: next,
            past_simple_error: false, 
            perfect_error: false
        })
    }

    cleanInputs() {
        this.refs.perfect.value = "";
        this.refs.past.value = "";
    }

    addErrorOnInput(errors) {
        this.setState(errors);
    }

    render () {
        return (
            <div className="test-block">
                <h2>Alternate test</h2>
                <h3>Enter the correct forms of the displayed verb in the appropriate fields.</h3>
                <div className="test-body" onKeyPress={(e) => this.EnterPress(e)}>
                    <div className="test-header">
                        <span className="verb-number">
                            {this.state.current_word}.
                        </span>
                        <span className="verb-infinitive">
                            {this.state._words[this.state.current_word]['infinitive']}
                        </span>
                        <span className="verb-russian">
                            {this.state._words[this.state.current_word]['russian_translate']}
                        </span>
                    </div>
                    <hr />
                    <div className="test-test">
                        <label htmlFor="verb-past-simple">
                            Past simple: 
                            <input 
                                type="text" 
                                id="verb-past-simple" 
                                onMouseEnter={this.AddFocus} 
                                ref="past" 
                                className={this.state.past_simple_error ? "error": ""} 
                            />
                        </label>
                        <label htmlFor="verb-present-perfect">
                            Past participle: 
                            <input 
                                type="text"
                                id="verb-present-perfect" 
                                onMouseEnter={this.AddFocus} 
                                ref="perfect" 
                                className={this.state.perfect_error ? "error": ""} 
                            />
                        </label>
                    </div>
                    <div className="button check" onClick={this.CheckWords}>Check</div>
                </div>
            </div>
        )
    }
}