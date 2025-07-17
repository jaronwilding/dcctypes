"""Stub files for General category in Maya commands, command: distanceDimension."""

from typing import Any, overload

@overload #Overload for distanceDimension in ['create']
def distanceDimension(endPoint: [linear, linear, linear] = ..., startPoint: [linear, linear, linear] = ...) -> str:
    """distanceDimension is undoable, NOT queryable, and NOT editable.
    
    This command is used to create a distance dimension to display the distance
    between two specified points.

    Example:
    ```python
        import maya.cmds as cmds
        # To measure ths distance between [0,2,2] and [1,5,6]:
        cmds.distanceDimension( sp=(0, 2, 2), ep=(1, 5, 6) )
        #  Result: distanceDimensionShape1  #
    ```

    ---
    - Args:
        - endPoint (ep): Specifies the point to measure distance to, from the startPoint.
        - startPoint (sp): Specifies the point to start measuring distance from.
    """
@overload #Overload for distanceDimension in ['create']
def distanceDimension(ep: [linear, linear, linear] = ..., sp: [linear, linear, linear] = ...) -> str:
    """distanceDimension is undoable, NOT queryable, and NOT editable.
    
    This command is used to create a distance dimension to display the distance
    between two specified points.

    Example:
    ```python
        import maya.cmds as cmds
        # To measure ths distance between [0,2,2] and [1,5,6]:
        cmds.distanceDimension( sp=(0, 2, 2), ep=(1, 5, 6) )
        #  Result: distanceDimensionShape1  #
    ```

    ---
    - Args:
        - endPoint (ep): Specifies the point to measure distance to, from the startPoint.
        - startPoint (sp): Specifies the point to start measuring distance from.
    """
@overload #Overload for distanceDimension in ['create']
def distanceDimension(endPoint: [linear, linear, linear] = ..., ep: [linear, linear, linear] = ..., startPoint: [linear, linear, linear] = ..., sp: [linear, linear, linear] = ...) -> str:
    """distanceDimension is undoable, NOT queryable, and NOT editable.
    
    This command is used to create a distance dimension to display the distance
    between two specified points.

    Example:
    ```python
        import maya.cmds as cmds
        # To measure ths distance between [0,2,2] and [1,5,6]:
        cmds.distanceDimension( sp=(0, 2, 2), ep=(1, 5, 6) )
        #  Result: distanceDimensionShape1  #
    ```

    ---
    - Args:
        - endPoint (ep): Specifies the point to measure distance to, from the startPoint.
        - startPoint (sp): Specifies the point to start measuring distance from.
    """
