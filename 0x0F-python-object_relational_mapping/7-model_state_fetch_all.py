#!/usr/bin/python3
"""
 script that lists all State objects from the database hbtn_0e_6_usa

 Your script should take 3 arguments: mysql username,
 mysql password and database name
 You must use the module SQLAlchemy
 You must import State and Base from model_state
 Your script should connect to a MySQL server running on
 localhost at port 3306

 Results must be sorted in ascending order by states.id
 The results must be displayed as they are in the example below
 Your code should not be executed when imported
 """


def fetch_all():
    """lists all State objects from the database hbtn_0e_6_usa"""
    from sqlalchemy.orm import Session, sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv

    passwd = argv[2]
    user = argv[1]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db))  # creating a connection

    # Create all tables stored in this metadata.
    Base.metadata.create_all(engine)

    # creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    for state in session.query(State).order_by(State.id).all():
        print('{}: {}'. format(state.id, state.name))
    session.close()


if __name__ == '__main__':
    fetch_all()
