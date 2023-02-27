import React, { useEffect } from "react";
import { useDispatch} from "react-redux";
import { actionAddTeamPlayer, actionRemoveTeamPlayer } from "../../store/teamPlayers";
import { actionAddBudget, actionRemoveBudget } from "../../store/team";
import { useModal } from "../../context/Modal";
import "./PlayerModal.css"

export default function PlayerModal({team, player, teamPlayers}) {
    const dispatch = useDispatch();
    const {closeModal} = useModal()

    let teamPlayersArray = Object.values(teamPlayers)
    let teamPlayersIds = teamPlayersArray.map(player => (player.id))
    console.log("teamplayers ----->", teamPlayersIds)

    let matchDay = team.match_day



    let playerMatchDayStats = player.stats[matchDay -1]

    const transferIn = (player) => {
        dispatch(actionAddTeamPlayer(player))
        dispatch(actionRemoveBudget(player.value))
        closeModal()
    }

    const transferOut = (player) => {
        dispatch(actionRemoveTeamPlayer(player))
        dispatch(actionAddBudget(player.value))
        closeModal()
    }



    return (
        <div className="player-modal-card">
            <img className="player-modal-card-img" src={player.picture}></img>
            <div className="player-modal-card-right">
                <div className="player-modal-card-info">
                    <div className="player-modal-card-name">{player.first_name} {player.last_name}</div>
                    <div className="player-modal-card-team">{player.team} {player.year}</div>
                    {player.position == "GK" && (
                    <div className="player-modal-card-position">Goal Keeper</div>
                    )}
                    {player.position == "DF" && (
                    <div className="player-modal-card-position">Defender</div>
                    )}
                    {player.position == "MF" && (
                    <div className="player-modal-card-position">Midfielder</div>
                    )}
                    {player.position == "FW" && (
                    <div className="player-modal-card-position">Forward</div>
                    )}
                    <div className="player-modal-card-value">€{player.value} million</div>
                    {matchDay > 0 && (
                    <div className="player-modal-card-matchday-outer-div">
                        {matchDay < 4 && (
                        <div className="player-modal-card-matchday">Matchday {playerMatchDayStats.week}</div>
                        )}
                        {matchDay == 4 && (
                        <div className="player-modal-card-matchday">Round of 16</div>
                        )}
                        {matchDay == 5 && (
                        <div className="player-modal-card-matchday">Quarter-Final</div>
                        )}
                        {matchDay == 6 && (
                        <div className="player-modal-card-matchday">Semi-Final</div>
                        )}
                        {matchDay == 7 && (
                        <div className="player-modal-card-matchday">Final</div>
                        )}
                        <div className="player-modal-card-stats">
                            <div className="player-modal-card-stats-inner">Total Points: {playerMatchDayStats.points}</div>
                            <div className="player-modal-card-stats-inner">Goals: {playerMatchDayStats.goals}</div>
                            <div className="player-modal-card-stats-inner">Assists: {playerMatchDayStats.assists}</div>
                            {playerMatchDayStats.clean_sheet && (
                            <div className="player-modal-card-stats-inner motm">Clean Sheet</div>
                            )}
                            {playerMatchDayStats.man_of_the_match && (
                            <div className="player-modal-card-stats-inner">Man of the Match</div>
                            )}
                        </div>
                    </div>
                    )}
                </div>
                <div className="player-modal-card-tranfers">
                    {teamPlayersIds.includes(player.id) && (
                        <div className="transfer-button transfer-out" onClick={() => transferOut(player)}> Transfer Out</div>
                    )}
                    {!teamPlayersIds.includes(player.id) && teamPlayersArray.length < 11 && (
                        <div className="transfer-button transfer-in" onClick={() => transferIn(player)}> Transfer In</div>
                    )}
                    {!teamPlayersIds.includes(player.id) && teamPlayersArray.length == 11 && (
                        <div className="transfer-button-too-many-players">Can't have more than 11 players</div>
                    )}
                </div>
            </div>
        </div>
    )

}
