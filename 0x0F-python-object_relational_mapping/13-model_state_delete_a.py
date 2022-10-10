#!/usr/bin/python3
"""
script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password
and database name
You must use the module SQLAlchemy
You must import State and Base from model_state
Your script should connect to a MySQL server running on localhost at port 3306
Your code should not be executed when imported
"""


def delete():
    """ deletes state that contain letter 'a'"""

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
    search = State.name.like('%a%')
    states = session.query(State).filter(search).order_by(State.id).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == '__main__':
    delete()
