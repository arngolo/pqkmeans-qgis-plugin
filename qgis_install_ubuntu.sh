
sudo snap install cmake --classic
sudo apt-get install --yes build-essential # gcc, g++

# install QGIS
sudo apt install --yes gnupg software-properties-common

sudo mkdir -m755 -p /etc/apt/keyrings # QGIS Signing Key. no need if ubuntu 22 or newer

sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg

touch /etc/apt/sources.list.d/qgis.sources
cat qgis.source | sudo tee /etc/apt/sources.list.d/qgis.sources >/dev/null
sudo apt update
sudo apt --yes install qgis qgis-plugin-grass
sudo apt install python3-pip
