"""Stub files for Attributes category in Maya commands, command: connectAttr."""

from typing import Any, overload

@overload #Overload for connectAttr in ['create']
def connectAttr(attribute attribute: attribute attribute, force: bool = ..., lock: bool = ..., nextAvailable: bool = ..., referenceDest: str = ...) -> str:
    """connectAttr is undoable, NOT queryable, and NOT editable.
    
    Connect the attributes of two dependency nodes and return the names of the two
    connected attributes. The connected attributes must be be of compatible types.
    First argument is the source attribute, second one is the destination.
    
    Refer to dependency node documentation.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'transform', n='firstGuy' )
        cmds.createNode( 'transform', n='secondGuy' )
        # Connect the translation of two nodes together
        cmds.connectAttr( 'firstGuy.t', 'secondGuy.translate' )
        # Connect the rotation of one node to the override colour
        # of a second node.
        cmds.connectAttr( 'firstGuy.rotate', 'secondGuy.overrideColor' )
    ```

    ---
    - Args:
        - attribute attribute: Input item(s).
        - force (f): Forces the connection.  If the destination is already connected, the old connection is broken and the new one made.
        - lock (l): If the argument is true, the destination attribute is locked after making the connection. If the argument is false, the connection is unlocked before making the connection.
        - nextAvailable (na): If the destination multi-attribute has set the indexMatters to be false with this flag specified, a connection is made to the next available index. No index need be specified.
        - referenceDest (rd): This flag is used for file io only. The flag indicates that the connection replaces a connection made in a referenced file, and the flag argument indicates the original destination from the referenced file. This flag is used so that if the
            reference file is modified, maya can still attempt to make the appropriate connections in the main scene to the referenced object.
    """
@overload #Overload for connectAttr in ['create']
def connectAttr(attribute attribute: attribute attribute, f: bool = ..., l: bool = ..., na: bool = ..., rd: str = ...) -> str:
    """connectAttr is undoable, NOT queryable, and NOT editable.
    
    Connect the attributes of two dependency nodes and return the names of the two
    connected attributes. The connected attributes must be be of compatible types.
    First argument is the source attribute, second one is the destination.
    
    Refer to dependency node documentation.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'transform', n='firstGuy' )
        cmds.createNode( 'transform', n='secondGuy' )
        # Connect the translation of two nodes together
        cmds.connectAttr( 'firstGuy.t', 'secondGuy.translate' )
        # Connect the rotation of one node to the override colour
        # of a second node.
        cmds.connectAttr( 'firstGuy.rotate', 'secondGuy.overrideColor' )
    ```

    ---
    - Args:
        - attribute attribute: Input item(s).
        - force (f): Forces the connection.  If the destination is already connected, the old connection is broken and the new one made.
        - lock (l): If the argument is true, the destination attribute is locked after making the connection. If the argument is false, the connection is unlocked before making the connection.
        - nextAvailable (na): If the destination multi-attribute has set the indexMatters to be false with this flag specified, a connection is made to the next available index. No index need be specified.
        - referenceDest (rd): This flag is used for file io only. The flag indicates that the connection replaces a connection made in a referenced file, and the flag argument indicates the original destination from the referenced file. This flag is used so that if the
            reference file is modified, maya can still attempt to make the appropriate connections in the main scene to the referenced object.
    """
@overload #Overload for connectAttr in ['create']
def connectAttr(attribute attribute: attribute attribute, force: bool = ..., f: bool = ..., lock: bool = ..., l: bool = ..., nextAvailable: bool = ..., na: bool = ..., referenceDest: str = ..., rd: str = ...) -> str:
    """connectAttr is undoable, NOT queryable, and NOT editable.
    
    Connect the attributes of two dependency nodes and return the names of the two
    connected attributes. The connected attributes must be be of compatible types.
    First argument is the source attribute, second one is the destination.
    
    Refer to dependency node documentation.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'transform', n='firstGuy' )
        cmds.createNode( 'transform', n='secondGuy' )
        # Connect the translation of two nodes together
        cmds.connectAttr( 'firstGuy.t', 'secondGuy.translate' )
        # Connect the rotation of one node to the override colour
        # of a second node.
        cmds.connectAttr( 'firstGuy.rotate', 'secondGuy.overrideColor' )
    ```

    ---
    - Args:
        - attribute attribute: Input item(s).
        - force (f): Forces the connection.  If the destination is already connected, the old connection is broken and the new one made.
        - lock (l): If the argument is true, the destination attribute is locked after making the connection. If the argument is false, the connection is unlocked before making the connection.
        - nextAvailable (na): If the destination multi-attribute has set the indexMatters to be false with this flag specified, a connection is made to the next available index. No index need be specified.
        - referenceDest (rd): This flag is used for file io only. The flag indicates that the connection replaces a connection made in a referenced file, and the flag argument indicates the original destination from the referenced file. This flag is used so that if the
            reference file is modified, maya can still attempt to make the appropriate connections in the main scene to the referenced object.
    """
