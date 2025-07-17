"""Stub files for Contexts category in Maya commands, command: ctxEditMode."""

from typing import Any, overload

@overload #Overload for ctxEditMode in ['create']
def ctxEditMode(buttonDown: bool = ..., buttonUp: bool = ...) -> None:
    """ctxEditMode is undoable, NOT queryable, and NOT editable.
    
    This command tells the current context to switch edit modes.
    It acts as a toggle.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly cube
        cmds.polyCube(w=2, h=2, d=2, n='pCube1')
        # Create a new rotate manip context, then switch to it.
        cmds.manipRotateContext('manipRotateContext1')
        cmds.setToolTo('manipRotateContext1')
        # Switch to edit mode to change pivots
        cmds.ctxEditMode()
    ```

    ---
    - Args:
        - buttonDown (btd): Edit mode is being invoked from a hotkey press event.
        - buttonUp (btu): Edit mode is being invoked from a hotkey release event.
    """
@overload #Overload for ctxEditMode in ['create']
def ctxEditMode(btd: bool = ..., btu: bool = ...) -> None:
    """ctxEditMode is undoable, NOT queryable, and NOT editable.
    
    This command tells the current context to switch edit modes.
    It acts as a toggle.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly cube
        cmds.polyCube(w=2, h=2, d=2, n='pCube1')
        # Create a new rotate manip context, then switch to it.
        cmds.manipRotateContext('manipRotateContext1')
        cmds.setToolTo('manipRotateContext1')
        # Switch to edit mode to change pivots
        cmds.ctxEditMode()
    ```

    ---
    - Args:
        - buttonDown (btd): Edit mode is being invoked from a hotkey press event.
        - buttonUp (btu): Edit mode is being invoked from a hotkey release event.
    """
@overload #Overload for ctxEditMode in ['create']
def ctxEditMode(buttonDown: bool = ..., btd: bool = ..., buttonUp: bool = ..., btu: bool = ...) -> None:
    """ctxEditMode is undoable, NOT queryable, and NOT editable.
    
    This command tells the current context to switch edit modes.
    It acts as a toggle.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly cube
        cmds.polyCube(w=2, h=2, d=2, n='pCube1')
        # Create a new rotate manip context, then switch to it.
        cmds.manipRotateContext('manipRotateContext1')
        cmds.setToolTo('manipRotateContext1')
        # Switch to edit mode to change pivots
        cmds.ctxEditMode()
    ```

    ---
    - Args:
        - buttonDown (btd): Edit mode is being invoked from a hotkey press event.
        - buttonUp (btu): Edit mode is being invoked from a hotkey release event.
    """
