"""Stub files for Attributes category in Maya commands, command: deleteAttr."""

from typing import Any, overload

@overload #Overload for deleteAttr in ['create']
def deleteAttr(node...|attribute...: node...|attribute..., attribute: str = ...) -> None:
    """deleteAttr is undoable, queryable, and editable.
    
    This command is used to delete a dynamic attribute from a node or nodes. The
    attribute can be specified by using either the long or short name. Only one
    dynamic attribute can be deleted at a time. Static attributes cannot be
    deleted. Children of a compound attribute cannot be deleted. You must delete
    the complete compound attribute. This command has no edit capabilities. The
    only query ability is to list all the dynamic attributes of a node.

    ---
    - Args:
        - node...|attribute...: Input item(s).
        - attribute (at): Specify either the long or short name of the attribute.
    """
@overload #Overload for deleteAttr in ['create']
def deleteAttr(node...|attribute...: node...|attribute..., at: str = ...) -> None:
    """deleteAttr is undoable, queryable, and editable.
    
    This command is used to delete a dynamic attribute from a node or nodes. The
    attribute can be specified by using either the long or short name. Only one
    dynamic attribute can be deleted at a time. Static attributes cannot be
    deleted. Children of a compound attribute cannot be deleted. You must delete
    the complete compound attribute. This command has no edit capabilities. The
    only query ability is to list all the dynamic attributes of a node.

    ---
    - Args:
        - node...|attribute...: Input item(s).
        - attribute (at): Specify either the long or short name of the attribute.
    """
@overload #Overload for deleteAttr in ['create']
def deleteAttr(node...|attribute...: node...|attribute..., attribute: str = ..., at: str = ...) -> None:
    """deleteAttr is undoable, queryable, and editable.
    
    This command is used to delete a dynamic attribute from a node or nodes. The
    attribute can be specified by using either the long or short name. Only one
    dynamic attribute can be deleted at a time. Static attributes cannot be
    deleted. Children of a compound attribute cannot be deleted. You must delete
    the complete compound attribute. This command has no edit capabilities. The
    only query ability is to list all the dynamic attributes of a node.

    ---
    - Args:
        - node...|attribute...: Input item(s).
        - attribute (at): Specify either the long or short name of the attribute.
    """
