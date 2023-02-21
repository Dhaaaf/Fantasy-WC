from flask.cli import AppGroup
from .users import seed_users, undo_users
from .tournaments import seed_tournaments, undo_tournaments
from .players import seed_players, undo_players
from .gameweekstats import seed_game_week_stats, undo_game_week_stats
from .leagues import seed_leagues, undo_leagues
from .leaguestournaments import seed_leagues_tournaments, undo_leagues_tournaments

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_leagues_tournaments()
        undo_leagues()
        undo_game_week_stats()
        undo_players()
        undo_tournaments()
        undo_users()
    seed_users()
    seed_tournaments()
    seed_players()
    seed_game_week_stats()
    seed_leagues()
    seed_leagues_tournaments()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_leagues_tournaments()
    undo_leagues()
    undo_game_week_stats
    undo_players()
    undo_tournaments()
    undo_users()
    # Add other undo functions here
