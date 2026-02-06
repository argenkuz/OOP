from PyQt6 import QtWidgets, QtCore
import sys
import random
from shapes_classes import  Sphere, Cylinder, Cube

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, shapes):
        super().__init__()
        self.shapes = shapes
        self.headers = ["Shape", "Surface Area", "Volume"]

    def rowCount(self, parent=None):
        return len(self.shapes)

    def columnCount(self, parent=None):
        return 3

    def data(self, index, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            shape = self.shapes[index.row()]
            if index.column() == 0:
                return shape.name()
            elif index.column() == 1:
                return f"{shape.surface_area():.2f}"
            elif index.column() == 2:
                return f"{shape.volume():.2f}"

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return self.headers[section]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Shapes Table")

        self.table = QtWidgets.QTableView()

        self.shapes = self.generate_random_shapes()
        self.model = TableModel(self.shapes)

        self.table.setModel(self.model)
        self.setCentralWidget(self.table)
        self.resize(500, 400)

        self.print_shapes_info()  # Печать в терминал

    def generate_random_shapes(self):
        shapes = []
        for _ in range(10):
            shape_type = random.choice(["Sphere", "Cylinder", "Cube"])
            if shape_type == "Sphere":
                radius = random.randint(1, 10)
                shapes.append(Sphere(radius))
            elif shape_type == "Cylinder":
                radius = random.randint(1, 10)
                height = random.randint(5, 20)
                shapes.append(Cylinder(radius, height))
            else:
                side = random.randint(1, 10)
                shapes.append(Cube(side))
        return shapes

    def print_shapes_info(self):
        i = 0
        print("\nGenerated 3D Shapes:")
        for shape in self.shapes:
            i += 1
            print(f"Shape {i}:")
            print(f"Shape: {shape.name()}")
            print(f"Surface Area: {shape.surface_area():.2f}")
            print(f"Volume: {shape.volume():.2f}")
            print(30*"-")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())