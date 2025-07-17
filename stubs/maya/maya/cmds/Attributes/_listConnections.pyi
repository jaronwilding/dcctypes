"""Stub files for Attributes category in Maya commands, command: listConnections."""

from typing import Any, overload

@overload #Overload for listConnections in ['create']
def listConnections(connections: bool = ..., destination: bool = ..., exactType: bool = ..., fullNodeName: bool = ..., plugs: bool = ..., shapes: bool = ..., skipConversionNodes: bool = ..., source: bool = ..., type: str = ...) -> list[str]:
    """listConnections is NOT undoable, NOT queryable, and NOT editable.
    
    This command returns a list of all attributes/objects of a specified type that
    are connected to the given object(s). If no objects are specified then the
    command lists the connections on selected nodes.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere( ch=True, n='BALL' )
        cmds.setKeyframe()
        # List all connections to BALL
        list = cmds.listConnections('BALL')
        # List only incoming connections from BALL.tx
        cmds.listConnections( 'BALL.tx', d=False, s=True )
        # List connections from BALL to nodes of type 'transform'
        cmds.listConnections( t='transform' )
        # List connections on BALL, ignoring unit conversion nodes
        cmds.listConnections( 'BALL', scn=True )
    ```

    ---
    - Args:
        - connections (c): If true, return both attributes involved in the connection. The one on the specified object is given first.  Default false.
        - destination (d): Give the attributes/objects that are on the "destination" side of connection to the given object.  Default true.
        - exactType (et): When set to true, -t/type only considers node of this exact type. Otherwise, derived types are also taken into account.
        - fullNodeName (fnn): Return full node name in result.
        - plugs (p): If true, return the connected attribute names; if false, return the connected object names only.  Default false;
        - shapes (sh): Actually return the shape name instead of the transform when the shape is "selected".  Default false.
        - skipConversionNodes (scn): If true, skip over unit conversion nodes and return the node connected to the conversion node on the other side.  Default false.
        - source (s): Give the attributes/objects that are on the "source" side of connection to the given object.  Default true.
        - type (t): If specified, only take objects of a specified type.
    """
@overload #Overload for listConnections in ['create']
def listConnections(c: bool = ..., d: bool = ..., et: bool = ..., fnn: bool = ..., p: bool = ..., sh: bool = ..., scn: bool = ..., s: bool = ..., t: str = ...) -> list[str]:
    """listConnections is NOT undoable, NOT queryable, and NOT editable.
    
    This command returns a list of all attributes/objects of a specified type that
    are connected to the given object(s). If no objects are specified then the
    command lists the connections on selected nodes.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere( ch=True, n='BALL' )
        cmds.setKeyframe()
        # List all connections to BALL
        list = cmds.listConnections('BALL')
        # List only incoming connections from BALL.tx
        cmds.listConnections( 'BALL.tx', d=False, s=True )
        # List connections from BALL to nodes of type 'transform'
        cmds.listConnections( t='transform' )
        # List connections on BALL, ignoring unit conversion nodes
        cmds.listConnections( 'BALL', scn=True )
    ```

    ---
    - Args:
        - connections (c): If true, return both attributes involved in the connection. The one on the specified object is given first.  Default false.
        - destination (d): Give the attributes/objects that are on the "destination" side of connection to the given object.  Default true.
        - exactType (et): When set to true, -t/type only considers node of this exact type. Otherwise, derived types are also taken into account.
        - fullNodeName (fnn): Return full node name in result.
        - plugs (p): If true, return the connected attribute names; if false, return the connected object names only.  Default false;
        - shapes (sh): Actually return the shape name instead of the transform when the shape is "selected".  Default false.
        - skipConversionNodes (scn): If true, skip over unit conversion nodes and return the node connected to the conversion node on the other side.  Default false.
        - source (s): Give the attributes/objects that are on the "source" side of connection to the given object.  Default true.
        - type (t): If specified, only take objects of a specified type.
    """
@overload #Overload for listConnections in ['create']
def listConnections(connections: bool = ..., c: bool = ..., destination: bool = ..., d: bool = ..., exactType: bool = ..., et: bool = ..., fullNodeName: bool = ..., fnn: bool = ..., plugs: bool = ..., p: bool = ..., shapes: bool = ..., sh: bool = ..., skipConversionNodes: bool = ..., scn: bool = ..., source: bool = ..., s: bool = ..., type: str = ..., t: str = ...) -> list[str]:
    """listConnections is NOT undoable, NOT queryable, and NOT editable.
    
    This command returns a list of all attributes/objects of a specified type that
    are connected to the given object(s). If no objects are specified then the
    command lists the connections on selected nodes.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere( ch=True, n='BALL' )
        cmds.setKeyframe()
        # List all connections to BALL
        list = cmds.listConnections('BALL')
        # List only incoming connections from BALL.tx
        cmds.listConnections( 'BALL.tx', d=False, s=True )
        # List connections from BALL to nodes of type 'transform'
        cmds.listConnections( t='transform' )
        # List connections on BALL, ignoring unit conversion nodes
        cmds.listConnections( 'BALL', scn=True )
    ```

    ---
    - Args:
        - connections (c): If true, return both attributes involved in the connection. The one on the specified object is given first.  Default false.
        - destination (d): Give the attributes/objects that are on the "destination" side of connection to the given object.  Default true.
        - exactType (et): When set to true, -t/type only considers node of this exact type. Otherwise, derived types are also taken into account.
        - fullNodeName (fnn): Return full node name in result.
        - plugs (p): If true, return the connected attribute names; if false, return the connected object names only.  Default false;
        - shapes (sh): Actually return the shape name instead of the transform when the shape is "selected".  Default false.
        - skipConversionNodes (scn): If true, skip over unit conversion nodes and return the node connected to the conversion node on the other side.  Default false.
        - source (s): Give the attributes/objects that are on the "source" side of connection to the given object.  Default true.
        - type (t): If specified, only take objects of a specified type.
    """
