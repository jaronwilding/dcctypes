"""Stub files for Contexts category in Maya commands, command: polySplitCtx."""

from typing import Any, overload

@overload #Overload for polySplitCtx in ['create']
def polySplitCtx(enablesnap: bool = ..., exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., magnetsnap: int = ..., precsnap: float = ..., smoothingangle: angle = ..., snaptoedge: bool = ..., subdivision: int = ...) -> None:
    """polySplitCtx is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx('polySplitCtx1')
        cmds.setToolTo('polySplitCtx1')
    ```

    ---
    - Args:
        - enablesnap (es): Enable/disable custom magnet snapping to start/middle/end of edge
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - magnetsnap (ms): number of extra magnets to snap onto, regularly spaced along the edge
        - precsnap (ps): precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.
        - smoothingangle (sma): the threshold that controls whether newly created edges are hard or soft
        - snaptoedge (ste): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - subdivision (s): number of sub-edges to add between 2 consecutive edge points. Default is 1.
    """
@overload #Overload for polySplitCtx in ['create']
def polySplitCtx(es: bool = ..., ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ms: int = ..., ps: float = ..., sma: angle = ..., ste: bool = ..., s: int = ...) -> None:
    """polySplitCtx is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx('polySplitCtx1')
        cmds.setToolTo('polySplitCtx1')
    ```

    ---
    - Args:
        - enablesnap (es): Enable/disable custom magnet snapping to start/middle/end of edge
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - magnetsnap (ms): number of extra magnets to snap onto, regularly spaced along the edge
        - precsnap (ps): precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.
        - smoothingangle (sma): the threshold that controls whether newly created edges are hard or soft
        - snaptoedge (ste): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - subdivision (s): number of sub-edges to add between 2 consecutive edge points. Default is 1.
    """
@overload #Overload for polySplitCtx in ['create']
def polySplitCtx(enablesnap: bool = ..., es: bool = ..., exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., magnetsnap: int = ..., ms: int = ..., precsnap: float = ..., ps: float = ..., smoothingangle: angle = ..., sma: angle = ..., snaptoedge: bool = ..., ste: bool = ..., subdivision: int = ..., s: int = ...) -> None:
    """polySplitCtx is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx('polySplitCtx1')
        cmds.setToolTo('polySplitCtx1')
    ```

    ---
    - Args:
        - enablesnap (es): Enable/disable custom magnet snapping to start/middle/end of edge
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - magnetsnap (ms): number of extra magnets to snap onto, regularly spaced along the edge
        - precsnap (ps): precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.
        - smoothingangle (sma): the threshold that controls whether newly created edges are hard or soft
        - snaptoedge (ste): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - subdivision (s): number of sub-edges to add between 2 consecutive edge points. Default is 1.
    """
@overload #Overload for polySplitCtx in ['query']
def polySplitCtx(enablesnap: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., magnetsnap: int = ..., precsnap: float = ..., smoothingangle: angle = ..., snaptoedge: bool = ..., subdivision: int = ..., query: bool = ...) -> None:
    """polySplitCtx is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx('polySplitCtx1')
        cmds.setToolTo('polySplitCtx1')
    ```

    ---
    - Args:
        - enablesnap (es): Enable/disable custom magnet snapping to start/middle/end of edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - magnetsnap (ms): number of extra magnets to snap onto, regularly spaced along the edge
        - precsnap (ps): precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.
        - smoothingangle (sma): the threshold that controls whether newly created edges are hard or soft
        - snaptoedge (ste): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - subdivision (s): number of sub-edges to add between 2 consecutive edge points. Default is 1.
        - query (q): Query mode flag
    """
@overload #Overload for polySplitCtx in ['query']
def polySplitCtx(es: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ms: int = ..., ps: float = ..., sma: angle = ..., ste: bool = ..., s: int = ..., q: bool = ...) -> None:
    """polySplitCtx is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx('polySplitCtx1')
        cmds.setToolTo('polySplitCtx1')
    ```

    ---
    - Args:
        - enablesnap (es): Enable/disable custom magnet snapping to start/middle/end of edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - magnetsnap (ms): number of extra magnets to snap onto, regularly spaced along the edge
        - precsnap (ps): precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.
        - smoothingangle (sma): the threshold that controls whether newly created edges are hard or soft
        - snaptoedge (ste): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - subdivision (s): number of sub-edges to add between 2 consecutive edge points. Default is 1.
        - query (q): Query mode flag
    """
@overload #Overload for polySplitCtx in ['query']
def polySplitCtx(enablesnap: bool = ..., es: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., magnetsnap: int = ..., ms: int = ..., precsnap: float = ..., ps: float = ..., smoothingangle: angle = ..., sma: angle = ..., snaptoedge: bool = ..., ste: bool = ..., subdivision: int = ..., s: int = ..., query: bool = ..., q: bool = ...) -> None:
    """polySplitCtx is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx('polySplitCtx1')
        cmds.setToolTo('polySplitCtx1')
    ```

    ---
    - Args:
        - enablesnap (es): Enable/disable custom magnet snapping to start/middle/end of edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - magnetsnap (ms): number of extra magnets to snap onto, regularly spaced along the edge
        - precsnap (ps): precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.
        - smoothingangle (sma): the threshold that controls whether newly created edges are hard or soft
        - snaptoedge (ste): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - subdivision (s): number of sub-edges to add between 2 consecutive edge points. Default is 1.
        - query (q): Query mode flag
    """
@overload #Overload for polySplitCtx in ['edit']
def polySplitCtx(enablesnap: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., magnetsnap: int = ..., precsnap: float = ..., smoothingangle: angle = ..., snaptoedge: bool = ..., subdivision: int = ..., edit: bool = ...) -> None:
    """polySplitCtx is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx('polySplitCtx1')
        cmds.setToolTo('polySplitCtx1')
    ```

    ---
    - Args:
        - enablesnap (es): Enable/disable custom magnet snapping to start/middle/end of edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - magnetsnap (ms): number of extra magnets to snap onto, regularly spaced along the edge
        - precsnap (ps): precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.
        - smoothingangle (sma): the threshold that controls whether newly created edges are hard or soft
        - snaptoedge (ste): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - subdivision (s): number of sub-edges to add between 2 consecutive edge points. Default is 1.
        - edit (e): Edit mode flag
    """
@overload #Overload for polySplitCtx in ['edit']
def polySplitCtx(es: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ms: int = ..., ps: float = ..., sma: angle = ..., ste: bool = ..., s: int = ..., e: bool = ...) -> None:
    """polySplitCtx is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx('polySplitCtx1')
        cmds.setToolTo('polySplitCtx1')
    ```

    ---
    - Args:
        - enablesnap (es): Enable/disable custom magnet snapping to start/middle/end of edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - magnetsnap (ms): number of extra magnets to snap onto, regularly spaced along the edge
        - precsnap (ps): precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.
        - smoothingangle (sma): the threshold that controls whether newly created edges are hard or soft
        - snaptoedge (ste): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - subdivision (s): number of sub-edges to add between 2 consecutive edge points. Default is 1.
        - edit (e): Edit mode flag
    """
@overload #Overload for polySplitCtx in ['edit']
def polySplitCtx(enablesnap: bool = ..., es: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., magnetsnap: int = ..., ms: int = ..., precsnap: float = ..., ps: float = ..., smoothingangle: angle = ..., sma: angle = ..., snaptoedge: bool = ..., ste: bool = ..., subdivision: int = ..., s: int = ..., edit: bool = ..., e: bool = ...) -> None:
    """polySplitCtx is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx('polySplitCtx1')
        cmds.setToolTo('polySplitCtx1')
    ```

    ---
    - Args:
        - enablesnap (es): Enable/disable custom magnet snapping to start/middle/end of edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - magnetsnap (ms): number of extra magnets to snap onto, regularly spaced along the edge
        - precsnap (ps): precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.
        - smoothingangle (sma): the threshold that controls whether newly created edges are hard or soft
        - snaptoedge (ste): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - subdivision (s): number of sub-edges to add between 2 consecutive edge points. Default is 1.
        - edit (e): Edit mode flag
    """
