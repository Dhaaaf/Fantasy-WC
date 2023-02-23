import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import {
    thunkAddLeague,
} from "../../store/leagues"
import {
    thunkGetTournaments
} from "../../store/tournaments"
import "./CreateLeagueForm.css"

export default function CreateLeague() {
    const dispatch = useDispatch();
    const [name, setName] = useState("")
    let [isLoaded, setIsLoaded] = useState(false)
    const [display_pic, setDisplay_pic] = useState("")
    const [team_budget, setTeam_BUdget] = useState(100)
    const [is_private, setIs_Private] = useState(false)
    const [is2022, setis2022] = useState(true)
    const [is2018, setis2018] = useState(true)
    const [is2014, setis2014] = useState(true)
    const [is2010, setis2010] = useState(true)
    const [is2006, setis2006] = useState(true)
    const [is2002, setis2002] = useState(true)
    const [is1998, setis1998] = useState(true)
	const [errors, setErrors] = useState([]);

    useEffect(() => {
		dispatch(thunkGetTournaments()).
        then(() => setIsLoaded(true));
	}, [dispatch]);

    let tournaments = []

    const handleSubmit = (e) => {
        e.preventDefault();
		setErrors([]);
    }

    console.log(is_private)

    if (isLoaded) {
		return (
            <div className="form-div">
                <div className="title">
                    <div className="form-title">Creat League</div>
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
                            <label htmlFor="team_budget" className="team_budget">Team Budget</label>
                        </div>
                        <input
                        type="text"
                        value={team_budget}
                        onChange={(e) => setTeam_BUdget(e.target.value)}
                        required
                        id='league-budget-input'
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

                    <div className="entries">
                        <div className="form-label">
                            <label htmlFor="is2022" className="is2022">2022 World Cup</label>
                        </div>
                        <input
							className="CreateChannelForm-checkbox"
							type="checkbox"
							checked={is2022}
							onChange={() => setis2022(!is2022)}
						/>
                        <div className="CreateLeagueForm-switch">
							<div></div>
						</div>
        		    </div>

                    <div className="entries">
                        <div className="form-label">
                            <label htmlFor="is2018" className="is2018">2018 World Cup</label>
                        </div>
                        <input
							className="CreateChannelForm-checkbox"
							type="checkbox"
							checked={is2018}
							onChange={() => setis2018(!is2018)}
						/>
                        <div className="CreateLeagueForm-switch">
							<div></div>
						</div>
        		    </div>

                    <div className="entries">
                        <div className="form-label">
                            <label htmlFor="is2014" className="is2014">2014 World Cup</label>
                        </div>
                        <input
							className="CreateChannelForm-checkbox"
							type="checkbox"
							checked={is2014}
							onChange={() => setis2014(!is2014)}
						/>
                        <div className="CreateLeagueForm-switch">
							<div></div>
						</div>
        		    </div>

                    <div className="entries">
                        <div className="form-label">
                            <label htmlFor="is2010" className="is2010">2010 World Cup</label>
                        </div>
                        <input
							className="CreateChannelForm-checkbox"
							type="checkbox"
							checked={is2010}
							onChange={() => setis2010(!is2010)}
						/>
                        <div className="CreateLeagueForm-switch">
							<div></div>
						</div>
        		    </div>

                    <div className="entries">
                        <div className="form-label">
                            <label htmlFor="is2006" className="is2006">2006 World Cup</label>
                        </div>
                        <input
							className="CreateChannelForm-checkbox"
							type="checkbox"
							checked={is2006}
							onChange={() => setis2006(!is2006)}
						/>
                        <div className="CreateLeagueForm-switch">
							<div></div>
						</div>
        		    </div>

                    <div className="entries">
                        <div className="form-label">
                            <label htmlFor="is2002" className="is2002">2002 World Cup</label>
                        </div>
                        <input
							className="CreateChannelForm-checkbox"
							type="checkbox"
							checked={is2002}
							onChange={() => setis2002(!is2002)}
						/>
                        <div className="CreateLeagueForm-switch">
							<div></div>
						</div>
        		    </div>

                    <div className="entries">
                        <div className="form-label">
                            <label htmlFor="is1998" className="is1998">1998 World Cup</label>
                        </div>
                        <input
							className="CreateChannelForm-checkbox"
							type="checkbox"
							checked={is1998}
							onChange={() => setis1998(!is1998)}
						/>
                        <div className="CreateLeagueForm-switch">
							<div></div>
						</div>
        		    </div>

                    <div className="form-button">
					<button type="submit" className="submit-button" id="create-league-button">Create League</button>
				</div>

                </form>
            </div>
		);
	} else return <div>Loading...</div>;
}
