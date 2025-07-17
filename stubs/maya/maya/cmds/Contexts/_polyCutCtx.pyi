"""Stub files for Contexts category in Maya commands, command: polyCutCtx."""

from typing import Any, overload

@overload #Overload for polyCutCtx in ['create']
def polyCutCtx(deleteFaces: bool = ..., exists: bool = ..., extractFaces: bool = ..., extractOffset: [linear, linear, linear] = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> None:
    """polyCutCtx is undoable, queryable, and editable.
    
    Create a new context to cut facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new cut facets context, then switch to it
        cmds.polyCutCtx('polyCutCtx1')
        cmds.setToolTo('polyCutCtx1')
    ```

    ---
    - Args:
        - deleteFaces (df): whether to delete the one-half of the cut-faces of the poly.  If true, they are deleted.Default:false
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - extractFaces (ef): whether to extract the cut-faces of the poly into a separate shell.  If true, they are extracted.Default:false
        - extractOffset (eo): The displacement offset of the cut faces.Default:0.5, 0.5, 0.5
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for polyCutCtx in ['create']
def polyCutCtx(df: bool = ..., ex: bool = ..., ef: bool = ..., eo: [linear, linear, linear] = ..., i1: str = ..., i2: str = ..., i3: str = ...) -> None:
    """polyCutCtx is undoable, queryable, and editable.
    
    Create a new context to cut facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new cut facets context, then switch to it
        cmds.polyCutCtx('polyCutCtx1')
        cmds.setToolTo('polyCutCtx1')
    ```

    ---
    - Args:
        - deleteFaces (df): whether to delete the one-half of the cut-faces of the poly.  If true, they are deleted.Default:false
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - extractFaces (ef): whether to extract the cut-faces of the poly into a separate shell.  If true, they are extracted.Default:false
        - extractOffset (eo): The displacement offset of the cut faces.Default:0.5, 0.5, 0.5
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for polyCutCtx in ['create']
def polyCutCtx(deleteFaces: bool = ..., df: bool = ..., exists: bool = ..., ex: bool = ..., extractFaces: bool = ..., ef: bool = ..., extractOffset: [linear, linear, linear] = ..., eo: [linear, linear, linear] = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ...) -> None:
    """polyCutCtx is undoable, queryable, and editable.
    
    Create a new context to cut facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new cut facets context, then switch to it
        cmds.polyCutCtx('polyCutCtx1')
        cmds.setToolTo('polyCutCtx1')
    ```

    ---
    - Args:
        - deleteFaces (df): whether to delete the one-half of the cut-faces of the poly.  If true, they are deleted.Default:false
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - extractFaces (ef): whether to extract the cut-faces of the poly into a separate shell.  If true, they are extracted.Default:false
        - extractOffset (eo): The displacement offset of the cut faces.Default:0.5, 0.5, 0.5
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
    """
@overload #Overload for polyCutCtx in ['query']
def polyCutCtx(deleteFaces: bool = ..., extractFaces: bool = ..., extractOffset: [linear, linear, linear] = ..., image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> None:
    """polyCutCtx is undoable, queryable, and editable.
    
    Create a new context to cut facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new cut facets context, then switch to it
        cmds.polyCutCtx('polyCutCtx1')
        cmds.setToolTo('polyCutCtx1')
    ```

    ---
    - Args:
        - deleteFaces (df): whether to delete the one-half of the cut-faces of the poly.  If true, they are deleted.Default:false
        - extractFaces (ef): whether to extract the cut-faces of the poly into a separate shell.  If true, they are extracted.Default:false
        - extractOffset (eo): The displacement offset of the cut faces.Default:0.5, 0.5, 0.5
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for polyCutCtx in ['query']
def polyCutCtx(df: bool = ..., ef: bool = ..., eo: [linear, linear, linear] = ..., i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> None:
    """polyCutCtx is undoable, queryable, and editable.
    
    Create a new context to cut facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new cut facets context, then switch to it
        cmds.polyCutCtx('polyCutCtx1')
        cmds.setToolTo('polyCutCtx1')
    ```

    ---
    - Args:
        - deleteFaces (df): whether to delete the one-half of the cut-faces of the poly.  If true, they are deleted.Default:false
        - extractFaces (ef): whether to extract the cut-faces of the poly into a separate shell.  If true, they are extracted.Default:false
        - extractOffset (eo): The displacement offset of the cut faces.Default:0.5, 0.5, 0.5
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for polyCutCtx in ['query']
def polyCutCtx(deleteFaces: bool = ..., df: bool = ..., extractFaces: bool = ..., ef: bool = ..., extractOffset: [linear, linear, linear] = ..., eo: [linear, linear, linear] = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> None:
    """polyCutCtx is undoable, queryable, and editable.
    
    Create a new context to cut facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new cut facets context, then switch to it
        cmds.polyCutCtx('polyCutCtx1')
        cmds.setToolTo('polyCutCtx1')
    ```

    ---
    - Args:
        - deleteFaces (df): whether to delete the one-half of the cut-faces of the poly.  If true, they are deleted.Default:false
        - extractFaces (ef): whether to extract the cut-faces of the poly into a separate shell.  If true, they are extracted.Default:false
        - extractOffset (eo): The displacement offset of the cut faces.Default:0.5, 0.5, 0.5
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for polyCutCtx in ['edit']
def polyCutCtx(deleteFaces: bool = ..., extractFaces: bool = ..., extractOffset: [linear, linear, linear] = ..., image1: str = ..., image2: str = ..., image3: str = ..., edit: bool = ...) -> None:
    """polyCutCtx is undoable, queryable, and editable.
    
    Create a new context to cut facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new cut facets context, then switch to it
        cmds.polyCutCtx('polyCutCtx1')
        cmds.setToolTo('polyCutCtx1')
    ```

    ---
    - Args:
        - deleteFaces (df): whether to delete the one-half of the cut-faces of the poly.  If true, they are deleted.Default:false
        - extractFaces (ef): whether to extract the cut-faces of the poly into a separate shell.  If true, they are extracted.Default:false
        - extractOffset (eo): The displacement offset of the cut faces.Default:0.5, 0.5, 0.5
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyCutCtx in ['edit']
def polyCutCtx(df: bool = ..., ef: bool = ..., eo: [linear, linear, linear] = ..., i1: str = ..., i2: str = ..., i3: str = ..., e: bool = ...) -> None:
    """polyCutCtx is undoable, queryable, and editable.
    
    Create a new context to cut facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new cut facets context, then switch to it
        cmds.polyCutCtx('polyCutCtx1')
        cmds.setToolTo('polyCutCtx1')
    ```

    ---
    - Args:
        - deleteFaces (df): whether to delete the one-half of the cut-faces of the poly.  If true, they are deleted.Default:false
        - extractFaces (ef): whether to extract the cut-faces of the poly into a separate shell.  If true, they are extracted.Default:false
        - extractOffset (eo): The displacement offset of the cut faces.Default:0.5, 0.5, 0.5
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyCutCtx in ['edit']
def polyCutCtx(deleteFaces: bool = ..., df: bool = ..., extractFaces: bool = ..., ef: bool = ..., extractOffset: [linear, linear, linear] = ..., eo: [linear, linear, linear] = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """polyCutCtx is undoable, queryable, and editable.
    
    Create a new context to cut facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new cut facets context, then switch to it
        cmds.polyCutCtx('polyCutCtx1')
        cmds.setToolTo('polyCutCtx1')
    ```

    ---
    - Args:
        - deleteFaces (df): whether to delete the one-half of the cut-faces of the poly.  If true, they are deleted.Default:false
        - extractFaces (ef): whether to extract the cut-faces of the poly into a separate shell.  If true, they are extracted.Default:false
        - extractOffset (eo): The displacement offset of the cut faces.Default:0.5, 0.5, 0.5
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - edit (e): Edit mode flag
    """
