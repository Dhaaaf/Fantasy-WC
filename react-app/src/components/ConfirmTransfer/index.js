import { thunkNextMatchDay, thunkGetTeam } from "../../store/team";
import { useModal } from "../../context/Modal";
import { useDispatch} from "react-redux";
import "./ConfirmTransfer.css"

export default function ConfirmTransfers({teamId, teamPlayersIds, transfersLeft, bank}) {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    console.log("IN MODAL ----->", teamId, teamPlayersIds, transfersLeft, bank)




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

    return (
        <div className="confirm-transfers-div">
            <div className="title">
                <div className="form-title-confirm-transfers">Confirm transfers and calculate points?</div>
            </div>
            <div className="yes-no-div">
                <div className="form-button">
                    <button onClick={() => closeModal()} type="submit" className="confirm-transfers-button no">Cancel</button>
                </div>
                <div className="form-button">
                    <button onClick={() => nextMatchDay()} type="submit" className="confirm-transfers-button yes">Yes</button>
                </div>
            </div>
        </div>
        )

}
