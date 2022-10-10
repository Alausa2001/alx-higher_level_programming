#!/usr/bin/python3
"""
script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa

Your script should take 4 arguments: mysql username, mysql password, i
database name and state name to search (SQL injection free)
You must use the module SQLAlchemy
You must import State and Base from model_state
Your script should connect to a MySQL server running on localhost at port 3306
You can assume you have one record with the state name to search
Results must display the states.id
If no state has the name you searched for, display Not found
Your code should not be executed when imported
"""


def my_get():
    """ searches for a state"""

    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import Session, sessionmaker
    from sys import argv
    db = argv[3]
    user = argv[1]
    passwd = argv[2]
    search = argv[4]

    if search.__contains__('TRUNCATE' or 'FROM' or 'SELECT' or '*'):
        search = ''

    # create connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, db))
    # cretae tables in the metadate
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    state = session.query(State).filter_by(name=search).first()
    if state is not None:
        print('{}'.format(state.id))
    else:
        print('Not found')
    session.close()


if __name__ == '__main__':
    my_get()
