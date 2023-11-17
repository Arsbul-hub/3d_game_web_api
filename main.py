import time
from threading import Thread
#
from app import application, blueprint, api
from app.server_tasks import BackgroundTask
# def f():
#     while True:
#         pass
#         #print(123)
#         #time.sleep(1/ 20)
# Thread(target=f).start()
BackgroundTask().start()
if __name__ == '__main__':
    # db_session.global_init("application.db")

    application.register_blueprint(api.blueprint)
    application.run(host='0.0.0.0', port=2000, debug=False)
