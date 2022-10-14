#!/usr/bin/python3
"""creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa"""

from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def relationship():
    """creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa"""

    # create connection
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                           argv[1], argv[2], argv[3]))
    # create Tables
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # new object
    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)
    # save
    session.add(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    relationship()
