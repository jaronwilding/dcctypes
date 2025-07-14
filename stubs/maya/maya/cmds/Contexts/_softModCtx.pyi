"""Stub files for Contexts category in Maya commands, command: softModCtx."""

from typing import Any, overload

@overload #Overload for softModCtx in ['create']
def softModCtx(string: str, exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., reset: bool = ...) -> str:
    """softModCtx is undoable, queryable, and editable.
    
    Controls the softMod context.

    ---
    - Args:
        - string: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (rst): Reset the tool options to their default values.
    """
@overload #Overload for softModCtx in ['create']
def softModCtx(string: str, ex: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., rst: bool = ...) -> str:
    """softModCtx is undoable, queryable, and editable.
    
    Controls the softMod context.

    ---
    - Args:
        - string: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (rst): Reset the tool options to their default values.
    """
@overload #Overload for softModCtx in ['create']
def softModCtx(string: str, exists: bool = ..., ex: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., reset: bool = ..., rst: bool = ...) -> str:
    """softModCtx is undoable, queryable, and editable.
    
    Controls the softMod context.

    ---
    - Args:
        - string: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (rst): Reset the tool options to their default values.
    """
@overload #Overload for softModCtx in ['query']
def softModCtx(string: str, image1: str = ..., image2: str = ..., image3: str = ..., reset: bool = ..., query: bool = ...) -> str:
    """softModCtx is undoable, queryable, and editable.
    
    Controls the softMod context.

    ---
    - Args:
        - string: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (rst): Reset the tool options to their default values.
        - query (q): Query mode flag
    """
@overload #Overload for softModCtx in ['query']
def softModCtx(string: str, i1: str = ..., i2: str = ..., i3: str = ..., rst: bool = ..., q: bool = ...) -> str:
    """softModCtx is undoable, queryable, and editable.
    
    Controls the softMod context.

    ---
    - Args:
        - string: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (rst): Reset the tool options to their default values.
        - query (q): Query mode flag
    """
@overload #Overload for softModCtx in ['query']
def softModCtx(string: str, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., reset: bool = ..., rst: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """softModCtx is undoable, queryable, and editable.
    
    Controls the softMod context.

    ---
    - Args:
        - string: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (rst): Reset the tool options to their default values.
        - query (q): Query mode flag
    """
@overload #Overload for softModCtx in ['edit']
def softModCtx(string: str, dragSlider: str = ..., falseColor: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., reset: bool = ..., edit: bool = ...) -> str:
    """softModCtx is undoable, queryable, and editable.
    
    Controls the softMod context.

    ---
    - Args:
        - string: Input item(s).
        - dragSlider (ds): Specify the slider mode for hotkey radius resizing.
        - falseColor (fc): Enable or disable false color display on the soft mod manipulator.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (rst): Reset the tool options to their default values.
        - edit (e): Edit mode flag
    """
@overload #Overload for softModCtx in ['edit']
def softModCtx(string: str, ds: str = ..., fc: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., rst: bool = ..., e: bool = ...) -> str:
    """softModCtx is undoable, queryable, and editable.
    
    Controls the softMod context.

    ---
    - Args:
        - string: Input item(s).
        - dragSlider (ds): Specify the slider mode for hotkey radius resizing.
        - falseColor (fc): Enable or disable false color display on the soft mod manipulator.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (rst): Reset the tool options to their default values.
        - edit (e): Edit mode flag
    """
@overload #Overload for softModCtx in ['edit']
def softModCtx(string: str, dragSlider: str = ..., ds: str = ..., falseColor: bool = ..., fc: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., reset: bool = ..., rst: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """softModCtx is undoable, queryable, and editable.
    
    Controls the softMod context.

    ---
    - Args:
        - string: Input item(s).
        - dragSlider (ds): Specify the slider mode for hotkey radius resizing.
        - falseColor (fc): Enable or disable false color display on the soft mod manipulator.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (rst): Reset the tool options to their default values.
        - edit (e): Edit mode flag
    """
