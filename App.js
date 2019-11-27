import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import _ from 'lodash';

// JSON = Javascript Object Notation
// React is a component based library; the webpage is built off of many components put together

function App() {
	
	const [subreddits, setSubreddits] = useState({});
	
	// When the component is first loaded, fetch subreddits
	useEffect(fetchSubreddits, []);
	
	async function fetchSubreddits() {
		const response = await fetch(`/subreddits`);
		if (response.ok) {
			const json = await response.json();
			setSubreddits(json);
		}
	}
	return (
		<div className="App">
			<h1 className="App-title">uCanada</h1>
			
			{_.map(subreddits, (subreddit, i) => (
				<Subreddit
					key={i}
					displayName={subreddit.displayName}
					subscribers={subreddit.subscribers}
					icon={subreddit.icon}
					wordCounts={subreddit.wordCounts}
				/>
			))}
		</div>
	);
}
function Subreddit(props) {
	
	const fontSizeMapper = word => word.value * 3
	const rotate = word => word.value*20 % 360
	
	const [isFavourite, fav] = useState(false)
	
	return (
		<div className="App">
			<h1>{props.displayName}</h1>
			<button onClick={() => fav(!isFavourite)}>
				Toggle Favourite
			</button>
			<p>{isFavourite ? "<3" : "D:"}</p>
			<img className="Subreddit-icon" src={props.icon} alt="A subreddit icon"/>
			<p>Subscribers: {props.subscribers}</p>

			
		</div>
	);
}

export default App;