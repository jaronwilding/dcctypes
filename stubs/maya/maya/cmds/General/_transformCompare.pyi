"""Stub files for General category in Maya commands, command: transformCompare."""

from typing import Any, overload

@overload #Overload for transformCompare in ['create']
def transformCompare([dagObject dagObject]: [dagObject dagObject], root: bool = ...) -> int:
    """transformCompare is undoable, NOT queryable, and NOT editable.
    
    Compares two transforms passed as arguments. If they are the same, returns 0.
    If they are different, returns 1. If no transforms are specified in the
    command line, then the transforms from the active list are used.

    Example:
    ```python
        import maya.cmds as cmds
        # Create some joints
        #
        cmds.select( d=True )
        cmds.joint( p=(-3.226531, 0, -4.866136) )
        cmds.joint( p=(2.817897, 0, -4.016915) )
        cmds.joint( 'joint1', e=True, zso=True, oj='xyz', sao='yup' )
        # Compare 2 different joints, a 1 will be returned
        #
        cmds.select( 'joint1', 'joint2', r=True )
        cmds.transformCompare()
        # Duplicate joint1 and compare the duplicate
        #
        cmds.select( 'joint1', r=True )
        cmds.duplicate()
        cmds.select( cl=True )
        cmds.select( 'joint1', 'joint3', r=True )
        cmds.transformCompare()
    ```

    ---
    - Args:
        - [dagObject dagObject]: Input item(s).
        - root (r): Compare the root only, rather than the entire hierarchy below the roots.
    """
@overload #Overload for transformCompare in ['create']
def transformCompare([dagObject dagObject]: [dagObject dagObject], r: bool = ...) -> int:
    """transformCompare is undoable, NOT queryable, and NOT editable.
    
    Compares two transforms passed as arguments. If they are the same, returns 0.
    If they are different, returns 1. If no transforms are specified in the
    command line, then the transforms from the active list are used.

    Example:
    ```python
        import maya.cmds as cmds
        # Create some joints
        #
        cmds.select( d=True )
        cmds.joint( p=(-3.226531, 0, -4.866136) )
        cmds.joint( p=(2.817897, 0, -4.016915) )
        cmds.joint( 'joint1', e=True, zso=True, oj='xyz', sao='yup' )
        # Compare 2 different joints, a 1 will be returned
        #
        cmds.select( 'joint1', 'joint2', r=True )
        cmds.transformCompare()
        # Duplicate joint1 and compare the duplicate
        #
        cmds.select( 'joint1', r=True )
        cmds.duplicate()
        cmds.select( cl=True )
        cmds.select( 'joint1', 'joint3', r=True )
        cmds.transformCompare()
    ```

    ---
    - Args:
        - [dagObject dagObject]: Input item(s).
        - root (r): Compare the root only, rather than the entire hierarchy below the roots.
    """
@overload #Overload for transformCompare in ['create']
def transformCompare([dagObject dagObject]: [dagObject dagObject], root: bool = ..., r: bool = ...) -> int:
    """transformCompare is undoable, NOT queryable, and NOT editable.
    
    Compares two transforms passed as arguments. If they are the same, returns 0.
    If they are different, returns 1. If no transforms are specified in the
    command line, then the transforms from the active list are used.

    Example:
    ```python
        import maya.cmds as cmds
        # Create some joints
        #
        cmds.select( d=True )
        cmds.joint( p=(-3.226531, 0, -4.866136) )
        cmds.joint( p=(2.817897, 0, -4.016915) )
        cmds.joint( 'joint1', e=True, zso=True, oj='xyz', sao='yup' )
        # Compare 2 different joints, a 1 will be returned
        #
        cmds.select( 'joint1', 'joint2', r=True )
        cmds.transformCompare()
        # Duplicate joint1 and compare the duplicate
        #
        cmds.select( 'joint1', r=True )
        cmds.duplicate()
        cmds.select( cl=True )
        cmds.select( 'joint1', 'joint3', r=True )
        cmds.transformCompare()
    ```

    ---
    - Args:
        - [dagObject dagObject]: Input item(s).
        - root (r): Compare the root only, rather than the entire hierarchy below the roots.
    """
