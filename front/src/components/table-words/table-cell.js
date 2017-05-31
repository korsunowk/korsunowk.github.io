import React from 'react';

export default function TableCell (props) {
    if (props.empty)
        return (
            <tr>
                <td colSpan="5" className="empty-td" style={{width: '835px', fontSize: '20px'}}>No match found!</td>
            </tr>
        )

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