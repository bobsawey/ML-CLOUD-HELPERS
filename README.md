# ML-CLOUD-HELPERS

Goals:

* Assist in packaging processed data, pushing, and pulling
  * png_to_jpg.sh
  * jpg_to_png.sh
    * crop_and_resize.py data_in_dir [WIDTH] [HEIGHT] data_out_dir
    * mkdir -p; for filename in 
* tar -cf - data_dir/ | xz -9e --threads=8 -c - > tarfile.tar.xz
* nice to have: install deps automagically
* Auto Auth for Google Drive( Not a full data persisting solution )
* Push
