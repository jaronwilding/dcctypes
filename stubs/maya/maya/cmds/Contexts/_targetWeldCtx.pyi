"""Stub files for Contexts category in Maya commands, command: targetWeldCtx."""

from typing import Any, overload

@overload #Overload for targetWeldCtx in ['create']
def targetWeldCtx(exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., mergeToCenter: bool = ..., preserveUV: bool = ...) -> None:
    """targetWeldCtx is undoable, queryable, and editable.
    
    Create a new context to weld vertices together on a poly object.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeToCenter (mtc): If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge.  If set to false the source vertex will be moved to the target vertex before doing the merge.
        - preserveUV (puv): When false, UVs are not changed when welding components. When true, the UVs are modified to stop texture swimming when welding components. Default is true.
    """
@overload #Overload for targetWeldCtx in ['create']
def targetWeldCtx(ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., mtc: bool = ..., puv: bool = ...) -> None:
    """targetWeldCtx is undoable, queryable, and editable.
    
    Create a new context to weld vertices together on a poly object.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeToCenter (mtc): If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge.  If set to false the source vertex will be moved to the target vertex before doing the merge.
        - preserveUV (puv): When false, UVs are not changed when welding components. When true, the UVs are modified to stop texture swimming when welding components. Default is true.
    """
@overload #Overload for targetWeldCtx in ['create']
def targetWeldCtx(exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mergeToCenter: bool = ..., mtc: bool = ..., preserveUV: bool = ..., puv: bool = ...) -> None:
    """targetWeldCtx is undoable, queryable, and editable.
    
    Create a new context to weld vertices together on a poly object.

    ---
    - Args:
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeToCenter (mtc): If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge.  If set to false the source vertex will be moved to the target vertex before doing the merge.
        - preserveUV (puv): When false, UVs are not changed when welding components. When true, the UVs are modified to stop texture swimming when welding components. Default is true.
    """
@overload #Overload for targetWeldCtx in ['query']
def targetWeldCtx(image1: str = ..., image2: str = ..., image3: str = ..., mergeToCenter: bool = ..., preserveUV: bool = ..., query: bool = ...) -> None:
    """targetWeldCtx is undoable, queryable, and editable.
    
    Create a new context to weld vertices together on a poly object.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeToCenter (mtc): If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge.  If set to false the source vertex will be moved to the target vertex before doing the merge.
        - preserveUV (puv): When false, UVs are not changed when welding components. When true, the UVs are modified to stop texture swimming when welding components. Default is true.
        - query (q): Query mode flag
    """
@overload #Overload for targetWeldCtx in ['query']
def targetWeldCtx(i1: str = ..., i2: str = ..., i3: str = ..., mtc: bool = ..., puv: bool = ..., q: bool = ...) -> None:
    """targetWeldCtx is undoable, queryable, and editable.
    
    Create a new context to weld vertices together on a poly object.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeToCenter (mtc): If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge.  If set to false the source vertex will be moved to the target vertex before doing the merge.
        - preserveUV (puv): When false, UVs are not changed when welding components. When true, the UVs are modified to stop texture swimming when welding components. Default is true.
        - query (q): Query mode flag
    """
@overload #Overload for targetWeldCtx in ['query']
def targetWeldCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mergeToCenter: bool = ..., mtc: bool = ..., preserveUV: bool = ..., puv: bool = ..., query: bool = ..., q: bool = ...) -> None:
    """targetWeldCtx is undoable, queryable, and editable.
    
    Create a new context to weld vertices together on a poly object.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeToCenter (mtc): If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge.  If set to false the source vertex will be moved to the target vertex before doing the merge.
        - preserveUV (puv): When false, UVs are not changed when welding components. When true, the UVs are modified to stop texture swimming when welding components. Default is true.
        - query (q): Query mode flag
    """
@overload #Overload for targetWeldCtx in ['edit']
def targetWeldCtx(image1: str = ..., image2: str = ..., image3: str = ..., mergeToCenter: bool = ..., preserveUV: bool = ..., edit: bool = ...) -> None:
    """targetWeldCtx is undoable, queryable, and editable.
    
    Create a new context to weld vertices together on a poly object.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeToCenter (mtc): If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge.  If set to false the source vertex will be moved to the target vertex before doing the merge.
        - preserveUV (puv): When false, UVs are not changed when welding components. When true, the UVs are modified to stop texture swimming when welding components. Default is true.
        - edit (e): Edit mode flag
    """
@overload #Overload for targetWeldCtx in ['edit']
def targetWeldCtx(i1: str = ..., i2: str = ..., i3: str = ..., mtc: bool = ..., puv: bool = ..., e: bool = ...) -> None:
    """targetWeldCtx is undoable, queryable, and editable.
    
    Create a new context to weld vertices together on a poly object.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeToCenter (mtc): If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge.  If set to false the source vertex will be moved to the target vertex before doing the merge.
        - preserveUV (puv): When false, UVs are not changed when welding components. When true, the UVs are modified to stop texture swimming when welding components. Default is true.
        - edit (e): Edit mode flag
    """
@overload #Overload for targetWeldCtx in ['edit']
def targetWeldCtx(image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mergeToCenter: bool = ..., mtc: bool = ..., preserveUV: bool = ..., puv: bool = ..., edit: bool = ..., e: bool = ...) -> None:
    """targetWeldCtx is undoable, queryable, and editable.
    
    Create a new context to weld vertices together on a poly object.

    ---
    - Args:
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mergeToCenter (mtc): If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge.  If set to false the source vertex will be moved to the target vertex before doing the merge.
        - preserveUV (puv): When false, UVs are not changed when welding components. When true, the UVs are modified to stop texture swimming when welding components. Default is true.
        - edit (e): Edit mode flag
    """
