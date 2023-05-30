import json
import translateUtil
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)  # 实例化 server，把当前这个 python 文件当做一个服务，__name__ 代表当前这个 python 文件
CORS(app, supports_credentials=True)

@app.route('/translate', methods=['POST'])  # 'index' 是接口路径，如果 methods 不写，则默认 get 请求
def index():
    data = json.loads(request.get_data())
    raw_add = data.get('data')
    res = translateUtil.translate(raw_add)

    return res

app.run(host="0.0.0.0", port=9080, debug=True)
