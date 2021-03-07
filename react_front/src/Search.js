import React, { useState } from 'react';
import { Typeahead } from 'react-bootstrap-typeahead';
import 'react-bootstrap-typeahead/css/Typeahead.css';
import HocWrap from './hoc/hoc_wrapper/HocWrap';
import DisplayRecommendations from './DisplayRecommendations';
import axios from './axios-api-connect'; 
import Spinner from './Spinner';
import './Spinner.css';

const Search = (props) =>  {
  const [multiSelections, setMultiSelections] = useState([]);
  const [getRecommendations, setGetRecommendations] = useState(false);
  const [gamesData, setGamesData] = useState([]);
  const [randomRecs, setRandomRecs] = useState(true);
  const [serverResponse, setServerResponse] = useState([]);
  const [spinnerRendered, setSpinnerRendered] = useState([]);

  /* This is used to keep number of selection to a maximum of 5
  if user tries to select more it will slice the selections list*/
  if (multiSelections.length > 5) {
    setMultiSelections(multiSelections.slice(0, 5))
  }

  const gameTargets = (props) => {
    setMultiSelections(props)
    if (! getRecommendations){
      // only way for user to get recs button working
      // again is to change their search items. Minor flaw in that
      // if a user deletes a game and adds it back they will be able to search
      // again eventhough it's the same list. I think this is correct though.
      // Alternative is to store users last search box. Not worth it imo.
      setGetRecommendations(true)
    }
  }

  const getRecs = (buttonType) => {
    if ((multiSelections.length > 0 && getRecommendations) || (randomRecs && buttonType === 'random')){
      

      // hide site info div
      document.getElementById("SiteInfo").style.display = "none";
      
      // need to extinguish previous recs if you click get rec button again to show spinner 
      if (gamesData !== []){
        setGamesData([]);
      }
      setSpinnerRendered(<Spinner/>);
      // ensure user cannot multiple click on getRecommendations button
      // while it's getting recs.
      setGetRecommendations(false);
      setRandomRecs(false);

      // set payload to be passed to backend
      let payload = '';
      if (buttonType ==='random'){
        payload = JSON.stringify('random');
      }
      else{
        payload = JSON.stringify(multiSelections);
      }

      axios.post('/recommend_games/', payload)
        .then(response => {
          setGamesData(response.data)
          setServerResponse(response.status)
          setSpinnerRendered([]);
          setRandomRecs(true);
          // if list has items but clicked random selection
          // allow user to get normal selections after.
          if (payload === '"random"') {
            setGetRecommendations(true);
          }
        })
        .catch(error => {
          setGamesData(null)
          setServerResponse(null)
      }); 
    }
  }
    return (
      <div className='App'>
        <HocWrap>
          <div className='Header'>
            <a href="/">
              <h2>Retro-Recommender</h2>
              <img
                className='logo'
                src={process.env.PUBLIC_URL + '/Images/' + 'logo.png'}
                alt="logo"
              />
            </a>
          </div>
          <div className='SearchBar'>
            <Typeahead
              id="basic-typeahead-multiple"
              labelKey="name"
              multiple
              onChange={gameTargets}
              options={props.returned}
              placeholder="PICK UP TO 5 GAMES..."
              selected={multiSelections}
            />
          </div>
          <div className='Buttons'>
            <button type="button" id='primary' className='btn btn-primary' onClick={getRecs}>
              GET RECOMMENDATIONS
            </button>  
            <button type="button" id='secondary' className='btn btn-success' onClick={() => getRecs('random')}>
              LUCKY DIP
            </button>
          </div>  
          <div className='SiteInfo' id='SiteInfo'>
            <ul> Welcome to <b>The Retro-Recommender.</b> </ul>
            <ul>We have all the games you could ever want here...as long as what you want
            is retro games from the SNES to the PS3 era... </ul>
            <ul><em>Pick up to 5</em> of your favourite games from the golden age
            of gaming and the professor will recommended 10 titles worth checking out based on those choices.</ul> 
            <ul>You can also try the lucky dip which will be 10 games highly rated by the professor.</ul>
          <img
            className='Professor'
            src={process.env.PUBLIC_URL + '/Images/' + 'professor.png'}
            alt="professor"
          />
          </div> 
          <div className='Recommendations'>
            <DisplayRecommendations
              data={gamesData}
            />
            {spinnerRendered}
          </div>
        </HocWrap>
      </div>
    );
};

export default Search;