Instructions to Use the Script in Unreal Engine:
Open the Unreal Engine Editor.

Navigate to the Output Log window (you can find this under Window → Developer Tools → Output Log).

In the Output Log, you should see a button for Python at the bottom. Click it to open the Python Editor.

Copy and paste the script above into the Python Editor.

In the script, update the FOLDER_PATH variable to match the path of the folder where your assets are located (e.g., /Game/MainGameFolder/R_D).

Save the script by clicking the disk icon in the Python Editor if you want to reuse it later, or simply press Run to execute the script.

The script will rename all the assets in the folder based on their original names, adding _Collectible at the end.
If you want to rename items in another folder, simply change the FOLDER_PATH variable in the script to point to the correct folder.
After running, the renamed assets will appear in the Content Browser with their new names.

Optional: Save the Script for Future Use
To save the script for future use, you can click Save Script in the Python Editor and give it a name like rename_collectibles.py.
In future Unreal sessions, you can load this saved script by clicking Open Script in the Python Editor, selecting it, and running it.
