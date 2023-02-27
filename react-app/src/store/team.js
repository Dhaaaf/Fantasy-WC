const GET_TEAM = "team/GET_TEAM";
const ADD_TEAM = "team/ADD_TEAM";
const EDIT_TEAM = "team/EDIT_TEAM"
// const ADD_PLAYER = "team/ADD_PLAYER";
// const REMOVE_PLAYER = "team/REMOVE_PLAYER";
const RESET_TEAM = "team/DELETE_TEAM"
const ADD_BUDGET = "team/ADD_BUDGET"
const REMOVE_BUDGET = "team/REMOVE/BUDGET"

const EDIT_NEXT_MATCHDAY = "team/EDIT_NEXT_MATCHDAY"


// ACTION

// GET
export const actionGetTeam = (team) => ({
    type: GET_TEAM,
    team
})

// CREATE
export const actionAddTeam = (team) => ({
    type: ADD_TEAM,
    team
})

// EDIT
export const actionEditTeam = (team) => ({
    type: EDIT_TEAM,
    team
})

// DELETE
export const actionResetTeam = () => ({
    type: RESET_TEAM
})

// ADD BUDGET
export const actionAddBudget = (value) => ({
    type: ADD_BUDGET,
    value
})

// Remove BUDGET
export const actionRemoveBudget = (value) => ({
    type: REMOVE_BUDGET,
    value
})

// EDIT NEXT MATCH DAY
export const actionNextMatchDay = (team) => ({
    type: EDIT_NEXT_MATCHDAY,
    team
})

// // ADD PLAYER
// export const actionAddPlayer = (player) => ({
//     type: ADD_PLAYER,
//     player
// })

// // REMOVE PLAYER
// export const actionRemovePlayer = (player) => ({
//     type: REMOVE_PLAYER,
//     player
// })



// Thunks

// GET

export const thunkGetTeam = (teamId) => async (dispatch) => {
    const res = await fetch(`/api/user_teams/${teamId}`);
    if (res.ok) {
        const team = await res.json()
        dispatch(actionGetTeam(team.team))
        return team.team
    } else if (res.status < 500) {
		const data = await res.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
}

// CREATE
export const thunkAddTeam = (payload) => async(dispatch) => {
    const {name, leagueId} = payload
    const res = await fetch (`/api/user_teams/league/${leagueId}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({name, leagueId}),
    });
    if (res.ok) {
        const data = await res.json()
        dispatch(actionAddTeam(data.team))
        return data.team;
    } else if (res.status < 500) {
        const data = await res.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return ["An error occurred. Please try again."];
    }
}

// EDIT

export const thunkNextMatchDay = (payload) => async(dispatch) => {
    const {teamId, teamPlayersIds, transfersLeft, bank} = payload
    const res = await fetch (`/api/user_teams/${teamId}/next_match`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({teamId, teamPlayersIds, transfersLeft, bank}),
    });
    if (res.ok) {
        const data = await res.json()
        dispatch(actionNextMatchDay(data.team))
        return data.team;
    } else if (res.status < 500) {
        const data = await res.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return ["An error occurred. Please try again."];
    }
}


// EDIT TEAM NAME

export const thunkEditTeamName = (payload) => async(dispatch) => {
    const {teamId, name} = payload
    const res = await fetch (`/api/user_teams/${teamId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({name}),
    });
    if (res.ok) {
        const data = await res.json()
        dispatch(actionEditTeam(data.team))
        return data.team;
    } else if (res.status < 500) {
        const data = await res.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return ["An error occurred. Please try again."];
    }
}

// DELETE

export const thunkDeleteTeam = (teamId) => async(dispatch) => {
    const res = await fetch (`/api/user_teams/${teamId}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    });
    if (res.ok) {
        const data = await res.json()
        dispatch(actionResetTeam())
        return data.team;
    } else if (res.status < 500) {
        const data = await res.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return ["An error occurred. Please try again."];
    }
}




const initialState = {team: {}}

export default function reducer(state = initialState, action) {
	switch (action.type) {
		case GET_TEAM: {
			let newState = { ...state };
			newState = action.team;
			return newState;
		}
        case ADD_TEAM: {
            let newState = { ...state };
			newState = action.team;
			return newState;
        }
        case ADD_BUDGET: {
            let newState = { ...state };
            newState.bank += action.value
            return newState
        }
        case REMOVE_BUDGET: {
            let newState = { ...state };
            newState.bank -= action.value
            return newState
        }
        case EDIT_TEAM:{
            let newState = {...state}
            newState = action.team
            return newState
        }
		case RESET_TEAM: {
			return {};
		}
		default:
			return state;
	}
}
