
from app import app, api
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

    #app.register_blueprint(api.blueprint)
    app.run(host="0.0.0.0", port=2000, debug=False)
