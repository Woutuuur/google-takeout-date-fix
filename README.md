# Google Takeout Date Fix
Script to update the "last accessed date" and "created date" of a Google Photos export. When you export your images from Google Takeout their creation date and last accessed metadata fields will be reset to the current time. Some apps use this date to determine the date the photo was taken (e.g. Synology Photos). This script takes the `"photoTakenTime"` field from each photo's associated json file and updates the metadata fields with that.

### Dependencies
- Python >= 3.10
- `filedate` Python module (`python -m pip install filedate`)

### Instructions
1. Place the `add_metadata.py` file in the "Google Photos" directory of the Google Takeout (e.g. `.../Takeout/Google Photos/add_metadata.py`).
2. Run the script: `python add_metadata.py`.
3. Once finished, you can use the `move_json_files.py` script to move all the json metadata files to a separate directory. To do this, run `python move_json_files.py` after placing the `move_json_files.py` in the same directory as the `add_metadata.py` file.

Note: this script only searches one directory level deep. If your export (somehow) has multiple levels of directories, this script won't account for those.
Note 2: Google Photo's Takeout has some weird edge cases due to file name length limits. The script exits when it encounters a `.json` file it cannot find a image or video file for. Update the file names of these edge cases manually.
