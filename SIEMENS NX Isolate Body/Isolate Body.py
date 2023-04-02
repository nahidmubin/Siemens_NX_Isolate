# This file is a part of the program called "Isolate Body" for SIEMENS NX.
# Version 1.0.0
# Created by Nahid Mubin

import NXOpen
import NXOpen.UF
import NXOpen.Features
from pathlib import Path
import json

# Get the Current Session, UI and UF Session.
theSession  = NXOpen.Session.GetSession()
theUI = NXOpen.UI.GetUI()
theUFSession = NXOpen.UF.UFSession.GetUFSession()
# Get the Work Part.
workPart = theSession.Parts.Work

def isolate_body() :

    # Check for active work part.
    if workPart is None:
        return theUFSession.Ui.DisplayMessage("NO Active Part! Open a Part First.", 1)

    # Get the Work Part name, Work Part UID and bodies in the Work Part.
    workPartName = workPart.Name
    workPartUID = workPart.UniqueIdentifier
    workBodies = workPart.Bodies
    workPartFeatures = workPart.Features
    # Set Undo mark for undoing.
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")

    # Initialize the path to save the visible_body list in a json file.
    # This bodies will be shown later when exiting isolation.
    location = Path(f"C:/SIEMENS NX Isolate Body/Temporary Json File/body_identifiers_{workPartName}_{workPartUID}.json")

    # Check for the existence of path
    if location.exists():
        try:
            # Path exist. Read the json file and get the body_identifiers list.
            contents = location.read_text()
            body_identifiers = json.loads(contents)

            # Create a list bodies_to_show and append the bodies in the list using the identifiers.
            bodies_to_show = []
            for identifier in body_identifiers:
                body = workBodies.FindObject(identifier)
                bodies_to_show.append(body)

            # Show the bodies that are in bodies_to_show list.
            theSession.DisplayManager.UnblankObjects(bodies_to_show)
            # Delete the json file
            location.unlink()
        except:
            # Delete the json file
            location.unlink()
        
    else:
        # json file doesn't exist. Create it at the end.
        # Make a list of current Visible bodies.   
        visible_bodies = [body for body in workBodies if not body.IsBlanked]
        # Make a list of identifiers of visible bodies
        body_identifiers = [body.JournalIdentifier for body in visible_bodies]
        # Initialize the bodies_to_hide list. Copy from visible body list.
        bodies_to_hide = visible_bodies[:]
    
        # Remove selected bodies from bodies_to_hide list
        number_of_object = theUI.SelectionManager.GetNumSelectedObjects()
        for i in range(number_of_object):
            # Get Body from selection
            object = theUI.SelectionManager.GetSelectedTaggedObject(i)
            if object in workPartFeatures:
                body_object = object.GetBodies()
                for body in body_object:
                    # Remove selected body
                    if body in bodies_to_hide:
                        bodies_to_hide.remove(body)
            elif object in workBodies:
                bodies_to_hide.remove(object)
            else:
                try:
                    body_object = object.GetBody()
                    # Remove selected body
                    if body_object in bodies_to_hide:
                        bodies_to_hide.remove(body_object)
                except:
                    return theUFSession.Ui.DisplayMessage("Select Bodies or Features or  or Faces or Edges Only.\nSelection in Assembly isn't Allowed.", 1)                   

        # Hide the Bodies in bodies_to_hide list
        theSession.DisplayManager.BlankObjects(bodies_to_hide)

        # Save the identifiers list in a json file
        contents = json.dumps(body_identifiers)
        location.write_text(contents)
        
    
if __name__ == '__main__':
    isolate_body()