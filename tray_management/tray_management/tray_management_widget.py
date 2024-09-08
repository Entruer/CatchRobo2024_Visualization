import os

import rclpy
from ament_index_python.packages import get_package_share_path

from python_qt_binding import loadUi
from PyQt5.QtWidgets import QWidget

class TrayManagementWidget(QWidget):
    def __init__(self, node, plugin=None):
        super(TrayManagementWidget, self).__init__()

        self.node = node
        self.logger = self.node.get_logger().get_child('TrayManagementWidget')
        self.plugin = plugin

        package_path = get_package_share_path('tray_management')
        ui_file = os.path.join(package_path, 'resource', 'TrayManagementWidget.ui')
        loadUi(ui_file, self)

    def shutdown(self):
        pass

    def save_settings(self, plugin_settings, instance_settings):
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        pass