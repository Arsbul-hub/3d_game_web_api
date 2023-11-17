from dataclasses import dataclass


@dataclass
class Entity:
    name: str
    pos: tuple = (0, 0, 0)
    hpr: tuple = (0, 0, 0)
    health: int = 100
    max_health: int = 100

    def reduce_health(self, value):
        if self.health - value >= 0:
            self.health -= value
        else:
            self.health = 0

    def restore_health(self, value):
        if self.health + value <= self.max_health:
            self.health += value
        else:
            self.health = self.max_health

    def kill(self):
        self.health = 0

    def to_dict(self):
        return {"username": self.name, "pos": self.pos, "hpr": self.hpr, "health": self.health}


# class Player(Entity):
#     kills: list
#
#     def __init__(self, username):
#         self.username = username
#
#     def to_dict(self):
#         return {"username": self.username, "pos": self.pos, "health": self.health, "kills": self.kills}
