from rqt_gui_py import plugin

from .tray_management_widget import TrayManagementWidget

class TrayManagement(plugin.Plugin):

    def __init__(self, context):
        super(TrayManagement, self).__init__(context)
        self.setObjectName('TrayManagement')
        self._widget = TrayManagementWidget(context.node, self)
        context.add_widget(self._widget)

    def shutdown_plugin(self):
        self._widget.shutdown()

    def save_settings(self, plugin_settings, instance_settings):
        self._widget.save_settings(plugin_settings, instance_settings)

    def restore_settings(self, plugin_settings, instance_settings):
        self._widget.restore_settings(plugin_settings, instance_settings)

    def trigger_configuration(self):
        self._widget.trigger_configuration()

    def shutdown(self):
        self._widget.shutdown()