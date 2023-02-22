const GET_LEAGUES = "server/GET_LEAGUES";
const ADD_LEAGUE = "server/ADD_LEAGUES";
const EDIT_LEAGUE = "server/EDIT_LEAGUE";
const DELETE_LEAGUE = "server/DELETE_LEAGUE";
const RESET_LEAGUE = "server/RESET_LEAGUE";

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
export const actionEditLeague = (league) => ({
	type: EDIT_LEAGUE,
	league,
});

// DELETE
export const actionDeleteServerMember = (leagueId) => ({
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
export const thunkAddLeague = (newLeague) => async(dispatch) => {
    
}
