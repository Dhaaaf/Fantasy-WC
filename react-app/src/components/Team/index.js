import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetTeam, actionResetTeam, thunkNextMatchDay } from"../../store/team"
import { thunkGetPlayers, actionResetPlayers } from "../../store/players";
import { thunkGetTeamPlayers, actionAddTeamPlayer, actionRemoveTeamPlayer, actionResetTeamPlayers } from "../../store/teamPlayers";
import { NavLink, useHistory } from "react-router-dom";
import { useParams } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import PlayerModal from "../PlayerModal";
import EditDeleteTeam from "../TeamEditDelete";
import FinalLeagueLeaderboard from "../LeagueLeaderboard/FinalLeagueLeaderboard";

import "./Team.css"

const TeamPage = () => {
    let dispatch = useDispatch()
    let [isLoaded, setIsLoaded] = useState(false)
	const user = useSelector((state) => state.session.user)
    const leagues = useSelector((state) => state.leagues)
    const players = useSelector((state) => state.players)
    const [showMenu, setShowMenu] = useState(false);
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

    // console.log("TEAMPLAYERS =======>", teamPlayersArray)
    // console.log("TEAMPLAYERS =======>", teamKeeper)
    // console.log("TEAMPLAYERS =======>", teamDefense)
    // console.log("TEAMPLAYERS =======>", teamMidfield)
    // console.log("TEAMPLAYERS =======>", teamAttack)





    //// Transfer Counter

    let transfers
    if (team.match_day == 0) {
        transfers = 9999999999999
    }
    if (team.match_day < 4 && team.match_day > 0) {
        transfers = 2
    }

    if (team.match_day >= 4) {
        transfers = 3
    }

    let zeroOrSeven = (team.match_day == 0 || team.match_day == 7)

    let teamPlayersIds
    let transfersMade = 0
    if (team && teamPlayersArray && team.players) {
        let dbPlayers = team.players
        let dbPlayersIds = dbPlayers.map(player => player.id)
        teamPlayersIds = teamPlayersArray.map(player => (player.id))

        // console.log("DB PLAYERS------>", dbPlayersIds)
        // console.log("COMPARING ARRAYS ------>", teamPlayersIds)

        const diff = teamPlayersIds.filter(id => !dbPlayersIds.includes(id));
        transfersMade = diff.length
    }

    let transfersLeft = transfers - transfersMade









    //// PLAYER SORTING

    let playersArray
    if (players) playersArray = Object.values(players)

    let keepers
    let defenders
    let midfielders
    let forwards
    //// Sorting by position, and then sorting by value
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


    //// RESET TRANSFERS BUTTON

    const resetTransfers = () => {
        dispatch(thunkGetTeamPlayers(teamId))
        dispatch(thunkGetTeam(teamId))
    }


    //// NEXT MATCHDAY

    const nextMatchDay = async () => {
        console.log("nextMatchDay stuff ----->", teamPlayersArray)
        console.log("nextMatchDay stuff ----->", teamPlayersIds)
        console.log("Transfers Left ---->", transfersLeft)

        let bank =team.bank

        let payload = {
            teamId,
            teamPlayersIds,
            transfersLeft,
            bank
        }

        dispatch(thunkNextMatchDay(payload)).
        then(() => dispatch(thunkGetTeam(teamId)))
    }

    let canMoveNext = false
    if (teamPlayersArray.length == 11 && team.match_day < 7) canMoveNext = true





  const closeMenu = () => setShowMenu(false);

    return (
        user &&
        team &&
        players && (
            <div className="game-page-container">
                <div className="team-div">
                    <div className="team-header">
                        {team.match_day === 0 && (
                        <div className="matchday-div">Select Squad</div>
                        )}
                        {team.match_day < 4 && team.match_day !== 0 && (
                        <div className="matchday-div">Matchday {team.match_day}</div>
                        )}
                        {team.match_day == 4 && (
                        <div className="matchday-div">Round of 16</div>
                        )}
                        {team.match_day == 5 && (
                        <div className="matchday-div">Quarter-Final</div>
                        )}
                        {team.match_day == 6 && (
                        <div className="matchday-div">Semi-Final</div>
                        )}
                        {team.match_day == 7 && (
                        <div className="matchday-div">Final</div>
                        )}
                        <div className="team-name-div">
                            <div className="reset-button" onClick={() => resetTransfers()}> <i className="fa-solid fa-arrows-rotate"></i>  Reset Transfers</div>
                            <div className="team-name">
                                <div className="inner-team-name">{team.name}</div>
                                <div className="name-edit-delete">
                                    <OpenModalButton
                                        modalComponent={<EditDeleteTeam team={team} />}
                                        buttonText="edit-team-name"
                                        onbuttonClick={closeMenu}
                                    />
                                </div>
                            </div>
                            {canMoveNext && (<div className="next-match-button" onClick={() => nextMatchDay()}>Next Match Day  <i className="fa-solid fa-arrow-right"></i></div>)}
                            {teamPlayersArray.length < 11 && (<div className="next-match-button disabled">Select a valid Squad </div>)}
                            {team.match_day == 7 && (
                            // <div className="check-table">League Table <i className="fa-solid fa-table"></i></div>
                            <div className="final-league-leaderboard">   
                                        <OpenModalButton
                                            modalComponent={<FinalLeagueLeaderboard leagueId={leagueId} team={team} />}
                                            buttonText="leaderboard"
                                            onbuttonClick={closeMenu}
                                            />
                                        </div>
                            )}
                        </div>
                        <div className="team-info-div">
                            <div className="transfers-div">
                                <div className="text-info">Transfers Left</div>
                                {zeroOrSeven ? (
                                    <div className="numbers-info"><i className="fa-solid fa-infinity"></i></div>
                                ): (
                                    <div>
                                        {transfersLeft >= 0 ? (
                                            <div className="numbers-info">{transfersLeft}</div>
                                        ) : (
                                            <div className="numbers-info red">{transfersLeft}</div>
                                        )}
                                    </div>
                                )}
                            </div>
                            <div className="points-div">
                                {team.match_day == 7 && (<div className="text-info">Final Points</div>)}
                                {team.match_day  < 7 && (<div className="text-info">Total Points</div>)}
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
                            {teamKeeper.length > 0 && (
                                teamKeeper.map(player => (
                                    <div key={player.id} className="team-11-player-card team-11-keeper">
                                        <img src={player.picture} className="team-11-player-img"></img>
                                        {/* <div className="team-11-player-name">{player.aka}</div> */}
                                        <div className="team-11-player-name">
                                            <OpenModalButton
                                            modalComponent={<PlayerModal team={team} player={player} teamPlayers={teamPlayers} />}
                                            buttonText={player.aka}
                                            onbuttonClick={closeMenu}
                                            />
                                        </div>
                                        {team.match_day > 0 ? (
                                            <div className="team-11-player-value">{player.stats[team.match_day -1].points} points</div>
                                        ) : (
                                            <div className="team-11-player-value">€ {player.value}</div>
                                        )}
                                    </div>
                                ))
                            )}
                        </div>
                        <div className="team-11-div team-defenders">
                        {teamDefense.length > 0 && (
                                teamDefense.map(player => (
                                    <div key={player.id} className="team-11-player-card team-11-keeper">
                                        <img src={player.picture} className="team-11-player-img"></img>
                                        {/* <div className="team-11-player-name">{player.aka}</div> */}
                                        <div className="team-11-player-name">
                                            <OpenModalButton
                                            modalComponent={<PlayerModal team={team} player={player} teamPlayers={teamPlayers} />}
                                            buttonText={player.aka}
                                            onbuttonClick={closeMenu}
                                            />
                                        </div>
                                        {team.match_day > 0 ? (
                                            <div className="team-11-player-value">{player.stats[team.match_day -1].points} points</div>
                                        ) : (
                                            <div className="team-11-player-value">€ {player.value}</div>
                                        )}
                                    </div>
                                ))
                            )}
                        </div>
                        <div className="team-11-div team-midfielders">
                        {teamMidfield.length > 0 && (
                                teamMidfield.map(player => (
                                    <div key={player.id} className="team-11-player-card team-11-keeper">
                                        <img src={player.picture} className="team-11-player-img"></img>
                                        {/* <div className="team-11-player-name">{player.aka}</div> */}
                                        <div className="team-11-player-name">
                                            <OpenModalButton
                                            modalComponent={<PlayerModal team={team} player={player} teamPlayers={teamPlayers} />}
                                            buttonText={player.aka}
                                            onbuttonClick={closeMenu}
                                            />
                                        </div>
                                        {team.match_day > 0 ? (
                                            <div className="team-11-player-value">{player.stats[team.match_day -1].points} points</div>
                                        ) : (
                                            <div className="team-11-player-value">€ {player.value}</div>
                                        )}
                                    </div>
                                ))
                            )}
                        </div>
                        <div className="team-11-div team-forwards">
                        {teamAttack.length > 0 && (
                                teamAttack.map(player => (
                                    <div key={player.id} className="team-11-player-card team-11-keeper">
                                        <img src={player.picture} className="team-11-player-img"></img>
                                        {/* <div className="team-11-player-name">{player.aka}</div> */}
                                        <div className="team-11-player-name">
                                            <OpenModalButton
                                            modalComponent={<PlayerModal team={team} player={player} teamPlayers={teamPlayers} />}
                                            buttonText={player.aka}
                                            onbuttonClick={closeMenu}
                                            />
                                        </div>
                                        {team.match_day > 0 ? (
                                            <div className="team-11-player-value">{player.stats[team.match_day -1].points} points</div>
                                        ) : (
                                            <div className="team-11-player-value">€ {player.value}</div>
                                        )}
                                    </div>
                                ))
                            )}
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
                                    {/* <div className="player-name">{player.aka}</div> */}
                                    <div className="player-name">
                                    <OpenModalButton
                                        modalComponent={<PlayerModal team={team} player={player} teamPlayers={teamPlayers} />}
                                        buttonText={player.aka}
                                        onbuttonClick={closeMenu}
                                        />
                                    </div>
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
                                    {/* <div className="player-name">{player.aka}</div> */}
                                    <div className="player-name">
                                    <OpenModalButton
                                        modalComponent={<PlayerModal team={team} player={player} teamPlayers={teamPlayers} />}
                                        buttonText={player.aka}
                                        onbuttonClick={closeMenu}
                                        />
                                    </div>
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
                                    {/* <div className="player-name">{player.aka}</div> */}
                                    <div className="player-name">
                                    <OpenModalButton
                                        modalComponent={<PlayerModal team={team} player={player} teamPlayers={teamPlayers} />}
                                        buttonText={player.aka}
                                        onbuttonClick={closeMenu}
                                        />
                                    </div>
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
                                    {/* <div className="player-name">{player.aka}</div> */}
                                    <div className="player-name">
                                    <OpenModalButton
                                        modalComponent={<PlayerModal team={team} player={player} teamPlayers={teamPlayers} />}
                                        buttonText={player.aka}
                                        onbuttonClick={closeMenu}
                                        />
                                    </div>
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
