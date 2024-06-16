from PyQt5.QtWidgets import QApplication
from PyQt5.QtSerialPort import QSerialPortInfo
from gui import Ui_MainWindow

def check_available_ports(self):
    available_ports = []
    for port in QSerialPortInfo.availablePorts():
        available_ports.append(port.portName())
    return available_ports
    
        
if __name__ == "__main__":
    app = QApplication([])
    ports = check_available_ports()
    if ports:
        print("Available ports:", ports)
    else:
        print("No serial ports available.")
        
#  show available ports in Ui interface dropdown list
#  in gui.py
#  add the following code to the __init__ method of the Ui_MainWindow class:
#
