import React from 'react';

export default function OneUser (props) {
    return (
        <span>
            {props.user.username}, {props.user.email}.
        </span>
    )
}