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

    Example:
    ```python
        import maya.cmds as cmds
        # Create a simple hierarchy
        cmds.sphere( n='sphere1' )
        cmds.move( 2, 0, 0 )
        cmds.sphere( n='sphere2' )
        cmds.move( -2, 0, 0 )
        cmds.group( 'sphere1', 'sphere2', n='group1' )
        cmds.move( 0, 2, 0 )
        cmds.sphere( n='sphere3' )
        cmds.move( 0, 0, 2 )
        cmds.group( 'group1', 'sphere3', n='group2' )
        cmds.group( em=True, n='group3' )
        # Remove group1 from the hierarchy. What should remain
        # is group2 with sphere3, sphere1, and sphere2 as children.
        # Note that the objects don't move since the absolute flag
        # is implied.
        #
        cmds.ungroup( 'group1' )
        # Try the same ungroup with the -relative flag.
        # Now sphere1 and sphere2 will move down 2 units in Y.
        #
        cmds.undo()
        cmds.ungroup( 'group1', relative=True )
        # Now try the same ungroup operation with the -parent flag.
        # This will move the children of group1 under group3.
        cmds.undo()
        cmds.ungroup( 'group1', parent='group3' )
    ```

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

    Example:
    ```python
        import maya.cmds as cmds
        # Create a simple hierarchy
        cmds.sphere( n='sphere1' )
        cmds.move( 2, 0, 0 )
        cmds.sphere( n='sphere2' )
        cmds.move( -2, 0, 0 )
        cmds.group( 'sphere1', 'sphere2', n='group1' )
        cmds.move( 0, 2, 0 )
        cmds.sphere( n='sphere3' )
        cmds.move( 0, 0, 2 )
        cmds.group( 'group1', 'sphere3', n='group2' )
        cmds.group( em=True, n='group3' )
        # Remove group1 from the hierarchy. What should remain
        # is group2 with sphere3, sphere1, and sphere2 as children.
        # Note that the objects don't move since the absolute flag
        # is implied.
        #
        cmds.ungroup( 'group1' )
        # Try the same ungroup with the -relative flag.
        # Now sphere1 and sphere2 will move down 2 units in Y.
        #
        cmds.undo()
        cmds.ungroup( 'group1', relative=True )
        # Now try the same ungroup operation with the -parent flag.
        # This will move the children of group1 under group3.
        cmds.undo()
        cmds.ungroup( 'group1', parent='group3' )
    ```

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

    Example:
    ```python
        import maya.cmds as cmds
        # Create a simple hierarchy
        cmds.sphere( n='sphere1' )
        cmds.move( 2, 0, 0 )
        cmds.sphere( n='sphere2' )
        cmds.move( -2, 0, 0 )
        cmds.group( 'sphere1', 'sphere2', n='group1' )
        cmds.move( 0, 2, 0 )
        cmds.sphere( n='sphere3' )
        cmds.move( 0, 0, 2 )
        cmds.group( 'group1', 'sphere3', n='group2' )
        cmds.group( em=True, n='group3' )
        # Remove group1 from the hierarchy. What should remain
        # is group2 with sphere3, sphere1, and sphere2 as children.
        # Note that the objects don't move since the absolute flag
        # is implied.
        #
        cmds.ungroup( 'group1' )
        # Try the same ungroup with the -relative flag.
        # Now sphere1 and sphere2 will move down 2 units in Y.
        #
        cmds.undo()
        cmds.ungroup( 'group1', relative=True )
        # Now try the same ungroup operation with the -parent flag.
        # This will move the children of group1 under group3.
        cmds.undo()
        cmds.ungroup( 'group1', parent='group3' )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - absolute (a): preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
        - parent (p): put the ungrouped objects under the given parent
        - relative (r): preserve existing local object transformations (don't modify local transformation)
        - world (w): put the ungrouped objects under the world
    """
