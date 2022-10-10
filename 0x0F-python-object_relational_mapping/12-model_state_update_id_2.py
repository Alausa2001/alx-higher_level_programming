#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and db name
You must use the module SQLAlchemy
You must import State and Base from model_state
Your script should connect to a MySQL server running on localhost at port 3306
Change the name of the State where id = 2 to New Mexico
Your code should not be executed when imported"
"""


def update():
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
    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()


if __name__ == '__main__':
    update()
