# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

from mcpi.vec3 import Vec3

from .scene import Scene
from .thing import Thing


class Line(Thing):

    width = 3
    length = 10

    def build(self):
        end_x = self.position.x + self.width - 1
        end_y = self.position.y - 1
        end_z = self.position.z + self.length - 1

        # Find the type of land block destroyed with the line
        self._block_empty = \
            Scene.server.getBlock(self.position.x, self.position.y-1, self.position.z)

        Scene.server.setBlocks(self.position.x, self.position.y-1, self.position.z,
                               end_x, end_y, end_z, self.block)

        self._end_position = Vec3(end_x, end_y + 1, end_z)
