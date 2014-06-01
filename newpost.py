#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#!/usr/bin/python
# simple.py
# -*- coding: utf-8 -*-

import webbrowser
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

#app = QtGui.QApplication(sys.argv)


# widget = QtGui.QWidget()
# widget.resize(250, 150)
# widget.setWindowTitle('newpost')
# widget.show()


class InputDialog(QtGui.QWidget):
   def __init__(self, parent=None):
       QtGui.QWidget.__init__(self, parent)
       self.setGeometry(600, 100, 500, 200)
       self.setWindowTitle('newpost')
       self.button = QtGui.QPushButton('Enter', self)
       self.button.setFocusPolicy(QtCore.Qt.NoFocus)
       self.button.move(20, 20)
       self.connect(self.button, QtCore.SIGNAL('clicked()'), self.enterbrowser)
       self.setFocus()
       self.label = QtGui.QLineEdit(self)
       self.label.move(130, 22)
       self.label.setGeometry(130, 22, 300, 150)


   def enterbrowser(self):
       
	a = 'http://dnevnik-galina.diary.ru/?newpost#vbform'
	b = 'http://www.livejournal.com/update.bml'
	c = 'http://www.tumblr.com/new/text'
	webbrowser.open(a)
	webbrowser.open(b)
	webbrowser.open(c)
	d = self.label.text()
	print(unicode(d))

app = QtGui.QApplication(sys.argv)
icon = InputDialog()
icon.show()
app.exec_()





