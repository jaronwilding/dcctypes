"""Stub files for Attributes category in Maya commands, command: disconnectAttr."""

from typing import Any, overload

@overload #Overload for disconnectAttr in ['create']
def disconnectAttr(attribute attribute: attribute attribute, nextAvailable: bool = ...) -> str:
    """disconnectAttr is undoable, NOT queryable, and NOT editable.
    
    Disconnects two connected attributes. First argument is the source attribute,
    second is the destination.

    ---
    - Args:
        - attribute attribute: Input item(s).
        - nextAvailable (na): If the destination multi-attribute has set the indexMatters to be false, the command will disconnect the first matching connection.  No index needs to be specified.
    """
@overload #Overload for disconnectAttr in ['create']
def disconnectAttr(attribute attribute: attribute attribute, na: bool = ...) -> str:
    """disconnectAttr is undoable, NOT queryable, and NOT editable.
    
    Disconnects two connected attributes. First argument is the source attribute,
    second is the destination.

    ---
    - Args:
        - attribute attribute: Input item(s).
        - nextAvailable (na): If the destination multi-attribute has set the indexMatters to be false, the command will disconnect the first matching connection.  No index needs to be specified.
    """
@overload #Overload for disconnectAttr in ['create']
def disconnectAttr(attribute attribute: attribute attribute, nextAvailable: bool = ..., na: bool = ...) -> str:
    """disconnectAttr is undoable, NOT queryable, and NOT editable.
    
    Disconnects two connected attributes. First argument is the source attribute,
    second is the destination.

    ---
    - Args:
        - attribute attribute: Input item(s).
        - nextAvailable (na): If the destination multi-attribute has set the indexMatters to be false, the command will disconnect the first matching connection.  No index needs to be specified.
    """
