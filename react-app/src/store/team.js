const GET_TEAM = "team/GET_TEAM";
const ADD_TEAM = "team/ADD_TEAM";
const ADD_PLAYER = "team/ADD_PLAYER";
const DELETE_PLAYER = "team/DELETE_PLAYER";
const DELETE_TEAM = "team/DELETE_TEAM"


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
