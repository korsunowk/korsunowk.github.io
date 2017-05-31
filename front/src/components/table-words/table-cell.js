import React from 'react';

export default function TableCell (props) {
    return (
        <tr>
            <td>{props.number}</td>
            <td>{props.infinitive}</td>
            <td>{props.past_simple}</td>
            <td>{props.perfect}</td>
            <td>{props.russian}</td>
        </tr>
    )
}