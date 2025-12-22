# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Animation addon.

import freecad.Animation as module
from importlib import resources


icons = resources.files(module) / 'icons'


def asIcon ( name : str ):

    file = name + '.png'

    icon = icons / file

    with resources.as_file(icon) as path:
        return str( path )