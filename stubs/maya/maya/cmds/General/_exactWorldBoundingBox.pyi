"""Stub files for General category in Maya commands, command: exactWorldBoundingBox."""

from typing import Any, overload

@overload #Overload for exactWorldBoundingBox in ['create']
def exactWorldBoundingBox([dagObject...]: [dagObject...], calculateExactly: bool = ..., ignoreInvisible: bool = ...) -> float[]:
    """exactWorldBoundingBox is undoable, NOT queryable, and NOT editable.
    
    This command figures out an exact-fit bounding box for the specified objects
    (or selected objects if none are specified) This bounding box is always in
    world space.

    ---
    - Args:
        - [dagObject...]: Input item(s).
        - calculateExactly (ce): Should the bounding box calculation be exact?
        - ignoreInvisible (ii): Should the bounding box calculation include or exclude invisible objects?
    """
@overload #Overload for exactWorldBoundingBox in ['create']
def exactWorldBoundingBox([dagObject...]: [dagObject...], ce: bool = ..., ii: bool = ...) -> float[]:
    """exactWorldBoundingBox is undoable, NOT queryable, and NOT editable.
    
    This command figures out an exact-fit bounding box for the specified objects
    (or selected objects if none are specified) This bounding box is always in
    world space.

    ---
    - Args:
        - [dagObject...]: Input item(s).
        - calculateExactly (ce): Should the bounding box calculation be exact?
        - ignoreInvisible (ii): Should the bounding box calculation include or exclude invisible objects?
    """
@overload #Overload for exactWorldBoundingBox in ['create']
def exactWorldBoundingBox([dagObject...]: [dagObject...], calculateExactly: bool = ..., ce: bool = ..., ignoreInvisible: bool = ..., ii: bool = ...) -> float[]:
    """exactWorldBoundingBox is undoable, NOT queryable, and NOT editable.
    
    This command figures out an exact-fit bounding box for the specified objects
    (or selected objects if none are specified) This bounding box is always in
    world space.

    ---
    - Args:
        - [dagObject...]: Input item(s).
        - calculateExactly (ce): Should the bounding box calculation be exact?
        - ignoreInvisible (ii): Should the bounding box calculation include or exclude invisible objects?
    """
