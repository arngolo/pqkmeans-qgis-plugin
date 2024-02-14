# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PqkMeansDialog
                                 A QGIS plugin
 This clustering algorithm is a quantized version of the K-Means algorithm that is memory and computationaly more efficient.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-01-31
        git sha              : $Format:%H$
        copyright            : (C) 2024 by armstrong ngolo
        email                : arngolo@outlook.com
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
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsRasterLayer, QgsProject
from qgis.utils import iface
from .scripts.pqkmeansClustering import PQKMeans

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'pqkmeans_clustering_dialog_base.ui'))


class PqkMeansDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(PqkMeansDialog, self).__init__(parent)
        self.setupUi(self)
        # OK/cancel button object name is button_box and its class is QDialogButtonBox.
        # to check for the event that triggers one or another, search from the Qt5 website. (event is button_box.accepted/rejected)
        self.button_box.accepted.connect(self.pqkmeans_clustering)
        self.outputButton.clicked.connect(self.select_output_file)
        # self.projections.addItems(["utm", "EPSG", "latlong", "longlat", "aea"])

    def pqkmeans_clustering(self):
        input_raster = self.inputRaster.currentLayer()
        input_raster = input_raster.source() # gives the path of the raster
        output_directory = self.outputDir.text()
        output_raster_name = self.outputRaster.text()
        output_raster = os.path.join(output_directory, output_raster_name)
        num_subdim = int(self.numSubdim.value())
        k = int(self.KParam.value())
        sample_size = int(self.SampleSize.value())
        Ks = int(self.KsParam.value())
        # proj = self.projections.currentText()
        # epsg_value = self.EPSGValue.value()
        # ellps = self.ellipsoid.value()
        # datum = self.Datum.value()

        PQKMeans(input_raster, output_directory, output_raster, k, num_subdim, Ks, sample_size)

        #LOAD RASTER INTO QGIS
        result_layer = QgsRasterLayer(output_raster, output_raster_name)
        if result_layer.isValid():
            # Add the layer to the map canvas
            QgsProject.instance().addMapLayer(result_layer)
            print("Raster layer added to the map canvas.")
        else:
            print("Error loading the raster layer.")

        # Refresh the map canvas to see the changes
        iface.mapCanvas().refresh()

    def select_output_file(self):
        dialog = QtWidgets.QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Select Folder")
        self.outputDir.setText(folder_path)
