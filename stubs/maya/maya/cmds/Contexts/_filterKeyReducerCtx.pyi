"""Stub files for Contexts category in Maya commands, command: filterKeyReducerCtx."""

from typing import Any, overload

@overload #Overload for filterKeyReducerCtx in ['create']
def filterKeyReducerCtx(contextName: contextName, endTime: time = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., keySync: bool = ..., name: str = ..., precision: float = ..., precisionMode: int = ..., preserveKeyTangent: str = ..., selectedKeys: bool = ..., startTime: time = ...) -> str:
    """filterKeyReducerCtx is undoable, queryable, and editable.
    
    Creates/edits a KeyReducer filter context. This context can be used to
    interactively preview/edit the KeyReducer filter on a set of animation curves.

    ---
    - Args:
        - contextName: Input item(s).
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keySync (ks): When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.
        - name (n): If this is a tool command, name the tool appropriately.
        - precision (pre): Defines the precision parameter.  For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        - precisionMode (pm): Specifies the precision mode for the Key Reducer filter. Avaiable modes are:  0: Absolute value. 1: Percentage  Default is 1 (percentage mode).
        - preserveKeyTangent (pkt): When specified, keys whose in or out tangent type match the specified type are preserved.  Supported tangent types:  fixed linear flat smooth step clamped plateau stepnext auto
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
    """
@overload #Overload for filterKeyReducerCtx in ['create']
def filterKeyReducerCtx(contextName: contextName, e: time = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ks: bool = ..., n: str = ..., pre: float = ..., pm: int = ..., pkt: str = ..., sk: bool = ..., s: time = ...) -> str:
    """filterKeyReducerCtx is undoable, queryable, and editable.
    
    Creates/edits a KeyReducer filter context. This context can be used to
    interactively preview/edit the KeyReducer filter on a set of animation curves.

    ---
    - Args:
        - contextName: Input item(s).
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keySync (ks): When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.
        - name (n): If this is a tool command, name the tool appropriately.
        - precision (pre): Defines the precision parameter.  For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        - precisionMode (pm): Specifies the precision mode for the Key Reducer filter. Avaiable modes are:  0: Absolute value. 1: Percentage  Default is 1 (percentage mode).
        - preserveKeyTangent (pkt): When specified, keys whose in or out tangent type match the specified type are preserved.  Supported tangent types:  fixed linear flat smooth step clamped plateau stepnext auto
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
    """
@overload #Overload for filterKeyReducerCtx in ['create']
def filterKeyReducerCtx(contextName: contextName, endTime: time = ..., e: time = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., keySync: bool = ..., ks: bool = ..., name: str = ..., n: str = ..., precision: float = ..., pre: float = ..., precisionMode: int = ..., pm: int = ..., preserveKeyTangent: str = ..., pkt: str = ..., selectedKeys: bool = ..., sk: bool = ..., startTime: time = ..., s: time = ...) -> str:
    """filterKeyReducerCtx is undoable, queryable, and editable.
    
    Creates/edits a KeyReducer filter context. This context can be used to
    interactively preview/edit the KeyReducer filter on a set of animation curves.

    ---
    - Args:
        - contextName: Input item(s).
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keySync (ks): When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.
        - name (n): If this is a tool command, name the tool appropriately.
        - precision (pre): Defines the precision parameter.  For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        - precisionMode (pm): Specifies the precision mode for the Key Reducer filter. Avaiable modes are:  0: Absolute value. 1: Percentage  Default is 1 (percentage mode).
        - preserveKeyTangent (pkt): When specified, keys whose in or out tangent type match the specified type are preserved.  Supported tangent types:  fixed linear flat smooth step clamped plateau stepnext auto
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
    """
@overload #Overload for filterKeyReducerCtx in ['query']
def filterKeyReducerCtx(contextName: contextName, endTime: time = ..., image1: str = ..., image2: str = ..., image3: str = ..., keySync: bool = ..., precision: float = ..., precisionMode: int = ..., preserveKeyTangent: str = ..., selectedKeys: bool = ..., startTime: time = ..., query: bool = ...) -> str:
    """filterKeyReducerCtx is undoable, queryable, and editable.
    
    Creates/edits a KeyReducer filter context. This context can be used to
    interactively preview/edit the KeyReducer filter on a set of animation curves.

    ---
    - Args:
        - contextName: Input item(s).
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keySync (ks): When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.
        - precision (pre): Defines the precision parameter.  For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        - precisionMode (pm): Specifies the precision mode for the Key Reducer filter. Avaiable modes are:  0: Absolute value. 1: Percentage  Default is 1 (percentage mode).
        - preserveKeyTangent (pkt): When specified, keys whose in or out tangent type match the specified type are preserved.  Supported tangent types:  fixed linear flat smooth step clamped plateau stepnext auto
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - query (q): Query mode flag
    """
@overload #Overload for filterKeyReducerCtx in ['query']
def filterKeyReducerCtx(contextName: contextName, e: time = ..., i1: str = ..., i2: str = ..., i3: str = ..., ks: bool = ..., pre: float = ..., pm: int = ..., pkt: str = ..., sk: bool = ..., s: time = ..., q: bool = ...) -> str:
    """filterKeyReducerCtx is undoable, queryable, and editable.
    
    Creates/edits a KeyReducer filter context. This context can be used to
    interactively preview/edit the KeyReducer filter on a set of animation curves.

    ---
    - Args:
        - contextName: Input item(s).
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keySync (ks): When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.
        - precision (pre): Defines the precision parameter.  For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        - precisionMode (pm): Specifies the precision mode for the Key Reducer filter. Avaiable modes are:  0: Absolute value. 1: Percentage  Default is 1 (percentage mode).
        - preserveKeyTangent (pkt): When specified, keys whose in or out tangent type match the specified type are preserved.  Supported tangent types:  fixed linear flat smooth step clamped plateau stepnext auto
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - query (q): Query mode flag
    """
@overload #Overload for filterKeyReducerCtx in ['query']
def filterKeyReducerCtx(contextName: contextName, endTime: time = ..., e: time = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., keySync: bool = ..., ks: bool = ..., precision: float = ..., pre: float = ..., precisionMode: int = ..., pm: int = ..., preserveKeyTangent: str = ..., pkt: str = ..., selectedKeys: bool = ..., sk: bool = ..., startTime: time = ..., s: time = ..., query: bool = ..., q: bool = ...) -> str:
    """filterKeyReducerCtx is undoable, queryable, and editable.
    
    Creates/edits a KeyReducer filter context. This context can be used to
    interactively preview/edit the KeyReducer filter on a set of animation curves.

    ---
    - Args:
        - contextName: Input item(s).
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keySync (ks): When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.
        - precision (pre): Defines the precision parameter.  For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        - precisionMode (pm): Specifies the precision mode for the Key Reducer filter. Avaiable modes are:  0: Absolute value. 1: Percentage  Default is 1 (percentage mode).
        - preserveKeyTangent (pkt): When specified, keys whose in or out tangent type match the specified type are preserved.  Supported tangent types:  fixed linear flat smooth step clamped plateau stepnext auto
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - query (q): Query mode flag
    """
@overload #Overload for filterKeyReducerCtx in ['edit']
def filterKeyReducerCtx(contextName: contextName, apply: bool = ..., endTime: time = ..., image1: str = ..., image2: str = ..., image3: str = ..., keySync: bool = ..., precision: float = ..., precisionMode: int = ..., preserveKeyTangent: str = ..., selectedKeys: bool = ..., startTime: time = ..., edit: bool = ...) -> str:
    """filterKeyReducerCtx is undoable, queryable, and editable.
    
    Creates/edits a KeyReducer filter context. This context can be used to
    interactively preview/edit the KeyReducer filter on a set of animation curves.

    ---
    - Args:
        - contextName: Input item(s).
        - apply (a): When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keySync (ks): When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.
        - precision (pre): Defines the precision parameter.  For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        - precisionMode (pm): Specifies the precision mode for the Key Reducer filter. Avaiable modes are:  0: Absolute value. 1: Percentage  Default is 1 (percentage mode).
        - preserveKeyTangent (pkt): When specified, keys whose in or out tangent type match the specified type are preserved.  Supported tangent types:  fixed linear flat smooth step clamped plateau stepnext auto
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - edit (e): Edit mode flag
    """
@overload #Overload for filterKeyReducerCtx in ['edit']
def filterKeyReducerCtx(contextName: contextName, a: bool = ..., e: time = ..., i1: str = ..., i2: str = ..., i3: str = ..., ks: bool = ..., pre: float = ..., pm: int = ..., pkt: str = ..., sk: bool = ..., s: time = ..., e: bool = ...) -> str:
    """filterKeyReducerCtx is undoable, queryable, and editable.
    
    Creates/edits a KeyReducer filter context. This context can be used to
    interactively preview/edit the KeyReducer filter on a set of animation curves.

    ---
    - Args:
        - contextName: Input item(s).
        - apply (a): When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keySync (ks): When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.
        - precision (pre): Defines the precision parameter.  For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        - precisionMode (pm): Specifies the precision mode for the Key Reducer filter. Avaiable modes are:  0: Absolute value. 1: Percentage  Default is 1 (percentage mode).
        - preserveKeyTangent (pkt): When specified, keys whose in or out tangent type match the specified type are preserved.  Supported tangent types:  fixed linear flat smooth step clamped plateau stepnext auto
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - edit (e): Edit mode flag
    """
@overload #Overload for filterKeyReducerCtx in ['edit']
def filterKeyReducerCtx(contextName: contextName, apply: bool = ..., a: bool = ..., endTime: time = ..., e: time = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., keySync: bool = ..., ks: bool = ..., precision: float = ..., pre: float = ..., precisionMode: int = ..., pm: int = ..., preserveKeyTangent: str = ..., pkt: str = ..., selectedKeys: bool = ..., sk: bool = ..., startTime: time = ..., s: time = ..., edit: bool = ..., e: bool = ...) -> str:
    """filterKeyReducerCtx is undoable, queryable, and editable.
    
    Creates/edits a KeyReducer filter context. This context can be used to
    interactively preview/edit the KeyReducer filter on a set of animation curves.

    ---
    - Args:
        - contextName: Input item(s).
        - apply (a): When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        - endTime (e): Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - keySync (ks): When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.
        - precision (pre): Defines the precision parameter.  For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        - precisionMode (pm): Specifies the precision mode for the Key Reducer filter. Avaiable modes are:  0: Absolute value. 1: Percentage  Default is 1 (percentage mode).
        - preserveKeyTangent (pkt): When specified, keys whose in or out tangent type match the specified type are preserved.  Supported tangent types:  fixed linear flat smooth step clamped plateau stepnext auto
        - selectedKeys (sk): If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        - startTime (s): Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        - edit (e): Edit mode flag
    """
