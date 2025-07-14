"""Stub files for General category in Maya commands, command: affects."""

from typing import Any, overload

@overload #Overload for affects in ['create']
def affects(string: str, by: bool = ..., type: str = ...) -> str:
    """affects is NOT undoable, NOT queryable, and NOT editable.
    
    This command returns the list of attributes on a node or node type which
    affect the named attribute.

    ---
    - Args:
        - string: Input item(s).
        - by ()): Show attributes that are affected by the given one rather than the ones that affect it.
        - type (t): static node type from which to get 'affects' information
    """
@overload #Overload for affects in ['create']
def affects(string: str, ): bool = ..., t: str = ...) -> str:
    """affects is NOT undoable, NOT queryable, and NOT editable.
    
    This command returns the list of attributes on a node or node type which
    affect the named attribute.

    ---
    - Args:
        - string: Input item(s).
        - by ()): Show attributes that are affected by the given one rather than the ones that affect it.
        - type (t): static node type from which to get 'affects' information
    """
@overload #Overload for affects in ['create']
def affects(string: str, by: bool = ..., ): bool = ..., type: str = ..., t: str = ...) -> str:
    """affects is NOT undoable, NOT queryable, and NOT editable.
    
    This command returns the list of attributes on a node or node type which
    affect the named attribute.

    ---
    - Args:
        - string: Input item(s).
        - by ()): Show attributes that are affected by the given one rather than the ones that affect it.
        - type (t): static node type from which to get 'affects' information
    """
