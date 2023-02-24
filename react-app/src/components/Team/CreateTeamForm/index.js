import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import {
    thunkAddTeam
} from "../../../store/team"
import { useModal } from "../../context/Modal";

import "./CreateTeam.css"

export default function CreateTeam({league}) {
    const dispatch = useDispatch()
    const [name, setName] = useState("")
    const { closeModal } = useModal();

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
            dispatch(thunkAddLeague({name, display_pic, team_budget, is_private, tournaments}));
            closeModal()
        }

    }

}
