# ML-CLOUD-HELPERS

## Goals:

### Assist in packaging processed data, pushing, and pulling
*Nice to have: install deps automagically*

```bash
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' the.package.name|grep "install ok installed")
echo Checking for somelib: $PKG_OK
if [ "" == "$PKG_OK" ]; then
  echo "No somelib. Setting up somelib."
  sudo apt-get --force-yes --yes install the.package.name
fi
```

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
