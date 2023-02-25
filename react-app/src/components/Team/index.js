import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetTeam, actionResetTeam } from"../../store/team"
import { thunkGetPlayers, actionResetPlayers } from "../../store/players";
import { NavLink, useHistory } from "react-router-dom";
import { useParams } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
// import pitch from "../../assets/Fantasy-Style-Football-Pitch2.jpg"


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
                        Team header
                    </div>
                    <div className="pitch">
                        Pitch header
                    </div>
                </div>
                <div className="players-list-div">Players</div>
            </div>
        )
    )
}

export default TeamPage
