import React from 'react';
import TableCell from './table-cell';

import '../../styles/table.css';
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
                    number={i}
                />
            )
        }
        return (
            <table>
                <tbody>
                    <tr>
                        <th>№</th>
                        <th>Infinitive</th>
                        <th>Past simple</th>
                        <th>Past participle</th>
                        <th>Russian translate</th>
                    </tr>
                    <tr className="empty-tr">
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    {cells}
                </tbody>
            </table>
        )
    }
}