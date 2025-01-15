
# Hospital Simulation Project

## Description

This project simulates the movement of groups of people through different rooms in a hospital using 3D visualization. It utilizes Matplotlib for rendering and allows for customizable configurations through a YAML file.

## Features

- **3D Visualization**: Visualize the movement of groups of people between various hospital rooms.
- **Configurable Parameters**: Easily configure room positions, group details, and movement times using a YAML configuration file.
- **Dynamic Movement**: Groups move smoothly between rooms, respecting defined travel and stay times.

## Requirements

- Python 3.x
- Matplotlib
- NumPy
- PyYAML

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ErwannL/Hospital-simulator.git
    cd Hospital-simulator
    ```

2. Install the required packages from **requirements.txt**:

    ```bash
    pip install -r requirements.txt
    ```

3. Custom the **config.yaml** file in the project directory

## Running the Simulation

Run the simulation by executing the following command:

```bash
python app.py
```

## Customization

You can customize:

Room positions in the **rooms** section.

Group configurations in the **groups** section.

Close delay for the simulation in the **close_delay** field.

## License

This project is licensed under the MIT License - see the [LICENSE](License) file for details.

## Acknowledgements

[Matplotlib](https://matplotlib.org/) for the 3D visualization capabilities.
[NumPy](https://numpy.org/) for numerical operations.
[PyYAML](https://pyyaml.org/) for parsing YAML files.

---
---

## For developpers

### To create the .exe

```bash
pip install pyinstaller
pyinstaller --onefile --add-data "config.yaml;." app.py
cp dist/app.exe .
```
