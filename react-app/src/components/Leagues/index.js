import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
    thunkAddLeague,
    thunkGetLeagues,
    thunkEditLeague,
    thunkDeleteLeague,
    actionResetLeague
} from "../../store/leagues"
import { NavLink, useHistory } from "react-router-dom";
import "./LeagueIndex.css"

const LeaguesIndex = () => {
    let dispatch = useDispatch();
    let [isLoaded, setIsLoaded] = useState(false)
	const user = useSelector((state) => state.session.user);
    let userId = user.id
    const leagues = useSelector((state) => state.leagues);
    const history = useHistory()

    useEffect(() => {
		dispatch(thunkGetLeagues()).
        then(() => setIsLoaded(true));

		return () => {
			dispatch(actionResetLeague());
		};
	}, [userId, dispatch]);

    let leaguesArray = null
    if (isLoaded) {
        leaguesArray = Object.values(leagues)
    }

    console.log("LEAGUES ARRAY---->", leaguesArray)

    return (
        <div className="leagues-main-page">
            <div className="header-leagues">
                <h1>Pick a League to compete in:</h1>
            </div>
            <div className="footer-leagues">
                <div className="leagues-mapper">
                    {leaguesArray && (
                        leaguesArray.map((league) => (
                            <div key={league.id} className="league-card">
                                <div className="league-img">
                                    <img
                                    className="league-image"
                                    src={league.display_pic}
                                    > 
                                    </img>
                                </div>
                                <div className="league-card-footer">
                                    <div className="league-name">{league.name}</div>
                                    <div className="league-budget">Budget: € {league.team_budget} million</div>
                                    <div className="league-tournaments">Tournaments: {league.tournaments.length}</div>
                                </div>
                            </div>
                        ))
                    )}
                </div>
                <div className="leagues-footer-right">

                </div>
            </div>
        </div>
    )
}

export default LeaguesIndex
