from setuptools import find_packages, setup

package_name = 'tray_management'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name + '/resource', ['resource/TrayManagementWidget.ui']),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Entruer',
    maintainer_email='xinjia0104@gmail.com',
    description='CatchRobo2024 tray management visualization',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'tray_management = ' + package_name + '.main:main',
        ],
    },
)
