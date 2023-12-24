#!/usr/bin/env python3
"""
    Defines a module with a DBStorage class which implements a mysql
    database storage engine
"""
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """implements a database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a DBStorage class"""
        # get environment variables
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        # create engine to conect to database
        engn = "mysql+mysqldb://{}:{}@{}/{}".format(user, passwd, host, db)
        self.__engine = create_engine(engn, pool_pre_ping=True)

        # drop tables if HBNB_ENV is equal to test
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if cls:
            objects = self.__session.query(cls).all()
            return {f"{cls.__name__}.{obj.id}": obj.to_dict()
                    for obj in objects}

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """saves changes of the current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.user import User
        from models.place import Place

        Base.metadata.create_all(self.__engine)  # Create tables

        # create session to interact with database
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
