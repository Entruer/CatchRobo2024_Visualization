import sys

from rqt_gui.main import Main


def main():
    main = Main()
    sys.exit(main.main(sys.argv, standalone='tray_management.tray_management.TrayManagement'))


if __name__ == '__main__':
    main()