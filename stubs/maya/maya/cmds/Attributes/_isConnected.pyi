"""Stub files for Attributes category in Maya commands, command: isConnected."""

from typing import Any, overload

@overload #Overload for isConnected in ['create']
def isConnected(string string: string string, ignoreUnitConversion: bool = ...) -> bool:
    """isConnected is undoable, NOT queryable, and NOT editable.
    
    The isConnected command is used to check if two plugs are connected in the
    dependency graph. The return value is false if they are not and true if they
    are.
    
    
    The first string specifies the source plug to check for connection.
    The second one specifies the destination plug to check for connection.

    ---
    - Args:
        - string string: Input item(s).
        - ignoreUnitConversion (iuc): In looking for connections, skip past unit conversion nodes.
    """
@overload #Overload for isConnected in ['create']
def isConnected(string string: string string, iuc: bool = ...) -> bool:
    """isConnected is undoable, NOT queryable, and NOT editable.
    
    The isConnected command is used to check if two plugs are connected in the
    dependency graph. The return value is false if they are not and true if they
    are.
    
    
    The first string specifies the source plug to check for connection.
    The second one specifies the destination plug to check for connection.

    ---
    - Args:
        - string string: Input item(s).
        - ignoreUnitConversion (iuc): In looking for connections, skip past unit conversion nodes.
    """
@overload #Overload for isConnected in ['create']
def isConnected(string string: string string, ignoreUnitConversion: bool = ..., iuc: bool = ...) -> bool:
    """isConnected is undoable, NOT queryable, and NOT editable.
    
    The isConnected command is used to check if two plugs are connected in the
    dependency graph. The return value is false if they are not and true if they
    are.
    
    
    The first string specifies the source plug to check for connection.
    The second one specifies the destination plug to check for connection.

    ---
    - Args:
        - string string: Input item(s).
        - ignoreUnitConversion (iuc): In looking for connections, skip past unit conversion nodes.
    """
