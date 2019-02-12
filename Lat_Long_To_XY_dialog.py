# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Lat_Long_To_XYDialog
                                 A QGIS plugin
 Lat_Long_To_XY
                             -------------------
        begin                : 2019-02-11
        git sha              : $Format:%H$
        copyright            : (C) 2019 by  
        email                :  
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import *
from qgis.core import *
from qgis.utils import *

from ui_LatLongXY import Ui_LatLongXY

class LatLongXYDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self, iface.mainWindow())
        self.ui = Ui_LatLongXY()
        self.ui.setupUi(self)