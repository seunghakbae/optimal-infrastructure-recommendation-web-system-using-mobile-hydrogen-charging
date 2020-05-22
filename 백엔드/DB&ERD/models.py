# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class ChargingStation(db.Model):
    __tablename__ = 'charging_station'

    Cs_id = db.Column(db.Integer, primary_key=True)
    cs_name = db.Column(db.Text)
    x_cor = db.Column(db.Float)
    y_cor = db.Column(db.Float)
    DONG_ID = db.Column(db.ForeignKey('dong.DONG_ID'))

    dong = db.relationship('Dong', primaryjoin='ChargingStation.DONG_ID == Dong.DONG_ID', backref='charging_stations')


class Dong(db.Model):
    __tablename__ = 'dong'

    DONG_ID = db.Column(db.Integer, primary_key=True)
    gu_name = db.Column(db.Text)
    name = db.Column(db.Text)
    code = db.Column(db.Float)
    _2020_rate = db.Column('2020_rate', db.Integer)
    _2022_rate = db.Column('2022_rate', db.Integer)
    _2024_rate = db.Column('2024_rate', db.Integer)
    _2026_rate = db.Column('2026_rate', db.Integer)
    _2028_rate = db.Column('2028_rate', db.Integer)


class Lpg(db.Model):
    __tablename__ = 'lpg'

    lpg_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    x_cor = db.Column(db.Float)
    y_cor = db.Column(db.Float)
    installed_2020 = db.Column(db.Integer)
    installed_2022 = db.Column(db.Integer)
    installed_2024 = db.Column(db.Integer)
    installed_2026 = db.Column(db.Integer)
    installed_2028 = db.Column(db.Integer)
    DONG_ID = db.Column(db.ForeignKey('dong.DONG_ID'))

    dong = db.relationship('Dong', primaryjoin='Lpg.DONG_ID == Dong.DONG_ID', backref='lpgs')


class ParkingLot(db.Model):
    __tablename__ = 'parking_lot'

    pl_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    x_cor = db.Column(db.Float)
    y_cor = db.Column(db.Float)
    installed_2020 = db.Column(db.Integer)
    installed_2022 = db.Column(db.Integer)
    installed_2024 = db.Column(db.Integer)
    installed_2026 = db.Column(db.Integer)
    installed_2028 = db.Column(db.Integer)
    DONG_ID = db.Column(db.Integer)


class Route(db.Model):
    __tablename__ = 'route'

    node1 = db.Column(db.Text)
    node2 = db.Column(db.Text)
    node3 = db.Column(db.Text)
    node4 = db.Column(db.Text)
    origin = db.Column(db.Text)
    _2022 = db.Column('2022', db.Integer)
    _2024 = db.Column('2024', db.Integer)
    _2026 = db.Column('2026', db.Integer)
    _2028 = db.Column('2028', db.Integer)
    lpg_id = db.Column(db.ForeignKey('lpg.lpg_id'))
    node1_id = db.Column(db.Integer)
    node2_id = db.Column(db.Integer)
    node3_id = db.Column(db.Integer)
    node4_id = db.Column(db.ForeignKey('parking_lot.pl_id'))
    origin_coor = db.Column(db.Text)
    node1_coor = db.Column(db.Text)
    node2_coor = db.Column(db.Text)
    node3_coor = db.Column(db.Text)
    node4_coor = db.Column(db.Text)
    route_id = db.Column(db.Integer, primary_key=True)

    lpg = db.relationship('Lpg', primaryjoin='Route.lpg_id == Lpg.lpg_id', backref='routes')
    node41 = db.relationship('ParkingLot', primaryjoin='Route.node4_id == ParkingLot.pl_id', backref='routes')
