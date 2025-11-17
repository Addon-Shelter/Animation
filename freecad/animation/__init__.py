# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileCopyrightText: 2014 microelly
# SPDX-FileNotice: Part of the Animation addon.

from FreeCAD import ParamGet

# Get the Parameter Group of this module
ParGrp = ParamGet("System parameter:Modules").GetGroup("Animation")

# Set the needed information
ParGrp.SetString("HelpIndex",        "http://www.freecadweb.org")
ParGrp.SetString("WorkBenchName",    "Animation")

