"""Stub files for Contexts category in Maya commands, command: skinBindCtx."""

from typing import Any, overload

@overload #Overload for skinBindCtx in ['create']
def skinBindCtx(string: str, about: str = ..., axis: str = ..., colorRamp: str = ..., currentInfluence: str = ..., displayInactiveMode: int = ..., displayNormalized: bool = ..., exists: bool = ..., falloffCurve: str = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., symmetry: bool = ..., tolerance: float = ...) -> str:
    """skinBindCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to edit volumes from an
    interactive bind.

    ---
    - Args:
        - string: Input item(s).
        - about (a): The space in which the axis should be mirrored. Valid values are: "world" and "object".
        - axis (ax): The mirror axis. Valid values are: "x","y", and "z".
        - colorRamp (cr): Set the values on the color ramp used to display the weight values.
        - currentInfluence (ci): Set the index of the current influence or volume to be adjusted by the manipulator.
        - displayInactiveMode (di): Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes
        - displayNormalized (dn): Display raw select weights (false) or finalized normalized weights (true).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - falloffCurve (fc): Set the values on the falloff curve control.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - symmetry (s): Controls whether or not the tool operates in symmetric (mirrored) mode.
        - tolerance (t): The tolerance setting for determining whether another influence is symmetric to the the current influence.
    """
@overload #Overload for skinBindCtx in ['create']
def skinBindCtx(string: str, a: str = ..., ax: str = ..., cr: str = ..., ci: str = ..., di: int = ..., dn: bool = ..., ex: bool = ..., fc: str = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., s: bool = ..., t: float = ...) -> str:
    """skinBindCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to edit volumes from an
    interactive bind.

    ---
    - Args:
        - string: Input item(s).
        - about (a): The space in which the axis should be mirrored. Valid values are: "world" and "object".
        - axis (ax): The mirror axis. Valid values are: "x","y", and "z".
        - colorRamp (cr): Set the values on the color ramp used to display the weight values.
        - currentInfluence (ci): Set the index of the current influence or volume to be adjusted by the manipulator.
        - displayInactiveMode (di): Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes
        - displayNormalized (dn): Display raw select weights (false) or finalized normalized weights (true).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - falloffCurve (fc): Set the values on the falloff curve control.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - symmetry (s): Controls whether or not the tool operates in symmetric (mirrored) mode.
        - tolerance (t): The tolerance setting for determining whether another influence is symmetric to the the current influence.
    """
@overload #Overload for skinBindCtx in ['create']
def skinBindCtx(string: str, about: str = ..., a: str = ..., axis: str = ..., ax: str = ..., colorRamp: str = ..., cr: str = ..., currentInfluence: str = ..., ci: str = ..., displayInactiveMode: int = ..., di: int = ..., displayNormalized: bool = ..., dn: bool = ..., exists: bool = ..., ex: bool = ..., falloffCurve: str = ..., fc: str = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., symmetry: bool = ..., s: bool = ..., tolerance: float = ..., t: float = ...) -> str:
    """skinBindCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to edit volumes from an
    interactive bind.

    ---
    - Args:
        - string: Input item(s).
        - about (a): The space in which the axis should be mirrored. Valid values are: "world" and "object".
        - axis (ax): The mirror axis. Valid values are: "x","y", and "z".
        - colorRamp (cr): Set the values on the color ramp used to display the weight values.
        - currentInfluence (ci): Set the index of the current influence or volume to be adjusted by the manipulator.
        - displayInactiveMode (di): Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes
        - displayNormalized (dn): Display raw select weights (false) or finalized normalized weights (true).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - falloffCurve (fc): Set the values on the falloff curve control.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - symmetry (s): Controls whether or not the tool operates in symmetric (mirrored) mode.
        - tolerance (t): The tolerance setting for determining whether another influence is symmetric to the the current influence.
    """
@overload #Overload for skinBindCtx in ['query']
def skinBindCtx(string: str, about: str = ..., axis: str = ..., colorRamp: str = ..., currentInfluence: str = ..., displayInactiveMode: int = ..., displayNormalized: bool = ..., falloffCurve: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., symmetry: bool = ..., tolerance: float = ..., query: bool = ...) -> str:
    """skinBindCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to edit volumes from an
    interactive bind.

    ---
    - Args:
        - string: Input item(s).
        - about (a): The space in which the axis should be mirrored. Valid values are: "world" and "object".
        - axis (ax): The mirror axis. Valid values are: "x","y", and "z".
        - colorRamp (cr): Set the values on the color ramp used to display the weight values.
        - currentInfluence (ci): Set the index of the current influence or volume to be adjusted by the manipulator.
        - displayInactiveMode (di): Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes
        - displayNormalized (dn): Display raw select weights (false) or finalized normalized weights (true).
        - falloffCurve (fc): Set the values on the falloff curve control.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - symmetry (s): Controls whether or not the tool operates in symmetric (mirrored) mode.
        - tolerance (t): The tolerance setting for determining whether another influence is symmetric to the the current influence.
        - query (q): Query mode flag
    """
@overload #Overload for skinBindCtx in ['query']
def skinBindCtx(string: str, a: str = ..., ax: str = ..., cr: str = ..., ci: str = ..., di: int = ..., dn: bool = ..., fc: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., s: bool = ..., t: float = ..., q: bool = ...) -> str:
    """skinBindCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to edit volumes from an
    interactive bind.

    ---
    - Args:
        - string: Input item(s).
        - about (a): The space in which the axis should be mirrored. Valid values are: "world" and "object".
        - axis (ax): The mirror axis. Valid values are: "x","y", and "z".
        - colorRamp (cr): Set the values on the color ramp used to display the weight values.
        - currentInfluence (ci): Set the index of the current influence or volume to be adjusted by the manipulator.
        - displayInactiveMode (di): Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes
        - displayNormalized (dn): Display raw select weights (false) or finalized normalized weights (true).
        - falloffCurve (fc): Set the values on the falloff curve control.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - symmetry (s): Controls whether or not the tool operates in symmetric (mirrored) mode.
        - tolerance (t): The tolerance setting for determining whether another influence is symmetric to the the current influence.
        - query (q): Query mode flag
    """
@overload #Overload for skinBindCtx in ['query']
def skinBindCtx(string: str, about: str = ..., a: str = ..., axis: str = ..., ax: str = ..., colorRamp: str = ..., cr: str = ..., currentInfluence: str = ..., ci: str = ..., displayInactiveMode: int = ..., di: int = ..., displayNormalized: bool = ..., dn: bool = ..., falloffCurve: str = ..., fc: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., symmetry: bool = ..., s: bool = ..., tolerance: float = ..., t: float = ..., query: bool = ..., q: bool = ...) -> str:
    """skinBindCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to edit volumes from an
    interactive bind.

    ---
    - Args:
        - string: Input item(s).
        - about (a): The space in which the axis should be mirrored. Valid values are: "world" and "object".
        - axis (ax): The mirror axis. Valid values are: "x","y", and "z".
        - colorRamp (cr): Set the values on the color ramp used to display the weight values.
        - currentInfluence (ci): Set the index of the current influence or volume to be adjusted by the manipulator.
        - displayInactiveMode (di): Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes
        - displayNormalized (dn): Display raw select weights (false) or finalized normalized weights (true).
        - falloffCurve (fc): Set the values on the falloff curve control.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - symmetry (s): Controls whether or not the tool operates in symmetric (mirrored) mode.
        - tolerance (t): The tolerance setting for determining whether another influence is symmetric to the the current influence.
        - query (q): Query mode flag
    """
@overload #Overload for skinBindCtx in ['edit']
def skinBindCtx(string: str, about: str = ..., axis: str = ..., colorRamp: str = ..., currentInfluence: str = ..., displayInactiveMode: int = ..., displayNormalized: bool = ..., falloffCurve: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., symmetry: bool = ..., tolerance: float = ..., edit: bool = ...) -> str:
    """skinBindCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to edit volumes from an
    interactive bind.

    ---
    - Args:
        - string: Input item(s).
        - about (a): The space in which the axis should be mirrored. Valid values are: "world" and "object".
        - axis (ax): The mirror axis. Valid values are: "x","y", and "z".
        - colorRamp (cr): Set the values on the color ramp used to display the weight values.
        - currentInfluence (ci): Set the index of the current influence or volume to be adjusted by the manipulator.
        - displayInactiveMode (di): Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes
        - displayNormalized (dn): Display raw select weights (false) or finalized normalized weights (true).
        - falloffCurve (fc): Set the values on the falloff curve control.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - symmetry (s): Controls whether or not the tool operates in symmetric (mirrored) mode.
        - tolerance (t): The tolerance setting for determining whether another influence is symmetric to the the current influence.
        - edit (e): Edit mode flag
    """
@overload #Overload for skinBindCtx in ['edit']
def skinBindCtx(string: str, a: str = ..., ax: str = ..., cr: str = ..., ci: str = ..., di: int = ..., dn: bool = ..., fc: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., s: bool = ..., t: float = ..., e: bool = ...) -> str:
    """skinBindCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to edit volumes from an
    interactive bind.

    ---
    - Args:
        - string: Input item(s).
        - about (a): The space in which the axis should be mirrored. Valid values are: "world" and "object".
        - axis (ax): The mirror axis. Valid values are: "x","y", and "z".
        - colorRamp (cr): Set the values on the color ramp used to display the weight values.
        - currentInfluence (ci): Set the index of the current influence or volume to be adjusted by the manipulator.
        - displayInactiveMode (di): Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes
        - displayNormalized (dn): Display raw select weights (false) or finalized normalized weights (true).
        - falloffCurve (fc): Set the values on the falloff curve control.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - symmetry (s): Controls whether or not the tool operates in symmetric (mirrored) mode.
        - tolerance (t): The tolerance setting for determining whether another influence is symmetric to the the current influence.
        - edit (e): Edit mode flag
    """
@overload #Overload for skinBindCtx in ['edit']
def skinBindCtx(string: str, about: str = ..., a: str = ..., axis: str = ..., ax: str = ..., colorRamp: str = ..., cr: str = ..., currentInfluence: str = ..., ci: str = ..., displayInactiveMode: int = ..., di: int = ..., displayNormalized: bool = ..., dn: bool = ..., falloffCurve: str = ..., fc: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., symmetry: bool = ..., s: bool = ..., tolerance: float = ..., t: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """skinBindCtx is undoable, queryable, and editable.
    
    This command creates a tool that can be used to edit volumes from an
    interactive bind.

    ---
    - Args:
        - string: Input item(s).
        - about (a): The space in which the axis should be mirrored. Valid values are: "world" and "object".
        - axis (ax): The mirror axis. Valid values are: "x","y", and "z".
        - colorRamp (cr): Set the values on the color ramp used to display the weight values.
        - currentInfluence (ci): Set the index of the current influence or volume to be adjusted by the manipulator.
        - displayInactiveMode (di): Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes
        - displayNormalized (dn): Display raw select weights (false) or finalized normalized weights (true).
        - falloffCurve (fc): Set the values on the falloff curve control.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - symmetry (s): Controls whether or not the tool operates in symmetric (mirrored) mode.
        - tolerance (t): The tolerance setting for determining whether another influence is symmetric to the the current influence.
        - edit (e): Edit mode flag
    """
