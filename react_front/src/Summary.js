import React, { Component } from 'react';
import HocWrap from './hoc/hoc_wrapper/HocWrap';

class MoreInfoPopUp extends Component{ 

    constructor(props) {
        super(props);
    
        this.state = {
            text_rendered: null,
            more_info: false,
            more_render:null
        };
    
        this.moreInfoHandler = this.moreInfoHandler.bind(this); // this syntax was required to get the methods working - not 100% what it does 
        this.closeMoreInfoHandler = this.closeMoreInfoHandler.bind(this);
    }

    componentDidMount () {


    let summary = this.props.summary_pass; 
    

    if (summary.includes('Sorry no summary') || summary.length < 400){

        this.setState({text_rendered:summary })
    }

    else {

        this.setState({ text_rendered: <HocWrap> <p>{summary.substring(0, 199) + "..."} </p>  <button className='btn btn-info btn-sm' onClick={this.moreInfoHandler} > Show more </button> </HocWrap>});
    }
}

    moreInfoHandler() {

        
        let more_info_copy = this.state.more_info;
        let more_info_inverse = !more_info_copy;


        

        this.setState({ more_info: more_info_inverse }, () => {
          }); 
          let summary = this.props.summary_pass;
        this.setState({
            more_render: <HocWrap> <p>{summary} </p> <button className='btn btn-info btn-sm' onClick={this.closeMoreInfoHandler} > Show less </button>  </HocWrap>,
                        text_rendered:null});


    }

    closeMoreInfoHandler(){
        let summary = this.props.summary_pass; 
        this.setState({more_render:null,
            text_rendered: <HocWrap> <p>{summary.substring(0, 199) + "..."} </p>  <button className='btn btn-info btn-sm' onClick={this.moreInfoHandler} > Show more </button>  </HocWrap>})
    }



    render() {
    
    return (
        <HocWrap>
         {this.state.text_rendered} 
         {this.state.more_render}
         </HocWrap>
    );
    
}

}

export default MoreInfoPopUp;




