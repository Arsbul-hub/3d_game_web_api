import datetime
from threading import Thread
from app import server_manager


class BackgroundTask(Thread):
    def __init__(self):
        super().__init__(target=self.task)

    def task(self):
        while True:

            for player_name in list(server_manager.server.last_packets_sent):
                timestamp = server_manager.server.last_packets_sent[player_name]
                if (datetime.datetime.now() - timestamp).seconds > 5:
                    server_manager.server.disconnect_player(player_name)
            #print(server_manager.server.players)
            # for player in server_manager.server.players:
            #     if player.
