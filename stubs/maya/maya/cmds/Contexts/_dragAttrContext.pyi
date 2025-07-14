"""Stub files for Contexts category in Maya commands, command: dragAttrContext."""

from typing import Any, overload

@overload #Overload for dragAttrContext in ['create']
def dragAttrContext([name]: [name], connectTo: name = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., reset: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - reset (r): Resets the list of attributes to which the context is connected.
    """
@overload #Overload for dragAttrContext in ['create']
def dragAttrContext([name]: [name], ct: name = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., r: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - reset (r): Resets the list of attributes to which the context is connected.
    """
@overload #Overload for dragAttrContext in ['create']
def dragAttrContext([name]: [name], connectTo: name = ..., ct: name = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., reset: bool = ..., r: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - reset (r): Resets the list of attributes to which the context is connected.
    """
@overload #Overload for dragAttrContext in ['query']
def dragAttrContext([name]: [name], connectTo: name = ..., image1: str = ..., image2: str = ..., image3: str = ..., reset: bool = ..., query: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (r): Resets the list of attributes to which the context is connected.
        - query (q): Query mode flag
    """
@overload #Overload for dragAttrContext in ['query']
def dragAttrContext([name]: [name], ct: name = ..., i1: str = ..., i2: str = ..., i3: str = ..., r: bool = ..., q: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (r): Resets the list of attributes to which the context is connected.
        - query (q): Query mode flag
    """
@overload #Overload for dragAttrContext in ['query']
def dragAttrContext([name]: [name], connectTo: name = ..., ct: name = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., reset: bool = ..., r: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (r): Resets the list of attributes to which the context is connected.
        - query (q): Query mode flag
    """
@overload #Overload for dragAttrContext in ['edit']
def dragAttrContext([name]: [name], connectTo: name = ..., image1: str = ..., image2: str = ..., image3: str = ..., reset: bool = ..., edit: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (r): Resets the list of attributes to which the context is connected.
        - edit (e): Edit mode flag
    """
@overload #Overload for dragAttrContext in ['edit']
def dragAttrContext([name]: [name], ct: name = ..., i1: str = ..., i2: str = ..., i3: str = ..., r: bool = ..., e: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (r): Resets the list of attributes to which the context is connected.
        - edit (e): Edit mode flag
    """
@overload #Overload for dragAttrContext in ['edit']
def dragAttrContext([name]: [name], connectTo: name = ..., ct: name = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., reset: bool = ..., r: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (r): Resets the list of attributes to which the context is connected.
        - edit (e): Edit mode flag
    """
