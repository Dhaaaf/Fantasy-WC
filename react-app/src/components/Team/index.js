import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetTeam, actionResetTeam } from"../../store/team"
import { thunkGetPlayers, actionResetPlayers } from "../../store/players";
import { NavLink, useHistory } from "react-router-dom";
import { useParams } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";

import "./Team.css"

const TeamPage = () => {
    let dispatch = useDispatch();
    let [isLoaded, setIsLoaded] = useState(false)
	const user = useSelector((state) => state.session.user);
    const leagues = useSelector((state) => state.leagues)
    const players = useSelector((state) => state.players)
    const team = useSelector((state) => state.team)
    const {leagueId, teamId} = useParams();
    let userId = user.id

    useEffect (() => {
        dispatch(thunkGetTeam(teamId)).
        then(() => setIsLoaded(true));

        return () => {
            dispatch(actionResetTeam());
        }
    }, [])

    useEffect (() => {
        dispatch(thunkGetPlayers(leagueId))

        return () => {
            dispatch(actionResetPlayers());
        }
    }, [])

    console.log("TEAM ------->", team)
    console.log("Players ------->", players)

    //// PLAYER SORTING

    let playersArray
    if (players) playersArray = Object.values(players)

    let keepers
    let defenders
    let midfielders
    let forwards
    if (players) {
        keepers = playersArray.filter (player => player.position == "GK")
        defenders = playersArray.filter (player => player.position == "DF")
        midfielders = playersArray.filter (player => player.position == "MF")
        forwards = playersArray.filter (player => player.position == "FW")
    }

    console.log ("GK ----->", keepers)
    console.log ("DF ----->", defenders)
    console.log ("MF ----->", midfielders)
    console.log ("FW ----->", forwards)

    return (
        user &&
        team &&
        players && (
            <div className="game-page-container">
                <div className="team-div">
                    <div className="team-header">
                        <div className="matchday-div">
                            Matchday {team.match_day}
                        </div>
                        <div className="team-name-div">
                            {team.name}
                        </div>
                        <div className="team-info-div">
                            <div className="transfers-div">
                                <div className="text-info">Transfers</div>
                                <div className="numbers-info">X</div>
                            </div>
                            <div className="points-div">
                                <div className="text-info">Total Points</div>
                                <div className="numbers-info">{team.points}</div>
                            </div>
                            <div className="bank-div">
                                <div className="text-info">Bank</div>
                                <div className="numbers-info">{team.bank} mil</div>
                            </div>
                        </div>
                    </div>
                    <div className="pitch">
                        <div className="team-11-div keeper">
                            <div>keeper</div>
                        </div>
                        <div className="team-11-div defenders">
                            <div>Defender</div>
                        </div>
                        <div className="team-11-div midfielders">
                            <div>midfielders</div>
                        </div>
                        <div className="team-11-div forwards">
                            <div>forwards</div>
                        </div>
                    </div>
                </div>
                <div className="players-list-div">Players</div>
            </div>
        )
    )
}

export default TeamPage
