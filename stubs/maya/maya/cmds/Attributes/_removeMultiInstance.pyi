"""Stub files for Attributes category in Maya commands, command: removeMultiInstance."""

from typing import Any, overload

@overload #Overload for removeMultiInstance in ['create']
def removeMultiInstance(attribute: attribute, allChildren: bool = ..., b: bool = ...) -> bool:
    """removeMultiInstance is undoable, NOT queryable, and NOT editable.
    
    Removes a particular instance of a multiElement. This is only useful for input
    attributes since outputs will get regenerated the next time the node gets
    executed. This command will remove the instance and optionally break all
    incoming and outgoing connections to that instance. If the connections are not
    broken (with the -b true) flag, then the command will fail if connections
    exist.

    ---
    - Args:
        - attribute: Input item(s).
        - allChildren (all): If the argument is true, remove all children of the multi parent.
        - b: If the argument is true, all connections to the attribute will be broken before the element is removed. If false, then the command will fail if the element is connected.
    """
@overload #Overload for removeMultiInstance in ['create']
def removeMultiInstance(attribute: attribute, all: bool = ...) -> bool:
    """removeMultiInstance is undoable, NOT queryable, and NOT editable.
    
    Removes a particular instance of a multiElement. This is only useful for input
    attributes since outputs will get regenerated the next time the node gets
    executed. This command will remove the instance and optionally break all
    incoming and outgoing connections to that instance. If the connections are not
    broken (with the -b true) flag, then the command will fail if connections
    exist.

    ---
    - Args:
        - attribute: Input item(s).
        - allChildren (all): If the argument is true, remove all children of the multi parent.
        - b: If the argument is true, all connections to the attribute will be broken before the element is removed. If false, then the command will fail if the element is connected.
    """
@overload #Overload for removeMultiInstance in ['create']
def removeMultiInstance(attribute: attribute, allChildren: bool = ..., all: bool = ..., b: bool = ...) -> bool:
    """removeMultiInstance is undoable, NOT queryable, and NOT editable.
    
    Removes a particular instance of a multiElement. This is only useful for input
    attributes since outputs will get regenerated the next time the node gets
    executed. This command will remove the instance and optionally break all
    incoming and outgoing connections to that instance. If the connections are not
    broken (with the -b true) flag, then the command will fail if connections
    exist.

    ---
    - Args:
        - attribute: Input item(s).
        - allChildren (all): If the argument is true, remove all children of the multi parent.
        - b: If the argument is true, all connections to the attribute will be broken before the element is removed. If false, then the command will fail if the element is connected.
    """
