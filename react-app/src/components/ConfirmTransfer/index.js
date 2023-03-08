import { thunkNextMatchDay, thunkGetTeam } from "../../store/team";
import { useState } from "react";
import { useModal } from "../../context/Modal";
import { useDispatch} from "react-redux";
import "./ConfirmTransfer.css"

export default function ConfirmTransfers({teamId, teamPlayersIds, transfersLeft, bank}) {
    const dispatch = useDispatch();
    const { closeModal } = useModal();
    const [isActive, setIsActive] = useState(true)




    const nextMatchDay = async () => {

        if (isActive) {
            let payload = {
                teamId,
                teamPlayersIds,
                transfersLeft,
                bank
            }

            setIsActive(false)
            
            
            dispatch(thunkNextMatchDay(payload)).
            then(() => dispatch(thunkGetTeam(teamId)))
            closeModal()
            
        }

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
