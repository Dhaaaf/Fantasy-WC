const GET_TEAM = "team/GET_TEAM";
const ADD_TEAM = "team/ADD_TEAM";
const EDIT_TEAM = "team/EDIT_TEAM"
const ADD_PLAYER = "team/ADD_PLAYER";
const DELETE_PLAYER = "team/DELETE_PLAYER";
const RESET_TEAM = "team/DELETE_TEAM"


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
export const thunkAddTeam = (name, leagueId) => async(dispatch) => {
    const res = await fetch (`/api/user_teams/league/${leagueId}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(name),
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
		case RESET_TEAM: {
			return {};
		}
		default:
			return state;
	}
}
