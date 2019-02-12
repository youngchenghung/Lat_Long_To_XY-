# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Lat_Long_To_XY
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from qgis.utils import *
from qgis.gui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from Lat_Long_To_XY_dialog import LatLongXYDialog
import os.path
from pyproj import Proj, transform

class Lat_Long_To_XY:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()
        self.cLayer = None

        self.lat_long_to_xy_dlg = LatLongXYDialog()
        self.lat_long_to_xy_dlg.setWindowTitle(u'經緯度定位')

    def initGui(self):
        self.menu = QMenu(self.iface.mainWindow())
        self.menu.setTitle(u'經緯度定位工具')

        self.toolBar = self.iface.addToolBar(u'經緯度定位工具列')
        self.toolBar.setObjectName('LatLongToXY')

        self.action_lat_long_to_xy = QAction(QIcon("C:/Users/tesla/.qgis2/python/plugins/Lat_Long_To_XY/LatLongXY.png"), u"經緯度定位", self.iface.mainWindow())
        self.action_lat_long_to_xy.setCheckable(True)
        self.action_lat_long_to_xy.triggered.connect(self.lat_long_to_xy_init)
        self.toolBar.addAction(self.action_lat_long_to_xy)

        self.lat_long_to_xy_dlg.ui.positioning.clicked.connect(self.positioning)
        self.lat_long_to_xy_dlg.ui.cancel.clicked.connect(self.cancel)

    def unload(self):
        self.iface.removeToolBarIcon(self.action_lat_long_to_xy)
        self.iface.removePluginMenu(u"&經緯度定位", self.action_lat_long_to_xy)

    # 經緯度定位工具 - 啟動點
    def lat_long_to_xy_init(self):
        self.mapInstance = QgsMapLayerRegistry.instance()
        self.mapLayers = self.mapInstance.mapLayers()
        if (len(self.mapLayers) < 2):
            QMessageBox.information(self.iface.mainWindow(), 
                                    "Error", 
                                    u"請先開啟系統圖資")
            return
        
        layers = self.iface.legendInterface().layers()


        for layer in layers:
            layerType = layer.type()
            if layerType == QgsMapLayer.VectorLayer:
                if layer.name() == "admin":
                    break


        self.lat_long_to_xy_dlg.show()

    # 定位
    def positioning(self):

        mc = self.canvas
        ijg = 0

        layers = mc.layers()
        layerCounts = mc.layerCount()
        for layer in layers:
            layerType = layer.type()
            ijg = ijg + 1
            if layerType == QgsMapLayer.VectorLayer:
                if layer.name() == "ZoomMarker":
                    vl = layer
                    vl.startEditing()

                    for feature in vl.getFeatures():
                        vl.deleteFeature(feature.id())
                    pr = vl.dataProvider()
                    break
                else:
                    if ijg == layerCounts:
                        vl = QgsVectorLayer("Point?crs=epsg:3826", "ZoomMarker", "memory")
                        pr = vl.dataProvider()

                        pr.addAttributes([QgsField("name", QVariant.String),
                                            QgsField("id1", QVariant.int),
                                            QgsFoeld("id2", Qvariant.Double)])
                        QgsMapLayerRegistry.instance().addMapLayer(vl)

        # https://epsg.io/transform#s_srs=4326&t_srs=3826
        # WGS84轉TWD97
        inProj = Proj(init='epsg:4326')
        outProj = Proj(init='epsg:3826')

        long = float(self.lat_long_to_xy_dlg.ui.Longitude_x.text())
        lat = float(self.lat_long_to_xy_dlg.ui.Latitude_y.text())

        x, y = transform(inProj, outProj, long, lat)
        print (x, y)

        fet = QgsFeature()
        fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(x,y)))
        fet.setAttributes(["Zoon", 0, 0])
        pr.addFeatures([fet])

        symbol_layer = QgsSvgMarkerSymbolLayerV2()

        symbol_layer.setPath(os.path.dirname(os.path.realpath(__file__))+'\\red-marker.svg')
        symbol_layer.setSize(12.0)
        symbol_layer.setVerticalAnchorPoint(QgsMarkerSymbolLayerV2.VerticalAnchorPoint(2))        
        vl.rendererV2().symbols()[0].changeSymbolLayer(0, symbol_layer)

        mc = self.iface.mapCanvas()
        rect = QgsRectangle(float(x)-50, float(y)-50, float(x)+50, float(y)+50)
        mc.setExtent(rect)
        mc.refresh()
        pass

    # 取消
    def cancel(self):
        self.lat_long_to_xy_dlg.close()