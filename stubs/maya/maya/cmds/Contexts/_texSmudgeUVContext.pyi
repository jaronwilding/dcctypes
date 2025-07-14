"""Stub files for Contexts category in Maya commands, command: texSmudgeUVContext."""

from typing import Any, overload

@overload #Overload for texSmudgeUVContext in ['create']
def texSmudgeUVContext(contextName: contextName, dragSlider: str = ..., effectType: str = ..., exists: bool = ..., functionType: str = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., pressure: float = ..., radius: float = ..., smudgeIsMiddle: bool = ...) -> str:
    """texSmudgeUVContext is undoable, queryable, and editable.
    
    This command creates a context for smudge UV tool. This context only works in
    the texture UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - dragSlider (ds): radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
        - effectType (et): fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - functionType (ft): exponential | linear | constant. Specifies how UVs fall off from the center of influence.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - pressure (prs): Pressure value when effect type is set to smudge.
        - radius (r): Radius of the smudge tool. All UVs within this radius are affected by the tool
        - smudgeIsMiddle (sim): By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.
    """
@overload #Overload for texSmudgeUVContext in ['create']
def texSmudgeUVContext(contextName: contextName, ds: str = ..., et: str = ..., ex: bool = ..., ft: str = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., prs: float = ..., r: float = ..., sim: bool = ...) -> str:
    """texSmudgeUVContext is undoable, queryable, and editable.
    
    This command creates a context for smudge UV tool. This context only works in
    the texture UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - dragSlider (ds): radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
        - effectType (et): fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - functionType (ft): exponential | linear | constant. Specifies how UVs fall off from the center of influence.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - pressure (prs): Pressure value when effect type is set to smudge.
        - radius (r): Radius of the smudge tool. All UVs within this radius are affected by the tool
        - smudgeIsMiddle (sim): By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.
    """
@overload #Overload for texSmudgeUVContext in ['create']
def texSmudgeUVContext(contextName: contextName, dragSlider: str = ..., ds: str = ..., effectType: str = ..., et: str = ..., exists: bool = ..., ex: bool = ..., functionType: str = ..., ft: str = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., pressure: float = ..., prs: float = ..., radius: float = ..., r: float = ..., smudgeIsMiddle: bool = ..., sim: bool = ...) -> str:
    """texSmudgeUVContext is undoable, queryable, and editable.
    
    This command creates a context for smudge UV tool. This context only works in
    the texture UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - dragSlider (ds): radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
        - effectType (et): fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - functionType (ft): exponential | linear | constant. Specifies how UVs fall off from the center of influence.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - pressure (prs): Pressure value when effect type is set to smudge.
        - radius (r): Radius of the smudge tool. All UVs within this radius are affected by the tool
        - smudgeIsMiddle (sim): By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.
    """
@overload #Overload for texSmudgeUVContext in ['query']
def texSmudgeUVContext(contextName: contextName, dragSlider: str = ..., effectType: str = ..., functionType: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., pressure: float = ..., radius: float = ..., smudgeIsMiddle: bool = ..., query: bool = ...) -> str:
    """texSmudgeUVContext is undoable, queryable, and editable.
    
    This command creates a context for smudge UV tool. This context only works in
    the texture UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - dragSlider (ds): radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
        - effectType (et): fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.
        - functionType (ft): exponential | linear | constant. Specifies how UVs fall off from the center of influence.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - pressure (prs): Pressure value when effect type is set to smudge.
        - radius (r): Radius of the smudge tool. All UVs within this radius are affected by the tool
        - smudgeIsMiddle (sim): By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.
        - query (q): Query mode flag
    """
@overload #Overload for texSmudgeUVContext in ['query']
def texSmudgeUVContext(contextName: contextName, ds: str = ..., et: str = ..., ft: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., prs: float = ..., r: float = ..., sim: bool = ..., q: bool = ...) -> str:
    """texSmudgeUVContext is undoable, queryable, and editable.
    
    This command creates a context for smudge UV tool. This context only works in
    the texture UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - dragSlider (ds): radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
        - effectType (et): fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.
        - functionType (ft): exponential | linear | constant. Specifies how UVs fall off from the center of influence.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - pressure (prs): Pressure value when effect type is set to smudge.
        - radius (r): Radius of the smudge tool. All UVs within this radius are affected by the tool
        - smudgeIsMiddle (sim): By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.
        - query (q): Query mode flag
    """
@overload #Overload for texSmudgeUVContext in ['query']
def texSmudgeUVContext(contextName: contextName, dragSlider: str = ..., ds: str = ..., effectType: str = ..., et: str = ..., functionType: str = ..., ft: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., pressure: float = ..., prs: float = ..., radius: float = ..., r: float = ..., smudgeIsMiddle: bool = ..., sim: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """texSmudgeUVContext is undoable, queryable, and editable.
    
    This command creates a context for smudge UV tool. This context only works in
    the texture UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - dragSlider (ds): radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
        - effectType (et): fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.
        - functionType (ft): exponential | linear | constant. Specifies how UVs fall off from the center of influence.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - pressure (prs): Pressure value when effect type is set to smudge.
        - radius (r): Radius of the smudge tool. All UVs within this radius are affected by the tool
        - smudgeIsMiddle (sim): By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.
        - query (q): Query mode flag
    """
@overload #Overload for texSmudgeUVContext in ['edit']
def texSmudgeUVContext(contextName: contextName, dragSlider: str = ..., effectType: str = ..., functionType: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., pressure: float = ..., radius: float = ..., smudgeIsMiddle: bool = ..., edit: bool = ...) -> str:
    """texSmudgeUVContext is undoable, queryable, and editable.
    
    This command creates a context for smudge UV tool. This context only works in
    the texture UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - dragSlider (ds): radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
        - effectType (et): fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.
        - functionType (ft): exponential | linear | constant. Specifies how UVs fall off from the center of influence.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - pressure (prs): Pressure value when effect type is set to smudge.
        - radius (r): Radius of the smudge tool. All UVs within this radius are affected by the tool
        - smudgeIsMiddle (sim): By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.
        - edit (e): Edit mode flag
    """
@overload #Overload for texSmudgeUVContext in ['edit']
def texSmudgeUVContext(contextName: contextName, ds: str = ..., et: str = ..., ft: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., prs: float = ..., r: float = ..., sim: bool = ..., e: bool = ...) -> str:
    """texSmudgeUVContext is undoable, queryable, and editable.
    
    This command creates a context for smudge UV tool. This context only works in
    the texture UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - dragSlider (ds): radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
        - effectType (et): fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.
        - functionType (ft): exponential | linear | constant. Specifies how UVs fall off from the center of influence.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - pressure (prs): Pressure value when effect type is set to smudge.
        - radius (r): Radius of the smudge tool. All UVs within this radius are affected by the tool
        - smudgeIsMiddle (sim): By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.
        - edit (e): Edit mode flag
    """
@overload #Overload for texSmudgeUVContext in ['edit']
def texSmudgeUVContext(contextName: contextName, dragSlider: str = ..., ds: str = ..., effectType: str = ..., et: str = ..., functionType: str = ..., ft: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., pressure: float = ..., prs: float = ..., radius: float = ..., r: float = ..., smudgeIsMiddle: bool = ..., sim: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """texSmudgeUVContext is undoable, queryable, and editable.
    
    This command creates a context for smudge UV tool. This context only works in
    the texture UV editor.

    ---
    - Args:
        - contextName: Input item(s).
        - dragSlider (ds): radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
        - effectType (et): fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.
        - functionType (ft): exponential | linear | constant. Specifies how UVs fall off from the center of influence.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - pressure (prs): Pressure value when effect type is set to smudge.
        - radius (r): Radius of the smudge tool. All UVs within this radius are affected by the tool
        - smudgeIsMiddle (sim): By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.
        - edit (e): Edit mode flag
    """
