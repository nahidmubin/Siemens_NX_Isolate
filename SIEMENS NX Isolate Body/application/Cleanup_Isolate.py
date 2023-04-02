# This file is a part of the program called "Isolate Body" for SIEMENS NX.
# Version 1.0.0
# Created by Nahid Mubin

import NXOpen
from pathlib import Path
import json

# Get the Current Session
theSession  = NXOpen.Session.GetSession()
# Get the Work Part.
workPart = theSession.Parts.Work

def clean_up_isolate(): 

    # Check for active work part.
    if workPart is None:
        return

    # Get the Work Part name, Work Part UID and bodies in the Work Part.
    workPartName = workPart.Name
    workPartUID = workPart.UniqueIdentifier
    workBodies = workPart.Bodies
    # Define the path
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
        
    
if __name__ == '__main__' and workPart is not None:
    clean_up_isolate()