import React from 'react';
import TableCell from './table-cell';
import SearchBlock from './search-block';

import '../../styles/table.css';
var words = require('../../words.json');

export default class WordsTable extends React.Component {
    constructor() {
        super();

        let _words = new Object();
        for(let i=1; i<= Object.keys(words).length; i++)
            _words[i] = words[i];
        this.state = {
            _words: _words
        };
        this.Search = this.Search.bind(this);
    }

    Search(e) {
        if (e.target.value !== "") {
            let new_words = new Object();
            for(let i=1; i<=Object.keys(words).length; i++) {
                if (e.target.value == i.toString())
                    new_words[i] = words[i];
            }
            this.setState({
                _words: new_words
            })
        }
        else {
            this.setState({
                _words: words
            })
        }
    }

    shouldComponentUpdate(nextProps, nextState) {
        return !(this.state._words == nextState)
    }

    render () {
        let cells = new Array();
        // console.log(this.state._words);
        for(let key in this.state._words) {
            cells.push(
                <TableCell
                    russian={this.state._words[key]['russian_translate']}
                    infinitive={this.state._words[key]['infinitive']}
                    past_simple={this.state._words[key]['past_simple']}
                    perfect={this.state._words[key]['perfect']}
                    key={key}
                    number={key}
                />
            )
        }
        console.log("Render------");
        return (
            <div>
                <SearchBlock onChange={this.Search} />
                <table>
                    <tbody>
                        <tr className="table-header">
                            <th>№</th>
                            <th>Infinitive</th>
                            <th>Past simple</th>
                            <th>Past participle</th>
                            <th>Russian translate</th>
                        </tr>
                        {cells}
                    </tbody>
                </table>
            </div>
        )
    }
}