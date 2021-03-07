import React, { Fragment } from "react";
import Summary from './Summary';


// control it all here 
// automatically restrict them and apply it to state 
// state{
//    summaries : {name: summary, 
//                 name2:summary2}
//}
// if no summary < 300 - don't render a popup link
// otherwise do - then pass associated state to modal 
// if they click on the popup render it 
// might br tricky but it would probably work 

// showModalHandler

const DisplayRecommendations = (props) => {
     return (
        <table>
            <tbody>
            {/* iterate through all selection objects */}
                {Object.keys(props.data).map((oneKey, i) => {
                    return (
                        <Fragment key={props.data[oneKey].id}>
                            <tr>
                                <td rowSpan="2">
                                    <img
                                        src={process.env.PUBLIC_URL + '/Images/' + props.data[oneKey].id + '.jpg'}
                                        alt={props.data[oneKey]['name']}
                                        className="SelectionImages"
                                    />
                                </td>
                                {/* below sets the text colour as per data.js */}
                                <th>{props.data[oneKey].name}</th>
                            </tr>
                            <tr>
                                <td> <Summary summary_pass={props.data[oneKey].summary.replace(/"/g,'')}/> </td> 
                            </tr>  
                        </Fragment>
                    )
                })}
            </tbody>
        </table>
    );
}

export default DisplayRecommendations;
