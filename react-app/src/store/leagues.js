const GET_LEAGUES = "league/GET_LEAGUES";
const ADD_LEAGUE = "league/ADD_LEAGUES";
const EDIT_LEAGUE = "league/EDIT_LEAGUE";
const DELETE_LEAGUE = "league/DELETE_LEAGUE";
const RESET_LEAGUE = "league/RESET_LEAGUE";

// ACTION

// GET
export const actionGetLeagues = (leagues) => ({
    type: GET_LEAGUES,
    leagues
})

// CREATE
export const actionAddLeague = (league) => ({
	type: ADD_LEAGUE,
	league,
});

// EDIT
export const actionEditLeague = (leagueId, league) => ({
	type: EDIT_LEAGUE,
    leagueId,
	league,
});

// DELETE
export const actionDeleteLeague= (leagueId) => ({
	type: DELETE_LEAGUE,
	leagueId,
});

// RESET
export const actionResetLeague = () => ({
	type: RESET_LEAGUE,
});


// Thunks

// GET
export const thunkGetLeagues = () => async (dispatch) => {
    const res = await fetch('/api/leagues/public');
    if (res.ok) {
        const leagues = await res.json();
        dispatch(actionGetLeagues(leagues.leagues))
        return leagues.leagues;
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
export const thunkAddLeague = (newLeague, tournaments) => async(dispatch) => {
	const {name, display_pic, team_budget, is_private} = newLeague
	const res = await fetch('/api/leagues/new', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(name, display_pic, team_budget, is_private, tournaments),
    });

    if (res.ok) {
        const data = await res.json();
        dispatch(actionAddLeague(data.league));
        return data.league;
    } else if (res.status < 500) {
        const data = await res.json();
        if (data.errors) {
            return data.errors;
        }
    } else {
        return ["An error occurred. Please try again."];
    }
}

//EDIT
export const thunkEditLeague = (leagueId, league) => async (dispatch) => {
    const res = await fetch(`/api/leagues/${leagueId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(league),
    })

    if (res.ok) {
        const data = await res.json();
        dispatch(actionEditLeague(data.league));
        return data.league;
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
export const thunkDeleteLeague = (leagueId) => async (dispatch) => {
    const res = await fetch (`/api/leagues/${leagueId}`, {
        method: "DELETE",
    });
    if (res.ok) {
		const data = await res.json();
		dispatch(actionDeleteLeague(leagueId));
		return data.league;
	} else if (res.status < 500) {
		const data = await res.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occured. Please try again."];
	}
}

const normalize = (leagues) => {
	const data = {};
	if (leagues) {
		leagues.forEach((league) => (data[league.id] = league));
		return data;
	}
};

const initialState = {leagues: {}}

export default function reducer(state = initialState, action) {
	switch (action.type) {
		case GET_LEAGUES: {
			let newState = { ...state };
			newState = normalize(action.leagues);
			return newState;
		}
		case ADD_LEAGUE: {
			let newState = { ...state };
			newState = {
				...state.leagues,
				[action.league.id]: action.league,
			};
			return newState;
		}
		case EDIT_LEAGUE: {
			let newState = { ...state };
			newState[action.league.id] = action.league;
			return newState;
		}
		case DELETE_LEAGUE: {
			let newState = { ...state };
			delete newState[action.leagueId];
			return newState;
		}
		case RESET_LEAGUE: {
			return {};
		}
		default:
			return state;
	}
}
