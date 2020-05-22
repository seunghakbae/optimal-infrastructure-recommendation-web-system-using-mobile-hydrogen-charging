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
    _2020_rate = db.Column('2020_rate', db.Float)
    _2022_rate = db.Column('2022_rate', db.Float)
    _2024_rate = db.Column('2024_rate', db.Float)
    _2026_rate = db.Column('2026_rate', db.Float)
    _2028_rate = db.Column('2028_rate', db.Float)


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
    DONG_ID = db.Column(db.ForeignKey('dong.DONG_ID'))

    dong = db.relationship('Dong', primaryjoin='ParkingLot.DONG_ID == Dong.DONG_ID', backref='parking_lots')
