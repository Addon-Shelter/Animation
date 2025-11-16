# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Animation addon.

import Part, Draft
App=FreeCAD

App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
b=App.ActiveDocument.addObject("Part::Box","Box")

c=Draft.clone(b)
import Animation


m=Animation.createManager("Skaler Manager")

import Scaler
reload(Scaler)

s=Scaler.createScaler("Mein Skalierer")
s.obj2=c
s.duration=80

m.addObject(s)
m.Proxy.run()

