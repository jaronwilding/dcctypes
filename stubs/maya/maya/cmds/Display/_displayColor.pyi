"""Stub files for Display category in Maya commands, command: displayColor."""

from typing import Any, overload

@overload #Overload for displayColor in ['create']
def displayColor(string: str, active: bool = ..., create: bool = ..., dormant: bool = ..., list: bool = ..., queryIndex: int = ..., resetToFactory: bool = ..., resetToSaved: bool = ...) -> None:
    """displayColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. The color is defined by a
    color index into either the dormant or active color palette. These colors are
    part of the UI and not part of the saved data for a model. This command is not
    undoable.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.displayColor( 'grid', 15, dormant=True )
        cmds.displayColor( 'grid', q=True, dormant=True )
        cmds.displayColor( list=True )
        cmds.displayColor( resetToFactory=True )
        cmds.displayColor( queryIndex=15 )
    ```

    ---
    - Args:
        - string: Input item(s).
        - active (a): Specifies the color index applies to active color palette. name Specifies the name of color to change. index The color index for the color.
        - create (c): Creates a new display color which can be queried or set. If is used only when saving color preferences.
        - dormant (d): Specifies the color index applies to dormant color palette. If neither of the dormant or active flags is specified, dormant is the default.
        - list (l): Writes out a list of all color names and their value.
        - queryIndex (qi): Allows you to obtain a list of color names with the given color indices.
        - resetToFactory (rf): Resets all display colors to their factory defaults.
        - resetToSaved (rs): Resets all display colors to their saved values.
    """
@overload #Overload for displayColor in ['create']
def displayColor(string: str, a: bool = ..., c: bool = ..., d: bool = ..., l: bool = ..., qi: int = ..., rf: bool = ..., rs: bool = ...) -> None:
    """displayColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. The color is defined by a
    color index into either the dormant or active color palette. These colors are
    part of the UI and not part of the saved data for a model. This command is not
    undoable.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.displayColor( 'grid', 15, dormant=True )
        cmds.displayColor( 'grid', q=True, dormant=True )
        cmds.displayColor( list=True )
        cmds.displayColor( resetToFactory=True )
        cmds.displayColor( queryIndex=15 )
    ```

    ---
    - Args:
        - string: Input item(s).
        - active (a): Specifies the color index applies to active color palette. name Specifies the name of color to change. index The color index for the color.
        - create (c): Creates a new display color which can be queried or set. If is used only when saving color preferences.
        - dormant (d): Specifies the color index applies to dormant color palette. If neither of the dormant or active flags is specified, dormant is the default.
        - list (l): Writes out a list of all color names and their value.
        - queryIndex (qi): Allows you to obtain a list of color names with the given color indices.
        - resetToFactory (rf): Resets all display colors to their factory defaults.
        - resetToSaved (rs): Resets all display colors to their saved values.
    """
@overload #Overload for displayColor in ['create']
def displayColor(string: str, active: bool = ..., a: bool = ..., create: bool = ..., c: bool = ..., dormant: bool = ..., d: bool = ..., list: bool = ..., l: bool = ..., queryIndex: int = ..., qi: int = ..., resetToFactory: bool = ..., rf: bool = ..., resetToSaved: bool = ..., rs: bool = ...) -> None:
    """displayColor is undoable, queryable, and NOT editable.
    
    This command changes or queries the display color for anything in the
    application that allows the user to set its color. The color is defined by a
    color index into either the dormant or active color palette. These colors are
    part of the UI and not part of the saved data for a model. This command is not
    undoable.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.displayColor( 'grid', 15, dormant=True )
        cmds.displayColor( 'grid', q=True, dormant=True )
        cmds.displayColor( list=True )
        cmds.displayColor( resetToFactory=True )
        cmds.displayColor( queryIndex=15 )
    ```

    ---
    - Args:
        - string: Input item(s).
        - active (a): Specifies the color index applies to active color palette. name Specifies the name of color to change. index The color index for the color.
        - create (c): Creates a new display color which can be queried or set. If is used only when saving color preferences.
        - dormant (d): Specifies the color index applies to dormant color palette. If neither of the dormant or active flags is specified, dormant is the default.
        - list (l): Writes out a list of all color names and their value.
        - queryIndex (qi): Allows you to obtain a list of color names with the given color indices.
        - resetToFactory (rf): Resets all display colors to their factory defaults.
        - resetToSaved (rs): Resets all display colors to their saved values.
    """
