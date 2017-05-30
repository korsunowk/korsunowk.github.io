import React from 'react';

export default class One extends React.Component {
    render () {
        return (
            <tr>
                <td>{this.props.infinitiv}</td>
                <td>{this.props.past_simple}</td>
                <td>{this.props.perfect}</td>
                <td>{this.props.russian}</td>
            </tr>
        )
    }
}