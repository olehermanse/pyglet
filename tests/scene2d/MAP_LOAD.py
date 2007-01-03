#!/usr/bin/env python

'''Testing loading of a map.

You should see a simple map with a circular road on it.
The tiles are not well-designed :)

Press escape or close the window to finish the test.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

import os
import unittest
from render_base import RenderBase, DummyImage
import pyglet.scene2d
from pyglet.GL.VERSION_1_1 import *

class MapLoadTest(RenderBase):
    def test_main(self):
        map_xml = os.path.join(os.path.dirname(__file__), 'map.xml')

        self.init_window(256, 256)
        m = pyglet.scene2d.Map.load_xml(map_xml)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_COLOR_MATERIAL)
        self.run_test(m, show_focus=True, debug=False)

if __name__ == '__main__':
    unittest.main()
