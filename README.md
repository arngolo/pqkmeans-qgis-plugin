# pqkmeans-qgis-plugin
This QGIS plugin is a quantized version of the clustering algorithm K-Means, used for image classification. It is memory and computationally more efficient than the original algorithym.

## Install the plugin:
To install pqkmeans_clustering plugin in QGIS follow the steps bellow:
- clone the repository https://github.com/arngolo/pqkmeans-qgis-plugin and copy the pqkmeans_clustering directory into the QGIS plugin directory as specified in the `pqkmeans_clustering/README.txt` file.
- Install the pluging: plugins > Manage and install plugins pqkmeans_clustering.
- Open the plugin. The UI will look as bellow:
<kbd> <img src="plugin_gui.png" /> </kbd>

## Using the plugin:
- **k:** as you wish for the number of clusters

- **num_of_subdimension (M):**  The  number of subdimensions (from the input nD image) for quantization. The higher the subdimension the slower the algorithm.

- **Ks:**  represents the maximum digital number. By default it is 256 that corresponds to 8 bits.

- **sample_size:** The number of pixels you select for quantization. (Good results where achieved with 9.5% of the total number of pixels (Ngolo and Watanabe, 2022)).

## WINDOWS requirements
- Install the dependencies by running the requirements.txt file (use the osgeo4w terminal for windows).
```
pip install -r requirements.txt
```
- Install cmake: pqkmeans library requires cmake:

  - If cmake is not available from OSGEOW4 shell, check from the default command prompt.
     `cmake --version`. You will most likely not find it!

  - From the OSGEO4W shell type ```echo %path%``` to check where libraries such as python and qt are installed (~\apps)

  - Once done, from the shell type $dir and copy the path.

  - Download and install cmake. install in the same directory where other libraries (python, qt are installed: <dir_output>\apps\CMake)

  - Once the installation is finished, from the OSGEO4W shell add cmake path to PATH!!!:

     ```
     set PATH=<dir_output>\apps\Cmake\bin;%PATH%
     ```

## MACOS requirements
One of the requirements for pqkmeans is cmake:

Make sure you have Xcode installed (Xcode has the necessary compilers) and add to path as (`try not adding to path!`):
```
export PATH="/Applications/Xcode.app/Contents/Developer/usr/bin:$PATH"
```

```
brew install cmake
```

You may need (`try without adding!`) to add it to path (despite being in `/usr/local/Cellar/cmake/3.28.3/bin` look for it in /usr/local/opt):
```
export PATH="/usr/local/opt/cmake/bin:$PATH"
```

In MACOS, QGIS python environment is not activated using the activate command. Instead, locate the python associated with it (from QGIS python console: `sys.executable`) and add -m flag followed by pip install command.

```
/Applications/QGIS.app/Contents/MacOS/bin/python3 -m pip install <library>
```

You may need (`try without adding!`) to add it to path:
```
export PATH="/Applications/QGIS.app/Contents/MacOS/bin:$PATH"
```

Plugins are located in a location similar to:
`/Users/<user_name>/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins`

**Note:** Plugins directory is not initially created unless you previously installed a plugin from QGIS. Create the directory yourself if necessary.

### One of the requirements to successfully install pqkmeans library is cmake:

```
brew install cmake
```

You may need to add it to path (locate it and add to path):
```
export PATH="/usr/local/Cellar/cmake/3.28.3/bin:$PATH
```

Upgrade necessary libraries:
```
<qgis_path>/python3 -m pip install --upgrade pip setuptools wheel
```

In Mac, QGIS python environment is not activated using the activate command. Instead, locate the python associated with it and add `-m` flag followed by `pip install` command.

When QGIS is installed from .dmg file (recommended), the python directory is `/Applications/QGIS.app/Contents/MacOS/bin/python3`. and you can export to `PATH` as:

```
export PATH="/Applications/QGIS.app/Contents/MacOS/include/python3.9:$PATH"
```

Install python libraries by running the command bellow:
```
<qgis_path>/python3 -m pip install -r requirements.txt
```

## LINUX/UBUNTU requirements
### You may need to install QGIS first:

```
./qgis_install_ubuntu.sh
```

Open qgis, and check the python path from python console: 

`Import sys` > `sys.executable`

You should get the python path for qgis and add it to system PATH:

```
export PATH=”$PATH:<path_to_qgis_python>”
```

```
pip install -r requirements_ubuntu.txt
```

**Note:** In ubuntu system, the plugins directoory is different from windows. From qgis python console run sys.path to check the plugins directory.  It should be somewhere like: `/home/ubuntu/.local/share/QGIS/QGIS3/profiles/default/python/plugins`. 


## WINDOWS Development environment

|  Software/library        |  version               |
|:------------------------:|:----------------------:|
| QGIS                     |  3.34.3-Prizren        |
| Qt                       |  5.15.3                |
| Python                   |  3.9.18                |
| GDAL/OGR                 |  3.8.3                 |
| PROJ                     |  9.3.1                 |
| EPSG registry database   |  v10.098 (2023-11-24)  |
| GEOS                     |  3.12.1-CAPI-1.18.1    |
| SQLite                   |  3.41.1                |
| PDAL                     |  2.6.0                 |
| PostgreSQL client        |  15.2                  |
| SpatiaLite               |  5.1.0                 |
| QWT                      |  6.1.6                 |
| QScintilla2              |  2.13.4                |
| rasterio                 |  1.3.9                 |
| pqkmeans                 |  1.0.6                 |
| cmake                    |  3.28.2                |
| OS                       |  Windows 10, 2009      |

## MAC Development environment
|  Software/library        |  version               |
|:------------------------:|:----------------------:|
| QGIS                     |  3.34.3-Prizren        |
| Qt                       |  5.15.2                |
| Python                   |  3.9.5                 |
| GDAL/OGR                 |  3.3.2                 |
| PROJ                     |  8.1.1                 |
| EPSG registry database   |  v10.028 (2021-07-07)  |
| GEOS                     |  3.9.1-CAPI-1.14.2     |
| SQLite                   |  3.35.2                |
| PDAL                     |  2.3.0                 |
| PostgreSQL client        |  unknown               |
| SpatiaLite               |  5.0.1                 |
| QWT                      |  6.1.6                 |
| QScintilla2              |  2.11.5                |
| rasterio                 |  1.1.5                 |
| pqkmeans                 |  1.0.6                 |
| cmake                    |  3.28.3                |
| xcode                    |  15.2                  |
| clang                    |  macOS 15.0.0          |
| OS                       |  macOS 14.3            |
| MAC architecture         |  x86_64                |

## UBUNTU Development environment
|  Software/library        |  version                               |
|:------------------------:|:--------------------------------------:|
| QGIS                     |  3.26.3-Buenos Aires                   |
| Qt                       |  5.12.8                                |
| Python                   |  3.8.10                                |
| GDAL/OGR                 |  3.0.4                                 |
| PROJ                     |  6.3.1                                 |
| EPSG registry database   |  v9.8.6 (2020-01-22)                   |
| GEOS                     |  3.8.0-CAPI-1.13.1                     |
| SQLite                   |  3.31.1                                |
| PDAL                     |  2.0.1                                 |
| PostgreSQL client        |  12.12 (ubuntu 12.12-0ubuntu0.20.04.1) |
| SpatiaLite               |  5.1.0                                 |
| QWT                      |  6.1.6                                 |
| QScintilla2              |  2.13.4                                |
| rasterio                 |  1.3.9                                 |
| pqkmeans                 |  1.0.6                                 |
| cmake                    |  3.28.2                                |
| gcc                      |  9.4.0                                 |
| g++                      |  9.4.0                                 |
| OS                       |  Ubuntu 20.04                          |

### References:

Matsui, Y., K. Ogaki, T. Yamasaki, and K. Aizawa 2017.“PQk-means: Billion-scale Clustering for Product-quantized Codes.” Paper presented at the proceedings of the ACM International Conference on Multimedia, Mountain View, California, USA, 23–27 October 1725-1733. https://arxiv.org/abs/1709.03708v1

Ngolo, A.M.E and T. Watanabe 2022. “Integrating geographical information systems, remote sensing, and machine learning techniques to monitor urban expansion: an application to Luanda, Angola.” Geo-spatial Information
Science 26 (3): 446–464. https://doi.org/10.1080/10095020.2022.2066574.

### CITATION
[![DOI](https://zenodo.org/badge/750484636.svg)](https://zenodo.org/doi/10.5281/zenodo.10655926)
