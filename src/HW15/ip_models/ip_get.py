from base_model import BaseModel
import sqlalchemy as sa


class UserLocation(BaseModel):
    __tablename__ = 'ip_adress'

    ip = sa.Column(sa.String(100), nullable=False)
