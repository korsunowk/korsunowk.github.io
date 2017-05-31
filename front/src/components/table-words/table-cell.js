import React from 'react';

export default class TableCell extends React.Component {
    render () {
        return (
            <tr>
                <td>{this.props.number}</td>
                <td>{this.props.infinitive}</td>
                <td>{this.props.past_simple}</td>
                <td>{this.props.perfect}</td>
                <td>{this.props.russian}</td>
            </tr>
        )
    }
}