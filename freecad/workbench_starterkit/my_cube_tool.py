# coding: utf-8

import os
import FreeCAD as App
import Part

if App.GuiUp:
    import FreeCADGui as Gui

    from PySide import QtCore, QtGui
    from DraftTools import translate
    from PySide.QtCore import QT_TRANSLATE_NOOP
else:
    # \cond
    def translate(ctxt, txt):
        return txt
    def QT_TRANSLATE_NOOP(ctxt, txt):
        return txt
    # \endcond

def create_cube(dimensions=15.0):
    """
    Create a cube
    :param dimensions: float
    """
    my_cube = App.ActiveDocument.addObject("Part::Box","Box")
    my_cube.Label = "Cube"
    my_cube.Length = dimensions
    my_cube.Width = dimensions
    my_cube.Height = dimensions


class _CommandmyCube:
    def __init__(self):
        pass

    def GetResources(self):
        "Tool resources"
        from freecad.workbench_starterkit import ICONPATH
        return {
            "Pixmap": os.path.join(ICONPATH, "template_resource.svg"),
            "MenuText": QT_TRANSLATE_NOOP("StarterKit", "MyCube"),
            "Accel": "C, B",
            "ToolTip": "<html><head/><body><p><b>Ajouter un cube.</b> \
                    <br><br> \
                    Aux dimensions de 15 mm. \
                    </p></body></html>",
        }

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""

        active = True
        if App.ActiveDocument:
            # If there is more than 2 objects in the current active document, then the tool is inactive.
            if len(App.ActiveDocument.Objects) > 2:
                active = False
        else:
            active = False
        return active

    def Activated(self):
        """Define what happen when the user clic on the tool"""
        create_cube(15.0)

if App.GuiUp:
    Gui.addCommand("MyCube", _CommandmyCube())