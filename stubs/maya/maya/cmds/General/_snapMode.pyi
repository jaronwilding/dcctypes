"""Stub files for General category in Maya commands, command: snapMode."""

from typing import Any, overload

@overload #Overload for snapMode in ['create']
def snapMode(curve: bool = ..., distanceIncrement: linear = ..., edgeMagnet: int = ..., edgeMagnetTolerance: float = ..., grid: bool = ..., liveFaceCenter: bool = ..., livePoint: bool = ..., meshCenter: bool = ..., pixelCenter: bool = ..., pixelSnap: bool = ..., point: bool = ..., tolerance: int = ..., useTolerance: bool = ..., uvTolerance: int = ..., viewPlane: bool = ...) -> bool:
    """snapMode is undoable, queryable, and NOT editable.
    
    The snapMode command is used to control snapping. It toggles the snapping
    modes in effect and sets information used for snapping.

    ---
    - Args:
        - curve (c): Set curve snap mode
        - distanceIncrement (dsi): Set the distance for the snapping to objects such as a lines or planes.
        - edgeMagnet (em): Number of extra magnets to snap onto, regularly spaced along the edge.
        - edgeMagnetTolerance (emt): Precision for edge magnet snapping.
        - grid (gr): Set grid snap mode
        - liveFaceCenter (lfc): While moving on live polygon objects, snap to its face centers.
        - livePoint (lp): While moving on live polygon objects, snap to its vertices.
        - meshCenter (mc): While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.
        - pixelCenter (pc): Snap UV to the center of the pixel instead of the corner.
        - pixelSnap (ps): Snap UVs to the nearest pixel center or corner.
        - point (p): Set point snap mode
        - tolerance (t): Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - useTolerance (ut): If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.
        - uvTolerance (uvt): uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor.  The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - viewPlane (vp): Set view-plane snap mode
    """
@overload #Overload for snapMode in ['create']
def snapMode(c: bool = ..., dsi: linear = ..., em: int = ..., emt: float = ..., gr: bool = ..., lfc: bool = ..., lp: bool = ..., mc: bool = ..., pc: bool = ..., ps: bool = ..., p: bool = ..., t: int = ..., ut: bool = ..., uvt: int = ..., vp: bool = ...) -> bool:
    """snapMode is undoable, queryable, and NOT editable.
    
    The snapMode command is used to control snapping. It toggles the snapping
    modes in effect and sets information used for snapping.

    ---
    - Args:
        - curve (c): Set curve snap mode
        - distanceIncrement (dsi): Set the distance for the snapping to objects such as a lines or planes.
        - edgeMagnet (em): Number of extra magnets to snap onto, regularly spaced along the edge.
        - edgeMagnetTolerance (emt): Precision for edge magnet snapping.
        - grid (gr): Set grid snap mode
        - liveFaceCenter (lfc): While moving on live polygon objects, snap to its face centers.
        - livePoint (lp): While moving on live polygon objects, snap to its vertices.
        - meshCenter (mc): While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.
        - pixelCenter (pc): Snap UV to the center of the pixel instead of the corner.
        - pixelSnap (ps): Snap UVs to the nearest pixel center or corner.
        - point (p): Set point snap mode
        - tolerance (t): Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - useTolerance (ut): If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.
        - uvTolerance (uvt): uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor.  The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - viewPlane (vp): Set view-plane snap mode
    """
@overload #Overload for snapMode in ['create']
def snapMode(curve: bool = ..., c: bool = ..., distanceIncrement: linear = ..., dsi: linear = ..., edgeMagnet: int = ..., em: int = ..., edgeMagnetTolerance: float = ..., emt: float = ..., grid: bool = ..., gr: bool = ..., liveFaceCenter: bool = ..., lfc: bool = ..., livePoint: bool = ..., lp: bool = ..., meshCenter: bool = ..., mc: bool = ..., pixelCenter: bool = ..., pc: bool = ..., pixelSnap: bool = ..., ps: bool = ..., point: bool = ..., p: bool = ..., tolerance: int = ..., t: int = ..., useTolerance: bool = ..., ut: bool = ..., uvTolerance: int = ..., uvt: int = ..., viewPlane: bool = ..., vp: bool = ...) -> bool:
    """snapMode is undoable, queryable, and NOT editable.
    
    The snapMode command is used to control snapping. It toggles the snapping
    modes in effect and sets information used for snapping.

    ---
    - Args:
        - curve (c): Set curve snap mode
        - distanceIncrement (dsi): Set the distance for the snapping to objects such as a lines or planes.
        - edgeMagnet (em): Number of extra magnets to snap onto, regularly spaced along the edge.
        - edgeMagnetTolerance (emt): Precision for edge magnet snapping.
        - grid (gr): Set grid snap mode
        - liveFaceCenter (lfc): While moving on live polygon objects, snap to its face centers.
        - livePoint (lp): While moving on live polygon objects, snap to its vertices.
        - meshCenter (mc): While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.
        - pixelCenter (pc): Snap UV to the center of the pixel instead of the corner.
        - pixelSnap (ps): Snap UVs to the nearest pixel center or corner.
        - point (p): Set point snap mode
        - tolerance (t): Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - useTolerance (ut): If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.
        - uvTolerance (uvt): uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor.  The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - viewPlane (vp): Set view-plane snap mode
    """
@overload #Overload for snapMode in ['query']
def snapMode(curve: bool = ..., distanceIncrement: linear = ..., edgeMagnet: int = ..., edgeMagnetTolerance: float = ..., grid: bool = ..., liveFaceCenter: bool = ..., livePoint: bool = ..., meshCenter: bool = ..., pixelCenter: bool = ..., pixelSnap: bool = ..., point: bool = ..., tolerance: int = ..., useTolerance: bool = ..., uvTolerance: int = ..., viewPlane: bool = ..., query: bool = ...) -> bool:
    """snapMode is undoable, queryable, and NOT editable.
    
    The snapMode command is used to control snapping. It toggles the snapping
    modes in effect and sets information used for snapping.

    ---
    - Args:
        - curve (c): Set curve snap mode
        - distanceIncrement (dsi): Set the distance for the snapping to objects such as a lines or planes.
        - edgeMagnet (em): Number of extra magnets to snap onto, regularly spaced along the edge.
        - edgeMagnetTolerance (emt): Precision for edge magnet snapping.
        - grid (gr): Set grid snap mode
        - liveFaceCenter (lfc): While moving on live polygon objects, snap to its face centers.
        - livePoint (lp): While moving on live polygon objects, snap to its vertices.
        - meshCenter (mc): While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.
        - pixelCenter (pc): Snap UV to the center of the pixel instead of the corner.
        - pixelSnap (ps): Snap UVs to the nearest pixel center or corner.
        - point (p): Set point snap mode
        - tolerance (t): Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - useTolerance (ut): If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.
        - uvTolerance (uvt): uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor.  The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - viewPlane (vp): Set view-plane snap mode
        - query (q): Query mode flag
    """
@overload #Overload for snapMode in ['query']
def snapMode(c: bool = ..., dsi: linear = ..., em: int = ..., emt: float = ..., gr: bool = ..., lfc: bool = ..., lp: bool = ..., mc: bool = ..., pc: bool = ..., ps: bool = ..., p: bool = ..., t: int = ..., ut: bool = ..., uvt: int = ..., vp: bool = ..., q: bool = ...) -> bool:
    """snapMode is undoable, queryable, and NOT editable.
    
    The snapMode command is used to control snapping. It toggles the snapping
    modes in effect and sets information used for snapping.

    ---
    - Args:
        - curve (c): Set curve snap mode
        - distanceIncrement (dsi): Set the distance for the snapping to objects such as a lines or planes.
        - edgeMagnet (em): Number of extra magnets to snap onto, regularly spaced along the edge.
        - edgeMagnetTolerance (emt): Precision for edge magnet snapping.
        - grid (gr): Set grid snap mode
        - liveFaceCenter (lfc): While moving on live polygon objects, snap to its face centers.
        - livePoint (lp): While moving on live polygon objects, snap to its vertices.
        - meshCenter (mc): While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.
        - pixelCenter (pc): Snap UV to the center of the pixel instead of the corner.
        - pixelSnap (ps): Snap UVs to the nearest pixel center or corner.
        - point (p): Set point snap mode
        - tolerance (t): Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - useTolerance (ut): If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.
        - uvTolerance (uvt): uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor.  The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - viewPlane (vp): Set view-plane snap mode
        - query (q): Query mode flag
    """
@overload #Overload for snapMode in ['query']
def snapMode(curve: bool = ..., c: bool = ..., distanceIncrement: linear = ..., dsi: linear = ..., edgeMagnet: int = ..., em: int = ..., edgeMagnetTolerance: float = ..., emt: float = ..., grid: bool = ..., gr: bool = ..., liveFaceCenter: bool = ..., lfc: bool = ..., livePoint: bool = ..., lp: bool = ..., meshCenter: bool = ..., mc: bool = ..., pixelCenter: bool = ..., pc: bool = ..., pixelSnap: bool = ..., ps: bool = ..., point: bool = ..., p: bool = ..., tolerance: int = ..., t: int = ..., useTolerance: bool = ..., ut: bool = ..., uvTolerance: int = ..., uvt: int = ..., viewPlane: bool = ..., vp: bool = ..., query: bool = ..., q: bool = ...) -> bool:
    """snapMode is undoable, queryable, and NOT editable.
    
    The snapMode command is used to control snapping. It toggles the snapping
    modes in effect and sets information used for snapping.

    ---
    - Args:
        - curve (c): Set curve snap mode
        - distanceIncrement (dsi): Set the distance for the snapping to objects such as a lines or planes.
        - edgeMagnet (em): Number of extra magnets to snap onto, regularly spaced along the edge.
        - edgeMagnetTolerance (emt): Precision for edge magnet snapping.
        - grid (gr): Set grid snap mode
        - liveFaceCenter (lfc): While moving on live polygon objects, snap to its face centers.
        - livePoint (lp): While moving on live polygon objects, snap to its vertices.
        - meshCenter (mc): While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.
        - pixelCenter (pc): Snap UV to the center of the pixel instead of the corner.
        - pixelSnap (ps): Snap UVs to the nearest pixel center or corner.
        - point (p): Set point snap mode
        - tolerance (t): Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - useTolerance (ut): If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.
        - uvTolerance (uvt): uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor.  The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - viewPlane (vp): Set view-plane snap mode
        - query (q): Query mode flag
    """
@overload #Overload for snapMode in ['edit']
def snapMode(curve: bool = ..., distanceIncrement: linear = ..., edgeMagnet: int = ..., edgeMagnetTolerance: float = ..., grid: bool = ..., liveFaceCenter: bool = ..., livePoint: bool = ..., meshCenter: bool = ..., pixelCenter: bool = ..., pixelSnap: bool = ..., point: bool = ..., tolerance: int = ..., useTolerance: bool = ..., uvTolerance: int = ..., viewPlane: bool = ..., edit: bool = ...) -> bool:
    """snapMode is undoable, queryable, and NOT editable.
    
    The snapMode command is used to control snapping. It toggles the snapping
    modes in effect and sets information used for snapping.

    ---
    - Args:
        - curve (c): Set curve snap mode
        - distanceIncrement (dsi): Set the distance for the snapping to objects such as a lines or planes.
        - edgeMagnet (em): Number of extra magnets to snap onto, regularly spaced along the edge.
        - edgeMagnetTolerance (emt): Precision for edge magnet snapping.
        - grid (gr): Set grid snap mode
        - liveFaceCenter (lfc): While moving on live polygon objects, snap to its face centers.
        - livePoint (lp): While moving on live polygon objects, snap to its vertices.
        - meshCenter (mc): While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.
        - pixelCenter (pc): Snap UV to the center of the pixel instead of the corner.
        - pixelSnap (ps): Snap UVs to the nearest pixel center or corner.
        - point (p): Set point snap mode
        - tolerance (t): Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - useTolerance (ut): If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.
        - uvTolerance (uvt): uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor.  The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - viewPlane (vp): Set view-plane snap mode
        - edit (e): Edit mode flag
    """
@overload #Overload for snapMode in ['edit']
def snapMode(c: bool = ..., dsi: linear = ..., em: int = ..., emt: float = ..., gr: bool = ..., lfc: bool = ..., lp: bool = ..., mc: bool = ..., pc: bool = ..., ps: bool = ..., p: bool = ..., t: int = ..., ut: bool = ..., uvt: int = ..., vp: bool = ..., e: bool = ...) -> bool:
    """snapMode is undoable, queryable, and NOT editable.
    
    The snapMode command is used to control snapping. It toggles the snapping
    modes in effect and sets information used for snapping.

    ---
    - Args:
        - curve (c): Set curve snap mode
        - distanceIncrement (dsi): Set the distance for the snapping to objects such as a lines or planes.
        - edgeMagnet (em): Number of extra magnets to snap onto, regularly spaced along the edge.
        - edgeMagnetTolerance (emt): Precision for edge magnet snapping.
        - grid (gr): Set grid snap mode
        - liveFaceCenter (lfc): While moving on live polygon objects, snap to its face centers.
        - livePoint (lp): While moving on live polygon objects, snap to its vertices.
        - meshCenter (mc): While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.
        - pixelCenter (pc): Snap UV to the center of the pixel instead of the corner.
        - pixelSnap (ps): Snap UVs to the nearest pixel center or corner.
        - point (p): Set point snap mode
        - tolerance (t): Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - useTolerance (ut): If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.
        - uvTolerance (uvt): uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor.  The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - viewPlane (vp): Set view-plane snap mode
        - edit (e): Edit mode flag
    """
@overload #Overload for snapMode in ['edit']
def snapMode(curve: bool = ..., c: bool = ..., distanceIncrement: linear = ..., dsi: linear = ..., edgeMagnet: int = ..., em: int = ..., edgeMagnetTolerance: float = ..., emt: float = ..., grid: bool = ..., gr: bool = ..., liveFaceCenter: bool = ..., lfc: bool = ..., livePoint: bool = ..., lp: bool = ..., meshCenter: bool = ..., mc: bool = ..., pixelCenter: bool = ..., pc: bool = ..., pixelSnap: bool = ..., ps: bool = ..., point: bool = ..., p: bool = ..., tolerance: int = ..., t: int = ..., useTolerance: bool = ..., ut: bool = ..., uvTolerance: int = ..., uvt: int = ..., viewPlane: bool = ..., vp: bool = ..., edit: bool = ..., e: bool = ...) -> bool:
    """snapMode is undoable, queryable, and NOT editable.
    
    The snapMode command is used to control snapping. It toggles the snapping
    modes in effect and sets information used for snapping.

    ---
    - Args:
        - curve (c): Set curve snap mode
        - distanceIncrement (dsi): Set the distance for the snapping to objects such as a lines or planes.
        - edgeMagnet (em): Number of extra magnets to snap onto, regularly spaced along the edge.
        - edgeMagnetTolerance (emt): Precision for edge magnet snapping.
        - grid (gr): Set grid snap mode
        - liveFaceCenter (lfc): While moving on live polygon objects, snap to its face centers.
        - livePoint (lp): While moving on live polygon objects, snap to its vertices.
        - meshCenter (mc): While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.
        - pixelCenter (pc): Snap UV to the center of the pixel instead of the corner.
        - pixelSnap (ps): Snap UVs to the nearest pixel center or corner.
        - point (p): Set point snap mode
        - tolerance (t): Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - useTolerance (ut): If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.
        - uvTolerance (uvt): uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor.  The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        - viewPlane (vp): Set view-plane snap mode
        - edit (e): Edit mode flag
    """
