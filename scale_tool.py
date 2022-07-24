import os
import sys
from imp import reload
from PySide2 import QtWidgets, QtCore, QtGui

dir_path = os.path.dirname(os.path.realpath(__file__))
if dir_path not in sys.path:
    sys.path.append(dir_path)

import maya.cmds as cmds
import ui.scaletool_mainwindow as window
import maya_window
import units

# Reload the modules
reload(units)
reload(window)
reload(maya_window)

class ScaleToolMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ScaleToolMainWindow, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)

        self.ui = window.Ui_MainWindow()
        self.ui.setupUi(self)

        # Members
        # UI Bindings
        self.ui.btn_perform_scale.clicked.connect(self._perform_scale_conversion)

        self.init_ui()

    def init_ui(self):
        self.ui.combo_current_unit.addItems([elem.name for elem in units.Unit])
        self.ui.combo_target_unit.addItems([elem.name for elem in units.Unit])

    def _get_multiplier(self, cur, target):
        conversion = {
            'Centimeters': units.get_cm_multiplier(target),
            'Meters': units.get_m_multiplier(target),
            'Foot': units.get_ft_multiplier(target),
            'Inches': units.get_in_multiplier(target),
            'Yard': units.get_yrd_multiplier(target)
        }

        return conversion[cur]

    def _perform_scale_conversion(self):
        cur_unit = self.ui.combo_current_unit.currentText()
        target_unit = self.ui.combo_target_unit.currentText()
        
        multiplier = self._get_multiplier(cur_unit, target_unit)
        print('Conversion: {0}'.format(multiplier))
        user_multiplier = self.ui.spnbox_scale_mult.value()
        targ_mult = multiplier * user_multiplier
        print('ConversionMult: {0}'.format(targ_mult))

        mesh_objs = cmds.ls(sl=True)
        for obj in mesh_objs:
            print('Scaling: {0}'.format(obj))
            scale_x, scale_y, scale_z = cmds.xform(obj, query=True, scale=True)
            print('CurScale: {0}'.format([scale_x, scale_y, scale_z]))
            targ_x = scale_x * targ_mult
            targ_y = scale_y * targ_mult
            targ_z = scale_z * targ_mult
            print('TargetScale: {0}'.format([targ_x, targ_y, targ_z]))
            cmds.scale(targ_x, targ_y, targ_z, obj, absolute=True)

        if self.ui.chkbox_reset_xform.isChecked():
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            


def main():
    mainWindow = ScaleToolMainWindow(maya_window.get_maya_main_window())
    mainWindow.show()
    return mainWindow