# 3D Shapes Table Viewer

This project is a PyQt6-based application that displays a table of randomly generated 3D shapes (Sphere, Cylinder, and Cube) along with their surface areas and volumes. The application uses a custom table model to populate the data dynamically.

## Project Structure

```
assigment9/
├── main.py
├── shapes_classes.py
├── README.md
├── screenshots/
│   ├── table screenshot.png
│   ├── output 1.png
│   └── output 2.png
```

## Classes and Methods

### `Shape3D` (Abstract Base Class)
- **Purpose**: Serves as a base class for all 3D shapes.
- **Abstract Methods**:
  - `surface_area(self)`: Calculates the surface area of the shape.
  - `volume(self)`: Calculates the volume of the shape.
  - `name(self)`: Returns the name of the shape.

### `Sphere` Class
- **Purpose**: Represents a sphere.
- **Methods**:
  - `__init__(self, radius)`: Initializes the sphere with a given radius.
  - `surface_area(self)`: Calculates the surface area of the sphere.
  - `volume(self)`: Calculates the volume of the sphere.
  - `name(self)`: Returns "Sphere".

### `Cylinder` Class
- **Purpose**: Represents a cylinder.
- **Methods**:
  - `__init__(self, radius, height)`: Initializes the cylinder with a given radius and height.
  - `surface_area(self)`: Calculates the surface area of the cylinder.
  - `volume(self)`: Calculates the volume of the cylinder.
  - `name(self)`: Returns "Cylinder".

### `Cube` Class
- **Purpose**: Represents a cube.
- **Methods**:
  - `__init__(self, side)`: Initializes the cube with a given side length.
  - `surface_area(self)`: Calculates the surface area of the cube.
  - `volume(self)`: Calculates the volume of the cube.
  - `name(self)`: Returns "Cube".

### `TableModel` Class
- **Purpose**: Custom table model for displaying shape data in a `QTableView`.
- **Methods**:
  - `__init__(self, shapes)`: Initializes the model with a list of shapes.
  - `rowCount(self, parent=None)`: Returns the number of rows in the table.
  - `columnCount(self, parent=None)`: Returns the number of columns in the table.
  - `data(self, index, role)`: Returns the data for a given cell.
  - `headerData(self, section, orientation, role)`: Returns the header labels for the table.

### `MainWindow` Class
- **Purpose**: Main application window that displays the table of shapes.
- **Methods**:
  - `__init__(self)`: Initializes the main window and sets up the table view.
  - `generate_random_shapes(self)`: Generates a list of random shapes (Sphere, Cylinder, Cube) with random dimensions.
  - `print_shapes_info(self)`: Prints the surface area and volume of each shape to the console.

## How to Run

```bash
   python main.py
```

### Screenshots of table
![table screenshot.png](screenshots/table%20screenshot.png)
### Screenshots of outputs
![output 1.png](screenshots/output%201.png)

![output 2.png](screenshots/output%202.png)
### Sample Output

```
Shape: Sphere
Surface Area: 314.16
Volume: 523.60

Shape: Cube
Surface Area: 150.00
Volume: 125.00

Shape: Cylinder
Surface Area: 471.24
Volume: 785.40
```
