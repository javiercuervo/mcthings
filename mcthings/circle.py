# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

from mcthings.scene import Scene
from mcthings.thing import Thing


class Circle(Thing):

    radius = None
    """ radius of the Sphere """

    def build(self):
        Scene.drawing.drawCircle(
            self.position.x,
            self.position.y,
            self.position.z,
            self.radius,
            self.block)
        self._end_position = self.position
