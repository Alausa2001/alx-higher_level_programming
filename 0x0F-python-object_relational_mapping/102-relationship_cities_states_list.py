#!/usr/bin/python3
"""many to one relationship"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import State, Base
from relationship_city import City


def relationship():
    """many to one relationship"""

    # create connection
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))
    # create Tables
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    rows = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for city, state in rows:
        print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()


if __name__ == "__main__":
    relationship()
