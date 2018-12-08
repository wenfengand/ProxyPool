from flask import Flask, g

import sys 
import os.path
pwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pwd) 

from proxypool.db import RedisClient 
from flask import request 
from proxypool.setting import * 
import json  
from functools import wraps
__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis 

def token_required(tokens,type='json'):
    def second(func):
        @wraps(func)
        def mywrapper(*arg, **kw): 
            token = request.args.get("token") 
            if token in tokens:
                return func(*arg, **kw) 
            else:
                if type=='json':
                    return "{'msg':'Invalid token!'}" 
                else:
                    return 'Invalid token!'
        return mywrapper
    return second

@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random') 
@token_required(API_TOKEN,'txt') 
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random() 
@app.route('/v1/proxy')
@token_required(API_TOKEN,'json')
def get_proxy_v1():
    num = request.args.get('num') 
    conn = get_conn() 
    return conn.random() 

@app.route('/count')
@token_required(API_TOKEN,'txt') 
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())
@app.route('/v1/count')
@token_required(API_TOKEN,'json') 
def get_counts_v1():
    conn = get_conn() 
    ret_dict = {}
    ret_dict['msg'] = 'ok'
    ret_dict['count'] = conn.count()  
    return json.dumps(ret_dict) 

if __name__ == '__main__':
    app.run()
