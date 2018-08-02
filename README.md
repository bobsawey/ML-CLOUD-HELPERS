# ml-cloud-helpers

## Goals:

### Assist in packaging processed data, pushing, and pulling
Nice to Haves before Need to Haves
#### Nice to haves: 
##### installs as a command toolset with !pip
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

#### Two Way

##### Goal: Easy Auth with Google for Pushing and Pulling.
**Using Gist from https://gist.github.com/rdinse/159f5d77f13d03e0183cb8f7154b170a , thank u [@rdinse](https://github.com/rdinse)!**

Put Gist into start ipynb


#### Pulling


#### Packaging
Goal: 
1. collect files with a handle like collect.sh files*.jpg
    ```bash
    #collect.sh
    TOPACKAGE=$1
    ```
2. get a files.tar.xz file
    ```bash
    tar -cf - data_dir/ | xz -9e --threads=8 -c - > tarfile.tar.xz
    ```
3. type download files.tar.xz and files.download('files.tar.xz') downloads 

```bash
python3 download.py sys.argv[1]
```
```bash
%run -i compress.py files_regex 
```
```bash
!kuu compress *.jpg
#outputs: [unique].txz
```
```Python
#compress.py
import os
import sys
import uuid

#process args
def tarxz(sys.argv[1]):
  filename = generate_filename()
  os.system(f"tar -vcf - {sys.argv[1]} | xz -v9e --threads=8 -c - > {filename}")
def generate_filename(ext="txz"):
  return f"{uuid.uuid4()}.txz"
```


DUNNO
```Python
import os
from subprocess import call
from google.colab import files
files = sys.argv[2]

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
