import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.workbench_starterkit import ICONPATH


class TemplateWorkbench(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """

    MenuText = "template workbench"
    ToolTip = "a simple template workbench"
    Icon = os.path.join(ICONPATH, "template_resource.svg")
    toolbox = ["MyCube"]
    toolbox_from_other_wb = [
        "Draft_Move",
        "Draft_Rotate",
    ]

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        from freecad.workbench_starterkit import my_numpy_function
        from freecad.workbench_starterkit import my_cube_tool
        App.Console.PrintMessage("switching to workbench_starterkit\n")
        App.Console.PrintMessage("run a numpy function: sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))

        self.appendToolbar("Tools", self.toolbox)
        self.appendMenu("Tools", self.toolbox)

        self.appendToolbar("Tools from other WB", self.toolbox_from_other_wb)
        self.appendMenu("Tools from other WB", self.toolbox_from_other_wb)

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        pass

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        pass


Gui.addWorkbench(TemplateWorkbench())
