#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""


def city_fetch_by_state():
    """prints all City object in the database passed as arg"""
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    from sys import argv

    # create a connection
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # create all tables
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    rows = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    city_fetch_by_state()
