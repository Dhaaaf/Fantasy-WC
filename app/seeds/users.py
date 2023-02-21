from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    sir_alex = User(
        username='SirAlex', email='demo@aa.io', password='password')
    pep = User(
        username='Pep Guardiola', email='pep@aa.io', password='password')
    scaloni = User(
        username='Scaloni', email='scaloni@aa.io', password='password')

    db.session.add(sir_alex)
    db.session.add(pep)
    db.session.add(scaloni)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")
        
    db.session.commit()
