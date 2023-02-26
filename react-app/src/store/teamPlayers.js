const GET_TEAMPLAYERS = "teamPlayers/GET_TEAMPLAYERS"
const ADD_TEAMPLAYER = "teamPlayers/ADD_TEAMPLAYERS"
const REMOVE_TEAMPLAYER = "teamPlayers/REMOVE_TEAMPLAYERS"
const RESET_TEAMPLAYER = "teamPlayers/RESET_TEAMPLAYERS"

// ACTION

// GET
export const actionGetTeamPlayers = (players) => ({
    type: GET_TEAMPLAYERS,
    players
})

// ADD
export const actionAddTeamPlayer = (player) => ({
    type: ADD_TEAMPLAYER,
    player
})

// REMOVE
export const actionRemoveTeamPlayer = (player) => ({
    type: REMOVE_TEAMPLAYER,
    player
})

// RESET
export const actionResetTeamPlayers = () => ({
    type: RESET_TEAMPLAYER
})



// THUNKS

// GET
export const thunkGetTeamPlayers = (teamId) => async (dispatch) => {
    const res = await fetch(`/api/user_teams/${teamId}/players`);
    if (res.ok) {
        const players = await res.json()
        dispatch(actionGetTeamPlayers(players.players))
        return players.players
    } else if (res.status < 500) {
		const data = await res.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
}



const normalize = (players) => {
	const data = {};
	if (players) {
		players.forEach((player) => (data[player.id] = player));
		return data;
	}
};

const initialState = {teamPlayers: {}}

export default function reducer(state = initialState, action) {
    switch(action.type) {
        case GET_TEAMPLAYERS: {
            let newState = { ...state };
            newState = normalize(action.players)
            return newState
        }
        case ADD_TEAMPLAYER: {
            let newState = { ...state };
            newState[action.player.id] = action.player
            return newState
        }
        case REMOVE_TEAMPLAYER: {
            let newState = { ...state }
            delete newState[action.player.id]
            return newState
        }
        case RESET_TEAMPLAYER: {
            return {};
        }
        default:
			return state;
    }
}
