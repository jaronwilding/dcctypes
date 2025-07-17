"""Stub files for General category in Maya commands, command: parent."""

from typing import Any, overload

@overload #Overload for parent in ['create']
def parent([dagObject...] [dagObject]: [dagObject...] [dagObject], absolute: bool = ..., addObject: bool = ..., noConnections: bool = ..., noInvScale: bool = ..., relative: bool = ..., removeObject: bool = ..., shape: bool = ..., world: bool = ...) -> list[str]:
    """parent is undoable, NOT queryable, and NOT editable.
    
    This command parents (moves) objects under a new group, removes objects from
    an existing group, or adds/removes parents.
    
    If the -w flag is specified all the selected or specified objects are parented
    to the world (unparented first).
    
    If the -rm flag is specified then all the selected or specified instances are
    removed.
    
    If there are more than two objects specified all the objects are parented to
    the last object specified.
    
    If the -add flag is specified, the objects are not reparented but also become
    children of the last object specified.
    
    If there is only a single object specified then the selected objects are
    parented to that object.
    
    If an object is parented under a different group and there is an object in
    that group with the same name then this command will rename the parented
    object.

    Example:
    ```python
        import maya.cmds as cmds
        # Create some objects
        cmds.circle( name='circle1' )
        cmds.move( 5, 0, 0 )
        cmds.group( n='group1' )
        cmds.move( -5, 0, 0 )
        cmds.group( em=True, n='group2' )
        # Move the circle under group2.
        # Note that the circle remains where it is.
        cmds.parent( 'circle1', 'group2' )
        # Let's try that again with the -relative flag. This time
        # the circle will move.
        cmds.undo()
        cmds.parent( 'circle1', 'group2', relative=True )
        # Create an instance of the circle using the parent command.
        # This makes circle1 a child of group1 and group2.
        cmds.undo()
        cmds.parent( 'circle1', 'group2', add=True )
        # Remove group1 as a parent of the circle
        cmds.parent( 'group1|circle1', removeObject=True )
        # Move the circle to the top of the hierarchy
        cmds.parent( 'group2|circle1', world=True )
        # Remove an instance of a shape from a parent
        cmds.parent('nurbsSphere3|nurbsSphereShape1',shape=True,rm=True)
    ```

    ---
    - Args:
        - [dagObject...] [dagObject]: Input item(s).
        - absolute (a): preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) If the object to parent is a joint, it will alter the translation and joint orientation of the joint
            to preserve the world object transformation if this suffices. Otherwise, a transform will be inserted between the joint and the parent for this purpose. In this case, the transformation inside the joint is not altered. [default]
        - addObject (add): preserve existing local object transformations but don't reparent, just add the object(s) under the parent. Use -world to add the world as a parent of the given objects.
        - noConnections (nc): The parent command will normally generate new instanced set connections when adding instances. (ie. make a connection to the shading engine for new instances) This flag suppresses this behaviour and is primarily used by the file format.
        - noInvScale (nis): The parent command will normally connect inverseScale to its parent scale on joints. This is used to compensate scale on joint. The connection of inverseScale will occur if both child and parent are joints and no connection is present on
            child's inverseScale. In case of a reparenting, the old inverseScale will only get broken if the old parent is a joint. Otherwise connection will remain intact. This flag suppresses this behaviour.
        - relative (r): preserve existing local object transformations (relative to the parent node)
        - removeObject (rm): Remove the immediate parent of every object specified. To remove only a single instance of a shape from a parent, the path to the shape should be specified. Note: if there is a single parent then the object is effectively deleted from the
            scene. Use -world to remove the world as a parent of the given object.
        - shape (s): The parent command usually only operates on transforms.  Using this flags allows a shape that is specified to be directly parented under the given transform.  This is used to instance a shape node. (ie. "parent -add -shape"    is equivalent
            to the "instance" command). This flag is primarily used by the file format.
        - world (w): unparent given object(s) (parent to world)
    """
@overload #Overload for parent in ['create']
def parent([dagObject...] [dagObject]: [dagObject...] [dagObject], a: bool = ..., add: bool = ..., nc: bool = ..., nis: bool = ..., r: bool = ..., rm: bool = ..., s: bool = ..., w: bool = ...) -> list[str]:
    """parent is undoable, NOT queryable, and NOT editable.
    
    This command parents (moves) objects under a new group, removes objects from
    an existing group, or adds/removes parents.
    
    If the -w flag is specified all the selected or specified objects are parented
    to the world (unparented first).
    
    If the -rm flag is specified then all the selected or specified instances are
    removed.
    
    If there are more than two objects specified all the objects are parented to
    the last object specified.
    
    If the -add flag is specified, the objects are not reparented but also become
    children of the last object specified.
    
    If there is only a single object specified then the selected objects are
    parented to that object.
    
    If an object is parented under a different group and there is an object in
    that group with the same name then this command will rename the parented
    object.

    Example:
    ```python
        import maya.cmds as cmds
        # Create some objects
        cmds.circle( name='circle1' )
        cmds.move( 5, 0, 0 )
        cmds.group( n='group1' )
        cmds.move( -5, 0, 0 )
        cmds.group( em=True, n='group2' )
        # Move the circle under group2.
        # Note that the circle remains where it is.
        cmds.parent( 'circle1', 'group2' )
        # Let's try that again with the -relative flag. This time
        # the circle will move.
        cmds.undo()
        cmds.parent( 'circle1', 'group2', relative=True )
        # Create an instance of the circle using the parent command.
        # This makes circle1 a child of group1 and group2.
        cmds.undo()
        cmds.parent( 'circle1', 'group2', add=True )
        # Remove group1 as a parent of the circle
        cmds.parent( 'group1|circle1', removeObject=True )
        # Move the circle to the top of the hierarchy
        cmds.parent( 'group2|circle1', world=True )
        # Remove an instance of a shape from a parent
        cmds.parent('nurbsSphere3|nurbsSphereShape1',shape=True,rm=True)
    ```

    ---
    - Args:
        - [dagObject...] [dagObject]: Input item(s).
        - absolute (a): preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) If the object to parent is a joint, it will alter the translation and joint orientation of the joint
            to preserve the world object transformation if this suffices. Otherwise, a transform will be inserted between the joint and the parent for this purpose. In this case, the transformation inside the joint is not altered. [default]
        - addObject (add): preserve existing local object transformations but don't reparent, just add the object(s) under the parent. Use -world to add the world as a parent of the given objects.
        - noConnections (nc): The parent command will normally generate new instanced set connections when adding instances. (ie. make a connection to the shading engine for new instances) This flag suppresses this behaviour and is primarily used by the file format.
        - noInvScale (nis): The parent command will normally connect inverseScale to its parent scale on joints. This is used to compensate scale on joint. The connection of inverseScale will occur if both child and parent are joints and no connection is present on
            child's inverseScale. In case of a reparenting, the old inverseScale will only get broken if the old parent is a joint. Otherwise connection will remain intact. This flag suppresses this behaviour.
        - relative (r): preserve existing local object transformations (relative to the parent node)
        - removeObject (rm): Remove the immediate parent of every object specified. To remove only a single instance of a shape from a parent, the path to the shape should be specified. Note: if there is a single parent then the object is effectively deleted from the
            scene. Use -world to remove the world as a parent of the given object.
        - shape (s): The parent command usually only operates on transforms.  Using this flags allows a shape that is specified to be directly parented under the given transform.  This is used to instance a shape node. (ie. "parent -add -shape"    is equivalent
            to the "instance" command). This flag is primarily used by the file format.
        - world (w): unparent given object(s) (parent to world)
    """
@overload #Overload for parent in ['create']
def parent([dagObject...] [dagObject]: [dagObject...] [dagObject], absolute: bool = ..., a: bool = ..., addObject: bool = ..., add: bool = ..., noConnections: bool = ..., nc: bool = ..., noInvScale: bool = ..., nis: bool = ..., relative: bool = ..., r: bool = ..., removeObject: bool = ..., rm: bool = ..., shape: bool = ..., s: bool = ..., world: bool = ..., w: bool = ...) -> list[str]:
    """parent is undoable, NOT queryable, and NOT editable.
    
    This command parents (moves) objects under a new group, removes objects from
    an existing group, or adds/removes parents.
    
    If the -w flag is specified all the selected or specified objects are parented
    to the world (unparented first).
    
    If the -rm flag is specified then all the selected or specified instances are
    removed.
    
    If there are more than two objects specified all the objects are parented to
    the last object specified.
    
    If the -add flag is specified, the objects are not reparented but also become
    children of the last object specified.
    
    If there is only a single object specified then the selected objects are
    parented to that object.
    
    If an object is parented under a different group and there is an object in
    that group with the same name then this command will rename the parented
    object.

    Example:
    ```python
        import maya.cmds as cmds
        # Create some objects
        cmds.circle( name='circle1' )
        cmds.move( 5, 0, 0 )
        cmds.group( n='group1' )
        cmds.move( -5, 0, 0 )
        cmds.group( em=True, n='group2' )
        # Move the circle under group2.
        # Note that the circle remains where it is.
        cmds.parent( 'circle1', 'group2' )
        # Let's try that again with the -relative flag. This time
        # the circle will move.
        cmds.undo()
        cmds.parent( 'circle1', 'group2', relative=True )
        # Create an instance of the circle using the parent command.
        # This makes circle1 a child of group1 and group2.
        cmds.undo()
        cmds.parent( 'circle1', 'group2', add=True )
        # Remove group1 as a parent of the circle
        cmds.parent( 'group1|circle1', removeObject=True )
        # Move the circle to the top of the hierarchy
        cmds.parent( 'group2|circle1', world=True )
        # Remove an instance of a shape from a parent
        cmds.parent('nurbsSphere3|nurbsSphereShape1',shape=True,rm=True)
    ```

    ---
    - Args:
        - [dagObject...] [dagObject]: Input item(s).
        - absolute (a): preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) If the object to parent is a joint, it will alter the translation and joint orientation of the joint
            to preserve the world object transformation if this suffices. Otherwise, a transform will be inserted between the joint and the parent for this purpose. In this case, the transformation inside the joint is not altered. [default]
        - addObject (add): preserve existing local object transformations but don't reparent, just add the object(s) under the parent. Use -world to add the world as a parent of the given objects.
        - noConnections (nc): The parent command will normally generate new instanced set connections when adding instances. (ie. make a connection to the shading engine for new instances) This flag suppresses this behaviour and is primarily used by the file format.
        - noInvScale (nis): The parent command will normally connect inverseScale to its parent scale on joints. This is used to compensate scale on joint. The connection of inverseScale will occur if both child and parent are joints and no connection is present on
            child's inverseScale. In case of a reparenting, the old inverseScale will only get broken if the old parent is a joint. Otherwise connection will remain intact. This flag suppresses this behaviour.
        - relative (r): preserve existing local object transformations (relative to the parent node)
        - removeObject (rm): Remove the immediate parent of every object specified. To remove only a single instance of a shape from a parent, the path to the shape should be specified. Note: if there is a single parent then the object is effectively deleted from the
            scene. Use -world to remove the world as a parent of the given object.
        - shape (s): The parent command usually only operates on transforms.  Using this flags allows a shape that is specified to be directly parented under the given transform.  This is used to instance a shape node. (ie. "parent -add -shape"    is equivalent
            to the "instance" command). This flag is primarily used by the file format.
        - world (w): unparent given object(s) (parent to world)
    """
