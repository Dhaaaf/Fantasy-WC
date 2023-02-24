const GET_TOURNAMENTS = "tournament/GET_TOURNAMENTS"

//ACTION

// GET
export const actionGetTournaments = (tournaments) => ({
    type: GET_TOURNAMENTS,
    tournaments
})


// THUNKS

// GET
export const thunkGetTournaments = () => async (dispatch) => {
    const res = await fetch('/api/tournaments/')
    if (res.ok) {
        const tournaments = await res.json();
        dispatch(actionGetTournaments(tournaments.tournaments))
        return tournaments.tournaments
    } else if (res.status < 500) {
		const data = await res.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
}


const normalize = (tournaments) => {
	const data = {};
	if (tournaments) {
		tournaments.forEach((tournament) => (data[tournament.id] = tournament));
		return data;
	}
};

const initialState = {tournaments: {}}


export default function reducer(state = initialState, action) {
	switch (action.type) {
		case GET_TOURNAMENTS: {
			let newState = { ...state };
			newState = normalize(action.tournaments);
			return newState;
		}
		default:
			return state;
	}
}
