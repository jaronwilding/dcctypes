"""Stub files for General category in Maya commands, command: reorderContainer."""

from typing import Any, overload

@overload #Overload for reorderContainer in ['create']
def reorderContainer(back: bool = ..., front: bool = ..., relative: int = ...) -> None:
    """reorderContainer is undoable, queryable, and editable.
    
    This command reorders (moves) objects relative to their siblings in a
    container.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    Only nodes within one container can be moved at a time. Note: The container
    command's -nodeList flag will return a sorted list of contained nodes. To see
    the effects of reordering, use the -unsortedOrder flag in conjunction with the
    -nodeList flag.

    Example:
    ```python
        import maya.cmds as cmds
        # create a container
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sphere( n='sphere3' )
        cmds.sphere( n='sphere4' )
        cmds.container( addNode=['sphere1', 'sphere2', 'sphere3', 'sphere4'], n='sphereCon' )
        # The container sphereCon contains sphere1, sphere2, sphere3 and sphere4.
        # The command below moves sphere2 before sphere1.
        cmds.reorderContainer( 'sphere2', r=-1 )
        # make sphere1 the first sibling
        cmds.reorderContainer( 'sphere1', front=True )
        # move sphere3 forward 2 siblings. Moving it forward one
        # sibling would put it at the end. Moving it forward again
        # puts it at the beginning.
        cmds.reorderContainer( 'sphere3', r=2 )
    ```

    ---
    - Args:
        - back (b): Move object(s) to back of container contents list
        - front (f): Move object(s) to front of container contents list
        - relative (r): Move object(s) relative to other container contents
    """
@overload #Overload for reorderContainer in ['create']
def reorderContainer(b: bool = ..., f: bool = ..., r: int = ...) -> None:
    """reorderContainer is undoable, queryable, and editable.
    
    This command reorders (moves) objects relative to their siblings in a
    container.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    Only nodes within one container can be moved at a time. Note: The container
    command's -nodeList flag will return a sorted list of contained nodes. To see
    the effects of reordering, use the -unsortedOrder flag in conjunction with the
    -nodeList flag.

    Example:
    ```python
        import maya.cmds as cmds
        # create a container
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sphere( n='sphere3' )
        cmds.sphere( n='sphere4' )
        cmds.container( addNode=['sphere1', 'sphere2', 'sphere3', 'sphere4'], n='sphereCon' )
        # The container sphereCon contains sphere1, sphere2, sphere3 and sphere4.
        # The command below moves sphere2 before sphere1.
        cmds.reorderContainer( 'sphere2', r=-1 )
        # make sphere1 the first sibling
        cmds.reorderContainer( 'sphere1', front=True )
        # move sphere3 forward 2 siblings. Moving it forward one
        # sibling would put it at the end. Moving it forward again
        # puts it at the beginning.
        cmds.reorderContainer( 'sphere3', r=2 )
    ```

    ---
    - Args:
        - back (b): Move object(s) to back of container contents list
        - front (f): Move object(s) to front of container contents list
        - relative (r): Move object(s) relative to other container contents
    """
@overload #Overload for reorderContainer in ['create']
def reorderContainer(back: bool = ..., b: bool = ..., front: bool = ..., f: bool = ..., relative: int = ..., r: int = ...) -> None:
    """reorderContainer is undoable, queryable, and editable.
    
    This command reorders (moves) objects relative to their siblings in a
    container.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    Only nodes within one container can be moved at a time. Note: The container
    command's -nodeList flag will return a sorted list of contained nodes. To see
    the effects of reordering, use the -unsortedOrder flag in conjunction with the
    -nodeList flag.

    Example:
    ```python
        import maya.cmds as cmds
        # create a container
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sphere( n='sphere3' )
        cmds.sphere( n='sphere4' )
        cmds.container( addNode=['sphere1', 'sphere2', 'sphere3', 'sphere4'], n='sphereCon' )
        # The container sphereCon contains sphere1, sphere2, sphere3 and sphere4.
        # The command below moves sphere2 before sphere1.
        cmds.reorderContainer( 'sphere2', r=-1 )
        # make sphere1 the first sibling
        cmds.reorderContainer( 'sphere1', front=True )
        # move sphere3 forward 2 siblings. Moving it forward one
        # sibling would put it at the end. Moving it forward again
        # puts it at the beginning.
        cmds.reorderContainer( 'sphere3', r=2 )
    ```

    ---
    - Args:
        - back (b): Move object(s) to back of container contents list
        - front (f): Move object(s) to front of container contents list
        - relative (r): Move object(s) relative to other container contents
    """
@overload #Overload for reorderContainer in ['query']
def reorderContainer(back: bool = ..., front: bool = ..., relative: int = ..., query: bool = ...) -> None:
    """reorderContainer is undoable, queryable, and editable.
    
    This command reorders (moves) objects relative to their siblings in a
    container.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    Only nodes within one container can be moved at a time. Note: The container
    command's -nodeList flag will return a sorted list of contained nodes. To see
    the effects of reordering, use the -unsortedOrder flag in conjunction with the
    -nodeList flag.

    Example:
    ```python
        import maya.cmds as cmds
        # create a container
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sphere( n='sphere3' )
        cmds.sphere( n='sphere4' )
        cmds.container( addNode=['sphere1', 'sphere2', 'sphere3', 'sphere4'], n='sphereCon' )
        # The container sphereCon contains sphere1, sphere2, sphere3 and sphere4.
        # The command below moves sphere2 before sphere1.
        cmds.reorderContainer( 'sphere2', r=-1 )
        # make sphere1 the first sibling
        cmds.reorderContainer( 'sphere1', front=True )
        # move sphere3 forward 2 siblings. Moving it forward one
        # sibling would put it at the end. Moving it forward again
        # puts it at the beginning.
        cmds.reorderContainer( 'sphere3', r=2 )
    ```

    ---
    - Args:
        - back (b): Move object(s) to back of container contents list
        - front (f): Move object(s) to front of container contents list
        - relative (r): Move object(s) relative to other container contents
        - query (q): Query mode flag
    """
@overload #Overload for reorderContainer in ['query']
def reorderContainer(b: bool = ..., f: bool = ..., r: int = ..., q: bool = ...) -> None:
    """reorderContainer is undoable, queryable, and editable.
    
    This command reorders (moves) objects relative to their siblings in a
    container.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    Only nodes within one container can be moved at a time. Note: The container
    command's -nodeList flag will return a sorted list of contained nodes. To see
    the effects of reordering, use the -unsortedOrder flag in conjunction with the
    -nodeList flag.

    Example:
    ```python
        import maya.cmds as cmds
        # create a container
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sphere( n='sphere3' )
        cmds.sphere( n='sphere4' )
        cmds.container( addNode=['sphere1', 'sphere2', 'sphere3', 'sphere4'], n='sphereCon' )
        # The container sphereCon contains sphere1, sphere2, sphere3 and sphere4.
        # The command below moves sphere2 before sphere1.
        cmds.reorderContainer( 'sphere2', r=-1 )
        # make sphere1 the first sibling
        cmds.reorderContainer( 'sphere1', front=True )
        # move sphere3 forward 2 siblings. Moving it forward one
        # sibling would put it at the end. Moving it forward again
        # puts it at the beginning.
        cmds.reorderContainer( 'sphere3', r=2 )
    ```

    ---
    - Args:
        - back (b): Move object(s) to back of container contents list
        - front (f): Move object(s) to front of container contents list
        - relative (r): Move object(s) relative to other container contents
        - query (q): Query mode flag
    """
@overload #Overload for reorderContainer in ['query']
def reorderContainer(back: bool = ..., b: bool = ..., front: bool = ..., f: bool = ..., relative: int = ..., r: int = ..., query: bool = ..., q: bool = ...) -> None:
    """reorderContainer is undoable, queryable, and editable.
    
    This command reorders (moves) objects relative to their siblings in a
    container.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    Only nodes within one container can be moved at a time. Note: The container
    command's -nodeList flag will return a sorted list of contained nodes. To see
    the effects of reordering, use the -unsortedOrder flag in conjunction with the
    -nodeList flag.

    Example:
    ```python
        import maya.cmds as cmds
        # create a container
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sphere( n='sphere3' )
        cmds.sphere( n='sphere4' )
        cmds.container( addNode=['sphere1', 'sphere2', 'sphere3', 'sphere4'], n='sphereCon' )
        # The container sphereCon contains sphere1, sphere2, sphere3 and sphere4.
        # The command below moves sphere2 before sphere1.
        cmds.reorderContainer( 'sphere2', r=-1 )
        # make sphere1 the first sibling
        cmds.reorderContainer( 'sphere1', front=True )
        # move sphere3 forward 2 siblings. Moving it forward one
        # sibling would put it at the end. Moving it forward again
        # puts it at the beginning.
        cmds.reorderContainer( 'sphere3', r=2 )
    ```

    ---
    - Args:
        - back (b): Move object(s) to back of container contents list
        - front (f): Move object(s) to front of container contents list
        - relative (r): Move object(s) relative to other container contents
        - query (q): Query mode flag
    """
@overload #Overload for reorderContainer in ['edit']
def reorderContainer(back: bool = ..., front: bool = ..., relative: int = ..., edit: bool = ...) -> None:
    """reorderContainer is undoable, queryable, and editable.
    
    This command reorders (moves) objects relative to their siblings in a
    container.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    Only nodes within one container can be moved at a time. Note: The container
    command's -nodeList flag will return a sorted list of contained nodes. To see
    the effects of reordering, use the -unsortedOrder flag in conjunction with the
    -nodeList flag.

    Example:
    ```python
        import maya.cmds as cmds
        # create a container
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sphere( n='sphere3' )
        cmds.sphere( n='sphere4' )
        cmds.container( addNode=['sphere1', 'sphere2', 'sphere3', 'sphere4'], n='sphereCon' )
        # The container sphereCon contains sphere1, sphere2, sphere3 and sphere4.
        # The command below moves sphere2 before sphere1.
        cmds.reorderContainer( 'sphere2', r=-1 )
        # make sphere1 the first sibling
        cmds.reorderContainer( 'sphere1', front=True )
        # move sphere3 forward 2 siblings. Moving it forward one
        # sibling would put it at the end. Moving it forward again
        # puts it at the beginning.
        cmds.reorderContainer( 'sphere3', r=2 )
    ```

    ---
    - Args:
        - back (b): Move object(s) to back of container contents list
        - front (f): Move object(s) to front of container contents list
        - relative (r): Move object(s) relative to other container contents
        - edit (e): Edit mode flag
    """
@overload #Overload for reorderContainer in ['edit']
def reorderContainer(b: bool = ..., f: bool = ..., r: int = ..., e: bool = ...) -> None:
    """reorderContainer is undoable, queryable, and editable.
    
    This command reorders (moves) objects relative to their siblings in a
    container.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    Only nodes within one container can be moved at a time. Note: The container
    command's -nodeList flag will return a sorted list of contained nodes. To see
    the effects of reordering, use the -unsortedOrder flag in conjunction with the
    -nodeList flag.

    Example:
    ```python
        import maya.cmds as cmds
        # create a container
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sphere( n='sphere3' )
        cmds.sphere( n='sphere4' )
        cmds.container( addNode=['sphere1', 'sphere2', 'sphere3', 'sphere4'], n='sphereCon' )
        # The container sphereCon contains sphere1, sphere2, sphere3 and sphere4.
        # The command below moves sphere2 before sphere1.
        cmds.reorderContainer( 'sphere2', r=-1 )
        # make sphere1 the first sibling
        cmds.reorderContainer( 'sphere1', front=True )
        # move sphere3 forward 2 siblings. Moving it forward one
        # sibling would put it at the end. Moving it forward again
        # puts it at the beginning.
        cmds.reorderContainer( 'sphere3', r=2 )
    ```

    ---
    - Args:
        - back (b): Move object(s) to back of container contents list
        - front (f): Move object(s) to front of container contents list
        - relative (r): Move object(s) relative to other container contents
        - edit (e): Edit mode flag
    """
@overload #Overload for reorderContainer in ['edit']
def reorderContainer(back: bool = ..., b: bool = ..., front: bool = ..., f: bool = ..., relative: int = ..., r: int = ..., edit: bool = ..., e: bool = ...) -> None:
    """reorderContainer is undoable, queryable, and editable.
    
    This command reorders (moves) objects relative to their siblings in a
    container.
    
    For relative moves, both positive and negative numbers may be specified.
    Positive numbers move the object forward and negative numbers move the object
    backward amoung its siblings. When an object is at the end (beginning) of the
    list of siblings, a relative move of 1 (-1) will put the object at the
    beginning (end) of the list of siblings. That is, relative moves will wrap if
    necessary.
    
    Only nodes within one container can be moved at a time. Note: The container
    command's -nodeList flag will return a sorted list of contained nodes. To see
    the effects of reordering, use the -unsortedOrder flag in conjunction with the
    -nodeList flag.

    Example:
    ```python
        import maya.cmds as cmds
        # create a container
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sphere( n='sphere3' )
        cmds.sphere( n='sphere4' )
        cmds.container( addNode=['sphere1', 'sphere2', 'sphere3', 'sphere4'], n='sphereCon' )
        # The container sphereCon contains sphere1, sphere2, sphere3 and sphere4.
        # The command below moves sphere2 before sphere1.
        cmds.reorderContainer( 'sphere2', r=-1 )
        # make sphere1 the first sibling
        cmds.reorderContainer( 'sphere1', front=True )
        # move sphere3 forward 2 siblings. Moving it forward one
        # sibling would put it at the end. Moving it forward again
        # puts it at the beginning.
        cmds.reorderContainer( 'sphere3', r=2 )
    ```

    ---
    - Args:
        - back (b): Move object(s) to back of container contents list
        - front (f): Move object(s) to front of container contents list
        - relative (r): Move object(s) relative to other container contents
        - edit (e): Edit mode flag
    """
