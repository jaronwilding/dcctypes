"""Stub files for Contexts category in Maya commands, command: retimeKeyCtx."""

from typing import Any, overload

@overload #Overload for retimeKeyCtx in ['create']
def retimeKeyCtx(contextName: contextName, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., snapOnFrame: bool = ...) -> bool:
    """retimeKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the retime tool.

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - snapOnFrame (sof): When set, the retime markers will snap on frames as they are moved.
    """
@overload #Overload for retimeKeyCtx in ['create']
def retimeKeyCtx(contextName: contextName, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., sof: bool = ...) -> bool:
    """retimeKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the retime tool.

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - snapOnFrame (sof): When set, the retime markers will snap on frames as they are moved.
    """
@overload #Overload for retimeKeyCtx in ['create']
def retimeKeyCtx(contextName: contextName, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., snapOnFrame: bool = ..., sof: bool = ...) -> bool:
    """retimeKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the retime tool.

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - snapOnFrame (sof): When set, the retime markers will snap on frames as they are moved.
    """
@overload #Overload for retimeKeyCtx in ['query']
def retimeKeyCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., snapOnFrame: bool = ..., query: bool = ...) -> bool:
    """retimeKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the retime tool.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - snapOnFrame (sof): When set, the retime markers will snap on frames as they are moved.
        - query (q): Query mode flag
    """
@overload #Overload for retimeKeyCtx in ['query']
def retimeKeyCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., sof: bool = ..., q: bool = ...) -> bool:
    """retimeKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the retime tool.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - snapOnFrame (sof): When set, the retime markers will snap on frames as they are moved.
        - query (q): Query mode flag
    """
@overload #Overload for retimeKeyCtx in ['query']
def retimeKeyCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., snapOnFrame: bool = ..., sof: bool = ..., query: bool = ..., q: bool = ...) -> bool:
    """retimeKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the retime tool.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - snapOnFrame (sof): When set, the retime markers will snap on frames as they are moved.
        - query (q): Query mode flag
    """
@overload #Overload for retimeKeyCtx in ['edit']
def retimeKeyCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., moveByFrame: int = ..., snapOnFrame: bool = ..., edit: bool = ...) -> bool:
    """retimeKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the retime tool.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - moveByFrame (mbf): Move the selected retime bar by the specified number of frames
        - snapOnFrame (sof): When set, the retime markers will snap on frames as they are moved.
        - edit (e): Edit mode flag
    """
@overload #Overload for retimeKeyCtx in ['edit']
def retimeKeyCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., mbf: int = ..., sof: bool = ..., e: bool = ...) -> bool:
    """retimeKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the retime tool.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - moveByFrame (mbf): Move the selected retime bar by the specified number of frames
        - snapOnFrame (sof): When set, the retime markers will snap on frames as they are moved.
        - edit (e): Edit mode flag
    """
@overload #Overload for retimeKeyCtx in ['edit']
def retimeKeyCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., moveByFrame: int = ..., mbf: int = ..., snapOnFrame: bool = ..., sof: bool = ..., edit: bool = ..., e: bool = ...) -> bool:
    """retimeKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor using the retime tool.

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - moveByFrame (mbf): Move the selected retime bar by the specified number of frames
        - snapOnFrame (sof): When set, the retime markers will snap on frames as they are moved.
        - edit (e): Edit mode flag
    """
