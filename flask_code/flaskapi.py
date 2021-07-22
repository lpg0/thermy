from flask import Flask, json

current_temp = [{"current-temp":"70"}]

api = Flask(__name__)

@api.route('/ThermsAreUs/api/v1.0/current-temp', methods=['GET'])
def get_current_temperature():
    return json.dumps(current_temp)

@api.route('/ThermsAreUs/api/v1.0/current-setpoint', methods=['GET'])
def get_current_setpoint():
    file0 = open("current_setpoint.txt", "r")
    current_setpoint = [{"current-setpoint":file0.read()}]
    file0.close()
    return json.dumps(current_setpoint)

@api.route('/ThermsAreUs/api/v1.0/current-setpoint', methods=['POST'])
def post_setpoint():
    file0 = open("current_setpoint.txt", "r+")
    num = int(file0.read())
    num = num + 3
    str_num = str(num)
    file0.close()
    file0 = open("current_setpoint.txt", "w")
    file0.write(str_num)
    file0.close()
    current_setpoint = [{"current-setpoint":str_num}]
    return json.dumps(current_setpoint)

if __name__ == '__main__':
    api.run(host='0.0.0.0')
