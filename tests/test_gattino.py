import pytest
from gattino import Gattino
import time


@pytest.mark.parametrize(("appid", "appid_expect"), [(None, not None), ("123", "123")])
@pytest.mark.parametrize(("conf", "conf_expect", "conf_name_expect"), [(None, "app.conf", "test_gattino"), ("tests/test.conf", "tests/test.conf", "test_a")])
@pytest.mark.parametrize(("argv", "argv_expect"), [("a", "a"), (["b", "c"], ["b", "c"]), ({"d": "e", "f": "g"}, {"d": "e", "f": "g"})])
def test_gattino_init(appid, appid_expect, conf, conf_expect, conf_name_expect, argv, argv_expect):
    app = Gattino(appid, conf, argv)
    if appid:
        assert app.appid == appid_expect
    else:
        print(app.appid)
        assert app.appid != None
    assert app.conf_file == conf_expect
    assert app.argv == argv_expect
    app.load_conf()
    assert app.conf["name"] == conf_name_expect

# @pytest.mark.current


@pytest.mark.parametrize(("args", "args_key_expect", "args_value_expect"), [({"key0": "value0"}, "key0", "value0"), ({"key0": "value0", "key1": "value1"}, "key1", "value1")])
@pytest.mark.parametrize(("kwargs", "kwargs_key_expect", "kwargs_value_expect"), [({"name": "abc"}, "name", "abc"), ])
def test_gattino_app_init(args, args_key_expect, args_value_expect, kwargs, kwargs_key_expect, kwargs_value_expect):
    app = Gattino()
    isruned = False

    @app.init(args, **kwargs)
    def add_conf():
        return True
    print(app.conf)
    isruned = add_conf()
    assert isruned
    assert app.conf[args_key_expect] == args_value_expect
    assert app.conf[kwargs_key_expect] == kwargs_value_expect


@pytest.mark.parametrize("delta_time", [1, 2, 5])
@pytest.mark.parametrize("at_once", [True, False])
def test_gattino_app_run(delta_time, at_once):
    app = Gattino()

    @ app.run(delta_time, at_once)
    def add_run():
        t2 = time.time()
        app.stop()
        if at_once:
            assert t2-t1 < 1
        else:
            assert t2-t1 > delta_time
    t1 = time.time()
    app.start()
    pass
