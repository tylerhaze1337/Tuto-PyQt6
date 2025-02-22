# Complete Tutorial on PyQt6

## Introduction

**PyQt6** is a Python library for creating graphical user interfaces (GUI) using the Qt framework. It offers great flexibility and allows designing modern applications with an intuitive interface.

### Installation

To install PyQt6, use the following command:

```bash
pip install PyQt6
```

### Creating a Basic Window

Here is a simple example of a window with PyQt6:

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt6 Window")
        self.resize(400, 300)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
```

## Managing Widgets

PyQt6 offers several widgets to build interfaces:

### Labels and Buttons

```python
from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Labels and Buttons")
        
        self.label = QLabel("Click the button")
        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.update_label)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
    
    def update_label(self):
        self.label.setText("Button clicked!")
```

## Managing Layouts

**Layouts** allow organizing widgets within a window.

### Vertical Layout (QVBoxLayout)

```python
layout = QVBoxLayout()
layout.addWidget(widget1)
layout.addWidget(widget2)
self.setLayout(layout)
```

### Horizontal Layout (QHBoxLayout)

```python
layout = QHBoxLayout()
layout.addWidget(widget1)
layout.addWidget(widget2)
self.setLayout(layout)
```

### Grid Layout (QGridLayout)

```python
layout = QGridLayout()
layout.addWidget(widget1, 0, 0)
layout.addWidget(widget2, 0, 1)
layout.addWidget(widget3, 1, 0, 1, 2) # Spanned over 2 columns
self.setLayout(layout)
```

## Managing Signals and Slots

Signals and slots allow handling user interactions.

```python
self.button.clicked.connect(self.action)

def action(self):
    print("Button pressed")
```

## Creating a Window with a Menu

```python
from PyQt6.QtWidgets import QMainWindow, QMenuBar, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window with Menu")
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
```


