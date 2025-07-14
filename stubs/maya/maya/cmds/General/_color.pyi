"""Stub files for General category in Maya commands, command: color."""

from typing import Any, overload

@overload #Overload for color in ['create']
def color([objects]: [objects], rgbColor: [float, float, float] = ..., userDefined: int = ...) -> None:
    """color is undoable, NOT queryable, and NOT editable.
    
    This command sets the dormant wireframe color of the specified objects to be
    their class color or if the -ud/userDefined flag is specified, one of the user
    defined colors. The -rgb/rgbColor flags can be specified if the user requires
    floating point RGB colors.

    ---
    - Args:
        - [objects]: Input item(s).
        - rgbColor (rgb): Specifies and rgb color to set the selected object to.
        - userDefined (ud): Specifies the user defined color index to set selected object to. The valid range of numbers is [1-8].
    """
@overload #Overload for color in ['create']
def color([objects]: [objects], rgb: [float, float, float] = ..., ud: int = ...) -> None:
    """color is undoable, NOT queryable, and NOT editable.
    
    This command sets the dormant wireframe color of the specified objects to be
    their class color or if the -ud/userDefined flag is specified, one of the user
    defined colors. The -rgb/rgbColor flags can be specified if the user requires
    floating point RGB colors.

    ---
    - Args:
        - [objects]: Input item(s).
        - rgbColor (rgb): Specifies and rgb color to set the selected object to.
        - userDefined (ud): Specifies the user defined color index to set selected object to. The valid range of numbers is [1-8].
    """
@overload #Overload for color in ['create']
def color([objects]: [objects], rgbColor: [float, float, float] = ..., rgb: [float, float, float] = ..., userDefined: int = ..., ud: int = ...) -> None:
    """color is undoable, NOT queryable, and NOT editable.
    
    This command sets the dormant wireframe color of the specified objects to be
    their class color or if the -ud/userDefined flag is specified, one of the user
    defined colors. The -rgb/rgbColor flags can be specified if the user requires
    floating point RGB colors.

    ---
    - Args:
        - [objects]: Input item(s).
        - rgbColor (rgb): Specifies and rgb color to set the selected object to.
        - userDefined (ud): Specifies the user defined color index to set selected object to. The valid range of numbers is [1-8].
    """
