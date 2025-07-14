"""Stub files for General category in Maya commands, command: listSets."""

from typing import Any, overload

@overload #Overload for listSets in ['create']
def listSets([object]: [object], allSets: bool = ..., extendToShape: bool = ..., object: name = ..., type: int = ...) -> list[str]:
    """listSets is undoable, NOT queryable, and NOT editable.
    
    The listSets command is used to get a list of all the sets an object belongs
    to. To get sets of a specific type for an object use the type flag as well.
    
    To get a list of all sets in the scene then don't use an object in the command
    line but use one of the flags instead.

    ---
    - Args:
        - [object]: Input item(s).
        - allSets: Returns all sets in the scene.
        - extendToShape (ets): When requesting a transform's sets also walk down to the shape immediately below it for its sets.
        - object (o): Returns all sets which this object is a member of.
        - type (t): Returns all sets in the scene of the given type:1 - all rendering sets2 - all deformer sets
    """
@overload #Overload for listSets in ['create']
def listSets([object]: [object], ets: bool = ..., o: name = ..., t: int = ...) -> list[str]:
    """listSets is undoable, NOT queryable, and NOT editable.
    
    The listSets command is used to get a list of all the sets an object belongs
    to. To get sets of a specific type for an object use the type flag as well.
    
    To get a list of all sets in the scene then don't use an object in the command
    line but use one of the flags instead.

    ---
    - Args:
        - [object]: Input item(s).
        - allSets: Returns all sets in the scene.
        - extendToShape (ets): When requesting a transform's sets also walk down to the shape immediately below it for its sets.
        - object (o): Returns all sets which this object is a member of.
        - type (t): Returns all sets in the scene of the given type:1 - all rendering sets2 - all deformer sets
    """
@overload #Overload for listSets in ['create']
def listSets([object]: [object], allSets: bool = ..., extendToShape: bool = ..., ets: bool = ..., object: name = ..., o: name = ..., type: int = ..., t: int = ...) -> list[str]:
    """listSets is undoable, NOT queryable, and NOT editable.
    
    The listSets command is used to get a list of all the sets an object belongs
    to. To get sets of a specific type for an object use the type flag as well.
    
    To get a list of all sets in the scene then don't use an object in the command
    line but use one of the flags instead.

    ---
    - Args:
        - [object]: Input item(s).
        - allSets: Returns all sets in the scene.
        - extendToShape (ets): When requesting a transform's sets also walk down to the shape immediately below it for its sets.
        - object (o): Returns all sets which this object is a member of.
        - type (t): Returns all sets in the scene of the given type:1 - all rendering sets2 - all deformer sets
    """
