
import random


from flask import request, jsonify

from app import blueprint, server_manager


#from app.models import Servers


#
# server_manager = ServerManager(db)

# @blueprint.route("/create_server", methods=["GET"])
# def create_server():
#     # server_manager.add("")
#
#     admin_username = request.args.get("admin_username")
#     server_name = request.args.get("name")
#     # server = Servers.query.filter_by(name=server_name).first()
#     # print(server_name)
#     if server_manager.servers.get(server_name):
#         return jsonify({"status": "error"})
#
#     invite_code = server_manager.add(server_name)
#     if not invite_code:
#         return jsonify({"status": "error"})
#     return jsonify({"status": "ok", "invite_code": invite_code})
#

@blueprint.route("/get_server", methods=["GET"])
def get_server():
    # code = request.args.get("code")

    server_name = request.args.get("name")
    print(server_name)
    # server = server_manager.get_server(server_name)
    #
    # if server.invite_code != code:
    #     return jsonify({"status": "error"})
    return jsonify({"status": "ok", "server": {"world": server_manager.server.world.to_dict(),
                                               "server_name": server_manager.server.name}})


@blueprint.route("/connect_user", methods=["POST"])
def connect_user():
    # code = request.args.get("code")

    server_name = request.args.get("name")
    player_name = request.args.get("player_name")

    # server = server_manager.get_server(server_name)
    #
    if server_manager.server.search_player(player_name):
        return jsonify({"status": "error"})
    server_manager.server.connect_player(player_name)
    # if server.invite_code != code:
    #     return jsonify({"status": "error"})
    return jsonify({"status": "ok"})


@blueprint.route("/update_user", methods=["GET"])
def update_user():
    # code = request.args.get("code")

    server_name = request.args.get("name")
    player_name = request.args.get("player_name")
    if server_manager.server.search_player(player_name).health == 0:
        return jsonify({"status": "no health"})
    x, y, z = float(request.args.get("x")), float(request.args.get("y")), float(request.args.get("z"))
    h, p, r = float(request.args.get("h")), float(request.args.get("p")), float(request.args.get("r"))
    if z < -20:
        server_manager.server.search_player(player_name).kill()
    server_manager.server.update_entity(player_name, [x, y, z], [h, p, r])

    # if server.invite_code != code:sa
    #     return jsonify({"status": "error"})
    return jsonify({"status": "ok"})


@blueprint.route("/respawn_user", methods=["GET"])
def respawn_user():
    # code = request.args.get("code")

    server_name = request.args.get("name")
    player_name = request.args.get("player_name")
    if server_manager.server.search_player(player_name).health > 0:
        return jsonify({"status": "error"})
    max_x = max(server_manager.server.world.world, key=lambda a: a["pos"][0])["pos"][0]
    max_y = max(server_manager.server.world.world, key=lambda a: a["pos"][1])["pos"][1]
    x, y, z = float(random.randint(0, max_x)), float(random.randint(0, max_y)), 10
    player = server_manager.server.search_player(player_name)
    server_manager.server.update_player(player_name, [x, y, z], health=player.max_health)

    # if server.invite_code != code:sa
    #     return jsonify({"status": "error"})
    return jsonify({"status": "ok", "x": x, "y": y, "z": z})


@blueprint.route("/hit_user", methods=["POST"])
def hit_user():
    # code = request.args.get("code")

    server_name = request.args.get("name")
    player_name = request.args.get("player_name")

    # for i in server.world.entities:
    #     if i.name == player_name:
    #         server.world.search_entity.reduce_health(20)
    server_manager.server.search_player(player_name).reduce_health(20)

    # if server.invite_code != code:
    #     return jsonify({"status": "error"})
    return jsonify({"status": "ok"})


@blueprint.route("/get_world", methods=["GET"])
def get_world():
    # code = request.args.get("code")

    server_name = request.args.get("name")

    # server = server_manager.get_server(server_name)
    #
    # if server.invite_code != code:
    #     return jsonify({"status": "error"})

    return jsonify({"status": "ok", "world": server_manager.server.world.to_dict()})


@blueprint.route("/disconnect_user", methods=["POST"])
def disconnect_user():
    # code = request.args.get("code")

    server_name = request.args.get("name")
    player_name = request.args.get("player_name")
    # server = server_manager.get_server(server_name)
    if server_manager.server.search_player(player_name) is None:
        return jsonify({"status": "error"})
    server_manager.server.disconnect_player(player_name)

    #
    # if server.invite_code != code:
    #     return jsonify({"status": "error"})
    return jsonify({"status": "ok"})


@blueprint.route("/set_block", methods=["POST"])
def set_block():
    # code = request.args.get("code")

    server_name = request.args.get("name")
    # server = server_manager.get_server(server_name)
    x = request.args.get("x")
    z = request.args.get("z")
    y = request.args.get("y")
    #
    # if server.invite_code != code:
    #     return jsonify({"status": "error"})
    server_manager.server.world.set_block("cobblestone", (float(x), float(y), float(z)))
    server_manager.save_servers()


@blueprint.route("/remove_block", methods=["POST"])
def remove_block():
    # code = request.args.get("code")

    server_name = request.args.get("name")
    #    server = server_manager.get_server(server_name)
    x = request.args.get("x")
    z = request.args.get("z")
    y = request.args.get("y")
    #
    # if server.invite_code != code:
    #     return jsonify({"status": "error"})
    block = server_manager.server.world.remove_block((float(x), float(y), float(z)))
    server_manager.save_servers()
    # print(block)
    if block:
        return jsonify({"status": "ok", "block": block})

    return jsonify({"status": "error"})

# @blueprint.route("/pop_block", methods=["POST"])
# def pop_block():
#     # code = request.args.get("code")
#
#     server_name = request.args.get("name")
#     server = server_manager.get_server(server_name)
#     x = request.args.get("x")
#     z = request.args.get("z")
#     y = request.args.get("y")
#
#     print(134)
#     server.world.remove_block(pos=(x, y, z))
#     # if server.invite_code != code:
#     #     return jsonify({"status": "error"})
