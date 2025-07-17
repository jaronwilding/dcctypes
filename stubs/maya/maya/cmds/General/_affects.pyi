"""Stub files for General category in Maya commands, command: affects."""

from typing import Any, overload

@overload #Overload for affects in ['create']
def affects(string: str, by: bool = ..., type: str = ...) -> str:
    """affects is NOT undoable, NOT queryable, and NOT editable.
    
    This command returns the list of attributes on a node or node type which
    affect the named attribute.

    Example:
    ```python
        import maya.cmds as cmds
        # List the attributes on node "sphere" that affect the "tx" attribute
        cmds.sphere( n='sphere' )
        cmds.affects( 'tx', 'sphere' )
        # List the attributes on nodes of type "transform" that are affected by
        # the "ty" attribute
        cmds.affects( 'ty', by=True, t='transform' )
        # List the attributes on nodes of type "revolve" that affect the
        # "outputSurface" attribute
        cmds.affects( 'outputSurface', t='revolve' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - by ()): Show attributes that are affected by the given one rather than the ones that affect it.
        - type (t): static node type from which to get 'affects' information
    """
@overload #Overload for affects in ['create']
def affects(string: str, ): bool = ..., t: str = ...) -> str:
    """affects is NOT undoable, NOT queryable, and NOT editable.
    
    This command returns the list of attributes on a node or node type which
    affect the named attribute.

    Example:
    ```python
        import maya.cmds as cmds
        # List the attributes on node "sphere" that affect the "tx" attribute
        cmds.sphere( n='sphere' )
        cmds.affects( 'tx', 'sphere' )
        # List the attributes on nodes of type "transform" that are affected by
        # the "ty" attribute
        cmds.affects( 'ty', by=True, t='transform' )
        # List the attributes on nodes of type "revolve" that affect the
        # "outputSurface" attribute
        cmds.affects( 'outputSurface', t='revolve' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - by ()): Show attributes that are affected by the given one rather than the ones that affect it.
        - type (t): static node type from which to get 'affects' information
    """
@overload #Overload for affects in ['create']
def affects(string: str, by: bool = ..., ): bool = ..., type: str = ..., t: str = ...) -> str:
    """affects is NOT undoable, NOT queryable, and NOT editable.
    
    This command returns the list of attributes on a node or node type which
    affect the named attribute.

    Example:
    ```python
        import maya.cmds as cmds
        # List the attributes on node "sphere" that affect the "tx" attribute
        cmds.sphere( n='sphere' )
        cmds.affects( 'tx', 'sphere' )
        # List the attributes on nodes of type "transform" that are affected by
        # the "ty" attribute
        cmds.affects( 'ty', by=True, t='transform' )
        # List the attributes on nodes of type "revolve" that affect the
        # "outputSurface" attribute
        cmds.affects( 'outputSurface', t='revolve' )
    ```

    ---
    - Args:
        - string: Input item(s).
        - by ()): Show attributes that are affected by the given one rather than the ones that affect it.
        - type (t): static node type from which to get 'affects' information
    """
