#!/usr/bin/python3
"""one to many relationship"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import State, Base
from relationship_city import City


def relationship():
    """one to many relationship"""

    # create connection
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))
    # create Tables
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    rows = session.query(State).all()
    for state in rows:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()


if __name__ == "__main__":
    relationship()
