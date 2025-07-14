"""Stub files for Display category in Maya commands, command: displayRGBColor."""

from typing import Any, overload

@overload #Overload for displayRGBColor in ['create']
def displayRGBColor(string: str, create: bool = ..., hueSaturationValue: bool = ..., list: bool = ..., resetToFactory: bool = ..., resetToSaved: bool = ...) -> str:
    """displayRGBColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. These colors are part of
    the UI and not part of the saved data for a model. This command is not
    undoable.

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

    ---
    - Args:
        - string: Input item(s).
        - alpha (a): Indicates that we want to query the alpha value of the color. Upon query, returns RGBA or HSVA as an array of 4 floats.
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        - query (q): Query mode flag
    """
@overload #Overload for displayRGBColor in ['edit']
def displayRGBColor(string: str, hueSaturationValue: bool = ..., edit: bool = ...) -> str:
    """displayRGBColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. These colors are part of
    the UI and not part of the saved data for a model. This command is not
    undoable.

    ---
    - Args:
        - string: Input item(s).
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        - edit (e): Edit mode flag
    """
@overload #Overload for displayRGBColor in ['edit']
def displayRGBColor(string: str, hsv: bool = ..., e: bool = ...) -> str:
    """displayRGBColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. These colors are part of
    the UI and not part of the saved data for a model. This command is not
    undoable.

    ---
    - Args:
        - string: Input item(s).
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        - edit (e): Edit mode flag
    """
@overload #Overload for displayRGBColor in ['edit']
def displayRGBColor(string: str, hueSaturationValue: bool = ..., hsv: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """displayRGBColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. These colors are part of
    the UI and not part of the saved data for a model. This command is not
    undoable.

    ---
    - Args:
        - string: Input item(s).
        - hueSaturationValue (hsv): Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        - edit (e): Edit mode flag
    """
