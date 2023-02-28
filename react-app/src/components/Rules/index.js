import { useModal } from "../../context/Modal";
import "./Rules.css"

export default function Rules() {
  const { closeModal } = useModal();

  return (
    <div className="rules-outer-div">
        <div className="rules-inner-div">
            <h1 className="rules-title">Rules :</h1>
            <div className="rules-leagues-div">
                <h2 className="rules-leagues">Leagues</h2>
                <p>1. Managers can join leagues where they may create their squads and compete</p>
                <p>2. Managers can select players from past world cups, and gain points based on their players' historical performances</p>
                <p>3. Each League is unique, and determines which tournaments players may be selected from and the budget for making a team</p>
                <p>4. Managers may also create custom and private leagues</p>
            </div>
            <div className="rules-teams-div">
                <h2 className="rules-teams">Teams</h2>
                <p>1. Upon team seletion managers may guide their team through 7 matchdays, the same amount of games a team reaching the world cup final would have played</p>
                <p>2. The score for each matchday will be determined by the individual points gained by each player on the team</p>
                <p>3. Players gain points accoring to the specific matchday they played in. For example Messi 2022 will have his goal against Saudi Arabia counted in matchday 1, and have his two goals against France counted as part of his matchday 7 points</p>
                <p>4. Managers get unlimited transfers when first selecting their team. Then 2 free transfers for the next three matchdays, and 3 free transfers for the last three matchdays</p>
                <p>5. Managers may make more than 2 or 3 transfers as well. However, doing so will incur a 4 point penalty to their gameday score</p>
                <p>6. Teams may consist of 11 players. Must have 1 goal-keeper, 3-5 defenders, 3-5 midfielders, and 1-3 forwards</p>
            </div>
            <div className="rules-scoring-div">
                <h2 className="rules-scoring">Scoring</h2>
                <p>1. Players gain points differently depending on their positions</p>
                <p>2. All players get 2 points for making an appearance in a match, and 0 points for not playing on the given matchday</p>
                <p>3. All players get 3 points for an assist</p>
                <p>4. All players get 6 points when they get the Man of the Match award</p>
                <p>5. Goalkeepers and Defenders get 4 points for keeping a clean sheet, and 6 points for scoring a goal</p>
                <p>6. Midifelders get 5 points for a goal, and 1 point for keeping a clean sheet</p>
                <p>7. Forwards get 4 points for scoring a goal, and 0 points for keeping a clean sheet</p>
                <p>8. Players may be avoided assists for winning penalties that have been scored, or for a shot that lead directly to an own goal</p>
                <p>9. Man of the match and assist statistics are harder to procure reliably the further back in time we go</p>
                <p className="exception">* More players will continue to be added to the game. Gathering individual gameday stats is a time inducive, and error-prone process</p>
            </div>
        </div>
    </div>
  )
}
