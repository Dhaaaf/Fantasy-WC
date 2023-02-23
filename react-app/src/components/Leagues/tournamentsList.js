import "./LeagueIndex.css"

function TournamentsList({tournaments, name}) {

    let tournamentNames = tournaments.map(tournament => (
        tournament.tournament_name
    ))

    tournamentNames.sort(function(a, b) {
        if (a > b) {
          return -1;
        }
        if (b > a) {
          return 1;
        }
        return 0;
      });

    return (
        <div className="tournaments-list">
          <div className="tournament-name-modal">{name}</div>
            {tournamentNames.map(tournament => (
                <div key={tournament.id} className="tournament-name">{tournament}</div>
            ))}
        </div>
    )
}

export default TournamentsList
