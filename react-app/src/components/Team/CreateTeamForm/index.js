import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import {
    thunkAddTeam
} from "../../../store/team"
import { useModal } from "../../../context/Modal";

import "./CreateTeam.css"

export default function CreateTeam({league}) {
    const dispatch = useDispatch()
    const [name, setName] = useState("")
	const [errors, setErrors] = useState([]);
    const { closeModal } = useModal();
    const history = useHistory();

    let errorsArray = []
    let leagueId = league.id

    const handleSubmit = async (e) => {
        e.preventDefault();
		setErrors([]);

        if (name.length < 3 || name.length > 20) {
            errorsArray.push("Name must be between 3 and 20 characters")
        }

        if (errorsArray.length > 0) setErrors(errorsArray)


        if (errorsArray.length == 0) {
            dispatch(thunkAddTeam({name, leagueId}))
            .then((data) =>
				history.push(`/league/${leagueId}/team/${data.id}`)
			)
            closeModal()
        }
    }

    return (
        <div className="form-div">
            <div className="title">
                <div className="form-title">Create Team</div>
            </div>
            <form onSubmit={handleSubmit}>
                <ul className="errors">
                    {errors.map((error, idx) => (
                        <li key={idx}>{error}</li>
                    ))}
                </ul>

                <div className="entries">
                    <div className="form-label">
                        <label htmlFor="name" className="name">Name</label>
                    </div>
                    <input
                        type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                    id='team-name-input'
                    />
                </div>

                <div className="form-button">
                    <button type="submit" className="submit-button" id="create-team-button">Create Team</button>
                </div>

            </form>
        </div>
    );

}
