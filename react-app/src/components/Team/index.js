import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetTeam, actionResetTeam } from"../../store/team"
import { thunkGetPlayers, actionResetPlayers } from "../../store/players";
import { thunkGetTeamPlayers, actionAddTeamPlayer, actionRemoveTeamPlayer, actionResetTeamPlayers } from "../../store/teamPlayers";
import { NavLink, useHistory } from "react-router-dom";
import { useParams } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";

import "./Team.css"

const TeamPage = () => {
    let dispatch = useDispatch()
    let [isLoaded, setIsLoaded] = useState(false)
	const user = useSelector((state) => state.session.user)
    const leagues = useSelector((state) => state.leagues)
    const players = useSelector((state) => state.players)
    const team = useSelector((state) => state.team)
    const teamPlayers = useSelector((state) => state.teamPlayers)
    const [filterGK, setfilterGK] = useState(false)
    const [filterDF, setfilterDF] = useState(false)
    const [filterMF, setfilterMF] = useState(false)
    const [filterFW, setfilterFW] = useState(true)
    const {leagueId, teamId} = useParams();
    let userId = user.id

    useEffect (() => {
        dispatch(thunkGetTeam(teamId)).
        then(() => setIsLoaded(true));

        return () => {
            dispatch(actionResetTeam());
        }
    }, [dispatch])

    useEffect (() => {
        dispatch(thunkGetTeamPlayers(teamId)).
        then(() => setIsLoaded(true));

        return () => {
            dispatch(actionResetTeamPlayers());
        }
    }, [dispatch])

    useEffect (() => {
        dispatch(thunkGetPlayers(leagueId))

        return () => {
            dispatch(actionResetPlayers());
        }
    }, [])

    // console.log("TEAM ------->", team)
    // console.log("Players ------->", players)

    //// TEAM PLAYERS

    let teamPlayersArray
    if (teamPlayers) {
        teamPlayersArray = Object.values(teamPlayers)
    }


    let teamKeeper;
    let teamDefense;
    let teamMidfield;
    let teamAttack

    if (teamPlayers) {
        teamKeeper = teamPlayersArray.filter(player => player.position == "GK")
        teamDefense = teamPlayersArray.filter(player => player.position == "DF")
        teamMidfield = teamPlayersArray.filter(player => player.position == "MF")
        teamAttack = teamPlayersArray.filter(player => player.position == "FW")
    }

















    //// PLAYER SORTING

    let playersArray
    if (players) playersArray = Object.values(players)

    let keepers
    let defenders
    let midfielders
    let forwards
    /// Sorting by position, and then sorting by value
    if (players) {
        keepers = playersArray.filter (player => player.position == "GK")
        keepers.sort((a, b) => b.value - a.value);
        defenders = playersArray.filter (player => player.position == "DF")
        defenders.sort((a, b) => b.value - a.value);
        midfielders = playersArray.filter (player => player.position == "MF")
        midfielders.sort((a, b) => b.value - a.value);
        forwards = playersArray.filter (player => player.position == "FW")
        forwards.sort((a, b) => b.value - a.value);
    }

    // console.log ("GK ----->", keepers)
    // console.log ("DF ----->", defenders)
    // console.log ("MF ----->", midfielders)
    // console.log ("FW ----->", forwards)

    //// FILTERING PLAYERS BY POSITION

    const filterForwards = () => {
        setfilterFW(true)
        setfilterMF(false)
        setfilterDF(false)
        setfilterGK(false)
    }

    const filterMidfielders = () => {
        setfilterFW(false)
        setfilterMF(true)
        setfilterDF(false)
        setfilterGK(false)
    }

    const filterDefenders = () => {
        setfilterFW(false)
        setfilterMF(false)
        setfilterDF(true)
        setfilterGK(false)
    }

    const filterKeepers = () => {
        setfilterFW(false)
        setfilterMF(false)
        setfilterDF(false)
        setfilterGK(true)
    }

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
                                <div className="numbers-info">{team.bank}</div>
                            </div>
                        </div>
                    </div>
                    <div className="pitch">
                        <div className="team-11-div team-keeper">
                            
                        </div>
                        <div className="team-11-div team-defenders">
                            <div>Defender</div>
                        </div>
                        <div className="team-11-div team-midfielders">
                            <div>midfielders</div>
                        </div>
                        <div className="team-11-div team-forwards">
                            <div>forwards</div>
                        </div>
                    </div>
                </div>



                {/* RIGHT SIDE OF PAGE */}
                <div className="players-list-div">
                    <div className="players-list-header">
                        <h1>Transfer Market</h1>
                    </div>
                    {filterGK && (
                    <div className="position-selector-div">
                        <div className="position-selector gold" onClick={filterKeepers}>GK</div>
                        <div className="position-selector" onClick={filterDefenders}>DF</div>
                        <div className="position-selector" onClick={filterMidfielders}>MF</div>
                        <div className="position-selector" onClick={filterForwards}>FW</div>
                    </div>
                    )}
                    {filterDF && (
                    <div className="position-selector-div">
                        <div className="position-selector" onClick={filterKeepers}>GK</div>
                        <div className="position-selector gold" onClick={filterDefenders}>DF</div>
                        <div className="position-selector" onClick={filterMidfielders}>MF</div>
                        <div className="position-selector" onClick={filterForwards}>FW</div>
                    </div>
                    )}
                    {filterMF && (
                    <div className="position-selector-div">
                        <div className="position-selector" onClick={filterKeepers}>GK</div>
                        <div className="position-selector" onClick={filterDefenders}>DF</div>
                        <div className="position-selector gold" onClick={filterMidfielders}>MF</div>
                        <div className="position-selector" onClick={filterForwards}>FW</div>
                    </div>
                    )}
                    {filterFW && (
                    <div className="position-selector-div">
                        <div className="position-selector" onClick={filterKeepers}>GK</div>
                        <div className="position-selector" onClick={filterDefenders}>DF</div>
                        <div className="position-selector" onClick={filterMidfielders}>MF</div>
                        <div className="position-selector gold" onClick={filterForwards}>FW</div>
                    </div>
                    )}
                    {filterGK && (
                        <div className="players-list">
                        {keepers.map(player => (
                            <div key={player.id} className="player-list-item">
                                <img src={player.picture} className="player-img"></img>
                                <div className="name-year-div">
                                    <div className="player-name">{player.aka}</div>
                                    <div className="player-year">{player.year}</div>
                                </div>
                                <div className="player-value">€ {player.value}</div>
                            </div>
                        ))}
                    </div>
                    )}
                    {filterDF && (
                        <div className="players-list">
                        {defenders.map(player => (
                            <div key={player.id} className="player-list-item">
                                <img src={player.picture} className="player-img"></img>
                                <div className="name-year-div">
                                    <div className="player-name">{player.aka}</div>
                                    <div className="player-year">{player.year}</div>
                                </div>
                                <div className="player-value">€ {player.value}</div>
                            </div>
                        ))}
                    </div>
                    )}
                    {filterMF && (
                    <div className="players-list">
                        {midfielders.map(player => (
                            <div key={player.id} className="player-list-item">
                                <img src={player.picture} className="player-img"></img>
                                <div className="name-year-div">
                                    <div className="player-name">{player.aka}</div>
                                    <div className="player-year">{player.year}</div>
                                </div>
                                <div className="player-value">€ {player.value}</div>
                            </div>
                        ))}
                    </div>
                        )}
                    {filterFW && (
                    <div className="players-list">
                        {forwards.map(player => (
                            <div key={player.id} className="player-list-item">
                                <img src={player.picture} className="player-img"></img>
                                <div className="name-year-div">
                                    <div className="player-name">{player.aka}</div>
                                    <div className="player-year">{player.year}</div>
                                </div>
                                <div className="player-value">€ {player.value}</div>
                            </div>
                        ))}
                    </div>
                    )}
                </div>
            </div>
        )
    )
}

export default TeamPage
