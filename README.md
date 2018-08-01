# ML-CLOUD-HELPERS

## Goals:

### Assist in packaging processed data, pushing, and pulling
Nice to Haves before Need to Haves
#### Nice to haves: 

##### install deps automagically 🤖

```bash
PACKAGE_ONE=$1
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $1|grep "install ok installed")
echo Checking for $1: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "No somelib. Setting up $1."
  sudo apt-get --force-yes --yes install $1
fi
```
```python
import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])    
```
#### Pulling

Goal: 
1 collect files with a handle like collect.sh files*.jpg
2 get a files.tar.xz file
3 type download files.tar.xz and files.download('files.tar.xz') downloads 

```bash
%run -i compress.py files_regex 
```
DUNNO
```Python
import os
from subprocess import call
from google.colab import files
files = sys.argv[1]

os.system("tar -cf - data_dir/ | xz -9e --threads=8 -c - > tarfile.tar.xz

files.download('example.txt')  
```
#### Pushing
* %run -i download.py .
  * download.py .
  * for filename in sys...(argv[1])
    * do 
  
#### Processing
* png_to_jpg.sh
* jpg_to_png.sh data_in_dir data_out_dir
  * mkdir -p argv[2]; mogrify --path..
* crop_and_resize.py data_in_dir [WIDTH] [HEIGHT] data_out_dir
* mkdir -p data_out; for filename in data_in: mogrify -path ....
* pull frames from videos
  * ffmpeg ... in_file .. data_out_dir
* tar -cf - data_dir/ | xz -9e --threads=8 -c - > tarfile.tar.xz
* Auto Auth for Google Drive( Not a full data persisting solution )
* Push
