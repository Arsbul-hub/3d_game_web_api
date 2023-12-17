import datetime
from threading import Thread
from app import server_manager


class BackgroundTask(Thread):
    def __init__(self):
        super().__init__(target=self.task)

    def task(self):
        while True:
            try:
                for player_name, timestamp in server_manager.server.last_packets_sent.items():
                    if (datetime.datetime.now() - timestamp).seconds > 5:
                        print("Kicked player sucsess!")
                        server_manager.server.disconnect_player(player_name)
            except:
                print("Error, while try to get players list")
            #print(server_manager.server.players)
            # for player in server_manager.server.players:
            #     if player.
