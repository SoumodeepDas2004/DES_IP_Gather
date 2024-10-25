from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QLabel,QHBoxLayout,QVBoxLayout,QLabel,QPushButton,QMessageBox,QLineEdit
from IPGET import ipadressTotDATA
from PyQt5.QtGui import QIcon
#starting Layout
app=QApplication([])
mWindow=QWidget()
mWindow.setWindowTitle("FindThe_IP_DATA")
mWindow.setWindowIcon(QIcon("LocatorIcon.png"))
mWindow.resize(1000,700)
#giving button functtionality
data=str()
result=str()

def usebutton():
    data=ipdata.text()
    result=ipadressTotDATA(data)
    output_text.clear()
    output_text.setText(result)
    print(result)


# eliment creation
label1=QLabel("Give the IP address which You need to find \n [otherwise It will find yours DATA]:")
label1.setStyleSheet("QWidget{ background-color:grey;font-size: 17px;color: black;font-weight: bold ;} ")

ipdata= QLineEdit()
ipdata.setPlaceholderText("PUT THE IP ADRESS HERE PROPERLY")
ipdata.setStyleSheet("QWidget{ background-color:white;} ")

Sbtn= QPushButton("Submit")
Sbtn.setStyleSheet("QWidget{ font-weight: bold ; background-color:lightgreen; border: 2px solid #007bff; border-radius: 5px; height:23px} ")
Sbtn.clicked.connect(usebutton)

output_text=QTextEdit()
output_text.setStyleSheet("QWidget{ background-color:lightyellow;font-size: 24px;} ")

output_text.setReadOnly(True)
label2=QLabel("RESULT->")
label2.setStyleSheet("QWidget{ background-color:lightgrey;font-size: 17px;color: black;font-weight: bold ; } ")





#adding layout
mLayout=QVBoxLayout()
r0=QHBoxLayout()
r0.addWidget(label1)
r1=QHBoxLayout()
r1.addWidget(ipdata)
r2=QHBoxLayout()
r2.addWidget(Sbtn)

rL2=QHBoxLayout()
rL2.addWidget(label2)

r3=QHBoxLayout()
r3.addWidget(output_text)

mLayout.addLayout(r0)
mLayout.addLayout(r1)
mLayout.addLayout(r2)
mLayout.addLayout(rL2)
mLayout.addLayout(r3)

mWindow.setLayout(mLayout)
mWindow.setStyleSheet("QWidget{ background-color:lightblue;} ")
mWindow.show()
app.exec_()
