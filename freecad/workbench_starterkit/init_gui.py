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
    toolbox = ["MyCube",
        "WarehouseProfiles"]
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
        from freecad.workbench_starterkit import warehouse_profiles_tool
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
        # This command will get group of parameters if it exist otherwise it will create a new one 
        p = App.ParamGet("User parameter:BaseApp/Preferences/Mod/workbench_starterkit")
        
        
        '''
        Theses commands will check if this is the first time the user activated this workbench,
        it will use parameter to check the first_startup status and store the new status
        '''
        is_first_startup = True
        # First check if there is article in group parameters
        if not p.IsEmpty():
            for article in p.GetContents():
                if "first_startup" in article:
                    # first_startup parameter exist so let's get is value
                    is_first_startup = p.GetBool("first_startup")
                else:
                    # If no article then create a boolean one called "first_startup" with True value
                    p.SetBool("first_startup", is_first_startup)
        else:
            # If no article then create a boolean one called "first_startup" with True value
            p.SetBool("first_startup", is_first_startup)
        # now show a QMessageBox if this is the first startup
        if is_first_startup is True:
            App.Console.PrintMessage("Welcome, this is your first time with this workbench\n")
            from PySide import QtGui
            mb = QtGui.QMessageBox()
            mb.setWindowTitle("First time?")
            mb.setText("Do you want to see a tutorial?")
            cb = QtGui.QCheckBox("Don't show this message again")
            mb.setCheckBox(cb)
            mb.setStandardButtons(mb.Yes | mb.No)
            reply = mb.exec_()
            if cb.isChecked():
                p.SetBool("first_startup", False)
            else:
                p.SetBool("first_startup", True)
            if reply == mb.No:
                App.Console.PrintMessage("Ok, no problem\n")
                pass
            elif reply == mb.Yes:
                App.Console.PrintMessage("Ok, let's go!\n")
                pass
        pass

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        pass


Gui.addWorkbench(TemplateWorkbench())
