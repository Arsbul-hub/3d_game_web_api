import dataclasses
import json
from dataclasses import dataclass

from panda3d.core import Vec3

blocks = {
    "cobblestone": {"texture": "cobblestone", "breakable": True},
    "bedrock": {"texture": "bedrock", "breakable": False}
}


def generate_default():
    sx, sy, sz = 30, 30, 2
    out = []
    for z in range(sz):
        for y in range(sy):
            for x in range(sx):
                if z == 0:
                    block = {"type": "bedrock", "pos": [x, y, z]}
                else:
                    block = {"type": "cobblestone", "pos": [x, y, z]}
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

    def set_block(self, block_type, pos):
        if block_type in blocks:
            self.world.insert(0, {"type": block_type, "pos": pos})

    def remove_block(self, pos):
        x, y, z = pos
        for block in self.world:
            if Vec3(x, y, z) == pos and blocks[block["type"]]["breakable"]:
                self.world.remove(block)
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
        return {"entities": {e.name: dataclasses.asdict(e) for e in self.entities}, "world": self.world}
