"""Stub files for Selection category in Maya commands, command: expandedSelection."""

from typing import Any, overload

@overload #Overload for expandedSelection in ['create']
def expandedSelection(depth: int = ..., expansionType: str = ...) -> str | list[str] | list[str]:
    """expandedSelection is NOT undoable, NOT queryable, and NOT editable.
    
    Examines the current selection list and returns that list, expanded to meet
    certain criteria. See the command flags for the exact criteria that will be
    used.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'transform' name='t1' )
        cmds.createNode( 'transform' name='t2' )
        cmds.connectAttr( 't1.tx', 't2.tx' )
        cmds.select( 't1' );
        # Get the list of all DG nodes at most one connection away from the selected one, including it
        cmds.expandedSelection( depth=1, expansionType='DG' )
        # Result: ['t1', 't2'] #
    ```

    ---
    - Args:
        - depth (d): Number of steps away from current selection to expand to. A value of 0 will not expand the selection at all.
        - expansionType (et): The type of graph along which to expand the selection. Legal values are:DG : Use the normal DG connectionsEG : Use the evaluation graph connectionsSG : Use the scheduling graph connections within the evaluation graphIf the actual selected
            node is not included in the graph being expanded on, e.g. there is no evaluation node when using theEGtype, then the selected node will not appear in the output. If this flag is not specified then the type defaults to DG.
    """
@overload #Overload for expandedSelection in ['create']
def expandedSelection(d: int = ..., et: str = ...) -> str | list[str] | list[str]:
    """expandedSelection is NOT undoable, NOT queryable, and NOT editable.
    
    Examines the current selection list and returns that list, expanded to meet
    certain criteria. See the command flags for the exact criteria that will be
    used.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'transform' name='t1' )
        cmds.createNode( 'transform' name='t2' )
        cmds.connectAttr( 't1.tx', 't2.tx' )
        cmds.select( 't1' );
        # Get the list of all DG nodes at most one connection away from the selected one, including it
        cmds.expandedSelection( depth=1, expansionType='DG' )
        # Result: ['t1', 't2'] #
    ```

    ---
    - Args:
        - depth (d): Number of steps away from current selection to expand to. A value of 0 will not expand the selection at all.
        - expansionType (et): The type of graph along which to expand the selection. Legal values are:DG : Use the normal DG connectionsEG : Use the evaluation graph connectionsSG : Use the scheduling graph connections within the evaluation graphIf the actual selected
            node is not included in the graph being expanded on, e.g. there is no evaluation node when using theEGtype, then the selected node will not appear in the output. If this flag is not specified then the type defaults to DG.
    """
@overload #Overload for expandedSelection in ['create']
def expandedSelection(depth: int = ..., d: int = ..., expansionType: str = ..., et: str = ...) -> str | list[str] | list[str]:
    """expandedSelection is NOT undoable, NOT queryable, and NOT editable.
    
    Examines the current selection list and returns that list, expanded to meet
    certain criteria. See the command flags for the exact criteria that will be
    used.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'transform' name='t1' )
        cmds.createNode( 'transform' name='t2' )
        cmds.connectAttr( 't1.tx', 't2.tx' )
        cmds.select( 't1' );
        # Get the list of all DG nodes at most one connection away from the selected one, including it
        cmds.expandedSelection( depth=1, expansionType='DG' )
        # Result: ['t1', 't2'] #
    ```

    ---
    - Args:
        - depth (d): Number of steps away from current selection to expand to. A value of 0 will not expand the selection at all.
        - expansionType (et): The type of graph along which to expand the selection. Legal values are:DG : Use the normal DG connectionsEG : Use the evaluation graph connectionsSG : Use the scheduling graph connections within the evaluation graphIf the actual selected
            node is not included in the graph being expanded on, e.g. there is no evaluation node when using theEGtype, then the selected node will not appear in the output. If this flag is not specified then the type defaults to DG.
    """
