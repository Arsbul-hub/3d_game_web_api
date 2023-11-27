import dataclasses

from dataclasses import dataclass

from panda3d.core import Vec3

blocks = {
    "cobblestone": {"type": "cobblestone", "broke_index": 1, "breakable": 1},
    "boxes": {"type": "boxes", "broke_index": 0, "breakable": 1},
    "bedrock": {"type": "bedrock", "broke_index": 0, "breakable": 0}
}


def generate_default():
    sx, sy, sz = 30, 30, 2
    out = []
    for z in range(sz):
        for y in range(sy):
            for x in range(sx):
                if z == 0:
                    block = blocks["bedrock"].copy()
                    block["pos"] = [x, y, z]
                    block["broke"] = block["broke_index"]
                    #print(blocks["bedrock"], block)
                else:
                    block = blocks["cobblestone"].copy()
                    block["pos"] = [x, y, z]
                    block["broke"] = block["broke_index"]
                out.append(block)
    return out


@dataclass()
class World:
    world: list

    def __init__(self, entities=None, world=None):
        if entities is not None:
            self.entities = entities
        else:
            self.entities = []
        if world is None:
            # with open(f"app/static/worlds/default.json", "r") as world:
            #     self.world = json.load(world)
            self.world = generate_default()
        else:
            self.world = world

    def set_block(self, inventory_item_name, pos):
        if inventory_item_name in blocks:
            new_block = blocks[inventory_item_name].copy()
            new_block["broke"] = new_block["broke_index"]
            new_block["pos"] = pos
            self.world.insert(0, new_block)

    def remove_block(self, pos):
        x, y, z = pos
        for block in self.world:
            xs, ys, zs = block["pos"]
            if Vec3(pos) == Vec3(xs, ys, zs) and block["breakable"]:
                if block["broke"] > 0:
                    block["broke"] -= 1
                else:
                    self.world.remove(block)
                return block

    def search_block(self, pos):
        x, y, z = pos
        for block in self.world:
            xs, ys, zs = block["pos"]
            if Vec3(pos) == Vec3(xs, ys, zs):
                return block

    def search_entity(self, name):
        for entity in self.entities:
            if entity.name == name:
                return entity

    def remove_entity(self, name):
        for entity in self.entities:
            if entity.name == name:
                self.entities.remove(entity)

    def to_dict(self):
        return {"entities": {e.name: e.to_dict() for e in self.entities}, "world": self.world}
