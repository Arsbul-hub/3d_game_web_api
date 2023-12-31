from dataclasses import dataclass, asdict

item_types = {
    "cobblestone": "block",
    "boxes": "block",
    "gun": "gun",
    "axe": "tool"
}


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


class Player(Entity):
    inventory: list = []
    kills: int = 0

    def add_to_inventory(self, item_name, count=1):
        item = self.search_item(item_name)
        if item:
            item["count"] += count
        else:
            self.inventory.append({"name": item_name, "count": count, "type": item_types[item_name]})

    def remove_from_inventory(self, item_name):
        item = self.search_item(item_name)
        if item and item["count"] > 0:
            item["count"] -= 1

    def search_item(self, item_name):
        for item in self.inventory:
            if item["name"] == item_name:
                return item

    def to_dict(self):
        out = asdict(self)
        out["inventory"] = self.inventory
        return out
