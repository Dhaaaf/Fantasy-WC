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
import CreateLeague from "../CreateLeagueForm";
import EditDeleteLeagueModal from "../EditDeleteModal";
import CreateTeam from "../Team/CreateTeamForm";
import LeagueLeaderboard from "../LeagueLeaderboard";

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
                <div className="add-league-div">
                    <div className="plus">+</div>
                    {/* <button className="add-league-button">Create a Custom League</button> */}
                    <OpenModalButton
                        modalComponent={<CreateLeague/>}
                        buttonText="Create a Custom League"
                        onbuttonClick={closeMenu}
                        className="add-league-button"
                    />
                </div>
                </div>
                <div className="leagues-mapper">
                    {leaguesArray && (
                        leaguesArray.map((league) => (
                            <div key={league.id} className="league-card-wrapper">
                                { league.owner_id === userId ? (
                                    <div className="league-card owner">
                                    <div className="gear-edit">
                                    <OpenModalButton
                                        modalComponent={<EditDeleteLeagueModal league={league} />}
                                        buttonText="edit-league"
                                        onbuttonClick={closeMenu}
                                        />
                                    </div>
                                    <div className="league-img">
                                        <img
                                        className="league-image"
                                        src={league.display_pic}
                                        onError={e => { e.currentTarget.src = "https://cloudinary.fifa.com/m/6e6c51d56752bd7a/original/The-FIFA-World-Cup-Trophy.jpg"; }}
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
                                            buttonText="i"
                                            onbuttonClick={closeMenu}
                                            />
                                        </div>


                                        <div className="compete">
                                            <div></div>
                                        <OpenModalButton
                                            modalComponent={<CreateTeam league={league} />}
                                            buttonText="Kick-off"
                                            onbuttonClick={closeMenu}
                                            />
                                            <div></div>
                                        </div>

                                        <div className="league-leaderboard">   
                                        <OpenModalButton
                                            modalComponent={<LeagueLeaderboard league={league} />}
                                            buttonText="leaderboard"
                                            onbuttonClick={closeMenu}
                                            />
                                        </div>
                                    </div>
                                </div>
                                ) : (
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
                                            buttonText="i"
                                            onbuttonClick={closeMenu}
                                            />
                                        </div>
                                        <div className="compete">
                                            <div></div>
                                        <OpenModalButton
                                            modalComponent={<CreateTeam league={league} />}
                                            buttonText="Kick-off"
                                            onbuttonClick={closeMenu}
                                            />
                                            <div></div>
                                        </div>

                                        <div className="league-leaderboard">   
                                        <OpenModalButton
                                            modalComponent={<LeagueLeaderboard league={league} />}
                                            buttonText="leaderboard"
                                            onbuttonClick={closeMenu}
                                            />
                                        </div>
                                    </div>
                                </div>
                                )}
                            </div>
                        ))
                    )}
                </div>
            </div>
        </div>
    )
}

export default LeaguesIndex
