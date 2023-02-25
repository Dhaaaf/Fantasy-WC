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
    const {serverId, teamId} = useParams();
    let userId = user.id

    useEffect (() => {
        dispatch(thunkGetTeam).
        then(() => setIsLoaded(true));

        return () => {
            dispatch(actionResetTeam);
        }
    })

    useEffect (() => {
        dispatch(thunkGetPlayers)

        return () => {
            dispatch(actionResetPlayers);
        }
    }, [])

    return (
        user &&
        team &&
        players && (
            <div> Team Page</div>
        )
    )
}

export default TeamPage
