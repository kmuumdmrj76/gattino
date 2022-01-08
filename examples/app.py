
from gattino import Gattino, GattinoEvent, ExtBase
import sys
import time

app = Gattino(argv=sys.argv)


@app.init({"key4": "value4", "key5": "value5"}, key0="value0",)
def app_conf(*args, **kwargs):
    args_conf = {}
    [args_conf.update(arg) for arg in args]
    print(
        f"配置函数:[{app_conf.__name__}]加载[{len(args_conf.items())}]项配置信息")
    app.conf.update(args_conf)
    print(
        f"配置函数:[{app_conf.__name__}-KV]加载[{len(kwargs.items())}]项配置信息")
    app.conf.update(kwargs)
    print(app.conf)
    return 10


@app.run(10, at_once=True)
def run_10s():
    print("10s:", time.time())


@app.run(6)
def run_6s():
    print("6s:", time.time())

# @app.run()
# def run_6s():
#     print("6s:",time.time())


if __name__ == '__main__':
    print(app_conf({"name": "AppNames"}, key1="testkey",
                   key2="value2", key3="value3"))
    # 项目启动
    app.start()
