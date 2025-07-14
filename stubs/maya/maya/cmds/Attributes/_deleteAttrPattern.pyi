"""Stub files for Attributes category in Maya commands, command: deleteAttrPattern."""

from typing import Any, overload

@overload #Overload for deleteAttrPattern in ['create']
def deleteAttrPattern(allPatterns: bool = ..., patternName: str = ..., patternType: str = ...) -> str:
    """deleteAttrPattern is undoable, NOT queryable, and NOT editable.
    
    After a while the list of attribute patterns could become cluttered. This
    command provides a way to remove patterns from memory so that only the ones of
    interest will show.

    ---
    - Args:
        - allPatterns (all): If specified it means delete all known attribute patterns.
        - patternName (pn): The name of the pattern to be deleted.
        - patternType (pt): Delete all patterns of the given type.
    """
@overload #Overload for deleteAttrPattern in ['create']
def deleteAttrPattern(all: bool = ..., pn: str = ..., pt: str = ...) -> str:
    """deleteAttrPattern is undoable, NOT queryable, and NOT editable.
    
    After a while the list of attribute patterns could become cluttered. This
    command provides a way to remove patterns from memory so that only the ones of
    interest will show.

    ---
    - Args:
        - allPatterns (all): If specified it means delete all known attribute patterns.
        - patternName (pn): The name of the pattern to be deleted.
        - patternType (pt): Delete all patterns of the given type.
    """
@overload #Overload for deleteAttrPattern in ['create']
def deleteAttrPattern(allPatterns: bool = ..., all: bool = ..., patternName: str = ..., pn: str = ..., patternType: str = ..., pt: str = ...) -> str:
    """deleteAttrPattern is undoable, NOT queryable, and NOT editable.
    
    After a while the list of attribute patterns could become cluttered. This
    command provides a way to remove patterns from memory so that only the ones of
    interest will show.

    ---
    - Args:
        - allPatterns (all): If specified it means delete all known attribute patterns.
        - patternName (pn): The name of the pattern to be deleted.
        - patternType (pt): Delete all patterns of the given type.
    """
