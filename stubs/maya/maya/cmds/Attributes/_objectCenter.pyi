"""Stub files for Attributes category in Maya commands, command: objectCenter."""

from typing import Any, overload

@overload #Overload for objectCenter in ['create']
def objectCenter(object: object, gl: bool = ..., local: bool = ..., x: bool = ..., y: bool = ..., z: bool = ...) -> float[] | float:
    """objectCenter is undoable, NOT queryable, and NOT editable.
    
    This command returns the coordinates of the center of the bounding box of the
    specified object. If one coordinate only is specified, it will be returned as
    a float. If no coordinates are specified, an array of floats is returned,
    containing x, y, and z. If you specify multiple coordinates, only one will be
    returned.

    Example:
    ```python
        import maya.cmds as cmds
        # create a simple hierarchy
        cmds.polyCube( name='a' )
        cmds.polyCube( name='b' )
        cmds.parent( 'b', 'a' )
        cmds.move( 3, 0, 0, 'a', localSpace=True )
        cmds.move( 2, 2, 2, 'b', localSpace=True )
        X_COORD = cmds.objectCenter('b',x=True)
        # Result: 5 #
        # Get the center of the bounding box of b in local space
        XYZ = cmds.objectCenter('b', l=True)
        # Result: 2 2 2 #
        # Get the center of the bounding box of b in world space
        XYZ = cmds.objectCenter('b', gl=True)
        # Result: 5 2 2 #
        # Get the center of the bounding box of a in world space
        XYZ = cmds.objectCenter('a', gl=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - gl: Return positional values in global coordinates (default).
        - local (l): Return positional values in local coordinates.
        - x: Return X value only
        - y: Return Y value only
        - z: Return Z value only
    """
@overload #Overload for objectCenter in ['create']
def objectCenter(object: object, l: bool = ...) -> float[] | float:
    """objectCenter is undoable, NOT queryable, and NOT editable.
    
    This command returns the coordinates of the center of the bounding box of the
    specified object. If one coordinate only is specified, it will be returned as
    a float. If no coordinates are specified, an array of floats is returned,
    containing x, y, and z. If you specify multiple coordinates, only one will be
    returned.

    Example:
    ```python
        import maya.cmds as cmds
        # create a simple hierarchy
        cmds.polyCube( name='a' )
        cmds.polyCube( name='b' )
        cmds.parent( 'b', 'a' )
        cmds.move( 3, 0, 0, 'a', localSpace=True )
        cmds.move( 2, 2, 2, 'b', localSpace=True )
        X_COORD = cmds.objectCenter('b',x=True)
        # Result: 5 #
        # Get the center of the bounding box of b in local space
        XYZ = cmds.objectCenter('b', l=True)
        # Result: 2 2 2 #
        # Get the center of the bounding box of b in world space
        XYZ = cmds.objectCenter('b', gl=True)
        # Result: 5 2 2 #
        # Get the center of the bounding box of a in world space
        XYZ = cmds.objectCenter('a', gl=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - gl: Return positional values in global coordinates (default).
        - local (l): Return positional values in local coordinates.
        - x: Return X value only
        - y: Return Y value only
        - z: Return Z value only
    """
@overload #Overload for objectCenter in ['create']
def objectCenter(object: object, gl: bool = ..., local: bool = ..., l: bool = ..., x: bool = ..., y: bool = ..., z: bool = ...) -> float[] | float:
    """objectCenter is undoable, NOT queryable, and NOT editable.
    
    This command returns the coordinates of the center of the bounding box of the
    specified object. If one coordinate only is specified, it will be returned as
    a float. If no coordinates are specified, an array of floats is returned,
    containing x, y, and z. If you specify multiple coordinates, only one will be
    returned.

    Example:
    ```python
        import maya.cmds as cmds
        # create a simple hierarchy
        cmds.polyCube( name='a' )
        cmds.polyCube( name='b' )
        cmds.parent( 'b', 'a' )
        cmds.move( 3, 0, 0, 'a', localSpace=True )
        cmds.move( 2, 2, 2, 'b', localSpace=True )
        X_COORD = cmds.objectCenter('b',x=True)
        # Result: 5 #
        # Get the center of the bounding box of b in local space
        XYZ = cmds.objectCenter('b', l=True)
        # Result: 2 2 2 #
        # Get the center of the bounding box of b in world space
        XYZ = cmds.objectCenter('b', gl=True)
        # Result: 5 2 2 #
        # Get the center of the bounding box of a in world space
        XYZ = cmds.objectCenter('a', gl=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - gl: Return positional values in global coordinates (default).
        - local (l): Return positional values in local coordinates.
        - x: Return X value only
        - y: Return Y value only
        - z: Return Z value only
    """
