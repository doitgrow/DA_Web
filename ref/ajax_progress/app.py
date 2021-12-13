from flask import Flask, render_template, request, jsonify
import time
import pandas as pd

import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('POST 요청 수신')
        data = request.get_json()
        print(data)
        print(data['username'])
        db = pd.read_excel('./db.xlsx')
        db_jsons = db.to_dict('records')      
        # return json.dumps(db_jsons, ensure_ascii=False)
        # time.sleep(2)
        print(type(db_jsons))
        return data
        # return "<p>" + str(db_jsons[0].get('id')) + "</p>" + "<p>" + db_jsons[0].get('이름') + "</p>"
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)