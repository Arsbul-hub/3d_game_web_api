import datetime
from dataclasses import dataclass
import json
import os
import random

from app.entities import Player

from app.world_manager import World


@dataclass()
class Server:
    name: str
    invite_code: str
    players = []
    last_packets_sent = {}
    world: World = World()

    def __init__(self, world=None, name="Star", invite_code=None):
        if world:
            self.world = world
        self.invite_code = str(random.randint(0, 100))

        if name:
            self.name = name
        if invite_code:
            self.invite_code = invite_code

    def connect_player(self, name):
        entity = Player(name=name, scale=(.5, .5, 2))
        self.players.append(entity)

        self.world.entities.append(entity)
        return entity

    def disconnect_player(self, name):

        self.remove_player(name)
        self.world.remove_entity(name)
        # try:
        self.last_packets_sent.pop(name)

    def remove_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)

    def search_player(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def update_player(self, name, pos=None, hpr=None, health=None):
        for player in self.players:
            if player.name == name:
                if pos is not None:
                    player.pos = pos
                if hpr is not None:
                    player.hpr = hpr
                if health is not None:
                    player.health = health
                self.last_packets_sent[name] = datetime.datetime.now()
                break
        self.update_entity(name, pos, hpr, health)

    def update_entity(self, name, pos=None, hpr=None, health=None):
        for entity in self.world.entities:
            if entity.name == name:
                if pos is not None:
                    entity.pos = pos
                if hpr is not None:
                    entity.hpr = hpr
                if health is not None:
                    entity.health = health
                self.last_packets_sent[name] = datetime.datetime.now()
                break


class ServerManager:
    server = Server()

    def __init__(self):
        if os.path.exists("./servers.json"):
            with open(f"./servers.json", "r") as file:
                server = json.load(file)

                world = server["world"]
                server_name = server["server_name"]
                # entities = []
                # for entity in world["entities"]:
                #     entities.append(Entity(**entity))

                self.server.world = World(world=world["world"])
                self.server.name = server_name

    def save_servers(self):
        with open(f"./servers.json", "w") as file:
            server = {
                "server_name": self.server.name,
                "world": self.server.world.to_dict()

            }
            json.dump(server, file)

        # print(self.servers)

        # pass
        # with open(f"servers.json", "w") as file:
        #     out = {}
        #
        #     for name, server in self.servers.items():
        #         out[name] = dataclasses.asdict(server)
        #     json.dump(out, file)

    # def from_dict(self, data):
    #     for
    # def to_dict(self):
    #     out = {}
    #
    #     for name, server in self.servers.items():
    #         out[name] = server.to_dict()
    #     return out
