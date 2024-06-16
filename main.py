from PyQt5.QtWidgets import QApplication, QMainWindow,QHBoxLayout,QComboBox, QWidget
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets,QtSerialPort
from gui import Ui_MainWindow


class App_window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(App_window, self).__init__()
        self.setupUi(self)
        self.setupPorts()
        self.clickedConfig()
     
    def check_available_ports(self):
        available_ports = []
        for port in QtSerialPort.QSerialPortInfo.availablePorts():
            available_ports.append(port.portName())
        return available_ports
        

    def setupPorts(self): 
        a = self.check_available_ports()    
        print(a)
        self.port.addItems(a)
        self.port.currentIndex()
            
            
        layout = QHBoxLayout(self.port)
        layout.addWidget(self.port)
        container = QWidget()
        container.setLayout(layout)
                            
    
    def selectionchange(self, i):
        print("Current index", i, "selection changed ", self.port.currentText())
        
    def clickedConnect(self):
        print("Connect")
            
    def clickedConfig(self):
        self.btn_config.clicked.connect(self.clickedConnect)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = App_window()
    MainWindow.show()
    sys.exit(app.exec_())