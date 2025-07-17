"""Stub files for General category in Maya commands, command: filterInstances."""

from typing import Any, overload

@overload #Overload for filterInstances in ['create']
def filterInstances(shapes: bool = ...) -> list[str]:
    """filterInstances is undoable, queryable, and NOT editable.
    
    This command filters the selection list to remove duplicate instances that
    refer to the same object/components. If any such instances are found they will
    be merged with the first selected instance.
    
    Returns a string array containing all matching selection items or true/false
    if the query flag is used.

    Example:
    ```python
        import maya.cmds as cmds
        # Returns true if any selected object(s) are instances of another selected object.
        cmds.filterInstances( q=True )
        # Returns a new selection list with duplicate instances removed.
        cmds.filterInstances()
    ```

    ---
    - Args:
        - shapes (s): If this is true then the command will check for an instanced shapes below the selected transform(s) and use them to decide whether the parent transforms should be considered instances. Default is false.
    """
@overload #Overload for filterInstances in ['create']
def filterInstances(s: bool = ...) -> list[str]:
    """filterInstances is undoable, queryable, and NOT editable.
    
    This command filters the selection list to remove duplicate instances that
    refer to the same object/components. If any such instances are found they will
    be merged with the first selected instance.
    
    Returns a string array containing all matching selection items or true/false
    if the query flag is used.

    Example:
    ```python
        import maya.cmds as cmds
        # Returns true if any selected object(s) are instances of another selected object.
        cmds.filterInstances( q=True )
        # Returns a new selection list with duplicate instances removed.
        cmds.filterInstances()
    ```

    ---
    - Args:
        - shapes (s): If this is true then the command will check for an instanced shapes below the selected transform(s) and use them to decide whether the parent transforms should be considered instances. Default is false.
    """
@overload #Overload for filterInstances in ['create']
def filterInstances(shapes: bool = ..., s: bool = ...) -> list[str]:
    """filterInstances is undoable, queryable, and NOT editable.
    
    This command filters the selection list to remove duplicate instances that
    refer to the same object/components. If any such instances are found they will
    be merged with the first selected instance.
    
    Returns a string array containing all matching selection items or true/false
    if the query flag is used.

    Example:
    ```python
        import maya.cmds as cmds
        # Returns true if any selected object(s) are instances of another selected object.
        cmds.filterInstances( q=True )
        # Returns a new selection list with duplicate instances removed.
        cmds.filterInstances()
    ```

    ---
    - Args:
        - shapes (s): If this is true then the command will check for an instanced shapes below the selected transform(s) and use them to decide whether the parent transforms should be considered instances. Default is false.
    """
