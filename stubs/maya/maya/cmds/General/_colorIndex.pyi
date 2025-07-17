"""Stub files for General category in Maya commands, command: colorIndex."""

from typing import Any, overload

@overload #Overload for colorIndex in ['create']
def colorIndex(int [float float float]: int [float float float], active: bool = ..., dormant: bool = ..., hueSaturationValue: bool = ..., resetToFactory: bool = ..., resetToSaved: bool = ..., userColor: bool = ...) -> int:
    """colorIndex is undoable, queryable, and NOT editable.
    
    The index specifies a color index in the color palette. The r, g, and b values
    (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is
    used) for the color.

    Example:
    ```python
        import maya.cmds as cmds
        # Set the first entry in the color palette to have RGB values 1 0 0 - red.
        cmds.colorIndex( 1, 1, 0, 0 )
        # Set the first entry in the color palette to have HSV values 360 1 1 - red.
        cmds.colorIndex( 1, 360, 0, 0, hsv=True )
        # Return the RGB color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True )
        # Return the HSV color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True, hsv=True )
    ```

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

    Example:
    ```python
        import maya.cmds as cmds
        # Set the first entry in the color palette to have RGB values 1 0 0 - red.
        cmds.colorIndex( 1, 1, 0, 0 )
        # Set the first entry in the color palette to have HSV values 360 1 1 - red.
        cmds.colorIndex( 1, 360, 0, 0, hsv=True )
        # Return the RGB color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True )
        # Return the HSV color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True, hsv=True )
    ```

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

    Example:
    ```python
        import maya.cmds as cmds
        # Set the first entry in the color palette to have RGB values 1 0 0 - red.
        cmds.colorIndex( 1, 1, 0, 0 )
        # Set the first entry in the color palette to have HSV values 360 1 1 - red.
        cmds.colorIndex( 1, 360, 0, 0, hsv=True )
        # Return the RGB color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True )
        # Return the HSV color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True, hsv=True )
    ```

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

    Example:
    ```python
        import maya.cmds as cmds
        # Set the first entry in the color palette to have RGB values 1 0 0 - red.
        cmds.colorIndex( 1, 1, 0, 0 )
        # Set the first entry in the color palette to have HSV values 360 1 1 - red.
        cmds.colorIndex( 1, 360, 0, 0, hsv=True )
        # Return the RGB color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True )
        # Return the HSV color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True, hsv=True )
    ```

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

    Example:
    ```python
        import maya.cmds as cmds
        # Set the first entry in the color palette to have RGB values 1 0 0 - red.
        cmds.colorIndex( 1, 1, 0, 0 )
        # Set the first entry in the color palette to have HSV values 360 1 1 - red.
        cmds.colorIndex( 1, 360, 0, 0, hsv=True )
        # Return the RGB color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True )
        # Return the HSV color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True, hsv=True )
    ```

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

    Example:
    ```python
        import maya.cmds as cmds
        # Set the first entry in the color palette to have RGB values 1 0 0 - red.
        cmds.colorIndex( 1, 1, 0, 0 )
        # Set the first entry in the color palette to have HSV values 360 1 1 - red.
        cmds.colorIndex( 1, 360, 0, 0, hsv=True )
        # Return the RGB color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True )
        # Return the HSV color values of the first entry of the color palette.
        cmds.colorIndex( 1, q=True, hsv=True )
    ```

    ---
    - Args:
        - int [float float float]: Input item(s).
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        - query (q): Query mode flag
    """
