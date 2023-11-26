from dataclasses import dataclass, asdict


@dataclass
class Entity:
    name: str
    scale: tuple
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
        return {"username": self.name, "pos": self.pos, "scale": self.scale, "hpr": self.hpr, "health": self.health}


@dataclass
class Player(Entity):
    kills: int = 0
    inventory = []

    def add_to_inventory(self, item_type, count=1):
        item = self.search_item(item_type)
        if item:
            item["count"] += count
        else:
            self.inventory.append({"item_type": item_type, "count": count})

    def remove_from_inventory(self, item_type):
        item = self.search_item(item_type)
        if item and item["count"] > 0:
            item["count"] -= 1

    def search_item(self, item_type):
        for item in self.inventory:
            if item["item_type"] == item_type:
                return item

    def to_dict(self):
        out = asdict(self)
        out["inventory"] = self.inventory
        return out
