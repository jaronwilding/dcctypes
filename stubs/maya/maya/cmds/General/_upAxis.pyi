"""Stub files for General category in Maya commands, command: upAxis."""

from typing import Any, overload

@overload #Overload for upAxis in ['create']
def upAxis(rotateView: bool = ...) -> None:
    """upAxis is undoable, queryable, and NOT editable.
    
    The upAxis command changes the world up direction. Current implementation
    provides only two choices of axis (the Y-axis or the Z-axis) as the world up
    direction.
    
    By default, the ground plane in Maya is on the XY plane. Hence, the default
    up-direction is the direction of the positive Z-axis.
    
    The -ax flag is mandatory. In conjunction with the -ax flag, when the -rv flag
    is specified, the camera of currently active view is revolved about the X-axis
    such that the position of the groundplane in the view will remain the same as
    before the the up direction is changed.
    
    The screen update is applied to all cameras of all views.

    Example:
    ```python
        import maya.cmds as cmds
        # 1. to make the Y-axis of the world to be the up axis:
        cmds.upAxis( ax='y' )
        # 2. to make the Z-axis of the world to be the up axis,
        # and rotate the view:
        cmds.upAxis( ax='z', rv=True )
        # 3. to query which axis is the current up axis
        # (returns a string: a "y" or a "z"):
        cmds.upAxis( q=True, axis=True )
    ```

    ---
    - Args:
        - rotateView (rv): This flag specifies to rotate the view as well.
    """
@overload #Overload for upAxis in ['create']
def upAxis(rv: bool = ...) -> None:
    """upAxis is undoable, queryable, and NOT editable.
    
    The upAxis command changes the world up direction. Current implementation
    provides only two choices of axis (the Y-axis or the Z-axis) as the world up
    direction.
    
    By default, the ground plane in Maya is on the XY plane. Hence, the default
    up-direction is the direction of the positive Z-axis.
    
    The -ax flag is mandatory. In conjunction with the -ax flag, when the -rv flag
    is specified, the camera of currently active view is revolved about the X-axis
    such that the position of the groundplane in the view will remain the same as
    before the the up direction is changed.
    
    The screen update is applied to all cameras of all views.

    Example:
    ```python
        import maya.cmds as cmds
        # 1. to make the Y-axis of the world to be the up axis:
        cmds.upAxis( ax='y' )
        # 2. to make the Z-axis of the world to be the up axis,
        # and rotate the view:
        cmds.upAxis( ax='z', rv=True )
        # 3. to query which axis is the current up axis
        # (returns a string: a "y" or a "z"):
        cmds.upAxis( q=True, axis=True )
    ```

    ---
    - Args:
        - rotateView (rv): This flag specifies to rotate the view as well.
    """
@overload #Overload for upAxis in ['create']
def upAxis(rotateView: bool = ..., rv: bool = ...) -> None:
    """upAxis is undoable, queryable, and NOT editable.
    
    The upAxis command changes the world up direction. Current implementation
    provides only two choices of axis (the Y-axis or the Z-axis) as the world up
    direction.
    
    By default, the ground plane in Maya is on the XY plane. Hence, the default
    up-direction is the direction of the positive Z-axis.
    
    The -ax flag is mandatory. In conjunction with the -ax flag, when the -rv flag
    is specified, the camera of currently active view is revolved about the X-axis
    such that the position of the groundplane in the view will remain the same as
    before the the up direction is changed.
    
    The screen update is applied to all cameras of all views.

    Example:
    ```python
        import maya.cmds as cmds
        # 1. to make the Y-axis of the world to be the up axis:
        cmds.upAxis( ax='y' )
        # 2. to make the Z-axis of the world to be the up axis,
        # and rotate the view:
        cmds.upAxis( ax='z', rv=True )
        # 3. to query which axis is the current up axis
        # (returns a string: a "y" or a "z"):
        cmds.upAxis( q=True, axis=True )
    ```

    ---
    - Args:
        - rotateView (rv): This flag specifies to rotate the view as well.
    """
@overload #Overload for upAxis in ['query']
def upAxis(axis: str = ..., query: bool = ...) -> None:
    """upAxis is undoable, queryable, and NOT editable.
    
    The upAxis command changes the world up direction. Current implementation
    provides only two choices of axis (the Y-axis or the Z-axis) as the world up
    direction.
    
    By default, the ground plane in Maya is on the XY plane. Hence, the default
    up-direction is the direction of the positive Z-axis.
    
    The -ax flag is mandatory. In conjunction with the -ax flag, when the -rv flag
    is specified, the camera of currently active view is revolved about the X-axis
    such that the position of the groundplane in the view will remain the same as
    before the the up direction is changed.
    
    The screen update is applied to all cameras of all views.

    Example:
    ```python
        import maya.cmds as cmds
        # 1. to make the Y-axis of the world to be the up axis:
        cmds.upAxis( ax='y' )
        # 2. to make the Z-axis of the world to be the up axis,
        # and rotate the view:
        cmds.upAxis( ax='z', rv=True )
        # 3. to query which axis is the current up axis
        # (returns a string: a "y" or a "z"):
        cmds.upAxis( q=True, axis=True )
    ```

    ---
    - Args:
        - axis (ax): This flag specifies the axis as the world up direction. The valid axis are either "y" or "z".When queried, it returns astring.
        - query (q): Query mode flag
    """
@overload #Overload for upAxis in ['query']
def upAxis(ax: str = ..., q: bool = ...) -> None:
    """upAxis is undoable, queryable, and NOT editable.
    
    The upAxis command changes the world up direction. Current implementation
    provides only two choices of axis (the Y-axis or the Z-axis) as the world up
    direction.
    
    By default, the ground plane in Maya is on the XY plane. Hence, the default
    up-direction is the direction of the positive Z-axis.
    
    The -ax flag is mandatory. In conjunction with the -ax flag, when the -rv flag
    is specified, the camera of currently active view is revolved about the X-axis
    such that the position of the groundplane in the view will remain the same as
    before the the up direction is changed.
    
    The screen update is applied to all cameras of all views.

    Example:
    ```python
        import maya.cmds as cmds
        # 1. to make the Y-axis of the world to be the up axis:
        cmds.upAxis( ax='y' )
        # 2. to make the Z-axis of the world to be the up axis,
        # and rotate the view:
        cmds.upAxis( ax='z', rv=True )
        # 3. to query which axis is the current up axis
        # (returns a string: a "y" or a "z"):
        cmds.upAxis( q=True, axis=True )
    ```

    ---
    - Args:
        - axis (ax): This flag specifies the axis as the world up direction. The valid axis are either "y" or "z".When queried, it returns astring.
        - query (q): Query mode flag
    """
@overload #Overload for upAxis in ['query']
def upAxis(axis: str = ..., ax: str = ..., query: bool = ..., q: bool = ...) -> None:
    """upAxis is undoable, queryable, and NOT editable.
    
    The upAxis command changes the world up direction. Current implementation
    provides only two choices of axis (the Y-axis or the Z-axis) as the world up
    direction.
    
    By default, the ground plane in Maya is on the XY plane. Hence, the default
    up-direction is the direction of the positive Z-axis.
    
    The -ax flag is mandatory. In conjunction with the -ax flag, when the -rv flag
    is specified, the camera of currently active view is revolved about the X-axis
    such that the position of the groundplane in the view will remain the same as
    before the the up direction is changed.
    
    The screen update is applied to all cameras of all views.

    Example:
    ```python
        import maya.cmds as cmds
        # 1. to make the Y-axis of the world to be the up axis:
        cmds.upAxis( ax='y' )
        # 2. to make the Z-axis of the world to be the up axis,
        # and rotate the view:
        cmds.upAxis( ax='z', rv=True )
        # 3. to query which axis is the current up axis
        # (returns a string: a "y" or a "z"):
        cmds.upAxis( q=True, axis=True )
    ```

    ---
    - Args:
        - axis (ax): This flag specifies the axis as the world up direction. The valid axis are either "y" or "z".When queried, it returns astring.
        - query (q): Query mode flag
    """
