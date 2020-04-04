#coding=utf-8
from flask import Flask, render_template, request, jsonify
import Random_sampling
import get_history_num

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        pass

@app.route('/admin369369',methods=['GET','POST'])
def admin():
    if request.method == 'GET':
        return render_template('admin369369.html')
    else:
        pass

@app.route('/get_num',methods=['GET'])
def get_num():
    list = Random_sampling.random_sampling()
    list_num = []
    list_num.append(list)
    return jsonify(res = list_num)

@app.route('/clean_data',methods=['GET'])
def clean_data():
    information = '清理完毕，现有：' + str(get_history_num.get_history_data()) + '注未开'
    list_num = []
    list_num.append(information)
    return jsonify(res = list_num)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)