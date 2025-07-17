"""Stub files for General category in Maya commands, command: instance."""

from typing import Any, overload

@overload #Overload for instance in ['create']
def instance([objects]: [objects], leaf: bool = ..., name: str = ..., smartTransform: bool = ...) -> str:
    """instance is undoable, NOT queryable, and NOT editable.
    
    Instancing is a way of making the same object appear twice in the scene. This
    is accomplished by creation of a new transform node that points to an
    exisiting object. Changes to the transform are independent but changes to the
    "instanced" object affect all instances since the node is shared.
    
    If no objects are given, then the selected list is instanced. When an object
    is instanced a new transform node is created that points to the selected
    object.
    
    The smart transform feature allows instance to transform newly instanced
    objects based on previous transformations between instances.
    
    Example: Instance an object and move it to a new location. Instance it again
    with the smart transform flag. It should have moved once again the distance
    you had previously moved it.
    
    Note: changing the selected list between smart instances will cause the
    transform information to be deleted.
    
    It returns a list of the new objects created by the instance operation.
    
    See also: duplicate

    Example:
    ```python
        import maya.cmds as cmds
        # Create a hierarchy
        cmds.sphere( n='sphere1' )
        cmds.move( 3, 0, 0 )
        cmds.sphere( n='sphere2' )
        cmds.move( -3, 0, 0 )
        cmds.group( 'sphere1', 'sphere2', n='group1' )
        cmds.group( 'group1', n='group2' )
        # Create an instance of one of the spheres
        cmds.instance( 'sphere1' )
        # Duplicate the hierarchy except for the shapes which are
        # instanced.instances of all leaf level shapes
        cmds.instance( 'group1', leaf=True )
        # Create a row of 4 instanced circles which are equally spaced
        cmds.circle( n='circle1' )
        cmds.instance()
        cmds.move( 3, 0, 0 )
        cmds.instance( smartTransform=True )
        cmds.instance( smartTransform=True )
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - leaf (lf): Instances leaf-level objects. Acts like duplicate except leaf-level objects are instanced.
        - name (n): Name to give new instance
        - smartTransform (st): Transforms instances item based on movements between transforms
    """
@overload #Overload for instance in ['create']
def instance([objects]: [objects], lf: bool = ..., n: str = ..., st: bool = ...) -> str:
    """instance is undoable, NOT queryable, and NOT editable.
    
    Instancing is a way of making the same object appear twice in the scene. This
    is accomplished by creation of a new transform node that points to an
    exisiting object. Changes to the transform are independent but changes to the
    "instanced" object affect all instances since the node is shared.
    
    If no objects are given, then the selected list is instanced. When an object
    is instanced a new transform node is created that points to the selected
    object.
    
    The smart transform feature allows instance to transform newly instanced
    objects based on previous transformations between instances.
    
    Example: Instance an object and move it to a new location. Instance it again
    with the smart transform flag. It should have moved once again the distance
    you had previously moved it.
    
    Note: changing the selected list between smart instances will cause the
    transform information to be deleted.
    
    It returns a list of the new objects created by the instance operation.
    
    See also: duplicate

    Example:
    ```python
        import maya.cmds as cmds
        # Create a hierarchy
        cmds.sphere( n='sphere1' )
        cmds.move( 3, 0, 0 )
        cmds.sphere( n='sphere2' )
        cmds.move( -3, 0, 0 )
        cmds.group( 'sphere1', 'sphere2', n='group1' )
        cmds.group( 'group1', n='group2' )
        # Create an instance of one of the spheres
        cmds.instance( 'sphere1' )
        # Duplicate the hierarchy except for the shapes which are
        # instanced.instances of all leaf level shapes
        cmds.instance( 'group1', leaf=True )
        # Create a row of 4 instanced circles which are equally spaced
        cmds.circle( n='circle1' )
        cmds.instance()
        cmds.move( 3, 0, 0 )
        cmds.instance( smartTransform=True )
        cmds.instance( smartTransform=True )
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - leaf (lf): Instances leaf-level objects. Acts like duplicate except leaf-level objects are instanced.
        - name (n): Name to give new instance
        - smartTransform (st): Transforms instances item based on movements between transforms
    """
@overload #Overload for instance in ['create']
def instance([objects]: [objects], leaf: bool = ..., lf: bool = ..., name: str = ..., n: str = ..., smartTransform: bool = ..., st: bool = ...) -> str:
    """instance is undoable, NOT queryable, and NOT editable.
    
    Instancing is a way of making the same object appear twice in the scene. This
    is accomplished by creation of a new transform node that points to an
    exisiting object. Changes to the transform are independent but changes to the
    "instanced" object affect all instances since the node is shared.
    
    If no objects are given, then the selected list is instanced. When an object
    is instanced a new transform node is created that points to the selected
    object.
    
    The smart transform feature allows instance to transform newly instanced
    objects based on previous transformations between instances.
    
    Example: Instance an object and move it to a new location. Instance it again
    with the smart transform flag. It should have moved once again the distance
    you had previously moved it.
    
    Note: changing the selected list between smart instances will cause the
    transform information to be deleted.
    
    It returns a list of the new objects created by the instance operation.
    
    See also: duplicate

    Example:
    ```python
        import maya.cmds as cmds
        # Create a hierarchy
        cmds.sphere( n='sphere1' )
        cmds.move( 3, 0, 0 )
        cmds.sphere( n='sphere2' )
        cmds.move( -3, 0, 0 )
        cmds.group( 'sphere1', 'sphere2', n='group1' )
        cmds.group( 'group1', n='group2' )
        # Create an instance of one of the spheres
        cmds.instance( 'sphere1' )
        # Duplicate the hierarchy except for the shapes which are
        # instanced.instances of all leaf level shapes
        cmds.instance( 'group1', leaf=True )
        # Create a row of 4 instanced circles which are equally spaced
        cmds.circle( n='circle1' )
        cmds.instance()
        cmds.move( 3, 0, 0 )
        cmds.instance( smartTransform=True )
        cmds.instance( smartTransform=True )
    ```

    ---
    - Args:
        - [objects]: Input item(s).
        - leaf (lf): Instances leaf-level objects. Acts like duplicate except leaf-level objects are instanced.
        - name (n): Name to give new instance
        - smartTransform (st): Transforms instances item based on movements between transforms
    """
