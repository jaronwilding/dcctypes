"""Stub files for General category in Maya commands, command: ungroup."""

from typing import Any, overload

@overload #Overload for ungroup in ['create']
def ungroup([objects...]: [objects...], absolute: bool = ..., parent: str = ..., relative: bool = ..., world: bool = ...) -> None:
    """ungroup is undoable, NOT queryable, and NOT editable.
    
    This command ungroups the specified objects.
    
    The objects will be placed at the same level in the hierarchy the group node
    occupied unless the -w flag is specified, in which case they will be placed
    under the world.
    
    If an object is ungrouped and there is an object in the new group with the
    same name then this command will rename the ungrouped object.
    
    See also: group, parent, instance, duplicate

    ---
    - Args:
        - [objects...]: Input item(s).
        - absolute (a): preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
        - parent (p): put the ungrouped objects under the given parent
        - relative (r): preserve existing local object transformations (don't modify local transformation)
        - world (w): put the ungrouped objects under the world
    """
@overload #Overload for ungroup in ['create']
def ungroup([objects...]: [objects...], a: bool = ..., p: str = ..., r: bool = ..., w: bool = ...) -> None:
    """ungroup is undoable, NOT queryable, and NOT editable.
    
    This command ungroups the specified objects.
    
    The objects will be placed at the same level in the hierarchy the group node
    occupied unless the -w flag is specified, in which case they will be placed
    under the world.
    
    If an object is ungrouped and there is an object in the new group with the
    same name then this command will rename the ungrouped object.
    
    See also: group, parent, instance, duplicate

    ---
    - Args:
        - [objects...]: Input item(s).
        - absolute (a): preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
        - parent (p): put the ungrouped objects under the given parent
        - relative (r): preserve existing local object transformations (don't modify local transformation)
        - world (w): put the ungrouped objects under the world
    """
@overload #Overload for ungroup in ['create']
def ungroup([objects...]: [objects...], absolute: bool = ..., a: bool = ..., parent: str = ..., p: str = ..., relative: bool = ..., r: bool = ..., world: bool = ..., w: bool = ...) -> None:
    """ungroup is undoable, NOT queryable, and NOT editable.
    
    This command ungroups the specified objects.
    
    The objects will be placed at the same level in the hierarchy the group node
    occupied unless the -w flag is specified, in which case they will be placed
    under the world.
    
    If an object is ungrouped and there is an object in the new group with the
    same name then this command will rename the ungrouped object.
    
    See also: group, parent, instance, duplicate

    ---
    - Args:
        - [objects...]: Input item(s).
        - absolute (a): preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
        - parent (p): put the ungrouped objects under the given parent
        - relative (r): preserve existing local object transformations (don't modify local transformation)
        - world (w): put the ungrouped objects under the world
    """
