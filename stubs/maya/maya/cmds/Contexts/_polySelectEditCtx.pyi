"""Stub files for Contexts category in Maya commands, command: polySelectEditCtx."""

from typing import Any, overload

@overload #Overload for polySelectEditCtx in ['create']
def polySelectEditCtx(absoluteOffset: bool = ..., adjustEdgeFlow: float = ..., autoComplete: bool = ..., deleteEdge: bool = ..., divisions: int = ..., endVertexOffset: float = ..., exists: bool = ..., fixQuads: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., insertWithEdgeFlow: bool = ..., mode: int = ..., smoothingAngle: angle = ..., splitType: int = ..., startVertexOffset: float = ..., useEqualMultiplier: bool = ...) -> str:
    """polySelectEditCtx is undoable, queryable, and editable.
    
    Create a new context to select and edit polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=5, sy=5, n='pPlane1')
        # Create a new poly select and edit context, then switch to it
        cmds.polySelectEditCtx('polySelectEditCtx1')
        cmds.setToolTo('polySelectEditCtx1')
    ```

    ---
    - Args:
        - absoluteOffset (abo): This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.Default:1.0f
        - autoComplete (ac): If true then use auto completion on selections
        - deleteEdge (de): When true, the end edges are deleted so the end triangles are converted to quads.
        - divisions (div): Number of divisions.Default:2
        - endVertexOffset (evo): Weight value controlling the offset of the end vertex of the edgeloop.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - fixQuads (fq): Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face.Default:false
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.Default:false
        - mode (m): which mode to work on.  Available modes are 1-loop and 2-ring
        - smoothingAngle (sma): Angle below which new edges will be smoothedDefault:kPi
        - splitType (stp): Format: 0 - Absolute, 1 - Relative, 2 - MultiDefault:TdnpolySplitRing::Relative
        - startVertexOffset (svo): Weight value controlling the offset of the start vertex of the edgeloop.
        - useEqualMultiplier (uem): Changes how the profile curve effects the offset when doing a multisplit.  If true then the verts will be offset the same distance based on the shortest edge being split.  If false then each inserted edge loop will be offset a distance
            relative to the length of the edge that is being split.Default:true
    """
@overload #Overload for polySelectEditCtx in ['create']
def polySelectEditCtx(abo: bool = ..., aef: float = ..., ac: bool = ..., de: bool = ..., div: int = ..., evo: float = ..., ex: bool = ..., fq: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ief: bool = ..., m: int = ..., sma: angle = ..., stp: int = ..., svo: float = ..., uem: bool = ...) -> str:
    """polySelectEditCtx is undoable, queryable, and editable.
    
    Create a new context to select and edit polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=5, sy=5, n='pPlane1')
        # Create a new poly select and edit context, then switch to it
        cmds.polySelectEditCtx('polySelectEditCtx1')
        cmds.setToolTo('polySelectEditCtx1')
    ```

    ---
    - Args:
        - absoluteOffset (abo): This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.Default:1.0f
        - autoComplete (ac): If true then use auto completion on selections
        - deleteEdge (de): When true, the end edges are deleted so the end triangles are converted to quads.
        - divisions (div): Number of divisions.Default:2
        - endVertexOffset (evo): Weight value controlling the offset of the end vertex of the edgeloop.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - fixQuads (fq): Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face.Default:false
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.Default:false
        - mode (m): which mode to work on.  Available modes are 1-loop and 2-ring
        - smoothingAngle (sma): Angle below which new edges will be smoothedDefault:kPi
        - splitType (stp): Format: 0 - Absolute, 1 - Relative, 2 - MultiDefault:TdnpolySplitRing::Relative
        - startVertexOffset (svo): Weight value controlling the offset of the start vertex of the edgeloop.
        - useEqualMultiplier (uem): Changes how the profile curve effects the offset when doing a multisplit.  If true then the verts will be offset the same distance based on the shortest edge being split.  If false then each inserted edge loop will be offset a distance
            relative to the length of the edge that is being split.Default:true
    """
@overload #Overload for polySelectEditCtx in ['create']
def polySelectEditCtx(absoluteOffset: bool = ..., abo: bool = ..., adjustEdgeFlow: float = ..., aef: float = ..., autoComplete: bool = ..., ac: bool = ..., deleteEdge: bool = ..., de: bool = ..., divisions: int = ..., div: int = ..., endVertexOffset: float = ..., evo: float = ..., exists: bool = ..., ex: bool = ..., fixQuads: bool = ..., fq: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., insertWithEdgeFlow: bool = ..., ief: bool = ..., mode: int = ..., m: int = ..., smoothingAngle: angle = ..., sma: angle = ..., splitType: int = ..., stp: int = ..., startVertexOffset: float = ..., svo: float = ..., useEqualMultiplier: bool = ..., uem: bool = ...) -> str:
    """polySelectEditCtx is undoable, queryable, and editable.
    
    Create a new context to select and edit polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=5, sy=5, n='pPlane1')
        # Create a new poly select and edit context, then switch to it
        cmds.polySelectEditCtx('polySelectEditCtx1')
        cmds.setToolTo('polySelectEditCtx1')
    ```

    ---
    - Args:
        - absoluteOffset (abo): This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.Default:1.0f
        - autoComplete (ac): If true then use auto completion on selections
        - deleteEdge (de): When true, the end edges are deleted so the end triangles are converted to quads.
        - divisions (div): Number of divisions.Default:2
        - endVertexOffset (evo): Weight value controlling the offset of the end vertex of the edgeloop.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - fixQuads (fq): Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face.Default:false
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.Default:false
        - mode (m): which mode to work on.  Available modes are 1-loop and 2-ring
        - smoothingAngle (sma): Angle below which new edges will be smoothedDefault:kPi
        - splitType (stp): Format: 0 - Absolute, 1 - Relative, 2 - MultiDefault:TdnpolySplitRing::Relative
        - startVertexOffset (svo): Weight value controlling the offset of the start vertex of the edgeloop.
        - useEqualMultiplier (uem): Changes how the profile curve effects the offset when doing a multisplit.  If true then the verts will be offset the same distance based on the shortest edge being split.  If false then each inserted edge loop will be offset a distance
            relative to the length of the edge that is being split.Default:true
    """
@overload #Overload for polySelectEditCtx in ['query']
def polySelectEditCtx(absoluteOffset: bool = ..., adjustEdgeFlow: float = ..., deleteEdge: bool = ..., divisions: int = ..., endVertexOffset: float = ..., fixQuads: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., insertWithEdgeFlow: bool = ..., mode: int = ..., smoothingAngle: angle = ..., splitType: int = ..., startVertexOffset: float = ..., useEqualMultiplier: bool = ..., query: bool = ...) -> str:
    """polySelectEditCtx is undoable, queryable, and editable.
    
    Create a new context to select and edit polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=5, sy=5, n='pPlane1')
        # Create a new poly select and edit context, then switch to it
        cmds.polySelectEditCtx('polySelectEditCtx1')
        cmds.setToolTo('polySelectEditCtx1')
    ```

    ---
    - Args:
        - absoluteOffset (abo): This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.Default:1.0f
        - deleteEdge (de): When true, the end edges are deleted so the end triangles are converted to quads.
        - divisions (div): Number of divisions.Default:2
        - endVertexOffset (evo): Weight value controlling the offset of the end vertex of the edgeloop.
        - fixQuads (fq): Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face.Default:false
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.Default:false
        - mode (m): which mode to work on.  Available modes are 1-loop and 2-ring
        - smoothingAngle (sma): Angle below which new edges will be smoothedDefault:kPi
        - splitType (stp): Format: 0 - Absolute, 1 - Relative, 2 - MultiDefault:TdnpolySplitRing::Relative
        - startVertexOffset (svo): Weight value controlling the offset of the start vertex of the edgeloop.
        - useEqualMultiplier (uem): Changes how the profile curve effects the offset when doing a multisplit.  If true then the verts will be offset the same distance based on the shortest edge being split.  If false then each inserted edge loop will be offset a distance
            relative to the length of the edge that is being split.Default:true
        - query (q): Query mode flag
    """
@overload #Overload for polySelectEditCtx in ['query']
def polySelectEditCtx(abo: bool = ..., aef: float = ..., de: bool = ..., div: int = ..., evo: float = ..., fq: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ief: bool = ..., m: int = ..., sma: angle = ..., stp: int = ..., svo: float = ..., uem: bool = ..., q: bool = ...) -> str:
    """polySelectEditCtx is undoable, queryable, and editable.
    
    Create a new context to select and edit polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=5, sy=5, n='pPlane1')
        # Create a new poly select and edit context, then switch to it
        cmds.polySelectEditCtx('polySelectEditCtx1')
        cmds.setToolTo('polySelectEditCtx1')
    ```

    ---
    - Args:
        - absoluteOffset (abo): This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.Default:1.0f
        - deleteEdge (de): When true, the end edges are deleted so the end triangles are converted to quads.
        - divisions (div): Number of divisions.Default:2
        - endVertexOffset (evo): Weight value controlling the offset of the end vertex of the edgeloop.
        - fixQuads (fq): Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face.Default:false
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.Default:false
        - mode (m): which mode to work on.  Available modes are 1-loop and 2-ring
        - smoothingAngle (sma): Angle below which new edges will be smoothedDefault:kPi
        - splitType (stp): Format: 0 - Absolute, 1 - Relative, 2 - MultiDefault:TdnpolySplitRing::Relative
        - startVertexOffset (svo): Weight value controlling the offset of the start vertex of the edgeloop.
        - useEqualMultiplier (uem): Changes how the profile curve effects the offset when doing a multisplit.  If true then the verts will be offset the same distance based on the shortest edge being split.  If false then each inserted edge loop will be offset a distance
            relative to the length of the edge that is being split.Default:true
        - query (q): Query mode flag
    """
@overload #Overload for polySelectEditCtx in ['query']
def polySelectEditCtx(absoluteOffset: bool = ..., abo: bool = ..., adjustEdgeFlow: float = ..., aef: float = ..., deleteEdge: bool = ..., de: bool = ..., divisions: int = ..., div: int = ..., endVertexOffset: float = ..., evo: float = ..., fixQuads: bool = ..., fq: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., insertWithEdgeFlow: bool = ..., ief: bool = ..., mode: int = ..., m: int = ..., smoothingAngle: angle = ..., sma: angle = ..., splitType: int = ..., stp: int = ..., startVertexOffset: float = ..., svo: float = ..., useEqualMultiplier: bool = ..., uem: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """polySelectEditCtx is undoable, queryable, and editable.
    
    Create a new context to select and edit polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=5, sy=5, n='pPlane1')
        # Create a new poly select and edit context, then switch to it
        cmds.polySelectEditCtx('polySelectEditCtx1')
        cmds.setToolTo('polySelectEditCtx1')
    ```

    ---
    - Args:
        - absoluteOffset (abo): This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.Default:1.0f
        - deleteEdge (de): When true, the end edges are deleted so the end triangles are converted to quads.
        - divisions (div): Number of divisions.Default:2
        - endVertexOffset (evo): Weight value controlling the offset of the end vertex of the edgeloop.
        - fixQuads (fq): Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face.Default:false
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.Default:false
        - mode (m): which mode to work on.  Available modes are 1-loop and 2-ring
        - smoothingAngle (sma): Angle below which new edges will be smoothedDefault:kPi
        - splitType (stp): Format: 0 - Absolute, 1 - Relative, 2 - MultiDefault:TdnpolySplitRing::Relative
        - startVertexOffset (svo): Weight value controlling the offset of the start vertex of the edgeloop.
        - useEqualMultiplier (uem): Changes how the profile curve effects the offset when doing a multisplit.  If true then the verts will be offset the same distance based on the shortest edge being split.  If false then each inserted edge loop will be offset a distance
            relative to the length of the edge that is being split.Default:true
        - query (q): Query mode flag
    """
@overload #Overload for polySelectEditCtx in ['edit']
def polySelectEditCtx(absoluteOffset: bool = ..., adjustEdgeFlow: float = ..., deleteEdge: bool = ..., divisions: int = ..., endVertexOffset: float = ..., fixQuads: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., insertWithEdgeFlow: bool = ..., mode: int = ..., smoothingAngle: angle = ..., splitType: int = ..., startVertexOffset: float = ..., useEqualMultiplier: bool = ..., edit: bool = ...) -> str:
    """polySelectEditCtx is undoable, queryable, and editable.
    
    Create a new context to select and edit polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=5, sy=5, n='pPlane1')
        # Create a new poly select and edit context, then switch to it
        cmds.polySelectEditCtx('polySelectEditCtx1')
        cmds.setToolTo('polySelectEditCtx1')
    ```

    ---
    - Args:
        - absoluteOffset (abo): This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.Default:1.0f
        - deleteEdge (de): When true, the end edges are deleted so the end triangles are converted to quads.
        - divisions (div): Number of divisions.Default:2
        - endVertexOffset (evo): Weight value controlling the offset of the end vertex of the edgeloop.
        - fixQuads (fq): Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face.Default:false
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.Default:false
        - mode (m): which mode to work on.  Available modes are 1-loop and 2-ring
        - smoothingAngle (sma): Angle below which new edges will be smoothedDefault:kPi
        - splitType (stp): Format: 0 - Absolute, 1 - Relative, 2 - MultiDefault:TdnpolySplitRing::Relative
        - startVertexOffset (svo): Weight value controlling the offset of the start vertex of the edgeloop.
        - useEqualMultiplier (uem): Changes how the profile curve effects the offset when doing a multisplit.  If true then the verts will be offset the same distance based on the shortest edge being split.  If false then each inserted edge loop will be offset a distance
            relative to the length of the edge that is being split.Default:true
        - edit (e): Edit mode flag
    """
@overload #Overload for polySelectEditCtx in ['edit']
def polySelectEditCtx(abo: bool = ..., aef: float = ..., de: bool = ..., div: int = ..., evo: float = ..., fq: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ief: bool = ..., m: int = ..., sma: angle = ..., stp: int = ..., svo: float = ..., uem: bool = ..., e: bool = ...) -> str:
    """polySelectEditCtx is undoable, queryable, and editable.
    
    Create a new context to select and edit polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=5, sy=5, n='pPlane1')
        # Create a new poly select and edit context, then switch to it
        cmds.polySelectEditCtx('polySelectEditCtx1')
        cmds.setToolTo('polySelectEditCtx1')
    ```

    ---
    - Args:
        - absoluteOffset (abo): This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.Default:1.0f
        - deleteEdge (de): When true, the end edges are deleted so the end triangles are converted to quads.
        - divisions (div): Number of divisions.Default:2
        - endVertexOffset (evo): Weight value controlling the offset of the end vertex of the edgeloop.
        - fixQuads (fq): Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face.Default:false
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.Default:false
        - mode (m): which mode to work on.  Available modes are 1-loop and 2-ring
        - smoothingAngle (sma): Angle below which new edges will be smoothedDefault:kPi
        - splitType (stp): Format: 0 - Absolute, 1 - Relative, 2 - MultiDefault:TdnpolySplitRing::Relative
        - startVertexOffset (svo): Weight value controlling the offset of the start vertex of the edgeloop.
        - useEqualMultiplier (uem): Changes how the profile curve effects the offset when doing a multisplit.  If true then the verts will be offset the same distance based on the shortest edge being split.  If false then each inserted edge loop will be offset a distance
            relative to the length of the edge that is being split.Default:true
        - edit (e): Edit mode flag
    """
@overload #Overload for polySelectEditCtx in ['edit']
def polySelectEditCtx(absoluteOffset: bool = ..., abo: bool = ..., adjustEdgeFlow: float = ..., aef: float = ..., deleteEdge: bool = ..., de: bool = ..., divisions: int = ..., div: int = ..., endVertexOffset: float = ..., evo: float = ..., fixQuads: bool = ..., fq: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., insertWithEdgeFlow: bool = ..., ief: bool = ..., mode: int = ..., m: int = ..., smoothingAngle: angle = ..., sma: angle = ..., splitType: int = ..., stp: int = ..., startVertexOffset: float = ..., svo: float = ..., useEqualMultiplier: bool = ..., uem: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """polySelectEditCtx is undoable, queryable, and editable.
    
    Create a new context to select and edit polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=5, sy=5, n='pPlane1')
        # Create a new poly select and edit context, then switch to it
        cmds.polySelectEditCtx('polySelectEditCtx1')
        cmds.setToolTo('polySelectEditCtx1')
    ```

    ---
    - Args:
        - absoluteOffset (abo): This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.
        - adjustEdgeFlow (aef): The weight value of the edge vertices to be positioned.Default:1.0f
        - deleteEdge (de): When true, the end edges are deleted so the end triangles are converted to quads.
        - divisions (div): Number of divisions.Default:2
        - endVertexOffset (evo): Weight value controlling the offset of the end vertex of the edgeloop.
        - fixQuads (fq): Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face.Default:false
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - insertWithEdgeFlow (ief): True to enable edge flow. Otherwise, the edge flow is disabled.Default:false
        - mode (m): which mode to work on.  Available modes are 1-loop and 2-ring
        - smoothingAngle (sma): Angle below which new edges will be smoothedDefault:kPi
        - splitType (stp): Format: 0 - Absolute, 1 - Relative, 2 - MultiDefault:TdnpolySplitRing::Relative
        - startVertexOffset (svo): Weight value controlling the offset of the start vertex of the edgeloop.
        - useEqualMultiplier (uem): Changes how the profile curve effects the offset when doing a multisplit.  If true then the verts will be offset the same distance based on the shortest edge being split.  If false then each inserted edge loop will be offset a distance
            relative to the length of the edge that is being split.Default:true
        - edit (e): Edit mode flag
    """
