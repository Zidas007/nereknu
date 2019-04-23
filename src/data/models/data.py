from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime,Float

from ..database import db
from ..mixins import CRUDModel

class Data(CRUDModel):
    __tablename__ = 'data'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    typ = Column(String, nullable=False, index=True)#1=hovezi,2=vepr,3=kure
    cas= Column(DateTime, nullable=False, index=True)#1=predni,2=zadni
    hodnota = Column(Float, nullable=True,default=0)
    disk = Column(Integer, nullable=True, default=0)
    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    @staticmethod
    def poslednich10minut(typ):
        from datetime import datetime, timedelta
        now=datetime.now()
        now_minus_10=now - timedelta(minutes=10)
        data= db.session.query(Data).filter(Data.cas > now_minus_10).filter(Data.typ == typ).all()
        return data