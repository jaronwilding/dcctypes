"""Stub files for Attributes category in Maya commands, command: nodeCast."""

from typing import Any, overload

@overload #Overload for nodeCast in ['create']
def nodeCast(stringstring: stringstring, copyDynamicAttrs: bool = ..., disableAPICallbacks: bool = ..., disableScriptJobCallbacks: bool = ..., disconnectUnmatchedAttrs: bool = ..., force: bool = ..., swapNames: bool = ..., swapValues: bool = ...) -> int:
    """nodeCast is undoable, NOT queryable, and NOT editable.
    
    Given two nodes, a source node of type A and a target node of type B, where
    type A is either type B or a sub-type of B, this command will replace the
    target node with the source node. That is, all node connections, DAG hierarchy
    and attribute values on the target node will be removed from the target node
    and placed on the source node. This operation will fail if either object is
    referenced, locked or if the nodes do not share a common sub-type. This
    operation is atomic. If the given parameters fail, then the source and target
    nodes will remain in their initial state prior to execution of the command.
    IMPORTANT: the command will currently ignore instance connections and instance
    objects. It will also ignore reference nodes.

    Example:
    ```python
        import maya.cmds as cmds
        tr1 = cmds.createNode( 'transform' )
        tr2 = cmds.createNode( 'transform' )
        cmds.connectAttr( tr1 + ".t", tr2 + ".t" )
        cmds.connectAttr( tr2 + ".r", tr1 + ".r" )
        theT = tr1
        cmds.select( theT, replace=1 )
        cmds.addAttr( ln="unmatched", at="long" )
        middle_man = cmds.createNode( 'transform' )
        cmds.connectAttr( theT + ".unmatched", middle_man + ".tx" )
        swapNode = cmds.createNode( 'transform' )
        cmds.nodeCast( theT, swapNode, disconnectUnmatchedAttrs=true )
    ```

    ---
    - Args:
        - stringstring: Input item(s).
        - copyDynamicAttrs (cda): If the target node contains any dynamic attributes that are not defined on the source node, then create identical dynamic attricutes on the source node and copy the values and connections from the target node into them.
        - disableAPICallbacks (dsa): add comment
        - disableScriptJobCallbacks (dsj): add comment
        - disconnectUnmatchedAttrs (dua): If the node that is being swapped out has any connections that do not exist on the target node, then indicate if the connection should be disconnected. By default these connections are not removed because they cannot be restored if the
            target node is swapped back with the source node.
        - force (f): Forces the command to do the node cast operation even if the nodes do not share a common base object. When this flag is specified the command will try to do the best possible attribute matching when swapping the command.  It
            isnotrecommended to use the '-swapValues/sv' flag with this flag.
        - swapNames (sn): Swap the names of the nodes. By default names are not swapped.
        - swapValues (sv): Indicates if the commands should exchange attributes on the common attributes between the two nodes.  For example, if the nodes are the same base type as a transform node, then rotate, scale, translate values would be copied over.
    """
@overload #Overload for nodeCast in ['create']
def nodeCast(stringstring: stringstring, cda: bool = ..., dsa: bool = ..., dsj: bool = ..., dua: bool = ..., f: bool = ..., sn: bool = ..., sv: bool = ...) -> int:
    """nodeCast is undoable, NOT queryable, and NOT editable.
    
    Given two nodes, a source node of type A and a target node of type B, where
    type A is either type B or a sub-type of B, this command will replace the
    target node with the source node. That is, all node connections, DAG hierarchy
    and attribute values on the target node will be removed from the target node
    and placed on the source node. This operation will fail if either object is
    referenced, locked or if the nodes do not share a common sub-type. This
    operation is atomic. If the given parameters fail, then the source and target
    nodes will remain in their initial state prior to execution of the command.
    IMPORTANT: the command will currently ignore instance connections and instance
    objects. It will also ignore reference nodes.

    Example:
    ```python
        import maya.cmds as cmds
        tr1 = cmds.createNode( 'transform' )
        tr2 = cmds.createNode( 'transform' )
        cmds.connectAttr( tr1 + ".t", tr2 + ".t" )
        cmds.connectAttr( tr2 + ".r", tr1 + ".r" )
        theT = tr1
        cmds.select( theT, replace=1 )
        cmds.addAttr( ln="unmatched", at="long" )
        middle_man = cmds.createNode( 'transform' )
        cmds.connectAttr( theT + ".unmatched", middle_man + ".tx" )
        swapNode = cmds.createNode( 'transform' )
        cmds.nodeCast( theT, swapNode, disconnectUnmatchedAttrs=true )
    ```

    ---
    - Args:
        - stringstring: Input item(s).
        - copyDynamicAttrs (cda): If the target node contains any dynamic attributes that are not defined on the source node, then create identical dynamic attricutes on the source node and copy the values and connections from the target node into them.
        - disableAPICallbacks (dsa): add comment
        - disableScriptJobCallbacks (dsj): add comment
        - disconnectUnmatchedAttrs (dua): If the node that is being swapped out has any connections that do not exist on the target node, then indicate if the connection should be disconnected. By default these connections are not removed because they cannot be restored if the
            target node is swapped back with the source node.
        - force (f): Forces the command to do the node cast operation even if the nodes do not share a common base object. When this flag is specified the command will try to do the best possible attribute matching when swapping the command.  It
            isnotrecommended to use the '-swapValues/sv' flag with this flag.
        - swapNames (sn): Swap the names of the nodes. By default names are not swapped.
        - swapValues (sv): Indicates if the commands should exchange attributes on the common attributes between the two nodes.  For example, if the nodes are the same base type as a transform node, then rotate, scale, translate values would be copied over.
    """
@overload #Overload for nodeCast in ['create']
def nodeCast(stringstring: stringstring, copyDynamicAttrs: bool = ..., cda: bool = ..., disableAPICallbacks: bool = ..., dsa: bool = ..., disableScriptJobCallbacks: bool = ..., dsj: bool = ..., disconnectUnmatchedAttrs: bool = ..., dua: bool = ..., force: bool = ..., f: bool = ..., swapNames: bool = ..., sn: bool = ..., swapValues: bool = ..., sv: bool = ...) -> int:
    """nodeCast is undoable, NOT queryable, and NOT editable.
    
    Given two nodes, a source node of type A and a target node of type B, where
    type A is either type B or a sub-type of B, this command will replace the
    target node with the source node. That is, all node connections, DAG hierarchy
    and attribute values on the target node will be removed from the target node
    and placed on the source node. This operation will fail if either object is
    referenced, locked or if the nodes do not share a common sub-type. This
    operation is atomic. If the given parameters fail, then the source and target
    nodes will remain in their initial state prior to execution of the command.
    IMPORTANT: the command will currently ignore instance connections and instance
    objects. It will also ignore reference nodes.

    Example:
    ```python
        import maya.cmds as cmds
        tr1 = cmds.createNode( 'transform' )
        tr2 = cmds.createNode( 'transform' )
        cmds.connectAttr( tr1 + ".t", tr2 + ".t" )
        cmds.connectAttr( tr2 + ".r", tr1 + ".r" )
        theT = tr1
        cmds.select( theT, replace=1 )
        cmds.addAttr( ln="unmatched", at="long" )
        middle_man = cmds.createNode( 'transform' )
        cmds.connectAttr( theT + ".unmatched", middle_man + ".tx" )
        swapNode = cmds.createNode( 'transform' )
        cmds.nodeCast( theT, swapNode, disconnectUnmatchedAttrs=true )
    ```

    ---
    - Args:
        - stringstring: Input item(s).
        - copyDynamicAttrs (cda): If the target node contains any dynamic attributes that are not defined on the source node, then create identical dynamic attricutes on the source node and copy the values and connections from the target node into them.
        - disableAPICallbacks (dsa): add comment
        - disableScriptJobCallbacks (dsj): add comment
        - disconnectUnmatchedAttrs (dua): If the node that is being swapped out has any connections that do not exist on the target node, then indicate if the connection should be disconnected. By default these connections are not removed because they cannot be restored if the
            target node is swapped back with the source node.
        - force (f): Forces the command to do the node cast operation even if the nodes do not share a common base object. When this flag is specified the command will try to do the best possible attribute matching when swapping the command.  It
            isnotrecommended to use the '-swapValues/sv' flag with this flag.
        - swapNames (sn): Swap the names of the nodes. By default names are not swapped.
        - swapValues (sv): Indicates if the commands should exchange attributes on the common attributes between the two nodes.  For example, if the nodes are the same base type as a transform node, then rotate, scale, translate values would be copied over.
    """
