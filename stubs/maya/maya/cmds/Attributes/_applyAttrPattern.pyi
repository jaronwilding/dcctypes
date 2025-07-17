"""Stub files for Attributes category in Maya commands, command: applyAttrPattern."""

from typing import Any, overload

@overload #Overload for applyAttrPattern in ['create']
def applyAttrPattern(nodeType: str = ..., patternName: str = ...) -> int:
    """applyAttrPattern is undoable, NOT queryable, and NOT editable.
    
    Take the attribute structure described by a pre-defined pattern and apply it
    either to a node (as dynamic attributes) or a node type (as extension
    attributes). The same pattern can be applied more than once to different nodes
    or node types as the operation duplicates the attribute structure described by
    the pattern. See the 'createAttrPatterns' command for a description of how to
    create a pattern.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.polySphere( name="sphere1" )
        cmds.applyAttrPattern( patternName="myXMLPattern" )
        // Result: 1 //
        name2 = cmds.polySphere( name="sphere2" )
        name3 = cmds.polySphere( name="sphere3" )
        cmds.select( [name2, name3] )
        cmds.applyAttrPattern( patternName="myXMLPattern" )
        // Result: 2 //
        cmds.applyAttrPattern( patternName="myXMLPattern", nodeType="transform" )
        // Result: 1 //
    ```

    ---
    - Args:
        - nodeType (nt): Name of the node type to which the attribute pattern is to be applied. This flag will cause a new extension attribute tree to be created, making the new attributes available on all nodes of the given type. If it is not specified then either
            a node name must be specified or a node must be selected for application of dynamic attributes.
        - patternName (pn): The name of the pattern to apply. The pattern with this name must have been previously created using the createAttrPatterns command.
    """
@overload #Overload for applyAttrPattern in ['create']
def applyAttrPattern(nt: str = ..., pn: str = ...) -> int:
    """applyAttrPattern is undoable, NOT queryable, and NOT editable.
    
    Take the attribute structure described by a pre-defined pattern and apply it
    either to a node (as dynamic attributes) or a node type (as extension
    attributes). The same pattern can be applied more than once to different nodes
    or node types as the operation duplicates the attribute structure described by
    the pattern. See the 'createAttrPatterns' command for a description of how to
    create a pattern.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.polySphere( name="sphere1" )
        cmds.applyAttrPattern( patternName="myXMLPattern" )
        // Result: 1 //
        name2 = cmds.polySphere( name="sphere2" )
        name3 = cmds.polySphere( name="sphere3" )
        cmds.select( [name2, name3] )
        cmds.applyAttrPattern( patternName="myXMLPattern" )
        // Result: 2 //
        cmds.applyAttrPattern( patternName="myXMLPattern", nodeType="transform" )
        // Result: 1 //
    ```

    ---
    - Args:
        - nodeType (nt): Name of the node type to which the attribute pattern is to be applied. This flag will cause a new extension attribute tree to be created, making the new attributes available on all nodes of the given type. If it is not specified then either
            a node name must be specified or a node must be selected for application of dynamic attributes.
        - patternName (pn): The name of the pattern to apply. The pattern with this name must have been previously created using the createAttrPatterns command.
    """
@overload #Overload for applyAttrPattern in ['create']
def applyAttrPattern(nodeType: str = ..., nt: str = ..., patternName: str = ..., pn: str = ...) -> int:
    """applyAttrPattern is undoable, NOT queryable, and NOT editable.
    
    Take the attribute structure described by a pre-defined pattern and apply it
    either to a node (as dynamic attributes) or a node type (as extension
    attributes). The same pattern can be applied more than once to different nodes
    or node types as the operation duplicates the attribute structure described by
    the pattern. See the 'createAttrPatterns' command for a description of how to
    create a pattern.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.polySphere( name="sphere1" )
        cmds.applyAttrPattern( patternName="myXMLPattern" )
        // Result: 1 //
        name2 = cmds.polySphere( name="sphere2" )
        name3 = cmds.polySphere( name="sphere3" )
        cmds.select( [name2, name3] )
        cmds.applyAttrPattern( patternName="myXMLPattern" )
        // Result: 2 //
        cmds.applyAttrPattern( patternName="myXMLPattern", nodeType="transform" )
        // Result: 1 //
    ```

    ---
    - Args:
        - nodeType (nt): Name of the node type to which the attribute pattern is to be applied. This flag will cause a new extension attribute tree to be created, making the new attributes available on all nodes of the given type. If it is not specified then either
            a node name must be specified or a node must be selected for application of dynamic attributes.
        - patternName (pn): The name of the pattern to apply. The pattern with this name must have been previously created using the createAttrPatterns command.
    """
