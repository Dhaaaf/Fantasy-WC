import { thunkNextMatchDay, thunkGetTeam } from "../../store/team";
import { useModal } from "../../context/Modal";
import { useDispatch} from "react-redux";
import "./ConfirmTransfers.css"

export default function ConfirmTransfers({teamId, teamPlayersIds, transfersLeft, bank}) {
    const dispatch = useDispatch();
    const { closeModal } = useModal();




    const nextMatchDay = async () => {
        // console.log("nextMatchDay stuff ----->", teamPlayersArray)
        // console.log("nextMatchDay stuff ----->", teamPlayersIds)
        // console.log("Transfers Left ---->", transfersLeft)

        let payload = {
            teamId,
            teamPlayersIds,
            transfersLeft,
            bank
        }

        dispatch(thunkNextMatchDay(payload)).
        then(() => dispatch(thunkGetTeam(teamId))).
        then(() => closeModal())
    }



}
