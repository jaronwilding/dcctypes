"""Stub files for General category in Maya commands, command: rename."""

from typing import Any, overload

@overload #Overload for rename in ['create']
def rename([object] string: [object] string, ignoreShape: bool = ..., uuid: bool = ...) -> str:
    """rename is undoable, NOT queryable, and NOT editable.
    
    Renames the given object to have the new name. If only one argument is
    supplied the command will rename the (first) selected object. If the new name
    conflicts with an existing name, the object will be given a unique name based
    on the supplied name. It is not legal to rename an object to the empty string.
    
    When a transform is renamed then any shape nodes beneath the transform that
    have the same prefix as the old transform name are renamed. For example,
    "rename nurbsSphere1 ball" would rename "nurbsSphere1|nurbsSphereShape1" to
    "ball|ballShape".
    
    If the new name ends in a single '#' then the rename command will replace the
    trailing '#' with a number that ensures the new name is unique.
    
    ## Notes
    
    If the name has an absolute namespace part, it will be considered. Namespaces
    that do not exist will be created automatically as needed. If the name has a
    relative namespace part, it will be ignored. In that case, the object will be
    put under the current namespace. (see example below).

    ---
    - Args:
        - [object] string: Input item(s).
        - ignoreShape: Indicates that renaming of shape nodes below transform nodes should be prevented.
        - uuid (uid): Indicates that the new name is actually a UUID, and that the command should change the node's UUID. (In which case its name remains unchanged.)
    """
@overload #Overload for rename in ['create']
def rename([object] string: [object] string, uid: bool = ...) -> str:
    """rename is undoable, NOT queryable, and NOT editable.
    
    Renames the given object to have the new name. If only one argument is
    supplied the command will rename the (first) selected object. If the new name
    conflicts with an existing name, the object will be given a unique name based
    on the supplied name. It is not legal to rename an object to the empty string.
    
    When a transform is renamed then any shape nodes beneath the transform that
    have the same prefix as the old transform name are renamed. For example,
    "rename nurbsSphere1 ball" would rename "nurbsSphere1|nurbsSphereShape1" to
    "ball|ballShape".
    
    If the new name ends in a single '#' then the rename command will replace the
    trailing '#' with a number that ensures the new name is unique.
    
    ## Notes
    
    If the name has an absolute namespace part, it will be considered. Namespaces
    that do not exist will be created automatically as needed. If the name has a
    relative namespace part, it will be ignored. In that case, the object will be
    put under the current namespace. (see example below).

    ---
    - Args:
        - [object] string: Input item(s).
        - ignoreShape: Indicates that renaming of shape nodes below transform nodes should be prevented.
        - uuid (uid): Indicates that the new name is actually a UUID, and that the command should change the node's UUID. (In which case its name remains unchanged.)
    """
@overload #Overload for rename in ['create']
def rename([object] string: [object] string, ignoreShape: bool = ..., uuid: bool = ..., uid: bool = ...) -> str:
    """rename is undoable, NOT queryable, and NOT editable.
    
    Renames the given object to have the new name. If only one argument is
    supplied the command will rename the (first) selected object. If the new name
    conflicts with an existing name, the object will be given a unique name based
    on the supplied name. It is not legal to rename an object to the empty string.
    
    When a transform is renamed then any shape nodes beneath the transform that
    have the same prefix as the old transform name are renamed. For example,
    "rename nurbsSphere1 ball" would rename "nurbsSphere1|nurbsSphereShape1" to
    "ball|ballShape".
    
    If the new name ends in a single '#' then the rename command will replace the
    trailing '#' with a number that ensures the new name is unique.
    
    ## Notes
    
    If the name has an absolute namespace part, it will be considered. Namespaces
    that do not exist will be created automatically as needed. If the name has a
    relative namespace part, it will be ignored. In that case, the object will be
    put under the current namespace. (see example below).

    ---
    - Args:
        - [object] string: Input item(s).
        - ignoreShape: Indicates that renaming of shape nodes below transform nodes should be prevented.
        - uuid (uid): Indicates that the new name is actually a UUID, and that the command should change the node's UUID. (In which case its name remains unchanged.)
    """
