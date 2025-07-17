"""Stub files for Attributes category in Maya commands, command: inheritTransform."""

from typing import Any, overload

@overload #Overload for inheritTransform in ['create']
def inheritTransform([objects...]: [objects...], off: bool = ..., on: bool = ..., preserve: bool = ..., toggle: bool = ...) -> None:
    """inheritTransform is undoable, queryable, and NOT editable.
    
    This command toggles the inherit state of an object. If this flag is off the
    object will not inherit transformations from its parent. In other words
    transformations applied to the parent node will not affect the object and it
    will act as though it is under the world.
    
    If the -p flag is specified then the object's transformation will be modified
    to compensate when changing the inherit flag so the object will not change its
    world-space location.

    Example:
    ```python
        import maya.cmds as cmds
        # create an circle, move it off center, group it
        # and move the group so that the circle is back in center
        cmds.circle( nr=(0, 1, 0), n='circle1' )
        cmds.move( 2, 0, 0 )
        cmds.group()
        cmds.move( -2, 0, 0 )
        # turn off inherits transform flag of circle1.
        # The circle will now appear at (2, 0, 0)
        cmds.inheritTransform( 'circle1', off=True )
        # turn off inherits transform flag of circle1 but preserve the
        # position of the circle. The circle will stay centered at (0, 0, 0)
        cmds.inheritTransform( 'circle1', on=True )
        cmds.inheritTransform( 'circle1', off=True, preserve=True )
        # query state of inherits transform flag
        cmds.inheritTransform( 'circle1', q=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - off: turn off inherit state for the given object(s)
        - on: turn on inherit state for the given object(s)
        - preserve (p): preserve the objects world-space position by modifying the object(s) transformation matrix.
        - toggle (tgl): toggle the inherit state for the given object(s) (default if no flags are given) -on turn on inherit state for the given object(s) -off turn off inherit state for the given object(s)
    """
@overload #Overload for inheritTransform in ['create']
def inheritTransform([objects...]: [objects...], p: bool = ..., tgl: bool = ...) -> None:
    """inheritTransform is undoable, queryable, and NOT editable.
    
    This command toggles the inherit state of an object. If this flag is off the
    object will not inherit transformations from its parent. In other words
    transformations applied to the parent node will not affect the object and it
    will act as though it is under the world.
    
    If the -p flag is specified then the object's transformation will be modified
    to compensate when changing the inherit flag so the object will not change its
    world-space location.

    Example:
    ```python
        import maya.cmds as cmds
        # create an circle, move it off center, group it
        # and move the group so that the circle is back in center
        cmds.circle( nr=(0, 1, 0), n='circle1' )
        cmds.move( 2, 0, 0 )
        cmds.group()
        cmds.move( -2, 0, 0 )
        # turn off inherits transform flag of circle1.
        # The circle will now appear at (2, 0, 0)
        cmds.inheritTransform( 'circle1', off=True )
        # turn off inherits transform flag of circle1 but preserve the
        # position of the circle. The circle will stay centered at (0, 0, 0)
        cmds.inheritTransform( 'circle1', on=True )
        cmds.inheritTransform( 'circle1', off=True, preserve=True )
        # query state of inherits transform flag
        cmds.inheritTransform( 'circle1', q=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - off: turn off inherit state for the given object(s)
        - on: turn on inherit state for the given object(s)
        - preserve (p): preserve the objects world-space position by modifying the object(s) transformation matrix.
        - toggle (tgl): toggle the inherit state for the given object(s) (default if no flags are given) -on turn on inherit state for the given object(s) -off turn off inherit state for the given object(s)
    """
@overload #Overload for inheritTransform in ['create']
def inheritTransform([objects...]: [objects...], off: bool = ..., on: bool = ..., preserve: bool = ..., p: bool = ..., toggle: bool = ..., tgl: bool = ...) -> None:
    """inheritTransform is undoable, queryable, and NOT editable.
    
    This command toggles the inherit state of an object. If this flag is off the
    object will not inherit transformations from its parent. In other words
    transformations applied to the parent node will not affect the object and it
    will act as though it is under the world.
    
    If the -p flag is specified then the object's transformation will be modified
    to compensate when changing the inherit flag so the object will not change its
    world-space location.

    Example:
    ```python
        import maya.cmds as cmds
        # create an circle, move it off center, group it
        # and move the group so that the circle is back in center
        cmds.circle( nr=(0, 1, 0), n='circle1' )
        cmds.move( 2, 0, 0 )
        cmds.group()
        cmds.move( -2, 0, 0 )
        # turn off inherits transform flag of circle1.
        # The circle will now appear at (2, 0, 0)
        cmds.inheritTransform( 'circle1', off=True )
        # turn off inherits transform flag of circle1 but preserve the
        # position of the circle. The circle will stay centered at (0, 0, 0)
        cmds.inheritTransform( 'circle1', on=True )
        cmds.inheritTransform( 'circle1', off=True, preserve=True )
        # query state of inherits transform flag
        cmds.inheritTransform( 'circle1', q=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - off: turn off inherit state for the given object(s)
        - on: turn on inherit state for the given object(s)
        - preserve (p): preserve the objects world-space position by modifying the object(s) transformation matrix.
        - toggle (tgl): toggle the inherit state for the given object(s) (default if no flags are given) -on turn on inherit state for the given object(s) -off turn off inherit state for the given object(s)
    """
@overload #Overload for inheritTransform in ['query']
def inheritTransform([objects...]: [objects...], off: bool = ..., on: bool = ..., preserve: bool = ..., toggle: bool = ..., query: bool = ...) -> None:
    """inheritTransform is undoable, queryable, and NOT editable.
    
    This command toggles the inherit state of an object. If this flag is off the
    object will not inherit transformations from its parent. In other words
    transformations applied to the parent node will not affect the object and it
    will act as though it is under the world.
    
    If the -p flag is specified then the object's transformation will be modified
    to compensate when changing the inherit flag so the object will not change its
    world-space location.

    Example:
    ```python
        import maya.cmds as cmds
        # create an circle, move it off center, group it
        # and move the group so that the circle is back in center
        cmds.circle( nr=(0, 1, 0), n='circle1' )
        cmds.move( 2, 0, 0 )
        cmds.group()
        cmds.move( -2, 0, 0 )
        # turn off inherits transform flag of circle1.
        # The circle will now appear at (2, 0, 0)
        cmds.inheritTransform( 'circle1', off=True )
        # turn off inherits transform flag of circle1 but preserve the
        # position of the circle. The circle will stay centered at (0, 0, 0)
        cmds.inheritTransform( 'circle1', on=True )
        cmds.inheritTransform( 'circle1', off=True, preserve=True )
        # query state of inherits transform flag
        cmds.inheritTransform( 'circle1', q=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - off: turn off inherit state for the given object(s)
        - on: turn on inherit state for the given object(s)
        - preserve (p): preserve the objects world-space position by modifying the object(s) transformation matrix.
        - toggle (tgl): toggle the inherit state for the given object(s) (default if no flags are given) -on turn on inherit state for the given object(s) -off turn off inherit state for the given object(s)
        - query (q): Query mode flag
    """
@overload #Overload for inheritTransform in ['query']
def inheritTransform([objects...]: [objects...], p: bool = ..., tgl: bool = ..., q: bool = ...) -> None:
    """inheritTransform is undoable, queryable, and NOT editable.
    
    This command toggles the inherit state of an object. If this flag is off the
    object will not inherit transformations from its parent. In other words
    transformations applied to the parent node will not affect the object and it
    will act as though it is under the world.
    
    If the -p flag is specified then the object's transformation will be modified
    to compensate when changing the inherit flag so the object will not change its
    world-space location.

    Example:
    ```python
        import maya.cmds as cmds
        # create an circle, move it off center, group it
        # and move the group so that the circle is back in center
        cmds.circle( nr=(0, 1, 0), n='circle1' )
        cmds.move( 2, 0, 0 )
        cmds.group()
        cmds.move( -2, 0, 0 )
        # turn off inherits transform flag of circle1.
        # The circle will now appear at (2, 0, 0)
        cmds.inheritTransform( 'circle1', off=True )
        # turn off inherits transform flag of circle1 but preserve the
        # position of the circle. The circle will stay centered at (0, 0, 0)
        cmds.inheritTransform( 'circle1', on=True )
        cmds.inheritTransform( 'circle1', off=True, preserve=True )
        # query state of inherits transform flag
        cmds.inheritTransform( 'circle1', q=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - off: turn off inherit state for the given object(s)
        - on: turn on inherit state for the given object(s)
        - preserve (p): preserve the objects world-space position by modifying the object(s) transformation matrix.
        - toggle (tgl): toggle the inherit state for the given object(s) (default if no flags are given) -on turn on inherit state for the given object(s) -off turn off inherit state for the given object(s)
        - query (q): Query mode flag
    """
@overload #Overload for inheritTransform in ['query']
def inheritTransform([objects...]: [objects...], off: bool = ..., on: bool = ..., preserve: bool = ..., p: bool = ..., toggle: bool = ..., tgl: bool = ..., query: bool = ..., q: bool = ...) -> None:
    """inheritTransform is undoable, queryable, and NOT editable.
    
    This command toggles the inherit state of an object. If this flag is off the
    object will not inherit transformations from its parent. In other words
    transformations applied to the parent node will not affect the object and it
    will act as though it is under the world.
    
    If the -p flag is specified then the object's transformation will be modified
    to compensate when changing the inherit flag so the object will not change its
    world-space location.

    Example:
    ```python
        import maya.cmds as cmds
        # create an circle, move it off center, group it
        # and move the group so that the circle is back in center
        cmds.circle( nr=(0, 1, 0), n='circle1' )
        cmds.move( 2, 0, 0 )
        cmds.group()
        cmds.move( -2, 0, 0 )
        # turn off inherits transform flag of circle1.
        # The circle will now appear at (2, 0, 0)
        cmds.inheritTransform( 'circle1', off=True )
        # turn off inherits transform flag of circle1 but preserve the
        # position of the circle. The circle will stay centered at (0, 0, 0)
        cmds.inheritTransform( 'circle1', on=True )
        cmds.inheritTransform( 'circle1', off=True, preserve=True )
        # query state of inherits transform flag
        cmds.inheritTransform( 'circle1', q=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - off: turn off inherit state for the given object(s)
        - on: turn on inherit state for the given object(s)
        - preserve (p): preserve the objects world-space position by modifying the object(s) transformation matrix.
        - toggle (tgl): toggle the inherit state for the given object(s) (default if no flags are given) -on turn on inherit state for the given object(s) -off turn off inherit state for the given object(s)
        - query (q): Query mode flag
    """
