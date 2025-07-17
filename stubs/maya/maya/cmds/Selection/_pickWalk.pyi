"""Stub files for Selection category in Maya commands, command: pickWalk."""

from typing import Any, overload

@overload #Overload for pickWalk in ['create']
def pickWalk([objects]: [objects], direction: str = ..., recurse: bool = ..., type: str = ...) -> list[str]:
    """pickWalk is undoable, NOT queryable, and NOT editable.
    
    The pickWalk command allows you to quickly change the selection list relative
    to the nodes that are currently selected. It is called pickWalk, because it
    walks from one selection list to another by unselecting what's currently
    selected, and selecting nodes that are in the specified direction from the
    currently selected list. If you specify objects on the command line, the
    pickWalk command will walk from those objects instead of the selected list.
    
    If the -type flag is instances, then the left and right direction will walk to
    the previous or next instance of the same selected dag node.

    Example:
    ```python
        import maya.cmds as cmds
        # Given the transforms A and B which are parented to a transform C,
        # and C is instanced with parents D and E.
        cmds.pickWalk( 'A', direction='right' )
        cmds.select('|E|C')
        cmds.pickWalk( type='instances', direction='left')
        # The pickWalk command also works on CVs and edit points
        cmds.select('nurbsPlaneShape1.cv[2][1]')
        cmds.pickWalk(direction='right' )
        # Result: nurbsPlaneShape1.cv[3][1] #
        cmds.pickWalk( direction='up' )
        # Result: nurbsPlaneShape1.cv[3][2] #
        cmds.select( 'curveShape2.ep[1]' )
        cmds.pickWalk( direction='left' )
        # Result: curveShape2.ep[0] #
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - direction (d): The direction to walk from the node. The choices are up | down | left | right | in | out. up walks to the parent node, down to the child node, and left and right to the sibling nodes. If a CV on a surface is selected, the left and right
            directions walk in the U parameter direction of the surface, and the up and down directions walk in the V parameter direction. In and out are only used if the type flag is 'latticepoints'. Default is right.
        - recurse (r): If specified then recurse down when walking
        - type (typ): The choices are nodes | instances | edgeloop | edgering | faceloop | keys | latticepoints | motiontrailpoints. If type is nodes, then the left and right direction walk to the next dag siblings. If type is instances, the left and right
            direction walk to the previous or next instance of the same dag node. If type is edgeloop, then the edge loop starting at the first selected edge will be selected. If type is edgering, then the edge ring starting at the first selected edge
            will be selected. If type is faceloop, and there are two connected quad faces selected which define a face loop, then that face loop will be selected.  edgeloop, edgering and faceloop all remember which was the first edge or faces selected
            for as long as consecutive selections are made by this command.  They use this information to determine what the "next" loop or ring selection should be.  Users can make selections forwards and backwards by using the direction flag with
            "left" or "right".  If type is motiontrailpoints, then the left and right direction walk to the previous or next motion trail points respectively.  Default is nodes.
    """
@overload #Overload for pickWalk in ['create']
def pickWalk([objects]: [objects], d: str = ..., r: bool = ..., typ: str = ...) -> list[str]:
    """pickWalk is undoable, NOT queryable, and NOT editable.
    
    The pickWalk command allows you to quickly change the selection list relative
    to the nodes that are currently selected. It is called pickWalk, because it
    walks from one selection list to another by unselecting what's currently
    selected, and selecting nodes that are in the specified direction from the
    currently selected list. If you specify objects on the command line, the
    pickWalk command will walk from those objects instead of the selected list.
    
    If the -type flag is instances, then the left and right direction will walk to
    the previous or next instance of the same selected dag node.

    Example:
    ```python
        import maya.cmds as cmds
        # Given the transforms A and B which are parented to a transform C,
        # and C is instanced with parents D and E.
        cmds.pickWalk( 'A', direction='right' )
        cmds.select('|E|C')
        cmds.pickWalk( type='instances', direction='left')
        # The pickWalk command also works on CVs and edit points
        cmds.select('nurbsPlaneShape1.cv[2][1]')
        cmds.pickWalk(direction='right' )
        # Result: nurbsPlaneShape1.cv[3][1] #
        cmds.pickWalk( direction='up' )
        # Result: nurbsPlaneShape1.cv[3][2] #
        cmds.select( 'curveShape2.ep[1]' )
        cmds.pickWalk( direction='left' )
        # Result: curveShape2.ep[0] #
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - direction (d): The direction to walk from the node. The choices are up | down | left | right | in | out. up walks to the parent node, down to the child node, and left and right to the sibling nodes. If a CV on a surface is selected, the left and right
            directions walk in the U parameter direction of the surface, and the up and down directions walk in the V parameter direction. In and out are only used if the type flag is 'latticepoints'. Default is right.
        - recurse (r): If specified then recurse down when walking
        - type (typ): The choices are nodes | instances | edgeloop | edgering | faceloop | keys | latticepoints | motiontrailpoints. If type is nodes, then the left and right direction walk to the next dag siblings. If type is instances, the left and right
            direction walk to the previous or next instance of the same dag node. If type is edgeloop, then the edge loop starting at the first selected edge will be selected. If type is edgering, then the edge ring starting at the first selected edge
            will be selected. If type is faceloop, and there are two connected quad faces selected which define a face loop, then that face loop will be selected.  edgeloop, edgering and faceloop all remember which was the first edge or faces selected
            for as long as consecutive selections are made by this command.  They use this information to determine what the "next" loop or ring selection should be.  Users can make selections forwards and backwards by using the direction flag with
            "left" or "right".  If type is motiontrailpoints, then the left and right direction walk to the previous or next motion trail points respectively.  Default is nodes.
    """
@overload #Overload for pickWalk in ['create']
def pickWalk([objects]: [objects], direction: str = ..., d: str = ..., recurse: bool = ..., r: bool = ..., type: str = ..., typ: str = ...) -> list[str]:
    """pickWalk is undoable, NOT queryable, and NOT editable.
    
    The pickWalk command allows you to quickly change the selection list relative
    to the nodes that are currently selected. It is called pickWalk, because it
    walks from one selection list to another by unselecting what's currently
    selected, and selecting nodes that are in the specified direction from the
    currently selected list. If you specify objects on the command line, the
    pickWalk command will walk from those objects instead of the selected list.
    
    If the -type flag is instances, then the left and right direction will walk to
    the previous or next instance of the same selected dag node.

    Example:
    ```python
        import maya.cmds as cmds
        # Given the transforms A and B which are parented to a transform C,
        # and C is instanced with parents D and E.
        cmds.pickWalk( 'A', direction='right' )
        cmds.select('|E|C')
        cmds.pickWalk( type='instances', direction='left')
        # The pickWalk command also works on CVs and edit points
        cmds.select('nurbsPlaneShape1.cv[2][1]')
        cmds.pickWalk(direction='right' )
        # Result: nurbsPlaneShape1.cv[3][1] #
        cmds.pickWalk( direction='up' )
        # Result: nurbsPlaneShape1.cv[3][2] #
        cmds.select( 'curveShape2.ep[1]' )
        cmds.pickWalk( direction='left' )
        # Result: curveShape2.ep[0] #
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - direction (d): The direction to walk from the node. The choices are up | down | left | right | in | out. up walks to the parent node, down to the child node, and left and right to the sibling nodes. If a CV on a surface is selected, the left and right
            directions walk in the U parameter direction of the surface, and the up and down directions walk in the V parameter direction. In and out are only used if the type flag is 'latticepoints'. Default is right.
        - recurse (r): If specified then recurse down when walking
        - type (typ): The choices are nodes | instances | edgeloop | edgering | faceloop | keys | latticepoints | motiontrailpoints. If type is nodes, then the left and right direction walk to the next dag siblings. If type is instances, the left and right
            direction walk to the previous or next instance of the same dag node. If type is edgeloop, then the edge loop starting at the first selected edge will be selected. If type is edgering, then the edge ring starting at the first selected edge
            will be selected. If type is faceloop, and there are two connected quad faces selected which define a face loop, then that face loop will be selected.  edgeloop, edgering and faceloop all remember which was the first edge or faces selected
            for as long as consecutive selections are made by this command.  They use this information to determine what the "next" loop or ring selection should be.  Users can make selections forwards and backwards by using the direction flag with
            "left" or "right".  If type is motiontrailpoints, then the left and right direction walk to the previous or next motion trail points respectively.  Default is nodes.
    """
