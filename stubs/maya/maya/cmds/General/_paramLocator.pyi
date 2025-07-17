"""Stub files for General category in Maya commands, command: paramLocator."""

from typing import Any, overload

@overload #Overload for paramLocator in ['create']
def paramLocator([object]: [object], position: bool = ...) -> str:
    """paramLocator is undoable, queryable, and editable.
    
    The command creates a locator in the underworld of a NURBS curve or NURBS
    surface at the specified parameter value. If no object is specified, then a
    locator will be created on the first valid selected item (either a curve point
    or a surface point).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a locator on curve1 at parameter value 0.5.
        cmds.paramLocator( 'curve1.u[0.5]' )
        # Creates a locator on curve1 at its second edit point. (ep[0] is the 1st edit point).
        cmds.paramLocator( 'curve1.ep[1]' )
        # Creates a locator on curve1 at normalized parameter value 0.25.
        cmds.paramLocator( 'curve1.un[0.25]' )
        # Creates a locator on surface1 at parameter value (0.5,0.5).
        cmds.paramLocator( 'surface1.uv[0.5][0.5]' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - position (p): Whether to set the locator position in normalized space.
    """
@overload #Overload for paramLocator in ['create']
def paramLocator([object]: [object], p: bool = ...) -> str:
    """paramLocator is undoable, queryable, and editable.
    
    The command creates a locator in the underworld of a NURBS curve or NURBS
    surface at the specified parameter value. If no object is specified, then a
    locator will be created on the first valid selected item (either a curve point
    or a surface point).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a locator on curve1 at parameter value 0.5.
        cmds.paramLocator( 'curve1.u[0.5]' )
        # Creates a locator on curve1 at its second edit point. (ep[0] is the 1st edit point).
        cmds.paramLocator( 'curve1.ep[1]' )
        # Creates a locator on curve1 at normalized parameter value 0.25.
        cmds.paramLocator( 'curve1.un[0.25]' )
        # Creates a locator on surface1 at parameter value (0.5,0.5).
        cmds.paramLocator( 'surface1.uv[0.5][0.5]' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - position (p): Whether to set the locator position in normalized space.
    """
@overload #Overload for paramLocator in ['create']
def paramLocator([object]: [object], position: bool = ..., p: bool = ...) -> str:
    """paramLocator is undoable, queryable, and editable.
    
    The command creates a locator in the underworld of a NURBS curve or NURBS
    surface at the specified parameter value. If no object is specified, then a
    locator will be created on the first valid selected item (either a curve point
    or a surface point).

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a locator on curve1 at parameter value 0.5.
        cmds.paramLocator( 'curve1.u[0.5]' )
        # Creates a locator on curve1 at its second edit point. (ep[0] is the 1st edit point).
        cmds.paramLocator( 'curve1.ep[1]' )
        # Creates a locator on curve1 at normalized parameter value 0.25.
        cmds.paramLocator( 'curve1.un[0.25]' )
        # Creates a locator on surface1 at parameter value (0.5,0.5).
        cmds.paramLocator( 'surface1.uv[0.5][0.5]' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - position (p): Whether to set the locator position in normalized space.
    """
