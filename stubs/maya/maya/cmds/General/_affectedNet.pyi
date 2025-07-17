"""Stub files for General category in Maya commands, command: affectedNet."""

from typing import Any, overload

@overload #Overload for affectedNet in ['create']
def affectedNet([node...]: [node...], type: str = ...) -> None:
    """affectedNet is undoable, queryable, and editable.
    
    This command gets the list of attributes on a node or node type and creates
    nodes of type TdnAffect, one for each attribute, that are connected iff the
    source node's attribute affects the destination node's attribute.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a network of this transform node's attributes that affect
        # each other
        cmds.affectedNet( 'transform1' )
        # Create a network all of the transform shared attributes that affect
        # each other
        cmds.affectedNet( t='transform' )
        # Create a network of the revolve and shape node type attributes that
        # affect each other
        cmds.affectedNet( t='revolve', t='shape' )
    ```

    ---
    - Args:
        - [node...]: Input item(s).
        - type (t): Get information from the given node type instead of one node
    """
@overload #Overload for affectedNet in ['create']
def affectedNet([node...]: [node...], t: str = ...) -> None:
    """affectedNet is undoable, queryable, and editable.
    
    This command gets the list of attributes on a node or node type and creates
    nodes of type TdnAffect, one for each attribute, that are connected iff the
    source node's attribute affects the destination node's attribute.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a network of this transform node's attributes that affect
        # each other
        cmds.affectedNet( 'transform1' )
        # Create a network all of the transform shared attributes that affect
        # each other
        cmds.affectedNet( t='transform' )
        # Create a network of the revolve and shape node type attributes that
        # affect each other
        cmds.affectedNet( t='revolve', t='shape' )
    ```

    ---
    - Args:
        - [node...]: Input item(s).
        - type (t): Get information from the given node type instead of one node
    """
@overload #Overload for affectedNet in ['create']
def affectedNet([node...]: [node...], type: str = ..., t: str = ...) -> None:
    """affectedNet is undoable, queryable, and editable.
    
    This command gets the list of attributes on a node or node type and creates
    nodes of type TdnAffect, one for each attribute, that are connected iff the
    source node's attribute affects the destination node's attribute.

    Example:
    ```python
        import maya.cmds as cmds
        # Create a network of this transform node's attributes that affect
        # each other
        cmds.affectedNet( 'transform1' )
        # Create a network all of the transform shared attributes that affect
        # each other
        cmds.affectedNet( t='transform' )
        # Create a network of the revolve and shape node type attributes that
        # affect each other
        cmds.affectedNet( t='revolve', t='shape' )
    ```

    ---
    - Args:
        - [node...]: Input item(s).
        - type (t): Get information from the given node type instead of one node
    """
