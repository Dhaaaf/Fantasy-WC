import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkDeleteTeam, thunkEditTeamName, thunkGetTeam } from "../../store/team";
import { useModal } from "../../context/Modal";
import { useHistory } from "react-router-dom";


import "./TeamEditDelete.css"

export default function EditDeleteTeam({team}) {
    const dispatch = useDispatch()
    const [errors, setErrors] = useState([]);
    const [name, setName] = useState(team.name)
    const { closeModal } = useModal();
    const history = useHistory();


    const teamId = team.id

    let errorsArray = []

    let bank = team.bank


    const handleEdit = async (e) => {
        e.preventDefault();
        setErrors([]);

        if (name.length < 3 || name.length > 20) {
            errorsArray.push("Name must be between 3 and 20 characters")
        }



        if (errorsArray.length > 0) setErrors(errorsArray)


        if (errorsArray.length == 0) {
            dispatch(thunkEditTeamName({teamId, name, bank})).
            then(() => dispatch(thunkGetTeam(teamId)))
            closeModal()
        }
    }

    const handleDelete = async (e) => {
        e.preventDefault()
        dispatch(thunkDeleteTeam(teamId))
        closeModal();
        history.push(`/leagues`)
    }


    return (
        <div className="form-div">
            <div className="title">
                <div className="form-title">Edit or Delete Team</div>
            </div>
            <form onSubmit={handleEdit}>
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
                        id='league-name-input'
                        />
        		    </div>

                    <div className="form-button">
					    <button type="submit" className="submit-button" id="edit-league-button">Edit Team</button>
				    </div>
            </form>
                    <div className="form-button">
					    <button onClick={handleDelete} className="submit-button" id="delete-league-button">Delete Team</button>
				    </div>
        </div>
    )



}
