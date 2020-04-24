import sys

import mcpi.block
import mcpi.minecraft
from mcpi.vec3 import Vec3

from mcthings.server import Server
from mcthings.town import Town

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building a town")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))

        town = Town(pos)
        town.block = mcpi.block.BEDROCK
        town.build()

        town = Town(Vec3(pos.x-5, pos.y, pos.z))
        town.block = mcpi.block.BEDROCK
        town.house_mirror = True
        town.build()


    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
