"""Stub files for Contexts category in Maya commands, command: ctxTraverse."""

from typing import Any, overload

@overload #Overload for ctxTraverse in ['create']
def ctxTraverse(down: bool = ..., left: bool = ..., right: bool = ..., up: bool = ...) -> None:
    """ctxTraverse is undoable, NOT queryable, and NOT editable.
    
    This command tells the current context to do a traversal.
    
    
    Some contexts will ignore this command. Individual contexts determine what
    up/down left/right mean.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a particle context, then switch to it
        cmds.dynParticleCtx('dynParticleCtx1')
        cmds.setToolTo('dynParticleCtx1')
        # Now you can create particles by mouse clicking
        # After creating several particles, we switch to edit mode
        cmds.ctxEditMode()
        # Traverse in the created particles
        cmds.ctxTraverse(left=True)
        cmds.ctxTraverse(left=True)
        cmds.ctxTraverse(right=True)
    ```

    ---
    - Args:
        - down (d): Move "down" as defined by the current context.
        - left (l): Move "left" as defined by the current context.
        - right (r): Move "right" as defined by the current context.
        - up: Move "up" as defined by the current context.
    """
@overload #Overload for ctxTraverse in ['create']
def ctxTraverse(d: bool = ..., l: bool = ..., r: bool = ...) -> None:
    """ctxTraverse is undoable, NOT queryable, and NOT editable.
    
    This command tells the current context to do a traversal.
    
    
    Some contexts will ignore this command. Individual contexts determine what
    up/down left/right mean.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a particle context, then switch to it
        cmds.dynParticleCtx('dynParticleCtx1')
        cmds.setToolTo('dynParticleCtx1')
        # Now you can create particles by mouse clicking
        # After creating several particles, we switch to edit mode
        cmds.ctxEditMode()
        # Traverse in the created particles
        cmds.ctxTraverse(left=True)
        cmds.ctxTraverse(left=True)
        cmds.ctxTraverse(right=True)
    ```

    ---
    - Args:
        - down (d): Move "down" as defined by the current context.
        - left (l): Move "left" as defined by the current context.
        - right (r): Move "right" as defined by the current context.
        - up: Move "up" as defined by the current context.
    """
@overload #Overload for ctxTraverse in ['create']
def ctxTraverse(down: bool = ..., d: bool = ..., left: bool = ..., l: bool = ..., right: bool = ..., r: bool = ..., up: bool = ...) -> None:
    """ctxTraverse is undoable, NOT queryable, and NOT editable.
    
    This command tells the current context to do a traversal.
    
    
    Some contexts will ignore this command. Individual contexts determine what
    up/down left/right mean.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a particle context, then switch to it
        cmds.dynParticleCtx('dynParticleCtx1')
        cmds.setToolTo('dynParticleCtx1')
        # Now you can create particles by mouse clicking
        # After creating several particles, we switch to edit mode
        cmds.ctxEditMode()
        # Traverse in the created particles
        cmds.ctxTraverse(left=True)
        cmds.ctxTraverse(left=True)
        cmds.ctxTraverse(right=True)
    ```

    ---
    - Args:
        - down (d): Move "down" as defined by the current context.
        - left (l): Move "left" as defined by the current context.
        - right (r): Move "right" as defined by the current context.
        - up: Move "up" as defined by the current context.
    """
