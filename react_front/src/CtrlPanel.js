import React, { Component } from 'react';
import Search from './Search';

import axios from './axios-api-connect';

class CtrlPanel extends Component {

    state = {
        games_data: null,
        server_response: null

    }

    // onload we want to ping the api for all the game names and ids 
    componentDidMount() {

        axios.get('/onLoadGameData/')
            .then(response => {
                this.setState({ games_data: response.data, server_response: response.status });
            })
            .catch(error => {
                this.setState({ games_data: null, server_response: null });
            });
    }

    render() {

        let data_returned = null; // null to be rendered in event of no response 

        if (this.state.server_response) { // ie if not null - status 200 eventually but placeholder for now 
            // let names=Object.values(this.state.games_data); //.values(); // need to extract the values from this object 
            // let ids = Object.keys(this.state.games_data);


            data_returned = <Search returned={this.state.games_data} />; // if ping successful - data returned becomes jsx with desired prop

        }

        // then if successful render the Search Jsx element which will receive the data as a prop
        return (
            <div>
                {data_returned}
            </div>
        )
    }
}

export default CtrlPanel;