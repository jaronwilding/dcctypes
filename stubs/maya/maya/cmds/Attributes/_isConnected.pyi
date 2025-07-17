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

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere( n='jupiter' )
        cmds.sphere( n='io' )
        cmds.connectAttr( 'jupiter.ty', 'io.ty' )
        # Are the two "tx" attributes on transform1 and transform2 connected?
        cmds.isConnected( 'jupiter.tx', 'io.tx' )
        # Result: 0 #
        # Are the two "ty" attributes on transform1 and transform2 connected?
        cmds.isConnected( 'jupiter.ty', 'io.ty' )
        # Result: 1 #
    ```

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

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere( n='jupiter' )
        cmds.sphere( n='io' )
        cmds.connectAttr( 'jupiter.ty', 'io.ty' )
        # Are the two "tx" attributes on transform1 and transform2 connected?
        cmds.isConnected( 'jupiter.tx', 'io.tx' )
        # Result: 0 #
        # Are the two "ty" attributes on transform1 and transform2 connected?
        cmds.isConnected( 'jupiter.ty', 'io.ty' )
        # Result: 1 #
    ```

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

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere( n='jupiter' )
        cmds.sphere( n='io' )
        cmds.connectAttr( 'jupiter.ty', 'io.ty' )
        # Are the two "tx" attributes on transform1 and transform2 connected?
        cmds.isConnected( 'jupiter.tx', 'io.tx' )
        # Result: 0 #
        # Are the two "ty" attributes on transform1 and transform2 connected?
        cmds.isConnected( 'jupiter.ty', 'io.ty' )
        # Result: 1 #
    ```

    ---
    - Args:
        - string string: Input item(s).
        - ignoreUnitConversion (iuc): In looking for connections, skip past unit conversion nodes.
    """
