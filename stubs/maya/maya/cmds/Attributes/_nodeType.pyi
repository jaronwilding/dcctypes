"""Stub files for Attributes category in Maya commands, command: nodeType."""

from typing import Any, overload

@overload #Overload for nodeType in ['create']
def nodeType(string: str, apiType: bool = ..., derived: bool = ..., inherited: bool = ..., isTypeName: bool = ..., ufeRuntimeName: bool = ...) -> str | list[str]:
    """nodeType is undoable, NOT queryable, and NOT editable.
    
    This command returns a string which identifies the given node's type.
    
    When no flags are used, the unique type name is returned. This can be useful
    for seeing if two nodes are of the same type.
    
    When the api flag is used, the MFn::Type of the node is returned. This can be
    useful for seeing if a plug-in node belongs to a given class. The api flag
    cannot be used in conjunction with any other flags.
    
    When the derived flag is used, the command returns a string array containing
    the names of all the currently known node types which derive from the node
    type of the given object.
    
    When the inherited flag is used, the command returns a string array containing
    the names of all the base node types inherited by the the given node.
    
    If the isTypeName flag is present then the argument provided to the command is
    taken to be the name of a node type rather than the name of a specific node.
    This makes it possible to query the hierarchy of node types without needing to
    have instances of each node type.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere( n='balloon' )
        # Find the type of node created by the sphere command
        cmds.nodeType( 'balloon' )
        # Result: transform #
        # What is the API type of the balloon node?
        cmds.nodeType( 'balloon', api=True )
        # Result: kTransform #
        # Which node types derive from camera?
        cmds.nodeType( 'camera', derived=True, isTypeName=True )
        # Result: [u'stereoRigCamera', u'camera'] #
    ```

    ---
    - Args:
        - string: Input item(s).
        - apiType (api): Return the MFn::Type value (as a string) corresponding to the given node.  This is particularly useful when the given node is defined by a plug-in, since in this case, the MFn::Type value corresponds to the underlying proxy class.This flag
            cannot be used in combination with any of the other flags.
        - derived (d): Return a string array containing the names of all the currently known node types which derive from the type of the specified node.
        - inherited (i): Return a string array containing the names of all the base node types inherited by the specified node.
        - isTypeName (itn): If this flag is present, then the argument provided to the command is the name of a node type rather than the name of a specific node.
        - ufeRuntimeName (urn): Return the UFE Runtime name corresponding to the given node. This is particularly useful to filter between native Maya objects and non-native objects exposed to Maya through the UFE interface.
    """
@overload #Overload for nodeType in ['create']
def nodeType(string: str, api: bool = ..., d: bool = ..., i: bool = ..., itn: bool = ..., urn: bool = ...) -> str | list[str]:
    """nodeType is undoable, NOT queryable, and NOT editable.
    
    This command returns a string which identifies the given node's type.
    
    When no flags are used, the unique type name is returned. This can be useful
    for seeing if two nodes are of the same type.
    
    When the api flag is used, the MFn::Type of the node is returned. This can be
    useful for seeing if a plug-in node belongs to a given class. The api flag
    cannot be used in conjunction with any other flags.
    
    When the derived flag is used, the command returns a string array containing
    the names of all the currently known node types which derive from the node
    type of the given object.
    
    When the inherited flag is used, the command returns a string array containing
    the names of all the base node types inherited by the the given node.
    
    If the isTypeName flag is present then the argument provided to the command is
    taken to be the name of a node type rather than the name of a specific node.
    This makes it possible to query the hierarchy of node types without needing to
    have instances of each node type.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere( n='balloon' )
        # Find the type of node created by the sphere command
        cmds.nodeType( 'balloon' )
        # Result: transform #
        # What is the API type of the balloon node?
        cmds.nodeType( 'balloon', api=True )
        # Result: kTransform #
        # Which node types derive from camera?
        cmds.nodeType( 'camera', derived=True, isTypeName=True )
        # Result: [u'stereoRigCamera', u'camera'] #
    ```

    ---
    - Args:
        - string: Input item(s).
        - apiType (api): Return the MFn::Type value (as a string) corresponding to the given node.  This is particularly useful when the given node is defined by a plug-in, since in this case, the MFn::Type value corresponds to the underlying proxy class.This flag
            cannot be used in combination with any of the other flags.
        - derived (d): Return a string array containing the names of all the currently known node types which derive from the type of the specified node.
        - inherited (i): Return a string array containing the names of all the base node types inherited by the specified node.
        - isTypeName (itn): If this flag is present, then the argument provided to the command is the name of a node type rather than the name of a specific node.
        - ufeRuntimeName (urn): Return the UFE Runtime name corresponding to the given node. This is particularly useful to filter between native Maya objects and non-native objects exposed to Maya through the UFE interface.
    """
@overload #Overload for nodeType in ['create']
def nodeType(string: str, apiType: bool = ..., api: bool = ..., derived: bool = ..., d: bool = ..., inherited: bool = ..., i: bool = ..., isTypeName: bool = ..., itn: bool = ..., ufeRuntimeName: bool = ..., urn: bool = ...) -> str | list[str]:
    """nodeType is undoable, NOT queryable, and NOT editable.
    
    This command returns a string which identifies the given node's type.
    
    When no flags are used, the unique type name is returned. This can be useful
    for seeing if two nodes are of the same type.
    
    When the api flag is used, the MFn::Type of the node is returned. This can be
    useful for seeing if a plug-in node belongs to a given class. The api flag
    cannot be used in conjunction with any other flags.
    
    When the derived flag is used, the command returns a string array containing
    the names of all the currently known node types which derive from the node
    type of the given object.
    
    When the inherited flag is used, the command returns a string array containing
    the names of all the base node types inherited by the the given node.
    
    If the isTypeName flag is present then the argument provided to the command is
    taken to be the name of a node type rather than the name of a specific node.
    This makes it possible to query the hierarchy of node types without needing to
    have instances of each node type.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.sphere( n='balloon' )
        # Find the type of node created by the sphere command
        cmds.nodeType( 'balloon' )
        # Result: transform #
        # What is the API type of the balloon node?
        cmds.nodeType( 'balloon', api=True )
        # Result: kTransform #
        # Which node types derive from camera?
        cmds.nodeType( 'camera', derived=True, isTypeName=True )
        # Result: [u'stereoRigCamera', u'camera'] #
    ```

    ---
    - Args:
        - string: Input item(s).
        - apiType (api): Return the MFn::Type value (as a string) corresponding to the given node.  This is particularly useful when the given node is defined by a plug-in, since in this case, the MFn::Type value corresponds to the underlying proxy class.This flag
            cannot be used in combination with any of the other flags.
        - derived (d): Return a string array containing the names of all the currently known node types which derive from the type of the specified node.
        - inherited (i): Return a string array containing the names of all the base node types inherited by the specified node.
        - isTypeName (itn): If this flag is present, then the argument provided to the command is the name of a node type rather than the name of a specific node.
        - ufeRuntimeName (urn): Return the UFE Runtime name corresponding to the given node. This is particularly useful to filter between native Maya objects and non-native objects exposed to Maya through the UFE interface.
    """
