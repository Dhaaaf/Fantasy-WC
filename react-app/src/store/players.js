const GET_PLAYERS = "players/GET_PLAYERS"
const RESET_PLAYERS = "players/RESET_PLAYERS"

// ACTION

// GET
export const actionGetPlayers = (players) => ({
    type: GET_PLAYERS,
    players
})

// RESET
export const actionResetPlayers = () => ({
    type: RESET_PLAYERS
})


// Thunks

// GET

export const thunkGetPlayers = (leagueId) => async (dispatch) => {
    const res = await fetch(`/api/players/league/${leagueId}`);
    if (res.ok) {
        const players = await res.json();
        dispatch(actionGetPlayers(players.players))
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



const initialState = {players: {}}

export default function reducer(state = initialState, action) {
	switch (action.type) {
		case GET_PLAYERS: {
			let newState = { ...state };
			newState = normalize(action.players);
			return newState;
		}
		case RESET_PLAYERS: {
			return {};
		}
		default:
			return state;
	}
}
