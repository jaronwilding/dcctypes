"""Stub files for Display category in Maya commands, command: curveRGBColor."""

from typing import Any, overload

@overload #Overload for curveRGBColor in ['create']
def curveRGBColor(hueSaturationValue: bool = ..., list: bool = ..., listNames: bool = ..., remove: bool = ..., resetToFactory: bool = ..., resetToSaved: bool = ...) -> float[]:
    """curveRGBColor is undoable, queryable, and NOT editable.
    
    This command creates, changes or removes custom curve colors, which are used
    to draw the curves in the Graph Editor. The custom curve names may contain the
    wildcards "?", which marches a single character, and "*", which matches any
    number of characters. These colors are part of the UI and not part of the
    saved data for a model. This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set all "translateX" curves to draw magenta
        cmds.curveRGBColor( 'translateX', 1, 0, 1 )
        # Set all curves whose names end in "Y" to draw yellow
        cmds.curveRGBColor( '*Y', 1, 1, 0 )
        # Remove the custom color for "translateX" curves
        # (which will revert to the standard UI color)
        cmds.curveRGBColor( r=True, 'translateX' )
        # List the currently defined custom curve colors
        cmds.curveRGBColor( list=True )
    ```

    ---
    - Args:
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values.
        - list (l): Writes out a list of all curve color names and their values.
        - listNames (ln): Returns an array of all curve color names.
        - remove (r): Removes the named curve color.
        - resetToFactory (rf): Resets all the curve colors to their factory defaults.
        - resetToSaved (rs): Resets all the curve colors to their saved values.
    """
@overload #Overload for curveRGBColor in ['create']
def curveRGBColor(hsv: bool = ..., l: bool = ..., ln: bool = ..., r: bool = ..., rf: bool = ..., rs: bool = ...) -> float[]:
    """curveRGBColor is undoable, queryable, and NOT editable.
    
    This command creates, changes or removes custom curve colors, which are used
    to draw the curves in the Graph Editor. The custom curve names may contain the
    wildcards "?", which marches a single character, and "*", which matches any
    number of characters. These colors are part of the UI and not part of the
    saved data for a model. This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set all "translateX" curves to draw magenta
        cmds.curveRGBColor( 'translateX', 1, 0, 1 )
        # Set all curves whose names end in "Y" to draw yellow
        cmds.curveRGBColor( '*Y', 1, 1, 0 )
        # Remove the custom color for "translateX" curves
        # (which will revert to the standard UI color)
        cmds.curveRGBColor( r=True, 'translateX' )
        # List the currently defined custom curve colors
        cmds.curveRGBColor( list=True )
    ```

    ---
    - Args:
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values.
        - list (l): Writes out a list of all curve color names and their values.
        - listNames (ln): Returns an array of all curve color names.
        - remove (r): Removes the named curve color.
        - resetToFactory (rf): Resets all the curve colors to their factory defaults.
        - resetToSaved (rs): Resets all the curve colors to their saved values.
    """
@overload #Overload for curveRGBColor in ['create']
def curveRGBColor(hueSaturationValue: bool = ..., hsv: bool = ..., list: bool = ..., l: bool = ..., listNames: bool = ..., ln: bool = ..., remove: bool = ..., r: bool = ..., resetToFactory: bool = ..., rf: bool = ..., resetToSaved: bool = ..., rs: bool = ...) -> float[]:
    """curveRGBColor is undoable, queryable, and NOT editable.
    
    This command creates, changes or removes custom curve colors, which are used
    to draw the curves in the Graph Editor. The custom curve names may contain the
    wildcards "?", which marches a single character, and "*", which matches any
    number of characters. These colors are part of the UI and not part of the
    saved data for a model. This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set all "translateX" curves to draw magenta
        cmds.curveRGBColor( 'translateX', 1, 0, 1 )
        # Set all curves whose names end in "Y" to draw yellow
        cmds.curveRGBColor( '*Y', 1, 1, 0 )
        # Remove the custom color for "translateX" curves
        # (which will revert to the standard UI color)
        cmds.curveRGBColor( r=True, 'translateX' )
        # List the currently defined custom curve colors
        cmds.curveRGBColor( list=True )
    ```

    ---
    - Args:
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values.
        - list (l): Writes out a list of all curve color names and their values.
        - listNames (ln): Returns an array of all curve color names.
        - remove (r): Removes the named curve color.
        - resetToFactory (rf): Resets all the curve colors to their factory defaults.
        - resetToSaved (rs): Resets all the curve colors to their saved values.
    """
@overload #Overload for curveRGBColor in ['query']
def curveRGBColor(hueSaturationValue: bool = ..., query: bool = ...) -> float[]:
    """curveRGBColor is undoable, queryable, and NOT editable.
    
    This command creates, changes or removes custom curve colors, which are used
    to draw the curves in the Graph Editor. The custom curve names may contain the
    wildcards "?", which marches a single character, and "*", which matches any
    number of characters. These colors are part of the UI and not part of the
    saved data for a model. This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set all "translateX" curves to draw magenta
        cmds.curveRGBColor( 'translateX', 1, 0, 1 )
        # Set all curves whose names end in "Y" to draw yellow
        cmds.curveRGBColor( '*Y', 1, 1, 0 )
        # Remove the custom color for "translateX" curves
        # (which will revert to the standard UI color)
        cmds.curveRGBColor( r=True, 'translateX' )
        # List the currently defined custom curve colors
        cmds.curveRGBColor( list=True )
    ```

    ---
    - Args:
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values.
        - query (q): Query mode flag
    """
@overload #Overload for curveRGBColor in ['query']
def curveRGBColor(hsv: bool = ..., q: bool = ...) -> float[]:
    """curveRGBColor is undoable, queryable, and NOT editable.
    
    This command creates, changes or removes custom curve colors, which are used
    to draw the curves in the Graph Editor. The custom curve names may contain the
    wildcards "?", which marches a single character, and "*", which matches any
    number of characters. These colors are part of the UI and not part of the
    saved data for a model. This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set all "translateX" curves to draw magenta
        cmds.curveRGBColor( 'translateX', 1, 0, 1 )
        # Set all curves whose names end in "Y" to draw yellow
        cmds.curveRGBColor( '*Y', 1, 1, 0 )
        # Remove the custom color for "translateX" curves
        # (which will revert to the standard UI color)
        cmds.curveRGBColor( r=True, 'translateX' )
        # List the currently defined custom curve colors
        cmds.curveRGBColor( list=True )
    ```

    ---
    - Args:
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values.
        - query (q): Query mode flag
    """
@overload #Overload for curveRGBColor in ['query']
def curveRGBColor(hueSaturationValue: bool = ..., hsv: bool = ..., query: bool = ..., q: bool = ...) -> float[]:
    """curveRGBColor is undoable, queryable, and NOT editable.
    
    This command creates, changes or removes custom curve colors, which are used
    to draw the curves in the Graph Editor. The custom curve names may contain the
    wildcards "?", which marches a single character, and "*", which matches any
    number of characters. These colors are part of the UI and not part of the
    saved data for a model. This command is not undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set all "translateX" curves to draw magenta
        cmds.curveRGBColor( 'translateX', 1, 0, 1 )
        # Set all curves whose names end in "Y" to draw yellow
        cmds.curveRGBColor( '*Y', 1, 1, 0 )
        # Remove the custom color for "translateX" curves
        # (which will revert to the standard UI color)
        cmds.curveRGBColor( r=True, 'translateX' )
        # List the currently defined custom curve colors
        cmds.curveRGBColor( list=True )
    ```

    ---
    - Args:
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values.
        - query (q): Query mode flag
    """
