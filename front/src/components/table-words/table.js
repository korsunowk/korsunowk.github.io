import React from 'react';
import TableCell from './table-cell';
import SearchBlock from './search-block';

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
            <div>
                <SearchBlock />
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