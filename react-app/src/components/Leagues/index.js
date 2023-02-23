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
import OpenModalButton from "../OpenModalButton";
import TournamentsList from "./tournamentsList";

const LeaguesIndex = () => {
    let dispatch = useDispatch();
    let [isLoaded, setIsLoaded] = useState(false)
	const user = useSelector((state) => state.session.user);
    let userId = user.id
    const leagues = useSelector((state) => state.leagues);
    const history = useHistory()
    const [showMenu, setShowMenu] = useState(false);

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


    const closeMenu = () => setShowMenu(false);

    return (
        <div className="leagues-main-page">
            <div className="leagues-container">
                <div className="leagues-container-header">
                <h1 className="header-league">Pick a League to compete in:</h1>
                </div>
                <div className="leagues-mapper">
                    {leaguesArray && (
                        leaguesArray.map((league) => (
                            <div key={league.id} className="league-card-wrapper">
                                <div className="league-card">
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
                                        <div className="league-tournaments-container">
                                            <div className="league-tournaments">Tournaments: {league.tournaments.length}</div>
                                            <OpenModalButton
                                            modalComponent={<TournamentsList tournaments={league.tournaments} name={league.name} />}
                                            buttonText="+"
                                            onbuttonClick={closeMenu}
                                            />
                                        </div>
                                        <button className="compete"> Compete</button>
                                    </div>
                                </div>
                            </div>
                        ))
                    )}
                </div>
            </div>
        </div>
    )
}

export default LeaguesIndex