import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkEditLeague, thunkDeleteLeague } from "../../store/leagues.js";
import { useModal } from "../../context/Modal";

import "./EditDeleteLeague.css"

export default function EditDeleteLeagueModal({league}) {
    const dispatch = useDispatch()
	const [errors, setErrors] = useState([]);
    const [name, setName] = useState(league.name)
    const [display_pic, setDisplay_pic] = useState(league.display_pic)
    const [is_private, setIs_Private] = useState(league.is_private)
    const { closeModal } = useModal();

    let errorsArray = []

    let leagueId = league.id


    const handleEdit = async (e) => {
        e.preventDefault();
        setErrors([]);

        if (name.length < 3 || name.length > 20) {
            errorsArray.push("Name must be between 3 and 20 characters")
        }

        if (!display_pic) {
            errorsArray.push("Please set a display picture")
        }

        if (errorsArray.length > 0) setErrors(errorsArray)

        console.log("leagueId ----->", leagueId)

        if (errorsArray.length == 0) {
            dispatch(thunkEditLeague(leagueId, name, display_pic, is_private))
            closeModal()
        }
    }

    const handleDelete = async (e) => {
        e.preventDefault()
        dispatch(thunkDeleteLeague(league.id))
        closeModal();
    }

    return (
        <div className="form-div">
            <div className="title">
                <div className="form-title">Edit or Delete League</div>
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

                    <div className="entries">
                        <div className="form-label">
                            <label htmlFor="display_pic" className="display_pic">Display Pic</label>
                        </div>
                        <input
                        type="text"
                        value={display_pic}
                        onChange={(e) => setDisplay_pic(e.target.value)}
                        required
                        id='league-display-pic-input'
                        />
                    </div>

                    <div className="entries">
                        <div className="form-label">
                            <label htmlFor="is_private" className="is_private">Private League?</label>
                        </div>
                        <input
							className="CreateChannelForm-checkbox"
							type="checkbox"
							checked={is_private}
							onChange={() => setIs_Private(!is_private)}
						/>
                        <div className="CreateLeagueForm-switch">
							<div></div>
						</div>
        		    </div>

                    <div className="form-button">
					    <button type="submit" className="submit-button" id="edit-league-button">Edit League</button>
				    </div>
            </form>
                    <div className="form-button">
					    <button onClick={handleDelete} className="submit-button" id="delete-league-button">Delete League</button>
				    </div>
        </div>
    )
}
