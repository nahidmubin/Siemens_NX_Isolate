# Siemens NX Isolate Body v1.0.0
-------------------------

Installation Procedure for Windows:

1. Copy the "SIEMENS NX Isolate Body" folder in C drive.
   So the path to the folder will be "C:\SIEMENS NX Isolate Body"

2. Go to the NX installation folder and navigate to "menus" folder.
   If NX is installed in C drive then usually the path will be-
   C:\Program Files\Siemens\NX2206\UGII\menus

3. Open the "custom_dirs.dat" file with notepad or any other editor.
   Paste "C:\SIEMENS NX Isolate Body" at the end of the file and Save it.

4. Start NX. Create a new model file.
   File > New > Model > OK

5. Right Click in the empty space of any Tab or Bar and Click "Customize".

6. Goto Commands > Categories > New Item > Items > New User Command
   Drag "New User Command" and Drop it in the Home Tab's empty space (Right Side).

7. Right Click on the User Command. Add "Isolate Body" to the Name and Change Icon.
   Right Click again Goto Edit Action > Browse.
   Select "Python Files" from the right bottom side drop down menu.
   Goto "Siemens NX Isolate Body" Folder in C Drive and Select "Isolate Body.py" file.
   Press Ok on the Button action window and Close the Customize window.

8. Add an shortcut key to this New "Isolate Body" command. (Optional but Recommended)

9. Open a Part file containing several bodies.

10. Select Feature / Face / Edge / Body and select the "Isolate Body" command or press the shortcut key.
    The intended bodies will be isolated.

11. Select the "Isolate Body" command or press the shortcut key again and the isolation will end.
