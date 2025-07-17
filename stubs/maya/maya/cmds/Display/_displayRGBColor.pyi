"""Stub files for Display category in Maya commands, command: displayRGBColor."""

from typing import Any, overload

@overload #Overload for displayRGBColor in ['create']
def displayRGBColor(string: str, create: bool = ..., hueSaturationValue: bool = ..., list: bool = ..., resetToFactory: bool = ..., resetToSaved: bool = ...) -> str:
    """displayRGBColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. These colors are part of
    the UI and not part of the saved data for a model. This command is not
    undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set the background colour to red
        cmds.displayRGBColor( 'background', 1, 0, 0 )
        # List the current RGB color settings
        cmds.displayRGBColor( list=True )
        # Query a RGB color by name
        cmds.displayRGBColor("object", query=True)
        # Query the HSVA values of a color
        cmds.displayRGBColor("object", query=True, hsv=True, alpha=True)
    ```

    ---
    - Args:
        - string: Input item(s).
        - create (c): Creates a new RGB display color which can be queried or set. If is used only when saving color preferences. name Specifies the name of color to change.
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        - list (l): Writes out a list of all RGB color names and their value.
        - resetToFactory (rf): Resets all the RGB display colors to their factory defaults.
        - resetToSaved (rs): Resets all the RGB display colors to their saved values.
    """
@overload #Overload for displayRGBColor in ['create']
def displayRGBColor(string: str, c: bool = ..., hsv: bool = ..., l: bool = ..., rf: bool = ..., rs: bool = ...) -> str:
    """displayRGBColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. These colors are part of
    the UI and not part of the saved data for a model. This command is not
    undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set the background colour to red
        cmds.displayRGBColor( 'background', 1, 0, 0 )
        # List the current RGB color settings
        cmds.displayRGBColor( list=True )
        # Query a RGB color by name
        cmds.displayRGBColor("object", query=True)
        # Query the HSVA values of a color
        cmds.displayRGBColor("object", query=True, hsv=True, alpha=True)
    ```

    ---
    - Args:
        - string: Input item(s).
        - create (c): Creates a new RGB display color which can be queried or set. If is used only when saving color preferences. name Specifies the name of color to change.
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        - list (l): Writes out a list of all RGB color names and their value.
        - resetToFactory (rf): Resets all the RGB display colors to their factory defaults.
        - resetToSaved (rs): Resets all the RGB display colors to their saved values.
    """
@overload #Overload for displayRGBColor in ['create']
def displayRGBColor(string: str, create: bool = ..., c: bool = ..., hueSaturationValue: bool = ..., hsv: bool = ..., list: bool = ..., l: bool = ..., resetToFactory: bool = ..., rf: bool = ..., resetToSaved: bool = ..., rs: bool = ...) -> str:
    """displayRGBColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. These colors are part of
    the UI and not part of the saved data for a model. This command is not
    undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set the background colour to red
        cmds.displayRGBColor( 'background', 1, 0, 0 )
        # List the current RGB color settings
        cmds.displayRGBColor( list=True )
        # Query a RGB color by name
        cmds.displayRGBColor("object", query=True)
        # Query the HSVA values of a color
        cmds.displayRGBColor("object", query=True, hsv=True, alpha=True)
    ```

    ---
    - Args:
        - string: Input item(s).
        - create (c): Creates a new RGB display color which can be queried or set. If is used only when saving color preferences. name Specifies the name of color to change.
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        - list (l): Writes out a list of all RGB color names and their value.
        - resetToFactory (rf): Resets all the RGB display colors to their factory defaults.
        - resetToSaved (rs): Resets all the RGB display colors to their saved values.
    """
@overload #Overload for displayRGBColor in ['query']
def displayRGBColor(string: str, alpha: bool = ..., hueSaturationValue: bool = ..., query: bool = ...) -> str:
    """displayRGBColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. These colors are part of
    the UI and not part of the saved data for a model. This command is not
    undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set the background colour to red
        cmds.displayRGBColor( 'background', 1, 0, 0 )
        # List the current RGB color settings
        cmds.displayRGBColor( list=True )
        # Query a RGB color by name
        cmds.displayRGBColor("object", query=True)
        # Query the HSVA values of a color
        cmds.displayRGBColor("object", query=True, hsv=True, alpha=True)
    ```

    ---
    - Args:
        - string: Input item(s).
        - alpha (a): Indicates that we want to query the alpha value of the color. Upon query, returns RGBA or HSVA as an array of 4 floats.
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        - query (q): Query mode flag
    """
@overload #Overload for displayRGBColor in ['query']
def displayRGBColor(string: str, a: bool = ..., hsv: bool = ..., q: bool = ...) -> str:
    """displayRGBColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. These colors are part of
    the UI and not part of the saved data for a model. This command is not
    undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set the background colour to red
        cmds.displayRGBColor( 'background', 1, 0, 0 )
        # List the current RGB color settings
        cmds.displayRGBColor( list=True )
        # Query a RGB color by name
        cmds.displayRGBColor("object", query=True)
        # Query the HSVA values of a color
        cmds.displayRGBColor("object", query=True, hsv=True, alpha=True)
    ```

    ---
    - Args:
        - string: Input item(s).
        - alpha (a): Indicates that we want to query the alpha value of the color. Upon query, returns RGBA or HSVA as an array of 4 floats.
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        - query (q): Query mode flag
    """
@overload #Overload for displayRGBColor in ['query']
def displayRGBColor(string: str, alpha: bool = ..., a: bool = ..., hueSaturationValue: bool = ..., hsv: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """displayRGBColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. These colors are part of
    the UI and not part of the saved data for a model. This command is not
    undoable.

    Example:
    ```python
        import maya.cmds as cmds
        # Set the background colour to red
        cmds.displayRGBColor( 'background', 1, 0, 0 )
        # List the current RGB color settings
        cmds.displayRGBColor( list=True )
        # Query a RGB color by name
        cmds.displayRGBColor("object", query=True)
        # Query the HSVA values of a color
        cmds.displayRGBColor("object", query=True, hsv=True, alpha=True)
    ```

    ---
    - Args:
        - string: Input item(s).
        - alpha (a): Indicates that we want to query the alpha value of the color. Upon query, returns RGBA or HSVA as an array of 4 floats.
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        - query (q): Query mode flag
    """
