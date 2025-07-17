"""Stub files for Attributes category in Maya commands, command: listRelatives."""

from typing import Any, overload

@overload #Overload for listRelatives in ['create']
def listRelatives([objects]: [objects], allDescendents: bool = ..., allParents: bool = ..., children: bool = ..., fullPath: bool = ..., noIntermediate: bool = ..., parent: bool = ..., path: bool = ..., shapes: bool = ..., type: str = ...) -> list[str]:
    """listRelatives is undoable, NOT queryable, and NOT editable.
    
    This command lists parents and children of DAG objects. The flags -c/children,
    -ad/allDescendents, -s/shapes, -p/parent and -ap/allParents are mutually
    exclusive. Only one can be used in a command.
    
    Unlike ls, this command does not return a unique path but simply returns the
    object's name by default. To get a unique path the -path flag must be used.
    
    When listing parents of objects directly under the world, the command will
    return an empty parent list. Listing parents of objects directly under a shape
    (underworld objects) will return their containing shape node in the list of
    parents. Listing parents of components of objects will return the object.
    
    When listing children, shape nodes will return their underworld objects in the
    list of children. Listing children of components of objects returns nothing.
    
    The -ni/noIntermediate flag works with the -s/shapes flag. It causes any
    intermediate shapes among the descendents to be ignored.

    Example:
    ```python
        import maya.cmds as cmds
        # create an object and an instance for queries
        cmds.sphere( n='nexus' )
        cmds.instance( n='ball' )
        # List the name of the shape below the transform node.
        shapes = cmds.listRelatives('nexus')
        # list all parents of shape
        # (The result of the command is shown)
        cmds.listRelatives( shapes[0], allParents=True )
        # Result:[u'nexus', u'ball'] #
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - allDescendents (ad): Returns all the children, grand-children etc. of this dag node.  If a descendent is instanced, it will appear only once on the list returned. Note that it lists grand-children before children.
        - allParents (ap): Returns all the parents of this dag node. Normally, this command only returns the parent corresponding to the first instance of the object
        - children (c): List all the children of this dag node (default).
        - fullPath (f): Return full pathnames instead of object names.
        - noIntermediate (ni): No intermediate objects
        - parent (p): Returns the parent of this dag node
        - path (pa): Return a proper object name that can be passed to other commands.
        - shapes (s): List all the children of this dag node that are shapes (ie, not transforms)
        - type (typ): List all relatives of the specified type.
    """
@overload #Overload for listRelatives in ['create']
def listRelatives([objects]: [objects], ad: bool = ..., ap: bool = ..., c: bool = ..., f: bool = ..., ni: bool = ..., p: bool = ..., pa: bool = ..., s: bool = ..., typ: str = ...) -> list[str]:
    """listRelatives is undoable, NOT queryable, and NOT editable.
    
    This command lists parents and children of DAG objects. The flags -c/children,
    -ad/allDescendents, -s/shapes, -p/parent and -ap/allParents are mutually
    exclusive. Only one can be used in a command.
    
    Unlike ls, this command does not return a unique path but simply returns the
    object's name by default. To get a unique path the -path flag must be used.
    
    When listing parents of objects directly under the world, the command will
    return an empty parent list. Listing parents of objects directly under a shape
    (underworld objects) will return their containing shape node in the list of
    parents. Listing parents of components of objects will return the object.
    
    When listing children, shape nodes will return their underworld objects in the
    list of children. Listing children of components of objects returns nothing.
    
    The -ni/noIntermediate flag works with the -s/shapes flag. It causes any
    intermediate shapes among the descendents to be ignored.

    Example:
    ```python
        import maya.cmds as cmds
        # create an object and an instance for queries
        cmds.sphere( n='nexus' )
        cmds.instance( n='ball' )
        # List the name of the shape below the transform node.
        shapes = cmds.listRelatives('nexus')
        # list all parents of shape
        # (The result of the command is shown)
        cmds.listRelatives( shapes[0], allParents=True )
        # Result:[u'nexus', u'ball'] #
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - allDescendents (ad): Returns all the children, grand-children etc. of this dag node.  If a descendent is instanced, it will appear only once on the list returned. Note that it lists grand-children before children.
        - allParents (ap): Returns all the parents of this dag node. Normally, this command only returns the parent corresponding to the first instance of the object
        - children (c): List all the children of this dag node (default).
        - fullPath (f): Return full pathnames instead of object names.
        - noIntermediate (ni): No intermediate objects
        - parent (p): Returns the parent of this dag node
        - path (pa): Return a proper object name that can be passed to other commands.
        - shapes (s): List all the children of this dag node that are shapes (ie, not transforms)
        - type (typ): List all relatives of the specified type.
    """
@overload #Overload for listRelatives in ['create']
def listRelatives([objects]: [objects], allDescendents: bool = ..., ad: bool = ..., allParents: bool = ..., ap: bool = ..., children: bool = ..., c: bool = ..., fullPath: bool = ..., f: bool = ..., noIntermediate: bool = ..., ni: bool = ..., parent: bool = ..., p: bool = ..., path: bool = ..., pa: bool = ..., shapes: bool = ..., s: bool = ..., type: str = ..., typ: str = ...) -> list[str]:
    """listRelatives is undoable, NOT queryable, and NOT editable.
    
    This command lists parents and children of DAG objects. The flags -c/children,
    -ad/allDescendents, -s/shapes, -p/parent and -ap/allParents are mutually
    exclusive. Only one can be used in a command.
    
    Unlike ls, this command does not return a unique path but simply returns the
    object's name by default. To get a unique path the -path flag must be used.
    
    When listing parents of objects directly under the world, the command will
    return an empty parent list. Listing parents of objects directly under a shape
    (underworld objects) will return their containing shape node in the list of
    parents. Listing parents of components of objects will return the object.
    
    When listing children, shape nodes will return their underworld objects in the
    list of children. Listing children of components of objects returns nothing.
    
    The -ni/noIntermediate flag works with the -s/shapes flag. It causes any
    intermediate shapes among the descendents to be ignored.

    Example:
    ```python
        import maya.cmds as cmds
        # create an object and an instance for queries
        cmds.sphere( n='nexus' )
        cmds.instance( n='ball' )
        # List the name of the shape below the transform node.
        shapes = cmds.listRelatives('nexus')
        # list all parents of shape
        # (The result of the command is shown)
        cmds.listRelatives( shapes[0], allParents=True )
        # Result:[u'nexus', u'ball'] #
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - allDescendents (ad): Returns all the children, grand-children etc. of this dag node.  If a descendent is instanced, it will appear only once on the list returned. Note that it lists grand-children before children.
        - allParents (ap): Returns all the parents of this dag node. Normally, this command only returns the parent corresponding to the first instance of the object
        - children (c): List all the children of this dag node (default).
        - fullPath (f): Return full pathnames instead of object names.
        - noIntermediate (ni): No intermediate objects
        - parent (p): Returns the parent of this dag node
        - path (pa): Return a proper object name that can be passed to other commands.
        - shapes (s): List all the children of this dag node that are shapes (ie, not transforms)
        - type (typ): List all relatives of the specified type.
    """
