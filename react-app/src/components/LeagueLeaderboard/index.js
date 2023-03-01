import React, { useEffect, useState } from "react";
import { useModal } from "../../context/Modal";

import "./LeagueLeaderboard.css"

export default function LeagueLeaderboard({league}) {
    // const {closeModal} = useModal()

    const teams = league.teams

    teams.sort((a,b) => b.points - a.points)

    return (
        <div className="leaderboard-outer-div">
            <div className="leaderboard-inner-div">
                <div className="leaderboard-league-name">{league.name}</div>
                <div className="leaderboard-header">
                    <div className="leaderboard-rank">Rank</div>
                    <div className="leaderboard-name-manager">Team & Manager</div>
                    <div className="leaderboard-match-day">Match Day</div>
                    <div className="leaderboard-points">Points</div>
                </div>
                {teams.length > 0 ? (
                <div className="leaderboard-footer">
                    {teams.map((team, i) => (
                        <div key={team.id} className="leaderboard-team-standings">
                            <div className="leaderboard-team-rank">{i + 1}</div>
                            <div className="team-name-manager">
                                <div className="leaderboard-team-name">{team.name}</div>
                                <div className="leaderboard-team-manager">{team.user.username}</div>
                            </div>
                            <div className="leaderboard-team-md">{team.match_day}</div>
                            <div className="leaderboard-team-points">{team.points}</div>
                        </div>
                    ))}
                </div>

                ): (
                <div className="no-teams">
                    No Teams
                </div>
                )}
            </div>
        </div>
    )
}
