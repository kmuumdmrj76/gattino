from gattino import ExtBase
from gattino import Gattino
from gattino import GattinoEvent
import pytest

def test_ext(gattino_app):

    class Gattino_T(ExtBase):
        is_start = False
        is_run = False
        is_stop = False

        def __init__(self, app: Gattino):
            super(Gattino_T, self).__init__(app)
            self.bind_event(GattinoEvent.EVENT_START, self.start)
            self.bind_event(GattinoEvent.EVENT_TICK, self.running)
            self.bind_event(GattinoEvent.EVENT_EXIT, self.stop)

        def load_conf(self):
            conf_dic = {}
            return conf_dic

        def start(self, params):
            print("start")
            self.is_start = True

        def running(self, ts):
            self.is_run = True

        def stop(self, params):
            self.is_stop = True
    app = gattino_app
    app_t = Gattino_T(app)

    @app.run(1)
    def add_run():
        app.stop()
        pass
    app.start()
    assert app_t.is_start == True
    assert app_t.is_run == True
    assert app_t.is_stop == True