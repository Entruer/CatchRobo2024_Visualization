import os

import rclpy
from catch24_msgs import msg
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

        self.data = msg.TrayState()
        self.data_pub = self.node.create_publisher(msg.TrayState, 'tray_state_receive', 10)
        self.data_sub = self.node.create_subscription(msg.TrayState, 'tray_state', self.on_data_receive, 10)

        for c in ['green', 'red', 'orange']:
            for i in range(6):
                getattr(self, f'{c}_{i}').valueChanged.connect(getattr(self, f'{c}_{i}_on_value_changed'))
                self.node.get_logger().info(f'Connect {c}_{i} to on_value_changed')

    def green_0_on_value_changed(self, value):
        self.data.green[0] = value
        self.data_pub.publish(self.data)

    def green_1_on_value_changed(self, value):
        self.data.green[1] = value
        self.data_pub.publish(self.data)

    def green_2_on_value_changed(self, value):
        self.data.green[2] = value
        self.data_pub.publish(self.data)

    def green_3_on_value_changed(self, value):
        self.data.green[3] = value
        self.data_pub.publish(self.data)

    def green_4_on_value_changed(self, value):
        self.data.green[4] = value
        self.data_pub.publish(self.data)

    def green_5_on_value_changed(self, value):
        self.data.green[5] = value
        self.data_pub.publish(self.data)

    def red_0_on_value_changed(self, value):
        self.data.red[0] = value
        self.data_pub.publish(self.data)

    def red_1_on_value_changed(self, value):
        self.data.red[1] = value
        self.data_pub.publish(self.data)

    def red_2_on_value_changed(self, value):
        self.data.red[2] = value
        self.data_pub.publish(self.data)

    def red_3_on_value_changed(self, value):
        self.data.red[3] = value
        self.data_pub.publish(self.data)

    def red_4_on_value_changed(self, value):
        self.data.red[4] = value
        self.data_pub.publish(self.data)

    def red_5_on_value_changed(self, value):
        self.data.red[5] = value
        self.data_pub.publish(self.data)

    def orange_0_on_value_changed(self, value):
        self.data.orange[0] = value
        self.data_pub.publish(self.data)

    def orange_1_on_value_changed(self, value):
        self.data.orange[1] = value
        self.data_pub.publish(self.data)

    def orange_2_on_value_changed(self, value):
        self.data.orange[2] = value
        self.data_pub.publish(self.data)

    def orange_3_on_value_changed(self, value):
        self.data.orange[3] = value
        self.data_pub.publish(self.data)

    def orange_4_on_value_changed(self, value):
        self.data.orange[4] = value
        self.data_pub.publish(self.data)

    def orange_5_on_value_changed(self, value):
        self.data.orange[5] = value
        self.data_pub.publish(self.data)

    def on_data_receive(self, msg):
        for i in range(6):
            getattr(self, f'green_{i}').setValue(msg.green[i])
            getattr(self, f'red_{i}').setValue(msg.red[i])
            getattr(self, f'orange_{i}').setValue(msg.orange[i])
            self.data = msg

    def shutdown(self):
        pass

    def save_settings(self, plugin_settings, instance_settings):
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        pass