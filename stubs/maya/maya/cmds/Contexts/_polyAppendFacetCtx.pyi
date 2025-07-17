"""Stub files for Contexts category in Maya commands, command: polyAppendFacetCtx."""

from typing import Any, overload

@overload #Overload for polyAppendFacetCtx in ['create']
def polyAppendFacetCtx(append: bool = ..., exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., maximumNumberOfPoints: int = ..., planarConstraint: bool = ..., rotate: float = ..., subdivision: int = ..., texture: int = ...) -> None:
    """polyAppendFacetCtx is undoable, queryable, and editable.
    
    Create a new context to append facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')
        # Create a new poly append facet context, set it to add four vertices per new edge, and then switch to it
        cmds.polyAppendFacetCtx('polyAppendFacetCtx1', s=4)
        cmds.setToolTo('polyAppendFacetCtx1')
    ```

    ---
    - Args:
        - append (ap): Allows to switch to polyCreateFacetCtx tool
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): Allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane. Selected edges will be checked as well.
        - rotate (r): Rotate current facet around the first edge selected.
        - subdivision (s): Number of sub-edges created for each new edge. Default is 1.
        - texture (tx): Number of textures. Default is 1.
    """
@overload #Overload for polyAppendFacetCtx in ['create']
def polyAppendFacetCtx(ap: bool = ..., ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., mp: int = ..., pc: bool = ..., r: float = ..., s: int = ..., tx: int = ...) -> None:
    """polyAppendFacetCtx is undoable, queryable, and editable.
    
    Create a new context to append facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')
        # Create a new poly append facet context, set it to add four vertices per new edge, and then switch to it
        cmds.polyAppendFacetCtx('polyAppendFacetCtx1', s=4)
        cmds.setToolTo('polyAppendFacetCtx1')
    ```

    ---
    - Args:
        - append (ap): Allows to switch to polyCreateFacetCtx tool
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): Allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane. Selected edges will be checked as well.
        - rotate (r): Rotate current facet around the first edge selected.
        - subdivision (s): Number of sub-edges created for each new edge. Default is 1.
        - texture (tx): Number of textures. Default is 1.
    """
@overload #Overload for polyAppendFacetCtx in ['create']
def polyAppendFacetCtx(append: bool = ..., ap: bool = ..., exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., maximumNumberOfPoints: int = ..., mp: int = ..., planarConstraint: bool = ..., pc: bool = ..., rotate: float = ..., r: float = ..., subdivision: int = ..., s: int = ..., texture: int = ..., tx: int = ...) -> None:
    """polyAppendFacetCtx is undoable, queryable, and editable.
    
    Create a new context to append facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')
        # Create a new poly append facet context, set it to add four vertices per new edge, and then switch to it
        cmds.polyAppendFacetCtx('polyAppendFacetCtx1', s=4)
        cmds.setToolTo('polyAppendFacetCtx1')
    ```

    ---
    - Args:
        - append (ap): Allows to switch to polyCreateFacetCtx tool
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): Allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane. Selected edges will be checked as well.
        - rotate (r): Rotate current facet around the first edge selected.
        - subdivision (s): Number of sub-edges created for each new edge. Default is 1.
        - texture (tx): Number of textures. Default is 1.
    """
@overload #Overload for polyAppendFacetCtx in ['query']
def polyAppendFacetCtx(append: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., isRotateAvailable: bool = ..., maximumNumberOfPoints: int = ..., planarConstraint: bool = ..., rotate: float = ..., subdivision: int = ..., texture: int = ..., query: bool = ...) -> None:
    """polyAppendFacetCtx is undoable, queryable, and editable.
    
    Create a new context to append facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')
        # Create a new poly append facet context, set it to add four vertices per new edge, and then switch to it
        cmds.polyAppendFacetCtx('polyAppendFacetCtx1', s=4)
        cmds.setToolTo('polyAppendFacetCtx1')
    ```

    ---
    - Args:
        - append (ap): Allows to switch to polyCreateFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - isRotateAvailable (isr): Tells if the control associated to rotate flag is available. If several edges are already selected and they are not aligned (thus there is no "rotation axis") the rotation is no longer available.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): Allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane. Selected edges will be checked as well.
        - rotate (r): Rotate current facet around the first edge selected.
        - subdivision (s): Number of sub-edges created for each new edge. Default is 1.
        - texture (tx): Number of textures. Default is 1.
        - query (q): Query mode flag
    """
@overload #Overload for polyAppendFacetCtx in ['query']
def polyAppendFacetCtx(ap: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., isr: bool = ..., mp: int = ..., pc: bool = ..., r: float = ..., s: int = ..., tx: int = ..., q: bool = ...) -> None:
    """polyAppendFacetCtx is undoable, queryable, and editable.
    
    Create a new context to append facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')
        # Create a new poly append facet context, set it to add four vertices per new edge, and then switch to it
        cmds.polyAppendFacetCtx('polyAppendFacetCtx1', s=4)
        cmds.setToolTo('polyAppendFacetCtx1')
    ```

    ---
    - Args:
        - append (ap): Allows to switch to polyCreateFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - isRotateAvailable (isr): Tells if the control associated to rotate flag is available. If several edges are already selected and they are not aligned (thus there is no "rotation axis") the rotation is no longer available.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): Allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane. Selected edges will be checked as well.
        - rotate (r): Rotate current facet around the first edge selected.
        - subdivision (s): Number of sub-edges created for each new edge. Default is 1.
        - texture (tx): Number of textures. Default is 1.
        - query (q): Query mode flag
    """
@overload #Overload for polyAppendFacetCtx in ['query']
def polyAppendFacetCtx(append: bool = ..., ap: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., isRotateAvailable: bool = ..., isr: bool = ..., maximumNumberOfPoints: int = ..., mp: int = ..., planarConstraint: bool = ..., pc: bool = ..., rotate: float = ..., r: float = ..., subdivision: int = ..., s: int = ..., texture: int = ..., tx: int = ..., query: bool = ..., q: bool = ...) -> None:
    """polyAppendFacetCtx is undoable, queryable, and editable.
    
    Create a new context to append facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')
        # Create a new poly append facet context, set it to add four vertices per new edge, and then switch to it
        cmds.polyAppendFacetCtx('polyAppendFacetCtx1', s=4)
        cmds.setToolTo('polyAppendFacetCtx1')
    ```

    ---
    - Args:
        - append (ap): Allows to switch to polyCreateFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - isRotateAvailable (isr): Tells if the control associated to rotate flag is available. If several edges are already selected and they are not aligned (thus there is no "rotation axis") the rotation is no longer available.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): Allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane. Selected edges will be checked as well.
        - rotate (r): Rotate current facet around the first edge selected.
        - subdivision (s): Number of sub-edges created for each new edge. Default is 1.
        - texture (tx): Number of textures. Default is 1.
        - query (q): Query mode flag
    """
@overload #Overload for polyAppendFacetCtx in ['edit']
def polyAppendFacetCtx(append: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., maximumNumberOfPoints: int = ..., planarConstraint: bool = ..., rotate: float = ..., subdivision: int = ..., texture: int = ..., edit: bool = ...) -> None:
    """polyAppendFacetCtx is undoable, queryable, and editable.
    
    Create a new context to append facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')
        # Create a new poly append facet context, set it to add four vertices per new edge, and then switch to it
        cmds.polyAppendFacetCtx('polyAppendFacetCtx1', s=4)
        cmds.setToolTo('polyAppendFacetCtx1')
    ```

    ---
    - Args:
        - append (ap): Allows to switch to polyCreateFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): Allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane. Selected edges will be checked as well.
        - rotate (r): Rotate current facet around the first edge selected.
        - subdivision (s): Number of sub-edges created for each new edge. Default is 1.
        - texture (tx): Number of textures. Default is 1.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyAppendFacetCtx in ['edit']
def polyAppendFacetCtx(ap: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., mp: int = ..., pc: bool = ..., r: float = ..., s: int = ..., tx: int = ..., e: bool = ...) -> None:
    """polyAppendFacetCtx is undoable, queryable, and editable.
    
    Create a new context to append facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')
        # Create a new poly append facet context, set it to add four vertices per new edge, and then switch to it
        cmds.polyAppendFacetCtx('polyAppendFacetCtx1', s=4)
        cmds.setToolTo('polyAppendFacetCtx1')
    ```

    ---
    - Args:
        - append (ap): Allows to switch to polyCreateFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): Allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane. Selected edges will be checked as well.
        - rotate (r): Rotate current facet around the first edge selected.
        - subdivision (s): Number of sub-edges created for each new edge. Default is 1.
        - texture (tx): Number of textures. Default is 1.
        - edit (e): Edit mode flag
    """
@overload #Overload for polyAppendFacetCtx in ['edit']
def polyAppendFacetCtx(append: bool = ..., ap: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., maximumNumberOfPoints: int = ..., mp: int = ..., planarConstraint: bool = ..., pc: bool = ..., rotate: float = ..., r: float = ..., subdivision: int = ..., s: int = ..., texture: int = ..., tx: int = ..., edit: bool = ..., e: bool = ...) -> None:
    """polyAppendFacetCtx is undoable, queryable, and editable.
    
    Create a new context to append facets on polygonal objects

    Example:
    ```python
        import maya.cmds as cmds
        # Create a poly plane
        cmds.polyPlane(w=10, h=10, sx=10, sy=10, n='pPlane1')
        # Create a new poly append facet context, set it to add four vertices per new edge, and then switch to it
        cmds.polyAppendFacetCtx('polyAppendFacetCtx1', s=4)
        cmds.setToolTo('polyAppendFacetCtx1')
    ```

    ---
    - Args:
        - append (ap): Allows to switch to polyCreateFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): Allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane. Selected edges will be checked as well.
        - rotate (r): Rotate current facet around the first edge selected.
        - subdivision (s): Number of sub-edges created for each new edge. Default is 1.
        - texture (tx): Number of textures. Default is 1.
        - edit (e): Edit mode flag
    """
