"""Stub files for General category in Maya commands, command: instancer."""

from typing import Any, overload

@overload #Overload for instancer in ['create']
def instancer(addObject: bool = ..., cycle: str = ..., cycleStep: float = ..., cycleStepUnits: str = ..., levelOfDetail: str = ..., name: str = ..., object: str = ..., rotationOrder: str = ..., rotationUnits: str = ...) -> str:
    """instancer is undoable, queryable, and editable.
    
    This command is used to create a instancer node and set the proper attributes
    in the node.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere(n='myShape')
        cmds.instancer( name='myInstancerNode', a=True, object='myShape' )
    ```

    ---
    - Args:
        - addObject (a): This flag indicates that objects specified by the -object flag will be added to the instancer node as instanced objects.
        - cycle (c): This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential".  The default is "none".
        - cycleStep (cs): This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).
        - cycleStepUnits (csu): This flag sets or queries the cycle step unit attribute for the instancer node.  The options are "frames" or "seconds".  The default is "frames".
        - levelOfDetail (lod): This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox", "boundingBoxes".  The default is "geometry".
        - name (n): This flag sets or queries the name of the instancer node.
        - object (obj): This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -add and -remove flags.  If neither of these flags is specified on the command line then -add is assumed.
        - rotationOrder (ro): This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        - rotationUnits (ru): This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
    """
@overload #Overload for instancer in ['create']
def instancer(a: bool = ..., c: str = ..., cs: float = ..., csu: str = ..., lod: str = ..., n: str = ..., obj: str = ..., ro: str = ..., ru: str = ...) -> str:
    """instancer is undoable, queryable, and editable.
    
    This command is used to create a instancer node and set the proper attributes
    in the node.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere(n='myShape')
        cmds.instancer( name='myInstancerNode', a=True, object='myShape' )
    ```

    ---
    - Args:
        - addObject (a): This flag indicates that objects specified by the -object flag will be added to the instancer node as instanced objects.
        - cycle (c): This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential".  The default is "none".
        - cycleStep (cs): This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).
        - cycleStepUnits (csu): This flag sets or queries the cycle step unit attribute for the instancer node.  The options are "frames" or "seconds".  The default is "frames".
        - levelOfDetail (lod): This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox", "boundingBoxes".  The default is "geometry".
        - name (n): This flag sets or queries the name of the instancer node.
        - object (obj): This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -add and -remove flags.  If neither of these flags is specified on the command line then -add is assumed.
        - rotationOrder (ro): This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        - rotationUnits (ru): This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
    """
@overload #Overload for instancer in ['create']
def instancer(addObject: bool = ..., a: bool = ..., cycle: str = ..., c: str = ..., cycleStep: float = ..., cs: float = ..., cycleStepUnits: str = ..., csu: str = ..., levelOfDetail: str = ..., lod: str = ..., name: str = ..., n: str = ..., object: str = ..., obj: str = ..., rotationOrder: str = ..., ro: str = ..., rotationUnits: str = ..., ru: str = ...) -> str:
    """instancer is undoable, queryable, and editable.
    
    This command is used to create a instancer node and set the proper attributes
    in the node.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere(n='myShape')
        cmds.instancer( name='myInstancerNode', a=True, object='myShape' )
    ```

    ---
    - Args:
        - addObject (a): This flag indicates that objects specified by the -object flag will be added to the instancer node as instanced objects.
        - cycle (c): This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential".  The default is "none".
        - cycleStep (cs): This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).
        - cycleStepUnits (csu): This flag sets or queries the cycle step unit attribute for the instancer node.  The options are "frames" or "seconds".  The default is "frames".
        - levelOfDetail (lod): This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox", "boundingBoxes".  The default is "geometry".
        - name (n): This flag sets or queries the name of the instancer node.
        - object (obj): This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -add and -remove flags.  If neither of these flags is specified on the command line then -add is assumed.
        - rotationOrder (ro): This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        - rotationUnits (ru): This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
    """
@overload #Overload for instancer in ['query']
def instancer(cycle: str = ..., cycleStep: float = ..., cycleStepUnits: str = ..., index: int = ..., levelOfDetail: str = ..., name: str = ..., object: str = ..., objectPosition: str = ..., objectRotation: str = ..., objectScale: str = ..., pointDataSource: bool = ..., rotationOrder: str = ..., rotationUnits: str = ..., valueName: str = ..., query: bool = ...) -> str:
    """instancer is undoable, queryable, and editable.
    
    This command is used to create a instancer node and set the proper attributes
    in the node.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere(n='myShape')
        cmds.instancer( name='myInstancerNode', a=True, object='myShape' )
    ```

    ---
    - Args:
        - cycle (c): This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential".  The default is "none".
        - cycleStep (cs): This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).
        - cycleStepUnits (csu): This flag sets or queries the cycle step unit attribute for the instancer node.  The options are "frames" or "seconds".  The default is "frames".
        - index (i): This flag is used to query the name of the ith instanced object.
        - levelOfDetail (lod): This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox", "boundingBoxes".  The default is "geometry".
        - name (n): This flag sets or queries the name of the instancer node.
        - object (obj): This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -add and -remove flags.  If neither of these flags is specified on the command line then -add is assumed.
        - objectPosition (op): This flag queries the given objects position.  This object can be any instanced object or sub-object.
        - objectRotation: This flag queries the given objects rotation.  This object can be any instanced object or sub-object.
        - objectScale (os): This flag queries the given objects scale.  This object can be any instanced object or sub-object.
        - pointDataSource (pds): This flag is used to query the source node supply the data for the input points.
        - rotationOrder (ro): This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        - rotationUnits (ru): This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
        - valueName (vn): This flag is used to query the value(s) of the array associated with the given name.  If the -index flag is used in conjuction with this flag then the ith value will be returned.  Otherwise, the entire array will be returned.
        - query (q): Query mode flag
    """
@overload #Overload for instancer in ['query']
def instancer(c: str = ..., cs: float = ..., csu: str = ..., i: int = ..., lod: str = ..., n: str = ..., obj: str = ..., op: str = ..., os: str = ..., pds: bool = ..., ro: str = ..., ru: str = ..., vn: str = ..., q: bool = ...) -> str:
    """instancer is undoable, queryable, and editable.
    
    This command is used to create a instancer node and set the proper attributes
    in the node.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere(n='myShape')
        cmds.instancer( name='myInstancerNode', a=True, object='myShape' )
    ```

    ---
    - Args:
        - cycle (c): This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential".  The default is "none".
        - cycleStep (cs): This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).
        - cycleStepUnits (csu): This flag sets or queries the cycle step unit attribute for the instancer node.  The options are "frames" or "seconds".  The default is "frames".
        - index (i): This flag is used to query the name of the ith instanced object.
        - levelOfDetail (lod): This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox", "boundingBoxes".  The default is "geometry".
        - name (n): This flag sets or queries the name of the instancer node.
        - object (obj): This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -add and -remove flags.  If neither of these flags is specified on the command line then -add is assumed.
        - objectPosition (op): This flag queries the given objects position.  This object can be any instanced object or sub-object.
        - objectRotation: This flag queries the given objects rotation.  This object can be any instanced object or sub-object.
        - objectScale (os): This flag queries the given objects scale.  This object can be any instanced object or sub-object.
        - pointDataSource (pds): This flag is used to query the source node supply the data for the input points.
        - rotationOrder (ro): This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        - rotationUnits (ru): This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
        - valueName (vn): This flag is used to query the value(s) of the array associated with the given name.  If the -index flag is used in conjuction with this flag then the ith value will be returned.  Otherwise, the entire array will be returned.
        - query (q): Query mode flag
    """
@overload #Overload for instancer in ['query']
def instancer(cycle: str = ..., c: str = ..., cycleStep: float = ..., cs: float = ..., cycleStepUnits: str = ..., csu: str = ..., index: int = ..., i: int = ..., levelOfDetail: str = ..., lod: str = ..., name: str = ..., n: str = ..., object: str = ..., obj: str = ..., objectPosition: str = ..., op: str = ..., objectRotation: str = ..., objectScale: str = ..., os: str = ..., pointDataSource: bool = ..., pds: bool = ..., rotationOrder: str = ..., ro: str = ..., rotationUnits: str = ..., ru: str = ..., valueName: str = ..., vn: str = ..., query: bool = ..., q: bool = ...) -> str:
    """instancer is undoable, queryable, and editable.
    
    This command is used to create a instancer node and set the proper attributes
    in the node.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere(n='myShape')
        cmds.instancer( name='myInstancerNode', a=True, object='myShape' )
    ```

    ---
    - Args:
        - cycle (c): This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential".  The default is "none".
        - cycleStep (cs): This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).
        - cycleStepUnits (csu): This flag sets or queries the cycle step unit attribute for the instancer node.  The options are "frames" or "seconds".  The default is "frames".
        - index (i): This flag is used to query the name of the ith instanced object.
        - levelOfDetail (lod): This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox", "boundingBoxes".  The default is "geometry".
        - name (n): This flag sets or queries the name of the instancer node.
        - object (obj): This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -add and -remove flags.  If neither of these flags is specified on the command line then -add is assumed.
        - objectPosition (op): This flag queries the given objects position.  This object can be any instanced object or sub-object.
        - objectRotation: This flag queries the given objects rotation.  This object can be any instanced object or sub-object.
        - objectScale (os): This flag queries the given objects scale.  This object can be any instanced object or sub-object.
        - pointDataSource (pds): This flag is used to query the source node supply the data for the input points.
        - rotationOrder (ro): This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        - rotationUnits (ru): This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
        - valueName (vn): This flag is used to query the value(s) of the array associated with the given name.  If the -index flag is used in conjuction with this flag then the ith value will be returned.  Otherwise, the entire array will be returned.
        - query (q): Query mode flag
    """
@overload #Overload for instancer in ['edit']
def instancer(addObject: bool = ..., cycle: str = ..., cycleStep: float = ..., cycleStepUnits: str = ..., levelOfDetail: str = ..., object: str = ..., removeObject: bool = ..., rotationOrder: str = ..., rotationUnits: str = ..., edit: bool = ...) -> str:
    """instancer is undoable, queryable, and editable.
    
    This command is used to create a instancer node and set the proper attributes
    in the node.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere(n='myShape')
        cmds.instancer( name='myInstancerNode', a=True, object='myShape' )
    ```

    ---
    - Args:
        - addObject (a): This flag indicates that objects specified by the -object flag will be added to the instancer node as instanced objects.
        - cycle (c): This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential".  The default is "none".
        - cycleStep (cs): This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).
        - cycleStepUnits (csu): This flag sets or queries the cycle step unit attribute for the instancer node.  The options are "frames" or "seconds".  The default is "frames".
        - levelOfDetail (lod): This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox", "boundingBoxes".  The default is "geometry".
        - object (obj): This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -add and -remove flags.  If neither of these flags is specified on the command line then -add is assumed.
        - removeObject (rm): This flag indicates that objects specified by the -object flag will be removed from the instancer node as instanced objects.
        - rotationOrder (ro): This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        - rotationUnits (ru): This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
        - edit (e): Edit mode flag
    """
@overload #Overload for instancer in ['edit']
def instancer(a: bool = ..., c: str = ..., cs: float = ..., csu: str = ..., lod: str = ..., obj: str = ..., rm: bool = ..., ro: str = ..., ru: str = ..., e: bool = ...) -> str:
    """instancer is undoable, queryable, and editable.
    
    This command is used to create a instancer node and set the proper attributes
    in the node.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere(n='myShape')
        cmds.instancer( name='myInstancerNode', a=True, object='myShape' )
    ```

    ---
    - Args:
        - addObject (a): This flag indicates that objects specified by the -object flag will be added to the instancer node as instanced objects.
        - cycle (c): This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential".  The default is "none".
        - cycleStep (cs): This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).
        - cycleStepUnits (csu): This flag sets or queries the cycle step unit attribute for the instancer node.  The options are "frames" or "seconds".  The default is "frames".
        - levelOfDetail (lod): This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox", "boundingBoxes".  The default is "geometry".
        - object (obj): This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -add and -remove flags.  If neither of these flags is specified on the command line then -add is assumed.
        - removeObject (rm): This flag indicates that objects specified by the -object flag will be removed from the instancer node as instanced objects.
        - rotationOrder (ro): This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        - rotationUnits (ru): This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
        - edit (e): Edit mode flag
    """
@overload #Overload for instancer in ['edit']
def instancer(addObject: bool = ..., a: bool = ..., cycle: str = ..., c: str = ..., cycleStep: float = ..., cs: float = ..., cycleStepUnits: str = ..., csu: str = ..., levelOfDetail: str = ..., lod: str = ..., object: str = ..., obj: str = ..., removeObject: bool = ..., rm: bool = ..., rotationOrder: str = ..., ro: str = ..., rotationUnits: str = ..., ru: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """instancer is undoable, queryable, and editable.
    
    This command is used to create a instancer node and set the proper attributes
    in the node.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polySphere(n='myShape')
        cmds.instancer( name='myInstancerNode', a=True, object='myShape' )
    ```

    ---
    - Args:
        - addObject (a): This flag indicates that objects specified by the -object flag will be added to the instancer node as instanced objects.
        - cycle (c): This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential".  The default is "none".
        - cycleStep (cs): This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).
        - cycleStepUnits (csu): This flag sets or queries the cycle step unit attribute for the instancer node.  The options are "frames" or "seconds".  The default is "frames".
        - levelOfDetail (lod): This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox", "boundingBoxes".  The default is "geometry".
        - object (obj): This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -add and -remove flags.  If neither of these flags is specified on the command line then -add is assumed.
        - removeObject (rm): This flag indicates that objects specified by the -object flag will be removed from the instancer node as instanced objects.
        - rotationOrder (ro): This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        - rotationUnits (ru): This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
        - edit (e): Edit mode flag
    """
