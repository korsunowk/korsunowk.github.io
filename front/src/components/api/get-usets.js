import React from 'react';

import OneUser from './one-user';


export default class UsersList extends React.Component {
    constructor() {
        super();

        this.state = {
            users: []
        };
    }

    componentDidMount () {
        this.UserList();
    }

    UserList() {
        return fetch('http://127.0.0.1:8000/v1/users.json')
        .then((response) => response.json())
        .then((responseJson) => {
            this.setState({
                users: responseJson
            });
        })
        .catch((error) => {
            console.error(error);
        });
    }

    render () {
        let users = [];
        for(let i=0; i < this.state.users.length; i++) {
            users.push(
                <OneUser key={i} user={this.state.users[i]} />
            )
        }

        return (
            <div className="users-block">
                {users}
            </div>
        )
    }
}