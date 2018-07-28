[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badge/) [![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)  



```
  _____                                  _____                    _ 
 |  __ \                                |  __ \                  | |
 | |__) |  _ __    ___   __  __  _   _  | |__) |   ___     ___   | |
 |  ___/  | '__|  / _ \  \ \/ / | | | | |  ___/   / _ \   / _ \  | |
 | |      | |    | (_) |  >  <  | |_| | | |      | (_) | | (_) | | |
 |_|      |_|     \___/  /_/\_\  \__, | |_|       \___/   \___/  |_|
                                  __/ |                             
                                 |___/                                               
```

# ProxyPool
##  IP池特性

- [x] **可多线程**
- [x] **可自定义**
- [x] **可扩展性**
- [x] **定时检测**
- [x] **简易接口**
![-w924](media/15323356040648/15323410191189.jpg)
代理池分为4个模块：存储模块、获取模块、检测模块、接口模块。
* 存储模块使用Redis的有序集合，用来做代理的去重标识，同时他也是中心模块和基础模块，将其他模块串联起来。
* 获取模块定时从代理网站获取代理，将获取的代理传递给存储模块，并保存数据库。
* 检测模块定时通过存储模块获取所有代理，并对代理进行检测，根据不同的检测结果对代理设置不同的标志。
* 接口模块通过Web API提供服务接口，接口通过连接数据库并通过Web形式返回可用代理。


##项目结构
```file
├── LICENSE
├── README.md
├── examples
│   ├── example.py
│   └── proxytest.py
├── importer.py
├── proxy\ provider.txt
├── proxypool
│   ├── __init__.py
│   ├── api.py
│   ├── crawler.py
│   ├── db.py
│   ├── error.py
│   ├── getter.py
│   ├── importer.py
│   ├── scheduler.py
│   ├── setting.py
│   ├── tester.py
│   └── utils.py
├── requirements.txt
└── run.py
```
## 安装

### 安装Python

至少Python3.5以上

### 安装Redis

安装好之后将Redis服务开启

### 配置代理池

```
cd proxypool
```

进入`proxypool`目录，修改`settings.py`文件

PASSWORD为Redis密码，如果为空，则设置为None

#### 安装依赖

```
pip3 install -r requirements.txt
```

#### 打开代理池和API

```
python3 run.py
```

## 获取代理


利用requests获取方法如下

```python
import requests

PROXY_POOL_URL = 'http://localhost:5555/random'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
```
