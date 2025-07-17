"""Stub files for Attributes category in Maya commands, command: connectionInfo."""

from typing import Any, overload

@overload #Overload for connectionInfo in ['create']
def connectionInfo(string: str, destinationFromSource: bool = ..., getExactDestination: bool = ..., getExactSource: bool = ..., getLockedAncestor: bool = ..., isDestination: bool = ..., isExactDestination: bool = ..., isExactSource: bool = ..., isLocked: bool = ..., isSource: bool = ..., sourceFromDestination: bool = ...) -> bool | str | list[str]:
    """connectionInfo is undoable, NOT queryable, and NOT editable.
    
    The connectionInfo command is used to get information about connection sources
    and destinations. Unlike the isConnected command, this command needs only one
    end of the connection.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a sphere and a cone and make the Z translation of the cone
        #    be dependent on the X translation of the sphere.
        #
        cone = cmds.cone()
        sphere = cmds.sphere()
        sphereTx = '%s.tx' % sphere[0]
        coneTz = '%s.tz' % cone[0]
        cmds.connectAttr(sphereTx, coneTz)
        #    Verify the connection and print out the source plug.
        #
        if cmds.connectionInfo( coneTz, isDestination=True):
        print( 'Source: %s' % cmds.connectionInfo(coneTz,sourceFromDestination=True) )
        #    Verify the connection and print out the destination plug.
        #
        if cmds.connectionInfo( sphereTx, isSource=True):
        destinations = cmds.connectionInfo(sphereTx, destinationFromSource=True)
        for destination in destinations:
        print destination
    ```

    ---
    - Args:
        - string: Input item(s).
        - destinationFromSource (dfs): If the specified plug (or its ancestor) is a source, this flag returns the list of destinations connected from the source. (array of strings, empty array if none)
        - getExactDestination (ged): If the plug or its ancestor is connection destination, this returns the name of the plug that is the exact destination. (empty string if there is no such connection).
        - getExactSource (ges): If the plug or its ancestor is a connection source, this returns the name of the plug that is the exact source. (empty string if there is no such connection).
        - getLockedAncestor (gla): If the specified plug is locked, its name is returned.  If an ancestor of the plug is locked, its name is returned.  If more than one ancestor is locked, only the name of the closest one is returned.  If neither this plug nor any ancestors
            are locked, an empty string is returned.
        - isDestination (id): Returns true if the plug (or its ancestor) is the destination of a connection, false otherwise.
        - isExactDestination (ied): Returns true if the plug is the exact destination of a connection, false otherwise.
        - isExactSource (ies): Returns true if the plug is the exact source of a connection, false otherwise.
        - isLocked (il): Returns true if this plug (or its ancestor) is locked
        - isSource: Returns true if the plug (or its ancestor) is the source of a connection, false otherwise.
        - sourceFromDestination (sfd): If the specified plug (or its ancestor) is a destination, this flag returns the source of the connection. (string, empty if none)
    """
@overload #Overload for connectionInfo in ['create']
def connectionInfo(string: str, dfs: bool = ..., ged: bool = ..., ges: bool = ..., gla: bool = ..., id: bool = ..., ied: bool = ..., ies: bool = ..., il: bool = ..., sfd: bool = ...) -> bool | str | list[str]:
    """connectionInfo is undoable, NOT queryable, and NOT editable.
    
    The connectionInfo command is used to get information about connection sources
    and destinations. Unlike the isConnected command, this command needs only one
    end of the connection.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a sphere and a cone and make the Z translation of the cone
        #    be dependent on the X translation of the sphere.
        #
        cone = cmds.cone()
        sphere = cmds.sphere()
        sphereTx = '%s.tx' % sphere[0]
        coneTz = '%s.tz' % cone[0]
        cmds.connectAttr(sphereTx, coneTz)
        #    Verify the connection and print out the source plug.
        #
        if cmds.connectionInfo( coneTz, isDestination=True):
        print( 'Source: %s' % cmds.connectionInfo(coneTz,sourceFromDestination=True) )
        #    Verify the connection and print out the destination plug.
        #
        if cmds.connectionInfo( sphereTx, isSource=True):
        destinations = cmds.connectionInfo(sphereTx, destinationFromSource=True)
        for destination in destinations:
        print destination
    ```

    ---
    - Args:
        - string: Input item(s).
        - destinationFromSource (dfs): If the specified plug (or its ancestor) is a source, this flag returns the list of destinations connected from the source. (array of strings, empty array if none)
        - getExactDestination (ged): If the plug or its ancestor is connection destination, this returns the name of the plug that is the exact destination. (empty string if there is no such connection).
        - getExactSource (ges): If the plug or its ancestor is a connection source, this returns the name of the plug that is the exact source. (empty string if there is no such connection).
        - getLockedAncestor (gla): If the specified plug is locked, its name is returned.  If an ancestor of the plug is locked, its name is returned.  If more than one ancestor is locked, only the name of the closest one is returned.  If neither this plug nor any ancestors
            are locked, an empty string is returned.
        - isDestination (id): Returns true if the plug (or its ancestor) is the destination of a connection, false otherwise.
        - isExactDestination (ied): Returns true if the plug is the exact destination of a connection, false otherwise.
        - isExactSource (ies): Returns true if the plug is the exact source of a connection, false otherwise.
        - isLocked (il): Returns true if this plug (or its ancestor) is locked
        - isSource: Returns true if the plug (or its ancestor) is the source of a connection, false otherwise.
        - sourceFromDestination (sfd): If the specified plug (or its ancestor) is a destination, this flag returns the source of the connection. (string, empty if none)
    """
@overload #Overload for connectionInfo in ['create']
def connectionInfo(string: str, destinationFromSource: bool = ..., dfs: bool = ..., getExactDestination: bool = ..., ged: bool = ..., getExactSource: bool = ..., ges: bool = ..., getLockedAncestor: bool = ..., gla: bool = ..., isDestination: bool = ..., id: bool = ..., isExactDestination: bool = ..., ied: bool = ..., isExactSource: bool = ..., ies: bool = ..., isLocked: bool = ..., il: bool = ..., isSource: bool = ..., sourceFromDestination: bool = ..., sfd: bool = ...) -> bool | str | list[str]:
    """connectionInfo is undoable, NOT queryable, and NOT editable.
    
    The connectionInfo command is used to get information about connection sources
    and destinations. Unlike the isConnected command, this command needs only one
    end of the connection.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a sphere and a cone and make the Z translation of the cone
        #    be dependent on the X translation of the sphere.
        #
        cone = cmds.cone()
        sphere = cmds.sphere()
        sphereTx = '%s.tx' % sphere[0]
        coneTz = '%s.tz' % cone[0]
        cmds.connectAttr(sphereTx, coneTz)
        #    Verify the connection and print out the source plug.
        #
        if cmds.connectionInfo( coneTz, isDestination=True):
        print( 'Source: %s' % cmds.connectionInfo(coneTz,sourceFromDestination=True) )
        #    Verify the connection and print out the destination plug.
        #
        if cmds.connectionInfo( sphereTx, isSource=True):
        destinations = cmds.connectionInfo(sphereTx, destinationFromSource=True)
        for destination in destinations:
        print destination
    ```

    ---
    - Args:
        - string: Input item(s).
        - destinationFromSource (dfs): If the specified plug (or its ancestor) is a source, this flag returns the list of destinations connected from the source. (array of strings, empty array if none)
        - getExactDestination (ged): If the plug or its ancestor is connection destination, this returns the name of the plug that is the exact destination. (empty string if there is no such connection).
        - getExactSource (ges): If the plug or its ancestor is a connection source, this returns the name of the plug that is the exact source. (empty string if there is no such connection).
        - getLockedAncestor (gla): If the specified plug is locked, its name is returned.  If an ancestor of the plug is locked, its name is returned.  If more than one ancestor is locked, only the name of the closest one is returned.  If neither this plug nor any ancestors
            are locked, an empty string is returned.
        - isDestination (id): Returns true if the plug (or its ancestor) is the destination of a connection, false otherwise.
        - isExactDestination (ied): Returns true if the plug is the exact destination of a connection, false otherwise.
        - isExactSource (ies): Returns true if the plug is the exact source of a connection, false otherwise.
        - isLocked (il): Returns true if this plug (or its ancestor) is locked
        - isSource: Returns true if the plug (or its ancestor) is the source of a connection, false otherwise.
        - sourceFromDestination (sfd): If the specified plug (or its ancestor) is a destination, this flag returns the source of the connection. (string, empty if none)
    """
