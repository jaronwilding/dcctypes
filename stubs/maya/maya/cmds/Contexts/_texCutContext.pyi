"""Stub files for Contexts category in Maya commands, command: texCutContext."""

from typing import Any, overload

@overload #Overload for texCutContext in ['create']
def texCutContext(contextName: contextName, displayShellBorders: bool = ..., edgeSelectSensitive: float = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., mode: str = ..., moveRatio: float = ..., name: str = ..., size: float = ..., steadyStroke: bool = ..., steadyStrokeDistance: float = ..., touchToSew: bool = ...) -> float | float | bool | float | float | str | bool | bool:
    """texCutContext is undoable, queryable, and editable.
    
    This command creates a context for cut uv tool. This context only works in the
    UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - displayShellBorders (dsb): Toggle the display of shell borders.
        - edgeSelectSensitive (ess): Set the value of the edge selection sensitivity.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Specifies the type of effect the brush will perform, Cut or Sew.
        - moveRatio (mvr): The cut open ratio relative to edge length.
        - name (n): If this is a tool command, name the tool appropriately.
        - size (sz): Brush size value of the brush ring.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - touchToSew (tts): Toggle the touch to sew mode.
    """
@overload #Overload for texCutContext in ['create']
def texCutContext(contextName: contextName, dsb: bool = ..., ess: float = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., m: str = ..., mvr: float = ..., n: str = ..., sz: float = ..., ss: bool = ..., ssd: float = ..., tts: bool = ...) -> float | float | bool | float | float | str | bool | bool:
    """texCutContext is undoable, queryable, and editable.
    
    This command creates a context for cut uv tool. This context only works in the
    UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - displayShellBorders (dsb): Toggle the display of shell borders.
        - edgeSelectSensitive (ess): Set the value of the edge selection sensitivity.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Specifies the type of effect the brush will perform, Cut or Sew.
        - moveRatio (mvr): The cut open ratio relative to edge length.
        - name (n): If this is a tool command, name the tool appropriately.
        - size (sz): Brush size value of the brush ring.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - touchToSew (tts): Toggle the touch to sew mode.
    """
@overload #Overload for texCutContext in ['create']
def texCutContext(contextName: contextName, displayShellBorders: bool = ..., dsb: bool = ..., edgeSelectSensitive: float = ..., ess: float = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mode: str = ..., m: str = ..., moveRatio: float = ..., mvr: float = ..., name: str = ..., n: str = ..., size: float = ..., sz: float = ..., steadyStroke: bool = ..., ss: bool = ..., steadyStrokeDistance: float = ..., ssd: float = ..., touchToSew: bool = ..., tts: bool = ...) -> float | float | bool | float | float | str | bool | bool:
    """texCutContext is undoable, queryable, and editable.
    
    This command creates a context for cut uv tool. This context only works in the
    UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - displayShellBorders (dsb): Toggle the display of shell borders.
        - edgeSelectSensitive (ess): Set the value of the edge selection sensitivity.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Specifies the type of effect the brush will perform, Cut or Sew.
        - moveRatio (mvr): The cut open ratio relative to edge length.
        - name (n): If this is a tool command, name the tool appropriately.
        - size (sz): Brush size value of the brush ring.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - touchToSew (tts): Toggle the touch to sew mode.
    """
@overload #Overload for texCutContext in ['query']
def texCutContext(contextName: contextName, displayShellBorders: bool = ..., edgeSelectSensitive: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., mode: str = ..., moveRatio: float = ..., size: float = ..., steadyStroke: bool = ..., steadyStrokeDistance: float = ..., touchToSew: bool = ..., query: bool = ...) -> float | float | bool | float | float | str | bool | bool:
    """texCutContext is undoable, queryable, and editable.
    
    This command creates a context for cut uv tool. This context only works in the
    UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - displayShellBorders (dsb): Toggle the display of shell borders.
        - edgeSelectSensitive (ess): Set the value of the edge selection sensitivity.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Specifies the type of effect the brush will perform, Cut or Sew.
        - moveRatio (mvr): The cut open ratio relative to edge length.
        - size (sz): Brush size value of the brush ring.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - touchToSew (tts): Toggle the touch to sew mode.
        - query (q): Query mode flag
    """
@overload #Overload for texCutContext in ['query']
def texCutContext(contextName: contextName, dsb: bool = ..., ess: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., m: str = ..., mvr: float = ..., sz: float = ..., ss: bool = ..., ssd: float = ..., tts: bool = ..., q: bool = ...) -> float | float | bool | float | float | str | bool | bool:
    """texCutContext is undoable, queryable, and editable.
    
    This command creates a context for cut uv tool. This context only works in the
    UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - displayShellBorders (dsb): Toggle the display of shell borders.
        - edgeSelectSensitive (ess): Set the value of the edge selection sensitivity.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Specifies the type of effect the brush will perform, Cut or Sew.
        - moveRatio (mvr): The cut open ratio relative to edge length.
        - size (sz): Brush size value of the brush ring.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - touchToSew (tts): Toggle the touch to sew mode.
        - query (q): Query mode flag
    """
@overload #Overload for texCutContext in ['query']
def texCutContext(contextName: contextName, displayShellBorders: bool = ..., dsb: bool = ..., edgeSelectSensitive: float = ..., ess: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mode: str = ..., m: str = ..., moveRatio: float = ..., mvr: float = ..., size: float = ..., sz: float = ..., steadyStroke: bool = ..., ss: bool = ..., steadyStrokeDistance: float = ..., ssd: float = ..., touchToSew: bool = ..., tts: bool = ..., query: bool = ..., q: bool = ...) -> float | float | bool | float | float | str | bool | bool:
    """texCutContext is undoable, queryable, and editable.
    
    This command creates a context for cut uv tool. This context only works in the
    UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - displayShellBorders (dsb): Toggle the display of shell borders.
        - edgeSelectSensitive (ess): Set the value of the edge selection sensitivity.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Specifies the type of effect the brush will perform, Cut or Sew.
        - moveRatio (mvr): The cut open ratio relative to edge length.
        - size (sz): Brush size value of the brush ring.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - touchToSew (tts): Toggle the touch to sew mode.
        - query (q): Query mode flag
    """
@overload #Overload for texCutContext in ['edit']
def texCutContext(contextName: contextName, adjustSize: bool = ..., displayShellBorders: bool = ..., edgeSelectSensitive: float = ..., image1: str = ..., image2: str = ..., image3: str = ..., mode: str = ..., moveRatio: float = ..., size: float = ..., steadyStroke: bool = ..., steadyStrokeDistance: float = ..., touchToSew: bool = ..., edit: bool = ...) -> float | float | bool | float | float | str | bool | bool:
    """texCutContext is undoable, queryable, and editable.
    
    This command creates a context for cut uv tool. This context only works in the
    UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - adjustSize (asz): If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous mode.
        - displayShellBorders (dsb): Toggle the display of shell borders.
        - edgeSelectSensitive (ess): Set the value of the edge selection sensitivity.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Specifies the type of effect the brush will perform, Cut or Sew.
        - moveRatio (mvr): The cut open ratio relative to edge length.
        - size (sz): Brush size value of the brush ring.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - touchToSew (tts): Toggle the touch to sew mode.
        - edit (e): Edit mode flag
    """
@overload #Overload for texCutContext in ['edit']
def texCutContext(contextName: contextName, asz: bool = ..., dsb: bool = ..., ess: float = ..., i1: str = ..., i2: str = ..., i3: str = ..., m: str = ..., mvr: float = ..., sz: float = ..., ss: bool = ..., ssd: float = ..., tts: bool = ..., e: bool = ...) -> float | float | bool | float | float | str | bool | bool:
    """texCutContext is undoable, queryable, and editable.
    
    This command creates a context for cut uv tool. This context only works in the
    UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - adjustSize (asz): If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous mode.
        - displayShellBorders (dsb): Toggle the display of shell borders.
        - edgeSelectSensitive (ess): Set the value of the edge selection sensitivity.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Specifies the type of effect the brush will perform, Cut or Sew.
        - moveRatio (mvr): The cut open ratio relative to edge length.
        - size (sz): Brush size value of the brush ring.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - touchToSew (tts): Toggle the touch to sew mode.
        - edit (e): Edit mode flag
    """
@overload #Overload for texCutContext in ['edit']
def texCutContext(contextName: contextName, adjustSize: bool = ..., asz: bool = ..., displayShellBorders: bool = ..., dsb: bool = ..., edgeSelectSensitive: float = ..., ess: float = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., mode: str = ..., m: str = ..., moveRatio: float = ..., mvr: float = ..., size: float = ..., sz: float = ..., steadyStroke: bool = ..., ss: bool = ..., steadyStrokeDistance: float = ..., ssd: float = ..., touchToSew: bool = ..., tts: bool = ..., edit: bool = ..., e: bool = ...) -> float | float | bool | float | float | str | bool | bool:
    """texCutContext is undoable, queryable, and editable.
    
    This command creates a context for cut uv tool. This context only works in the
    UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - adjustSize (asz): If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous mode.
        - displayShellBorders (dsb): Toggle the display of shell borders.
        - edgeSelectSensitive (ess): Set the value of the edge selection sensitivity.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - mode (m): Specifies the type of effect the brush will perform, Cut or Sew.
        - moveRatio (mvr): The cut open ratio relative to edge length.
        - size (sz): Brush size value of the brush ring.
        - steadyStroke (ss): Turn on steady stroke or not.
        - steadyStrokeDistance (ssd): The distance for steady stroke.
        - touchToSew (tts): Toggle the touch to sew mode.
        - edit (e): Edit mode flag
    """
