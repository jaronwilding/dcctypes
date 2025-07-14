"""Stub files for General category in Maya commands, command: colorIndex."""

from typing import Any, overload

@overload #Overload for colorIndex in ['create']
def colorIndex(int [float float float]: int [float float float], active: bool = ..., dormant: bool = ..., hueSaturationValue: bool = ..., resetToFactory: bool = ..., resetToSaved: bool = ..., userColor: bool = ...) -> int:
    """colorIndex is undoable, queryable, and NOT editable.
    
    The index specifies a color index in the color palette. The r, g, and b values
    (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is
    used) for the color.

    ---
    - Args:
        - int [float float float]: Input item(s).
        - active (atv): Combined with query mode, with given index, query the active color palette.
        - dormant (dor): Combined with query mode, with given index, query the dormant color palette.
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        - resetToFactory (rf): Resets all color index palette entries to their factory defaults.
        - resetToSaved (rs): Resets all color palette entries to their saved values.
        - userColor (uc): Combined with query mode, with given index, query the user color palette.
    """
@overload #Overload for colorIndex in ['create']
def colorIndex(int [float float float]: int [float float float], atv: bool = ..., dor: bool = ..., hsv: bool = ..., rf: bool = ..., rs: bool = ..., uc: bool = ...) -> int:
    """colorIndex is undoable, queryable, and NOT editable.
    
    The index specifies a color index in the color palette. The r, g, and b values
    (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is
    used) for the color.

    ---
    - Args:
        - int [float float float]: Input item(s).
        - active (atv): Combined with query mode, with given index, query the active color palette.
        - dormant (dor): Combined with query mode, with given index, query the dormant color palette.
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        - resetToFactory (rf): Resets all color index palette entries to their factory defaults.
        - resetToSaved (rs): Resets all color palette entries to their saved values.
        - userColor (uc): Combined with query mode, with given index, query the user color palette.
    """
@overload #Overload for colorIndex in ['create']
def colorIndex(int [float float float]: int [float float float], active: bool = ..., atv: bool = ..., dormant: bool = ..., dor: bool = ..., hueSaturationValue: bool = ..., hsv: bool = ..., resetToFactory: bool = ..., rf: bool = ..., resetToSaved: bool = ..., rs: bool = ..., userColor: bool = ..., uc: bool = ...) -> int:
    """colorIndex is undoable, queryable, and NOT editable.
    
    The index specifies a color index in the color palette. The r, g, and b values
    (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is
    used) for the color.

    ---
    - Args:
        - int [float float float]: Input item(s).
        - active (atv): Combined with query mode, with given index, query the active color palette.
        - dormant (dor): Combined with query mode, with given index, query the dormant color palette.
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        - resetToFactory (rf): Resets all color index palette entries to their factory defaults.
        - resetToSaved (rs): Resets all color palette entries to their saved values.
        - userColor (uc): Combined with query mode, with given index, query the user color palette.
    """
@overload #Overload for colorIndex in ['query']
def colorIndex(int [float float float]: int [float float float], hueSaturationValue: bool = ..., query: bool = ...) -> int:
    """colorIndex is undoable, queryable, and NOT editable.
    
    The index specifies a color index in the color palette. The r, g, and b values
    (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is
    used) for the color.

    ---
    - Args:
        - int [float float float]: Input item(s).
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        - query (q): Query mode flag
    """
@overload #Overload for colorIndex in ['query']
def colorIndex(int [float float float]: int [float float float], hsv: bool = ..., q: bool = ...) -> int:
    """colorIndex is undoable, queryable, and NOT editable.
    
    The index specifies a color index in the color palette. The r, g, and b values
    (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is
    used) for the color.

    ---
    - Args:
        - int [float float float]: Input item(s).
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        - query (q): Query mode flag
    """
@overload #Overload for colorIndex in ['query']
def colorIndex(int [float float float]: int [float float float], hueSaturationValue: bool = ..., hsv: bool = ..., query: bool = ..., q: bool = ...) -> int:
    """colorIndex is undoable, queryable, and NOT editable.
    
    The index specifies a color index in the color palette. The r, g, and b values
    (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is
    used) for the color.

    ---
    - Args:
        - int [float float float]: Input item(s).
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        - query (q): Query mode flag
    """
@overload #Overload for colorIndex in ['edit']
def colorIndex(int [float float float]: int [float float float], hueSaturationValue: bool = ..., edit: bool = ...) -> int:
    """colorIndex is undoable, queryable, and NOT editable.
    
    The index specifies a color index in the color palette. The r, g, and b values
    (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is
    used) for the color.

    ---
    - Args:
        - int [float float float]: Input item(s).
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        - edit (e): Edit mode flag
    """
@overload #Overload for colorIndex in ['edit']
def colorIndex(int [float float float]: int [float float float], hsv: bool = ..., e: bool = ...) -> int:
    """colorIndex is undoable, queryable, and NOT editable.
    
    The index specifies a color index in the color palette. The r, g, and b values
    (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is
    used) for the color.

    ---
    - Args:
        - int [float float float]: Input item(s).
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        - edit (e): Edit mode flag
    """
@overload #Overload for colorIndex in ['edit']
def colorIndex(int [float float float]: int [float float float], hueSaturationValue: bool = ..., hsv: bool = ..., edit: bool = ..., e: bool = ...) -> int:
    """colorIndex is undoable, queryable, and NOT editable.
    
    The index specifies a color index in the color palette. The r, g, and b values
    (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is
    used) for the color.

    ---
    - Args:
        - int [float float float]: Input item(s).
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        - edit (e): Edit mode flag
    """
