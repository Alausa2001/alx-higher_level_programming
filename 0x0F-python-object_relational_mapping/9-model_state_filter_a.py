#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username, mysql password and db name
You must use the module SQLAlchemy
You must import State and Base from model_state
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
our code should not be executed when imported
"""


def state_filter():
    """ script that prints the first State object
    from the database hbtn_0e_6_usa"""

    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import Session, sessionmaker
    from sys import argv
    db = argv[3]
    user = argv[1]
    passwd = argv[2]

    # create connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db))
    # cretae tables in the metadate
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    for state in session.query(State).order_by(State.id).all():
        if 'a' in state.name:
            print('{}: {}'.format(state.id, state.name))
    session.close()


if __name__ == '__main__':
    state_filter()
