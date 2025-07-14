"""Stub files for General category in Maya commands, command: group."""

from typing import Any, overload

@overload #Overload for group in ['create']
def group([objects...]: [objects...], absolute: bool = ..., empty: bool = ..., name: str = ..., parent: str = ..., relative: bool = ..., useAsGroup: str = ..., world: bool = ...) -> str:
    """group is undoable, NOT queryable, and NOT editable.
    
    This command groups the specified objects under a new group and returns the
    name of the new group.
    
    If the -em flag is specified, then an empty group (with no objects) is
    created.
    
    If the -w flag is specified then the new group is placed under the world,
    otherwise if -p is specified it is placed under the specified node. If neither
    -w or -p is specified the new group is placed under the lowest common group
    they have in common. (or the world if no such group exists)
    
    If an object is grouped with another object that has the same name then one of
    the objects will be renamed by this command.

    ---
    - Args:
        - [objects...]: Input item(s).
        - absolute (a): preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
        - empty (em): create an empty group (with no objects in it)
        - name (n): Assign given name to new group node.
        - parent (p): put the new group under the given parent
        - relative (r): preserve existing local object transformations (relative to the new group node)
        - useAsGroup (uag): Use the specified node as the group node. The specified node must be derived from the transform node and must not have any existing parents or children.
        - world (w): put the new group under the world
    """
@overload #Overload for group in ['create']
def group([objects...]: [objects...], a: bool = ..., em: bool = ..., n: str = ..., p: str = ..., r: bool = ..., uag: str = ..., w: bool = ...) -> str:
    """group is undoable, NOT queryable, and NOT editable.
    
    This command groups the specified objects under a new group and returns the
    name of the new group.
    
    If the -em flag is specified, then an empty group (with no objects) is
    created.
    
    If the -w flag is specified then the new group is placed under the world,
    otherwise if -p is specified it is placed under the specified node. If neither
    -w or -p is specified the new group is placed under the lowest common group
    they have in common. (or the world if no such group exists)
    
    If an object is grouped with another object that has the same name then one of
    the objects will be renamed by this command.

    ---
    - Args:
        - [objects...]: Input item(s).
        - absolute (a): preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
        - empty (em): create an empty group (with no objects in it)
        - name (n): Assign given name to new group node.
        - parent (p): put the new group under the given parent
        - relative (r): preserve existing local object transformations (relative to the new group node)
        - useAsGroup (uag): Use the specified node as the group node. The specified node must be derived from the transform node and must not have any existing parents or children.
        - world (w): put the new group under the world
    """
@overload #Overload for group in ['create']
def group([objects...]: [objects...], absolute: bool = ..., a: bool = ..., empty: bool = ..., em: bool = ..., name: str = ..., n: str = ..., parent: str = ..., p: str = ..., relative: bool = ..., r: bool = ..., useAsGroup: str = ..., uag: str = ..., world: bool = ..., w: bool = ...) -> str:
    """group is undoable, NOT queryable, and NOT editable.
    
    This command groups the specified objects under a new group and returns the
    name of the new group.
    
    If the -em flag is specified, then an empty group (with no objects) is
    created.
    
    If the -w flag is specified then the new group is placed under the world,
    otherwise if -p is specified it is placed under the specified node. If neither
    -w or -p is specified the new group is placed under the lowest common group
    they have in common. (or the world if no such group exists)
    
    If an object is grouped with another object that has the same name then one of
    the objects will be renamed by this command.

    ---
    - Args:
        - [objects...]: Input item(s).
        - absolute (a): preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
        - empty (em): create an empty group (with no objects in it)
        - name (n): Assign given name to new group node.
        - parent (p): put the new group under the given parent
        - relative (r): preserve existing local object transformations (relative to the new group node)
        - useAsGroup (uag): Use the specified node as the group node. The specified node must be derived from the transform node and must not have any existing parents or children.
        - world (w): put the new group under the world
    """
