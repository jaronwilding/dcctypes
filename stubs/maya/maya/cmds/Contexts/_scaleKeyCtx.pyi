"""Stub files for Contexts category in Maya commands, command: scaleKeyCtx."""

from typing import Any, overload

@overload #Overload for scaleKeyCtx in ['create']
def scaleKeyCtx(contextName: contextName, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., scaleSpecifiedKeys: bool = ..., type: str = ...) -> str | bool:
    """scaleKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - scaleSpecifiedKeys (ssk): Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        - type (typ): rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)
    """
@overload #Overload for scaleKeyCtx in ['create']
def scaleKeyCtx(contextName: contextName, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., ssk: bool = ..., typ: str = ...) -> str | bool:
    """scaleKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - scaleSpecifiedKeys (ssk): Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        - type (typ): rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)
    """
@overload #Overload for scaleKeyCtx in ['create']
def scaleKeyCtx(contextName: contextName, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., scaleSpecifiedKeys: bool = ..., ssk: bool = ..., type: str = ..., typ: str = ...) -> str | bool:
    """scaleKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - scaleSpecifiedKeys (ssk): Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        - type (typ): rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)
    """
@overload #Overload for scaleKeyCtx in ['query']
def scaleKeyCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., scaleSpecifiedKeys: bool = ..., type: str = ..., query: bool = ...) -> str | bool:
    """scaleKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - scaleSpecifiedKeys (ssk): Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        - type (typ): rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)
        - query (q): Query mode flag
    """
@overload #Overload for scaleKeyCtx in ['query']
def scaleKeyCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., ssk: bool = ..., typ: str = ..., q: bool = ...) -> str | bool:
    """scaleKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - scaleSpecifiedKeys (ssk): Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        - type (typ): rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)
        - query (q): Query mode flag
    """
@overload #Overload for scaleKeyCtx in ['query']
def scaleKeyCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., scaleSpecifiedKeys: bool = ..., ssk: bool = ..., type: str = ..., typ: str = ..., query: bool = ..., q: bool = ...) -> str | bool:
    """scaleKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - scaleSpecifiedKeys (ssk): Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        - type (typ): rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)
        - query (q): Query mode flag
    """
@overload #Overload for scaleKeyCtx in ['edit']
def scaleKeyCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., scaleSpecifiedKeys: bool = ..., type: str = ..., edit: bool = ...) -> str | bool:
    """scaleKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - scaleSpecifiedKeys (ssk): Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        - type (typ): rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)
        - edit (e): Edit mode flag
    """
@overload #Overload for scaleKeyCtx in ['edit']
def scaleKeyCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., ssk: bool = ..., typ: str = ..., e: bool = ...) -> str | bool:
    """scaleKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - scaleSpecifiedKeys (ssk): Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        - type (typ): rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)
        - edit (e): Edit mode flag
    """
@overload #Overload for scaleKeyCtx in ['edit']
def scaleKeyCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., scaleSpecifiedKeys: bool = ..., ssk: bool = ..., type: str = ..., typ: str = ..., edit: bool = ..., e: bool = ...) -> str | bool:
    """scaleKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to scale keyframes within the
    graph editor

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - scaleSpecifiedKeys (ssk): Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        - type (typ): rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)
        - edit (e): Edit mode flag
    """
