"""Stub files for General category in Maya commands, command: snapTogetherCtx."""

from typing import Any, overload

@overload #Overload for snapTogetherCtx in ['create']
def snapTogetherCtx([contextName]: [contextName], clearSelection: bool = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., setOrientation: bool = ..., snapPolygonFace: bool = ...) -> str:
    """snapTogetherCtx is undoable, queryable, and editable.
    
    The snapTogetherCtx command creates a tool for snapping surfaces together.

    Example:
    ```python
        import maya.cmds as cmds
        # Create two nurbs spheres, then move them apart
        cmds.sphere(r=3, n='nurbsSphere1')
        cmds.move(5, 0, 0)
        cmds.sphere(r=3, n='nurbsSphere2')
        cmds.move(-5, 0, 0)
        # Create a new snap together tool context, set it to move objects only, then switch to it
        # You can use this tool to snap two spheres together
        cmds.snapTogetherCtx('snapTogetherCtx1', so=False)
        cmds.setToolTo('snapTogetherCtx1')
    ```

    ---
    - Args:
        - [contextName]: Input item(s).
        - clearSelection (cs): Sets whether the tool should clear the selection on entry to the tool. Default true.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - setOrientation (so): Sets whether the tool should orient as well as moving an item. Default true.
        - snapPolygonFace (spf): Sets whether the tool should snap the cursor to polygon face centers. Default false.
    """
@overload #Overload for snapTogetherCtx in ['create']
def snapTogetherCtx([contextName]: [contextName], cs: bool = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., so: bool = ..., spf: bool = ...) -> str:
    """snapTogetherCtx is undoable, queryable, and editable.
    
    The snapTogetherCtx command creates a tool for snapping surfaces together.

    Example:
    ```python
        import maya.cmds as cmds
        # Create two nurbs spheres, then move them apart
        cmds.sphere(r=3, n='nurbsSphere1')
        cmds.move(5, 0, 0)
        cmds.sphere(r=3, n='nurbsSphere2')
        cmds.move(-5, 0, 0)
        # Create a new snap together tool context, set it to move objects only, then switch to it
        # You can use this tool to snap two spheres together
        cmds.snapTogetherCtx('snapTogetherCtx1', so=False)
        cmds.setToolTo('snapTogetherCtx1')
    ```

    ---
    - Args:
        - [contextName]: Input item(s).
        - clearSelection (cs): Sets whether the tool should clear the selection on entry to the tool. Default true.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - setOrientation (so): Sets whether the tool should orient as well as moving an item. Default true.
        - snapPolygonFace (spf): Sets whether the tool should snap the cursor to polygon face centers. Default false.
    """
@overload #Overload for snapTogetherCtx in ['create']
def snapTogetherCtx([contextName]: [contextName], clearSelection: bool = ..., cs: bool = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., setOrientation: bool = ..., so: bool = ..., snapPolygonFace: bool = ..., spf: bool = ...) -> str:
    """snapTogetherCtx is undoable, queryable, and editable.
    
    The snapTogetherCtx command creates a tool for snapping surfaces together.

    Example:
    ```python
        import maya.cmds as cmds
        # Create two nurbs spheres, then move them apart
        cmds.sphere(r=3, n='nurbsSphere1')
        cmds.move(5, 0, 0)
        cmds.sphere(r=3, n='nurbsSphere2')
        cmds.move(-5, 0, 0)
        # Create a new snap together tool context, set it to move objects only, then switch to it
        # You can use this tool to snap two spheres together
        cmds.snapTogetherCtx('snapTogetherCtx1', so=False)
        cmds.setToolTo('snapTogetherCtx1')
    ```

    ---
    - Args:
        - [contextName]: Input item(s).
        - clearSelection (cs): Sets whether the tool should clear the selection on entry to the tool. Default true.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - setOrientation (so): Sets whether the tool should orient as well as moving an item. Default true.
        - snapPolygonFace (spf): Sets whether the tool should snap the cursor to polygon face centers. Default false.
    """
@overload #Overload for snapTogetherCtx in ['query']
def snapTogetherCtx([contextName]: [contextName], clearSelection: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., setOrientation: bool = ..., snapPolygonFace: bool = ..., query: bool = ...) -> str:
    """snapTogetherCtx is undoable, queryable, and editable.
    
    The snapTogetherCtx command creates a tool for snapping surfaces together.

    Example:
    ```python
        import maya.cmds as cmds
        # Create two nurbs spheres, then move them apart
        cmds.sphere(r=3, n='nurbsSphere1')
        cmds.move(5, 0, 0)
        cmds.sphere(r=3, n='nurbsSphere2')
        cmds.move(-5, 0, 0)
        # Create a new snap together tool context, set it to move objects only, then switch to it
        # You can use this tool to snap two spheres together
        cmds.snapTogetherCtx('snapTogetherCtx1', so=False)
        cmds.setToolTo('snapTogetherCtx1')
    ```

    ---
    - Args:
        - [contextName]: Input item(s).
        - clearSelection (cs): Sets whether the tool should clear the selection on entry to the tool. Default true.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - setOrientation (so): Sets whether the tool should orient as well as moving an item. Default true.
        - snapPolygonFace (spf): Sets whether the tool should snap the cursor to polygon face centers. Default false.
        - query (q): Query mode flag
    """
@overload #Overload for snapTogetherCtx in ['query']
def snapTogetherCtx([contextName]: [contextName], cs: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., so: bool = ..., spf: bool = ..., q: bool = ...) -> str:
    """snapTogetherCtx is undoable, queryable, and editable.
    
    The snapTogetherCtx command creates a tool for snapping surfaces together.

    Example:
    ```python
        import maya.cmds as cmds
        # Create two nurbs spheres, then move them apart
        cmds.sphere(r=3, n='nurbsSphere1')
        cmds.move(5, 0, 0)
        cmds.sphere(r=3, n='nurbsSphere2')
        cmds.move(-5, 0, 0)
        # Create a new snap together tool context, set it to move objects only, then switch to it
        # You can use this tool to snap two spheres together
        cmds.snapTogetherCtx('snapTogetherCtx1', so=False)
        cmds.setToolTo('snapTogetherCtx1')
    ```

    ---
    - Args:
        - [contextName]: Input item(s).
        - clearSelection (cs): Sets whether the tool should clear the selection on entry to the tool. Default true.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - setOrientation (so): Sets whether the tool should orient as well as moving an item. Default true.
        - snapPolygonFace (spf): Sets whether the tool should snap the cursor to polygon face centers. Default false.
        - query (q): Query mode flag
    """
@overload #Overload for snapTogetherCtx in ['query']
def snapTogetherCtx([contextName]: [contextName], clearSelection: bool = ..., cs: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., setOrientation: bool = ..., so: bool = ..., snapPolygonFace: bool = ..., spf: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """snapTogetherCtx is undoable, queryable, and editable.
    
    The snapTogetherCtx command creates a tool for snapping surfaces together.

    Example:
    ```python
        import maya.cmds as cmds
        # Create two nurbs spheres, then move them apart
        cmds.sphere(r=3, n='nurbsSphere1')
        cmds.move(5, 0, 0)
        cmds.sphere(r=3, n='nurbsSphere2')
        cmds.move(-5, 0, 0)
        # Create a new snap together tool context, set it to move objects only, then switch to it
        # You can use this tool to snap two spheres together
        cmds.snapTogetherCtx('snapTogetherCtx1', so=False)
        cmds.setToolTo('snapTogetherCtx1')
    ```

    ---
    - Args:
        - [contextName]: Input item(s).
        - clearSelection (cs): Sets whether the tool should clear the selection on entry to the tool. Default true.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - setOrientation (so): Sets whether the tool should orient as well as moving an item. Default true.
        - snapPolygonFace (spf): Sets whether the tool should snap the cursor to polygon face centers. Default false.
        - query (q): Query mode flag
    """
@overload #Overload for snapTogetherCtx in ['edit']
def snapTogetherCtx([contextName]: [contextName], clearSelection: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., setOrientation: bool = ..., snapPolygonFace: bool = ..., edit: bool = ...) -> str:
    """snapTogetherCtx is undoable, queryable, and editable.
    
    The snapTogetherCtx command creates a tool for snapping surfaces together.

    Example:
    ```python
        import maya.cmds as cmds
        # Create two nurbs spheres, then move them apart
        cmds.sphere(r=3, n='nurbsSphere1')
        cmds.move(5, 0, 0)
        cmds.sphere(r=3, n='nurbsSphere2')
        cmds.move(-5, 0, 0)
        # Create a new snap together tool context, set it to move objects only, then switch to it
        # You can use this tool to snap two spheres together
        cmds.snapTogetherCtx('snapTogetherCtx1', so=False)
        cmds.setToolTo('snapTogetherCtx1')
    ```

    ---
    - Args:
        - [contextName]: Input item(s).
        - clearSelection (cs): Sets whether the tool should clear the selection on entry to the tool. Default true.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - setOrientation (so): Sets whether the tool should orient as well as moving an item. Default true.
        - snapPolygonFace (spf): Sets whether the tool should snap the cursor to polygon face centers. Default false.
        - edit (e): Edit mode flag
    """
@overload #Overload for snapTogetherCtx in ['edit']
def snapTogetherCtx([contextName]: [contextName], cs: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., so: bool = ..., spf: bool = ..., e: bool = ...) -> str:
    """snapTogetherCtx is undoable, queryable, and editable.
    
    The snapTogetherCtx command creates a tool for snapping surfaces together.

    Example:
    ```python
        import maya.cmds as cmds
        # Create two nurbs spheres, then move them apart
        cmds.sphere(r=3, n='nurbsSphere1')
        cmds.move(5, 0, 0)
        cmds.sphere(r=3, n='nurbsSphere2')
        cmds.move(-5, 0, 0)
        # Create a new snap together tool context, set it to move objects only, then switch to it
        # You can use this tool to snap two spheres together
        cmds.snapTogetherCtx('snapTogetherCtx1', so=False)
        cmds.setToolTo('snapTogetherCtx1')
    ```

    ---
    - Args:
        - [contextName]: Input item(s).
        - clearSelection (cs): Sets whether the tool should clear the selection on entry to the tool. Default true.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - setOrientation (so): Sets whether the tool should orient as well as moving an item. Default true.
        - snapPolygonFace (spf): Sets whether the tool should snap the cursor to polygon face centers. Default false.
        - edit (e): Edit mode flag
    """
@overload #Overload for snapTogetherCtx in ['edit']
def snapTogetherCtx([contextName]: [contextName], clearSelection: bool = ..., cs: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., setOrientation: bool = ..., so: bool = ..., snapPolygonFace: bool = ..., spf: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """snapTogetherCtx is undoable, queryable, and editable.
    
    The snapTogetherCtx command creates a tool for snapping surfaces together.

    Example:
    ```python
        import maya.cmds as cmds
        # Create two nurbs spheres, then move them apart
        cmds.sphere(r=3, n='nurbsSphere1')
        cmds.move(5, 0, 0)
        cmds.sphere(r=3, n='nurbsSphere2')
        cmds.move(-5, 0, 0)
        # Create a new snap together tool context, set it to move objects only, then switch to it
        # You can use this tool to snap two spheres together
        cmds.snapTogetherCtx('snapTogetherCtx1', so=False)
        cmds.setToolTo('snapTogetherCtx1')
    ```

    ---
    - Args:
        - [contextName]: Input item(s).
        - clearSelection (cs): Sets whether the tool should clear the selection on entry to the tool. Default true.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - setOrientation (so): Sets whether the tool should orient as well as moving an item. Default true.
        - snapPolygonFace (spf): Sets whether the tool should snap the cursor to polygon face centers. Default false.
        - edit (e): Edit mode flag
    """
