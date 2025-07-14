"""Stub files for Contexts category in Maya commands, command: latticeDeformKeyCtx."""

from typing import Any, overload

@overload #Overload for latticeDeformKeyCtx in ['create']
def latticeDeformKeyCtx(contextName: contextName, envelope: float = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., latticeColumns: int = ..., latticeRows: int = ..., name: str = ..., scaleLatticePts: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - name (n): If this is a tool command, name the tool appropriately.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
    """
@overload #Overload for latticeDeformKeyCtx in ['create']
def latticeDeformKeyCtx(contextName: contextName, ev: float = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., lc: int = ..., lr: int = ..., n: str = ..., slp: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - name (n): If this is a tool command, name the tool appropriately.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
    """
@overload #Overload for latticeDeformKeyCtx in ['create']
def latticeDeformKeyCtx(contextName: contextName, envelope: float = ..., ev: float = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., latticeColumns: int = ..., lc: int = ..., latticeRows: int = ..., lr: int = ..., name: str = ..., n: str = ..., scaleLatticePts: bool = ..., slp: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - name (n): If this is a tool command, name the tool appropriately.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
    """
@overload #Overload for latticeDeformKeyCtx in ['query']
def latticeDeformKeyCtx(contextName: contextName, envelope: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., latticeColumns: int = ..., latticeRows: int = ..., scaleLatticePts: bool = ..., query: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - query (q): Query mode flag
    """
@overload #Overload for latticeDeformKeyCtx in ['query']
def latticeDeformKeyCtx(contextName: contextName, ev: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., lc: int = ..., lr: int = ..., slp: bool = ..., q: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - query (q): Query mode flag
    """
@overload #Overload for latticeDeformKeyCtx in ['query']
def latticeDeformKeyCtx(contextName: contextName, envelope: float = ..., ev: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., latticeColumns: int = ..., lc: int = ..., latticeRows: int = ..., lr: int = ..., scaleLatticePts: bool = ..., slp: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - query (q): Query mode flag
    """
@overload #Overload for latticeDeformKeyCtx in ['edit']
def latticeDeformKeyCtx(contextName: contextName, envelope: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., latticeColumns: int = ..., latticeRows: int = ..., scaleLatticePts: bool = ..., edit: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - edit (e): Edit mode flag
    """
@overload #Overload for latticeDeformKeyCtx in ['edit']
def latticeDeformKeyCtx(contextName: contextName, ev: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., lc: int = ..., lr: int = ..., slp: bool = ..., e: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - edit (e): Edit mode flag
    """
@overload #Overload for latticeDeformKeyCtx in ['edit']
def latticeDeformKeyCtx(contextName: contextName, envelope: float = ..., ev: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., latticeColumns: int = ..., lc: int = ..., latticeRows: int = ..., lr: int = ..., scaleLatticePts: bool = ..., slp: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """latticeDeformKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to deform key frames with
    lattice manipulator. This context only works in the graph editor.

    ---
    - Args:
        - contextName: Input item(s).
        - envelope (ev): Specifies the influence of the lattice.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - latticeColumns (lc): Specifies the number column points the lattice contains.
        - latticeRows (lr): Specifies the number of rows the lattice contains.
        - scaleLatticePts (slp): Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
        - edit (e): Edit mode flag
    """
