"""Stub files for Contexts category in Maya commands, command: polySplitCtx2."""

from typing import Any, overload

@overload #Overload for polySplitCtx2 in ['create']
def polySplitCtx2(adjustEdgeFlow: float = ..., constrainToEdges: bool = ..., edgeMagnets: int = ..., exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., insertWithEdgeFlow: bool = ..., snapTolerance: float = ..., snappedToEdgeColor: [float, float, float] = ..., snappedToFaceColor: [float, float, float] = ..., snappedToMagnetColor: [float, float, float] = ..., snappedToVertexColor: [float, float, float] = ...) -> None:
    """polySplitCtx2 is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx2('polySplitCtx2')
        cmds.setToolTo('polySplitCtx2')
    ```

    ---
    - Args:
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.
        - constrainToEdges (cte): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - edgeMagnets (em): number of extra magnets to snap onto, regularly spaced along the edge
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.
        - snapTolerance (st): precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.
        - snappedToEdgeColor (sec): Color for edge snapping.
        - snappedToFaceColor (sfc): Color for face snapping.
        - snappedToMagnetColor (smc): Color for magnet snapping.
        - snappedToVertexColor (svc): Color for vertex snapping.
    """
@overload #Overload for polySplitCtx2 in ['create']
def polySplitCtx2(aef: float = ..., cte: bool = ..., em: int = ..., ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ief: bool = ..., st: float = ..., sec: [float, float, float] = ..., sfc: [float, float, float] = ..., smc: [float, float, float] = ..., svc: [float, float, float] = ...) -> None:
    """polySplitCtx2 is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx2('polySplitCtx2')
        cmds.setToolTo('polySplitCtx2')
    ```

    ---
    - Args:
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.
        - constrainToEdges (cte): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - edgeMagnets (em): number of extra magnets to snap onto, regularly spaced along the edge
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.
        - snapTolerance (st): precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.
        - snappedToEdgeColor (sec): Color for edge snapping.
        - snappedToFaceColor (sfc): Color for face snapping.
        - snappedToMagnetColor (smc): Color for magnet snapping.
        - snappedToVertexColor (svc): Color for vertex snapping.
    """
@overload #Overload for polySplitCtx2 in ['create']
def polySplitCtx2(adjustEdgeFlow: float = ..., aef: float = ..., constrainToEdges: bool = ..., cte: bool = ..., edgeMagnets: int = ..., em: int = ..., exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., insertWithEdgeFlow: bool = ..., ief: bool = ..., snapTolerance: float = ..., st: float = ..., snappedToEdgeColor: [float, float, float] = ..., sec: [float, float, float] = ..., snappedToFaceColor: [float, float, float] = ..., sfc: [float, float, float] = ..., snappedToMagnetColor: [float, float, float] = ..., smc: [float, float, float] = ..., snappedToVertexColor: [float, float, float] = ..., svc: [float, float, float] = ...) -> None:
    """polySplitCtx2 is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx2('polySplitCtx2')
        cmds.setToolTo('polySplitCtx2')
    ```

    ---
    - Args:
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.
        - constrainToEdges (cte): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - edgeMagnets (em): number of extra magnets to snap onto, regularly spaced along the edge
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.
        - snapTolerance (st): precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.
        - snappedToEdgeColor (sec): Color for edge snapping.
        - snappedToFaceColor (sfc): Color for face snapping.
        - snappedToMagnetColor (smc): Color for magnet snapping.
        - snappedToVertexColor (svc): Color for vertex snapping.
    """
@overload #Overload for polySplitCtx2 in ['query']
def polySplitCtx2(adjustEdgeFlow: float = ..., constrainToEdges: bool = ..., edgeMagnets: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., insertWithEdgeFlow: bool = ..., snapTolerance: float = ..., snappedToEdgeColor: [float, float, float] = ..., snappedToFaceColor: [float, float, float] = ..., snappedToMagnetColor: [float, float, float] = ..., snappedToVertexColor: [float, float, float] = ..., query: bool = ...) -> None:
    """polySplitCtx2 is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx2('polySplitCtx2')
        cmds.setToolTo('polySplitCtx2')
    ```

    ---
    - Args:
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.
        - constrainToEdges (cte): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - edgeMagnets (em): number of extra magnets to snap onto, regularly spaced along the edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.
        - snapTolerance (st): precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.
        - snappedToEdgeColor (sec): Color for edge snapping.
        - snappedToFaceColor (sfc): Color for face snapping.
        - snappedToMagnetColor (smc): Color for magnet snapping.
        - snappedToVertexColor (svc): Color for vertex snapping.
        - query (q): Query mode flag
    """
@overload #Overload for polySplitCtx2 in ['query']
def polySplitCtx2(aef: float = ..., cte: bool = ..., em: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., ief: bool = ..., st: float = ..., sec: [float, float, float] = ..., sfc: [float, float, float] = ..., smc: [float, float, float] = ..., svc: [float, float, float] = ..., q: bool = ...) -> None:
    """polySplitCtx2 is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx2('polySplitCtx2')
        cmds.setToolTo('polySplitCtx2')
    ```

    ---
    - Args:
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.
        - constrainToEdges (cte): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - edgeMagnets (em): number of extra magnets to snap onto, regularly spaced along the edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.
        - snapTolerance (st): precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.
        - snappedToEdgeColor (sec): Color for edge snapping.
        - snappedToFaceColor (sfc): Color for face snapping.
        - snappedToMagnetColor (smc): Color for magnet snapping.
        - snappedToVertexColor (svc): Color for vertex snapping.
        - query (q): Query mode flag
    """
@overload #Overload for polySplitCtx2 in ['query']
def polySplitCtx2(adjustEdgeFlow: float = ..., aef: float = ..., constrainToEdges: bool = ..., cte: bool = ..., edgeMagnets: int = ..., em: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., insertWithEdgeFlow: bool = ..., ief: bool = ..., snapTolerance: float = ..., st: float = ..., snappedToEdgeColor: [float, float, float] = ..., sec: [float, float, float] = ..., snappedToFaceColor: [float, float, float] = ..., sfc: [float, float, float] = ..., snappedToMagnetColor: [float, float, float] = ..., smc: [float, float, float] = ..., snappedToVertexColor: [float, float, float] = ..., svc: [float, float, float] = ..., query: bool = ..., q: bool = ...) -> None:
    """polySplitCtx2 is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx2('polySplitCtx2')
        cmds.setToolTo('polySplitCtx2')
    ```

    ---
    - Args:
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.
        - constrainToEdges (cte): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - edgeMagnets (em): number of extra magnets to snap onto, regularly spaced along the edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.
        - snapTolerance (st): precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.
        - snappedToEdgeColor (sec): Color for edge snapping.
        - snappedToFaceColor (sfc): Color for face snapping.
        - snappedToMagnetColor (smc): Color for magnet snapping.
        - snappedToVertexColor (svc): Color for vertex snapping.
        - query (q): Query mode flag
    """
@overload #Overload for polySplitCtx2 in ['edit']
def polySplitCtx2(adjustEdgeFlow: float = ..., constrainToEdges: bool = ..., edgeMagnets: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., insertWithEdgeFlow: bool = ..., snapTolerance: float = ..., snappedToEdgeColor: [float, float, float] = ..., snappedToFaceColor: [float, float, float] = ..., snappedToMagnetColor: [float, float, float] = ..., snappedToVertexColor: [float, float, float] = ..., edit: bool = ...) -> None:
    """polySplitCtx2 is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx2('polySplitCtx2')
        cmds.setToolTo('polySplitCtx2')
    ```

    ---
    - Args:
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.
        - constrainToEdges (cte): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - edgeMagnets (em): number of extra magnets to snap onto, regularly spaced along the edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.
        - snapTolerance (st): precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.
        - snappedToEdgeColor (sec): Color for edge snapping.
        - snappedToFaceColor (sfc): Color for face snapping.
        - snappedToMagnetColor (smc): Color for magnet snapping.
        - snappedToVertexColor (svc): Color for vertex snapping.
        - edit (e): Edit mode flag
    """
@overload #Overload for polySplitCtx2 in ['edit']
def polySplitCtx2(aef: float = ..., cte: bool = ..., em: int = ..., i1: str = ..., i2: str = ..., i3: str = ..., ief: bool = ..., st: float = ..., sec: [float, float, float] = ..., sfc: [float, float, float] = ..., smc: [float, float, float] = ..., svc: [float, float, float] = ..., e: bool = ...) -> None:
    """polySplitCtx2 is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx2('polySplitCtx2')
        cmds.setToolTo('polySplitCtx2')
    ```

    ---
    - Args:
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.
        - constrainToEdges (cte): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - edgeMagnets (em): number of extra magnets to snap onto, regularly spaced along the edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.
        - snapTolerance (st): precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.
        - snappedToEdgeColor (sec): Color for edge snapping.
        - snappedToFaceColor (sfc): Color for face snapping.
        - snappedToMagnetColor (smc): Color for magnet snapping.
        - snappedToVertexColor (svc): Color for vertex snapping.
        - edit (e): Edit mode flag
    """
@overload #Overload for polySplitCtx2 in ['edit']
def polySplitCtx2(adjustEdgeFlow: float = ..., aef: float = ..., constrainToEdges: bool = ..., cte: bool = ..., edgeMagnets: int = ..., em: int = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., insertWithEdgeFlow: bool = ..., ief: bool = ..., snapTolerance: float = ..., st: float = ..., snappedToEdgeColor: [float, float, float] = ..., sec: [float, float, float] = ..., snappedToFaceColor: [float, float, float] = ..., sfc: [float, float, float] = ..., snappedToMagnetColor: [float, float, float] = ..., smc: [float, float, float] = ..., snappedToVertexColor: [float, float, float] = ..., svc: [float, float, float] = ..., edit: bool = ..., e: bool = ...) -> None:
    """polySplitCtx2 is undoable, queryable, and editable.
    
    Create a new context to split facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=1, sy=1, n='pPlane1')
        # Create a new poly split context, then switch to it
        cmds.polySplitCtx2('polySplitCtx2')
        cmds.setToolTo('polySplitCtx2')
    ```

    ---
    - Args:
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.
        - constrainToEdges (cte): Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to
            snap to certain points along the edge.
        - edgeMagnets (em): number of extra magnets to snap onto, regularly spaced along the edge
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.
        - snapTolerance (st): precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.
        - snappedToEdgeColor (sec): Color for edge snapping.
        - snappedToFaceColor (sfc): Color for face snapping.
        - snappedToMagnetColor (smc): Color for magnet snapping.
        - snappedToVertexColor (svc): Color for vertex snapping.
        - edit (e): Edit mode flag
    """
