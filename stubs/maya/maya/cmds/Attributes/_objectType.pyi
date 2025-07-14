"""Stub files for Attributes category in Maya commands, command: objectType."""

from typing import Any, overload

@overload #Overload for objectType in ['create']
def objectType(object: object, isAType: str = ..., isType: str = ..., tagFromType: str = ..., typeFromTag: int = ..., typeTag: bool = ...) -> str | bool:
    """objectType is undoable, NOT queryable, and NOT editable.
    
    This command returns the type of elements. Warning: This command is incomplete
    and may not be supported by all object types.

    ---
    - Args:
        - object: Input item(s).
        - isAType (isa): Returns true if the object is the specified type or derives from an object that is of the specified type. This flag will only work with dependency nodes.
        - isType (i): Returns true if the object is exactly of the specified type. False otherwise.
        - tagFromType (tgt): Returns the type tag given a type name.
        - typeFromTag (tpt): Returns the type name given an integer type tag.
        - typeTag (tt): Returns an integer tag that is unique for that object type.  Not all object types will have tags.  This is the unique 4-byte value that is used to identify nodes of a given type in the binary file format.
    """
@overload #Overload for objectType in ['create']
def objectType(object: object, isa: str = ..., i: str = ..., tgt: str = ..., tpt: int = ..., tt: bool = ...) -> str | bool:
    """objectType is undoable, NOT queryable, and NOT editable.
    
    This command returns the type of elements. Warning: This command is incomplete
    and may not be supported by all object types.

    ---
    - Args:
        - object: Input item(s).
        - isAType (isa): Returns true if the object is the specified type or derives from an object that is of the specified type. This flag will only work with dependency nodes.
        - isType (i): Returns true if the object is exactly of the specified type. False otherwise.
        - tagFromType (tgt): Returns the type tag given a type name.
        - typeFromTag (tpt): Returns the type name given an integer type tag.
        - typeTag (tt): Returns an integer tag that is unique for that object type.  Not all object types will have tags.  This is the unique 4-byte value that is used to identify nodes of a given type in the binary file format.
    """
@overload #Overload for objectType in ['create']
def objectType(object: object, isAType: str = ..., isa: str = ..., isType: str = ..., i: str = ..., tagFromType: str = ..., tgt: str = ..., typeFromTag: int = ..., tpt: int = ..., typeTag: bool = ..., tt: bool = ...) -> str | bool:
    """objectType is undoable, NOT queryable, and NOT editable.
    
    This command returns the type of elements. Warning: This command is incomplete
    and may not be supported by all object types.

    ---
    - Args:
        - object: Input item(s).
        - isAType (isa): Returns true if the object is the specified type or derives from an object that is of the specified type. This flag will only work with dependency nodes.
        - isType (i): Returns true if the object is exactly of the specified type. False otherwise.
        - tagFromType (tgt): Returns the type tag given a type name.
        - typeFromTag (tpt): Returns the type name given an integer type tag.
        - typeTag (tt): Returns an integer tag that is unique for that object type.  Not all object types will have tags.  This is the unique 4-byte value that is used to identify nodes of a given type in the binary file format.
    """
