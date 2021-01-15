from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Numeric

from etl_api_assignment.config import db_details

user_name = db_details['user_name']
password = db_details['password']
server = db_details['server']
backend = db_details['backend']

MSSQL_URL = f"""mssql+pyodbc://{user_name}:{password}@{server}/{backend}"""

engine = create_engine(MSSQL_URL + "?driver=SQL+Server+Native+Client+11.0")
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Model = declarative_base(name='Model')
Model.query = db_session.query_property()
metadata = MetaData(Model.metadata)

class location(Model):
    __tablename__ = 'location'
    sr_no = Column(Integer)
    id = Column(Integer,primary_key=True)
    wgs84_polygon = Column(String)

    @staticmethod
    def get_loc(id):
        """Queries location table """
        loc_data = db_session.query(location.id, location.wgs84_polygon).filter_by(id=id).all()
        results = []

        if not loc_data:
            results = {"No Data Available for location"}
        else:
            res = []
            for id,wgs84_polygon in loc_data:
                res.append({"loc_id": id, "wgs84_polygon": wgs84_polygon})
                results = {"location_data": res}
        return results