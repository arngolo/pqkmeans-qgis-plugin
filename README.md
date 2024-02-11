# pqkmeans-qgis-plugin
This QGIS plugin is a quantized version of the clustering algorithm K-Means, used for image classification. It is memory and computationally more efficient than the original algorithym.

To install pqkmeans_clustering plugin in QGIS follow the steps bellow:
- clone the repository https://github.com/arngolo/pqkmeans-qgis-plugin and copy the pqkmeans_clustering directory into the QGIS plugin directory as specified in the `pqkmeans_clustering/README.txt` file.
- Install the pluging: plugins > Manage and install plugins pqkmeans_clustering.
- Open the plugin. The UI will look as bellow:
<kbd> <img src="plugin_gui.png" /> </kbd>

## WINDOWS requirements
- Install the dependencies by running the requirements.txt file (use the osgeo4w terminal for windows).
```pip install -r requirements.txt```
- Install cmake: pqkmeans library requires cmake:

  - If cmake is not available from OSGEOW4 shell, check from the default command prompt.
     `cmake --version`. You will most likely not find it!

  - From the OSGEO4W shell type ```echo %path%``` to check where libraries such as python and qt are installed (~\apps)

  - Once done, from the shell type $dir and copy the path.

  - Download and install cmake. install in the same directory where other libraries (python, qt are installed: <dir_output>\apps\CMake)

  - Once the installation is finished, from the OSGEO4W shell add cmake path to PATH!!!:

     ```set PATH=<dir_output>\apps\Cmake\bin;%PATH%```

## MAC requirements

## LINUX/UBUNTU requirements
### You may need to install QGIS first:

```./qgis_install_ubuntu.sh```

Open qgis, and check the python path from python console: 

`Import sys` > `sys.executable`

You should get the python path for qgis and add it to system PATH:

```export PATH=”$PATH:<path_to_qgis_python>”```

```pip install -r requirements_ubuntu.txt```

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
| rasterio                 |  1.3.9                 |
| pqkmeans                 |  1.0.6                 |
| cmake                    |  3.28.2                |
| QWT                      |  6.1.6                 |
| QScintilla2              |  2.13.4                |
| OS                       |  Windows 10, 2009      |

## MAC Development environment

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
| rasterio                 |  1.3.9                                 |
| pqkmeans                 |  1.0.6                                 |
| cmake                    |  3.28.2                                |
| gcc                      |  9.4.0                                 |
| g++                      |  9.4.0                                 |
| QWT                      |  6.1.6                                 |
| QScintilla2              |  2.13.4                                |
| OS                       |  Ubuntu 20.04                          |

## TO-DO
- update Readme
- publish the plugin