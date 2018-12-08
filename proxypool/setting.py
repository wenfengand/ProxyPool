# Redis数据库地址
import os 
if 'REDIS_PORT_6379_TCP_ADDR' in os.environ:
    REDIS_HOST = os.environ['REDIS_PORT_6379_TCP_ADDR']
else:
    REDIS_HOST = '127.0.0.1'
if 'REDIS_PORT_6379_TCP_PORT' in os.environ:
    REDIS_PORT = os.environ['REDIS_PORT_6379_TCP_PORT']
else:    
# Redis端口
    REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'http://www.baidu.com'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 8001

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10
