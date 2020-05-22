from flask import Flask, render_template, send_file, Markup, url_for
from models import Lpg, ChargingStation, Dong, ParkingLot
from models import db
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///real_Hydrogen.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/map')
def map():
    cg = ChargingStation.query.all()
    return render_template('map.html', station=cg)

@app.route('/map2')
def map2():
    lpg = Lpg.query.filter_by(installed_2022=1)
    parking = ParkingLot.query.filter_by(installed_2022=1)
    return render_template('map2.html', result=lpg, result2=parking)

@app.route('/map4')
def map4():
    lpg = Lpg.query.filter_by(installed_2024=1)
    parking = ParkingLot.query.filter_by(installed_2024=1)
    return render_template('map4.html', result=lpg, result2=parking)

@app.route('/map6')
def map6():
    lpg = Lpg.query.filter_by(installed_2026=1)
    parking = ParkingLot.query.filter_by(installed_2026=1)
    return render_template('map6.html', result=lpg, result2=parking)

@app.route('/map8')
def map8():
    lpg = Lpg.query.filter_by(installed_2028=1)
    parking = ParkingLot.query.filter_by(installed_2028=1)
    return render_template('map8.html', result=lpg, result2=parking)


@app.route('/line22')
def line22():
    #### 저장된 정보를 불러 오는 코드 ####
    with open("./2022/route_name_2022.txt", "r", encoding='utf-8') as f:
        route_name_2022 = f.read()
    with open("./2022/route_coor_2022.txt", "r", encoding='utf-8') as f:
        route_coor_2022 = f.read()

    # 경로16 solution.txt 불러오기
    with open("./2022/solution_22.txt", "r", encoding='utf-8') as f:
        route = f.read()

    # dong : 동 경계 표시 + 색칠
    with open("./2022/dong.txt", "r", encoding='utf-8') as f:
        dong = f.read()

    return render_template("2022.html", route_name_2022=route_name_2022, route_coor_2022=route_coor_2022,
                           optRoute=route, dong=dong)

@app.route('/line24')
def line24():
    #### 저장된 정보를 불러 오는 코드 ####
    with open("./2024/route_name_2024.txt", "r", encoding='utf-8') as f:
        route_name_2024 = f.read()
    with open("./2024/route_coor_2024.txt", "r", encoding='utf-8') as f:
        route_coor_2024 = f.read()

    # 경로16 solution.txt 불러오기
    with open("./2024/solution_24.txt", "r", encoding='utf-8') as f:
        route = f.read()

    # dong : 동 경계 표시 + 색칠
    with open("./2024/dong.txt", "r", encoding='utf-8') as f:
        dong = f.read()

    return render_template("2024.html", route_name_2024=route_name_2024, route_coor_2024=route_coor_2024,
                           optRoute=route, dong=dong)
@app.route('/line26')
def line26():
    #### 저장된 정보를 불러 오는 코드 ####
    with open("./2026/route_name_2026.txt", "r", encoding='utf-8') as f:
        route_name_2026 = f.read()
    with open("./2026/route_coor_2026.txt", "r", encoding='utf-8') as f:
        route_coor_2026 = f.read()

    # 경로16 solution.txt 불러오기
    with open("./2026/solution_26.txt", "r", encoding='utf-8') as f:
        route = f.read()

    # dong : 동 경계 표시 + 색칠
    with open("./2026/dong.txt", "r", encoding='utf-8') as f:
        dong = f.read()

    return render_template("2026.html", route_name_2026=route_name_2026, route_coor_2026=route_coor_2026,
                           optRoute=route, dong=dong)

@app.route('/line28')
def line28():
    #### 저장된 정보를 불러 오는 코드 ####
    with open("./2028/route_name_2028.txt", "r", encoding='utf-8') as f:
        route_name_2028 = f.read()
    with open("./2028/route_coor_2028.txt", "r", encoding='utf-8') as f:
        route_coor_2028 = f.read()

    # 경로16 solution.txt 불러오기
    with open("./2028/solution_28.txt", "r", encoding='utf-8') as f:
        route = f.read()

    # dong : 동 경계 표시 + 색칠
    with open("./2028/dong.txt", "r", encoding='utf-8') as f:
        dong = f.read()

    return render_template("2028.html", route_name_2028=route_name_2028, route_coor_2028=route_coor_2028,
                           optRoute=route, dong=dong)

@app.route('/cost22')
def cost22():
    return render_template('tables2.html')

@app.route('/cost24')
def cost24():
    return render_template('tables4.html')

@app.route('/cost26')
def cost26():
    return render_template('tables6.html')

@app.route('/cost28')
def cost28():
    return render_template('tables8.html')

# @app.route('/cost22')
# def cost():
#     return render_template('tables2.html')
@app.route('/analysis')
def gaeyo():
    return render_template('gaeyo.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/dash')
def dash():
    return render_template('dashboard.html')

@app.route('/a')
def index1():
    return render_template('/variable/edu_percent.html')

@app.route('/b')
def index2():
    return render_template('/variable/apart_mean_price.html')

@app.route('/c')
def index3():
    return render_template('/variable/furniture_car_num.html')

@app.route('/d')
def index4():
    return render_template('/variable/dong_hycar_num.html')

@app.route('/e')
def index5():
    return render_template('/variable/dong_eco_carNum.html')

@app.route('/f')
def index6():
    return render_template('/variable/taxi.html')

@app.route('/g')
def index7():
    return render_template('/variable/total_company_num.html')

@app.route('/h')
def index8():
    return render_template('/output.html')

@app.route('/model')
def model():
    return render_template('modeling.html')

if __name__ == '__main__':
    app.run()
