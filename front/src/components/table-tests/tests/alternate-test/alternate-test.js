import React from 'react';

export default class AlternateTest extends React.Component {
    constructor() {
        super();
        this.AddFocus = this.AddFocus.bind(this);
    }

    AddFocus(e) {
        e.target.focus()
    }

    render () {
        return (
            <div className="alternate-test">
                <h2>Alternate test</h2>
                <h3>Enter the correct forms of the displayed verb in the appropriate fields.</h3>
                <div className="test-body">
                    <div className="test-header">
                        <span className="verb-number">1.</span>
                        <span className="verb-infinitive">abide</span>
                        <span className="verb-russian">пребывать, придерживаться чего-либо</span>
                    </div>
                    <hr />
                    <div className="test-test">
                        <label htmlFor="verb-past-simple">
                            Past simple: 
                            <input type="text" id="verb-past-simple" onMouseEnter={this.AddFocus} />
                        </label>
                        <label htmlFor="verb-present-perfect">
                            Past participle: 
                            <input type="text" id="verb-present-perfect" onMouseEnter={this.AddFocus} />
                        </label>
                    </div>
                </div>
            </div>
        )
    }
}