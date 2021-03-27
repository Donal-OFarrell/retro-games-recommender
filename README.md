# Url/ Hosting 

http://retrorecommender.com

- screenshots of site here 

# Note on public repo

Development took place using a private repo and as this contained crednetials and enpoints, we created this repo to be exposed publically. As such commit history will not reflect accurately.

# Data

We gathered data on over 8500 games for 8 popular consoles. (Nintendo 64, PlayStation, PlayStation 2, Nintendo Entertainment System (NES), Super Nintendo Entertainment System (SNES), Nintendo GameCube, Dreamcast, Sega Mega Drive_Genesis, Sega Saturn). We stored these in a MySQL database which was hosted on Google Cloud. 

# Calculating similarities for recommendations

We used the Jaccard similarity coefficient to determine the similarity between games based on their genres. The Jaccard Index determines the similarity between two sample sets and is define as the size (count) of the intersection divided by the size of the union between the two sample sets. 

-screenshot of Jaccard Similarity 

We stored these results in a Matrix object which was essentially a dictionary of dictionaries. For example {game_id: 1: {2:.75, 3:1}} would indicate that the game id 1 had a similarity of .75 to game id 2 and a similarity of 1 to game id 3. We stored this Matrix as a pickle object as it was far more efficient than generating each time the website was loaded. 
As such every game relative to our candidate games were given a value from 0 to 1 ( 1 being the closest similarity to our targets). We then compiled the top 10 recs (i.e. values closest to 1) and these become the recommendations we deliver to the user. 

When a user selects more than one target game for example the user wants recommendations for ‘Silent Hill’ and ‘Metal Gear Solid’ we compare all other games to both of those titles and take the mean score as the similarity. This ensures that any recommendations made are relevant to the entire set and not solely based on the similarity to one game.

# Django Backend 

Django was used to produce an API which ,connects an MVC ORM model to a MySQL database and provides two functional views/routes. 
- onLoadGameData - Returns all games required to generate the autocomplete list for the search bar.
- recommend_games - Generates recommendations for a user if they pass games back, or generates a Lucky Dip if they request this on the ui. The Lucky dip - will obtain a subset of games highly rated by users from our dataset ( rated >80 and rated by 10 or more users).

# React User Interface 

The React UI boasted a combination of class based stateful components as well as stateless functional components, and the more modern functional react hooks (which allow for state management in functional components). Async communications to the API were facilitated using axios. 

The parent child progression/data flow in React components is roughly as follows 

Index -> App -> CtrlPanel -> Search -> Typeahead (3rd party) -> Display Recommendations - > Summary 
 
Utility components included a stateless Spinner component (a spinner that renders during recommendation loads). 

On load the CtrlPanel component uses the lifecycle hook componentDidMount to send an async axios request to the API (communicating with the onLoadGamesData endpoint on the Django box).
This returns a json object with the game ids mapped to their names. This will then be used to generate the search bar using the 3rd party react-bootstrap-typeahead component (see: https://www.npmjs.com/package/react-bootstrap-typeahead). 

The user can then avail of two main functionalities on the user interface. They can opt for a LUCKY DIP (see above for explanation of this), or they can choose a group of up to 5 games. These will ping the same route on the API; recommend_games. Therein the logic determines whether the user has opted for a LUCKY DIP or a standard GET RECOMMENDATIONS call. While loading and retrieving recommendations from the API - the Spinner component will render. These will be returned to the UI and Display Recommendations will ingest the returns. React will then seek image files associated with these game ids and retrieve them (residing on the same box), and all of these elements i.e. the name, description and image will be rendered as ‘tables’ on the UI.  

# Deployment 

The applications infrastructure is all hosted on GCP (Google Cloud Platform). The database as mentioned is a Cloud SQL Instance. The Django API is hosted over http using nginx, while the react front end is hosted on a separate box also using nginx. 

Moving from development to production posed some challenges. 

In our version of react-scripts 4.0.2, the npm run build command didn’t allow us to stipulate the location where the app was hosted by adjusting the homepage parameter in package.json (known issue: https://github.com/facebook/create-react-app/issues/8813). As such React assumed the project was hosted at root. As a result it could not retrieve the images residing on the box. A workaround was devised whereby we stipulated a .env file with the appropriate endpoint with PUBLIC_URL={http://"server ip"}. This allowed nom run build to build assuming the project was hosted at the endpoint rather than root. 

We also had to remove references to manifest.json in index.html as we could not get this to play nice with Django. 

We also had to adjust settings.py on django side to allow CORs traffic between the two respective boxes. 

We also attempted to run over https and we successfully managed this on the react side. But when pinging the Django api, this was still served over http, so this caused an error. As such the only viable workaround to this that we could imagine if we were to retain the current infrastructure (ie 2 boxes with the Django box serving as an API), would require servicing the Django api over https. This is currently under consideration, along with potentially investigating containerisation (Docker, Kubernetes). 



Screenshots 
![image](https://user-images.githubusercontent.com/55091575/112724100-809a3700-8f09-11eb-928c-82e9d270a1e0.png)
![image](https://user-images.githubusercontent.com/55091575/112724121-9b6cab80-8f09-11eb-9070-620728f0eea8.png)
![image](https://user-images.githubusercontent.com/55091575/112724125-a7f10400-8f09-11eb-9194-7295fa530c61.png)
![image](https://user-images.githubusercontent.com/55091575/112724140-bb9c6a80-8f09-11eb-851a-47e3ff1f9ea7.png)
![image](https://user-images.githubusercontent.com/55091575/112724166-dc64c000-8f09-11eb-983a-756b9e5134d4.png)


# Future Work 

- Host over https (either host the API over https or consider containerisation).
- Improve the Spinner/loader to be more engaging to allow for potentially laggy loads. 
