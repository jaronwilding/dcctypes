"""Stub files for General category in Maya commands, command: toggleAxis."""

from typing import Any, overload

@overload #Overload for toggleAxis in ['create']
def toggleAxis(origin: bool = ..., view: bool = ...) -> bool:
    """toggleAxis is undoable, queryable, and NOT editable.
    
    Toggles the state of the display axis.
    
    Note: the display of the axis in the bottom left corner has been rendered
    obsolete by the headsUpDisplay command.

    Example:
    ```python
        import maya.cmds as cmds
        # Turns origin axis on
        cmds.toggleAxis( o=True )
        # Turns origin axis off.
        cmds.toggleAxis( o=False )
        # Returns true if the axis at the origin is on.
        cmds.toggleAxis( q=True, o=True )
        # Toggles the display of the axis
        cmds.toggleAxis()
    ```

    ---
    - Args:
        - origin (o): Turns display of the axis at the origin of the ground plane on or off.
        - view (v): Turns display of the axis at the bottom left of each view on or off. (Obsolete - refer to the headsUpDisplay command)
    """
@overload #Overload for toggleAxis in ['create']
def toggleAxis(o: bool = ..., v: bool = ...) -> bool:
    """toggleAxis is undoable, queryable, and NOT editable.
    
    Toggles the state of the display axis.
    
    Note: the display of the axis in the bottom left corner has been rendered
    obsolete by the headsUpDisplay command.

    Example:
    ```python
        import maya.cmds as cmds
        # Turns origin axis on
        cmds.toggleAxis( o=True )
        # Turns origin axis off.
        cmds.toggleAxis( o=False )
        # Returns true if the axis at the origin is on.
        cmds.toggleAxis( q=True, o=True )
        # Toggles the display of the axis
        cmds.toggleAxis()
    ```

    ---
    - Args:
        - origin (o): Turns display of the axis at the origin of the ground plane on or off.
        - view (v): Turns display of the axis at the bottom left of each view on or off. (Obsolete - refer to the headsUpDisplay command)
    """
@overload #Overload for toggleAxis in ['create']
def toggleAxis(origin: bool = ..., o: bool = ..., view: bool = ..., v: bool = ...) -> bool:
    """toggleAxis is undoable, queryable, and NOT editable.
    
    Toggles the state of the display axis.
    
    Note: the display of the axis in the bottom left corner has been rendered
    obsolete by the headsUpDisplay command.

    Example:
    ```python
        import maya.cmds as cmds
        # Turns origin axis on
        cmds.toggleAxis( o=True )
        # Turns origin axis off.
        cmds.toggleAxis( o=False )
        # Returns true if the axis at the origin is on.
        cmds.toggleAxis( q=True, o=True )
        # Toggles the display of the axis
        cmds.toggleAxis()
    ```

    ---
    - Args:
        - origin (o): Turns display of the axis at the origin of the ground plane on or off.
        - view (v): Turns display of the axis at the bottom left of each view on or off. (Obsolete - refer to the headsUpDisplay command)
    """
@overload #Overload for toggleAxis in ['query']
def toggleAxis(origin: bool = ..., view: bool = ..., query: bool = ...) -> bool:
    """toggleAxis is undoable, queryable, and NOT editable.
    
    Toggles the state of the display axis.
    
    Note: the display of the axis in the bottom left corner has been rendered
    obsolete by the headsUpDisplay command.

    Example:
    ```python
        import maya.cmds as cmds
        # Turns origin axis on
        cmds.toggleAxis( o=True )
        # Turns origin axis off.
        cmds.toggleAxis( o=False )
        # Returns true if the axis at the origin is on.
        cmds.toggleAxis( q=True, o=True )
        # Toggles the display of the axis
        cmds.toggleAxis()
    ```

    ---
    - Args:
        - origin (o): Turns display of the axis at the origin of the ground plane on or off.
        - view (v): Turns display of the axis at the bottom left of each view on or off. (Obsolete - refer to the headsUpDisplay command)
        - query (q): Query mode flag
    """
@overload #Overload for toggleAxis in ['query']
def toggleAxis(o: bool = ..., v: bool = ..., q: bool = ...) -> bool:
    """toggleAxis is undoable, queryable, and NOT editable.
    
    Toggles the state of the display axis.
    
    Note: the display of the axis in the bottom left corner has been rendered
    obsolete by the headsUpDisplay command.

    Example:
    ```python
        import maya.cmds as cmds
        # Turns origin axis on
        cmds.toggleAxis( o=True )
        # Turns origin axis off.
        cmds.toggleAxis( o=False )
        # Returns true if the axis at the origin is on.
        cmds.toggleAxis( q=True, o=True )
        # Toggles the display of the axis
        cmds.toggleAxis()
    ```

    ---
    - Args:
        - origin (o): Turns display of the axis at the origin of the ground plane on or off.
        - view (v): Turns display of the axis at the bottom left of each view on or off. (Obsolete - refer to the headsUpDisplay command)
        - query (q): Query mode flag
    """
@overload #Overload for toggleAxis in ['query']
def toggleAxis(origin: bool = ..., o: bool = ..., view: bool = ..., v: bool = ..., query: bool = ..., q: bool = ...) -> bool:
    """toggleAxis is undoable, queryable, and NOT editable.
    
    Toggles the state of the display axis.
    
    Note: the display of the axis in the bottom left corner has been rendered
    obsolete by the headsUpDisplay command.

    Example:
    ```python
        import maya.cmds as cmds
        # Turns origin axis on
        cmds.toggleAxis( o=True )
        # Turns origin axis off.
        cmds.toggleAxis( o=False )
        # Returns true if the axis at the origin is on.
        cmds.toggleAxis( q=True, o=True )
        # Toggles the display of the axis
        cmds.toggleAxis()
    ```

    ---
    - Args:
        - origin (o): Turns display of the axis at the origin of the ground plane on or off.
        - view (v): Turns display of the axis at the bottom left of each view on or off. (Obsolete - refer to the headsUpDisplay command)
        - query (q): Query mode flag
    """
