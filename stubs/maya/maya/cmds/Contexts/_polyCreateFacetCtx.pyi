"""Stub files for Contexts category in Maya commands, command: polyCreateFacetCtx."""

from typing import Any, overload

@overload #Overload for polyCreateFacetCtx in ['create']
def polyCreateFacetCtx(append: bool = ..., exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., maximumNumberOfPoints: int = ..., planarConstraint: bool = ..., subdivision: int = ..., texture: int = ...) -> None:
    """polyCreateFacetCtx is undoable, queryable, and editable.
    
    Create a new context to create polygonal objects

    ---
    - Args:
        - append (ap): Allows to switch to polyAppendFacetCtx tool
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane.
        - subdivision (s): Number of subdivisions for each edge.Default:1
        - texture (tx): What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized texturesDefault:0
    """
@overload #Overload for polyCreateFacetCtx in ['create']
def polyCreateFacetCtx(ap: bool = ..., ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., mp: int = ..., pc: bool = ..., s: int = ..., tx: int = ...) -> None:
    """polyCreateFacetCtx is undoable, queryable, and editable.
    
    Create a new context to create polygonal objects

    ---
    - Args:
        - append (ap): Allows to switch to polyAppendFacetCtx tool
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane.
        - subdivision (s): Number of subdivisions for each edge.Default:1
        - texture (tx): What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized texturesDefault:0
    """
@overload #Overload for polyCreateFacetCtx in ['create']
def polyCreateFacetCtx(append: bool = ..., ap: bool = ..., exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., maximumNumberOfPoints: int = ..., mp: int = ..., planarConstraint: bool = ..., pc: bool = ..., subdivision: int = ..., s: int = ..., texture: int = ..., tx: int = ...) -> None:
    """polyCreateFacetCtx is undoable, queryable, and editable.
    
    Create a new context to create polygonal objects

    ---
    - Args:
        - append (ap): Allows to switch to polyAppendFacetCtx tool
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane.
        - subdivision (s): Number of subdivisions for each edge.Default:1
        - texture (tx): What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized texturesDefault:0
    """
@overload #Overload for polyCreateFacetCtx in ['query']
def polyCreateFacetCtx(append: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., maximumNumberOfPoints: int = ..., planarConstraint: bool = ..., subdivision: int = ..., texture: int = ..., query: bool = ...) -> None:
    """polyCreateFacetCtx is undoable, queryable, and editable.
    
    Create a new context to create polygonal objects

    ---
    - Args:
        - append (ap): Allows to switch to polyAppendFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane.
        - subdivision (s): Number of subdivisions for each edge.Default:1
        - texture (tx): What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized texturesDefault:0
        - query (q): Query mode flag
    """
@overload #Overload for polyCreateFacetCtx in ['query']
def polyCreateFacetCtx(ap: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., mp: int = ..., pc: bool = ..., s: int = ..., tx: int = ..., q: bool = ...) -> None:
    """polyCreateFacetCtx is undoable, queryable, and editable.
    
    Create a new context to create polygonal objects

    ---
    - Args:
        - append (ap): Allows to switch to polyAppendFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane.
        - subdivision (s): Number of subdivisions for each edge.Default:1
        - texture (tx): What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized texturesDefault:0
        - query (q): Query mode flag
    """
@overload #Overload for polyCreateFacetCtx in ['query']
def polyCreateFacetCtx(append: bool = ..., ap: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., maximumNumberOfPoints: int = ..., mp: int = ..., planarConstraint: bool = ..., pc: bool = ..., subdivision: int = ..., s: int = ..., texture: int = ..., tx: int = ..., query: bool = ..., q: bool = ...) -> None:
    """polyCreateFacetCtx is undoable, queryable, and editable.
    
    Create a new context to create polygonal objects

    ---
    - Args:
        - append (ap): Allows to switch to polyAppendFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane.
        - subdivision (s): Number of subdivisions for each edge.Default:1
        - texture (tx): What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized texturesDefault:0
        - query (q): Query mode flag
    """
@overload #Overload for polyCreateFacetCtx in ['edit']
def polyCreateFacetCtx(append: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., maximumNumberOfPoints: int = ..., planarConstraint: bool = ..., subdivision: int = ..., texture: int = ..., edit: bool = ...) -> None:
    """polyCreateFacetCtx is undoable, queryable, and editable.
    
    Create a new context to create polygonal objects

    ---
    - Args:
        - append (ap): Allows to switch to polyAppendFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane.
        - subdivision (s): Number of subdivisions for each edge.Default:1
        - texture (tx): What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized texturesDefault:0
        - edit (e): Edit mode flag
    """
@overload #Overload for polyCreateFacetCtx in ['edit']
def polyCreateFacetCtx(ap: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., mp: int = ..., pc: bool = ..., s: int = ..., tx: int = ..., e: bool = ...) -> None:
    """polyCreateFacetCtx is undoable, queryable, and editable.
    
    Create a new context to create polygonal objects

    ---
    - Args:
        - append (ap): Allows to switch to polyAppendFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane.
        - subdivision (s): Number of subdivisions for each edge.Default:1
        - texture (tx): What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized texturesDefault:0
        - edit (e): Edit mode flag
    """
@overload #Overload for polyCreateFacetCtx in ['edit']
def polyCreateFacetCtx(append: bool = ..., ap: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., maximumNumberOfPoints: int = ..., mp: int = ..., planarConstraint: bool = ..., pc: bool = ..., subdivision: int = ..., s: int = ..., texture: int = ..., tx: int = ..., edit: bool = ..., e: bool = ...) -> None:
    """polyCreateFacetCtx is undoable, queryable, and editable.
    
    Create a new context to create polygonal objects

    ---
    - Args:
        - append (ap): Allows to switch to polyAppendFacetCtx tool
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - maximumNumberOfPoints (mp): Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        - planarConstraint (pc): allows/avoid new facet to be non-planar.Ifon, all new points will be projected onto current facet plane.
        - subdivision (s): Number of subdivisions for each edge.Default:1
        - texture (tx): What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized texturesDefault:0
        - edit (e): Edit mode flag
    """
