import React from 'react';
import TableCell from './table-cell';

var words = require('../../words.json');

export default class WordsTable extends React.Component {
    render () {
        let cells = new Array();
        for(let i=1; i<=Object.keys(words).length; i++) {
            cells.push(
                <TableCell
                    russian={words[i]['russian_translate']} 
                    infinitive={words[i]['infinitive']}
                    past_simple={words[i]['past_simple']}
                    perfect={words[i]['perfect']}
                    key={i}
                />
            )
        }
        return (
            <table>
                <tbody>
                    {cells}
                </tbody>
            </table>
        )
    }
}