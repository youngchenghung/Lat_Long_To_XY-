# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Lat_Long_To_XY
                                 A QGIS plugin
 Lat_Long_To_XY
                             -------------------
        begin                : 2019-02-11
        copyright            : (C) 2019 by  
        email                :  
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Lat_Long_To_XY class from file Lat_Long_To_XY.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .Lat_Long_To_XY import Lat_Long_To_XY
    return Lat_Long_To_XY(iface)
