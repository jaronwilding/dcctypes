"""Stub files for Attributes category in Maya commands, command: deleteExtension."""

from typing import Any, overload

@overload #Overload for deleteExtension in ['create']
def deleteExtension(attribute: str = ..., forceDelete: bool = ..., nodeType: str = ...) -> int:
    """deleteExtension is NOT undoable, NOT queryable, and NOT editable.
    
    This command is used to delete an extension attribute from a node type. The
    attribute can be specified by using either the long or short name. Only one
    extension attribute can be deleted at a time. Children of a compound attribute
    cannot be deleted, you must delete the complete compound attribute. This
    command has no undo, edit, or query capabilities.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.addExtension( nodeType='planet', longName='martians', shortName='mr', attributeType='double' )
        cmds.createNode( 'planet', name='jupiter' )
        cmds.createNode( 'planet', name='mars' )
        cmds.setAttr( 'mars.mr', 35 )
        # Delete an extension attribute named mr/martians.
        # Only returns 1 since the planet node 'jupiter'
        # does not have a non-default value on the extension.
        cmds.deleteExtension( nodeType='planet', forceDelete=True, attribute='martians' )
        # Return: 1 //
        # The attribute is gone since it was forced out
        cmds.attributeQuery( type='planet', attribute='mr', query=True, exists=True )
        # Return: 0 //
        # Re-add and delete the extension again, forcing the
        # attribute to remain if non-default values exist.
        cmds.addExtension( nodeType='planet', longName='martians', shortName='mr', attributeType='double' )
        cmds.setAttr( 'mars.mr', 35 )
        cmds.deleteExtension( nodeType='planet', forceDelete=False, attribute='mr' )
        # Return: 0 //
        # The attribute still exists since it had some non-default values
        cmds.attributeQuery( type='planet', attribute='mr', query=True, exists=True )
        # Return: 1 //
        cmds.attributeQuery( name='jupiter', attribute='mr', query=True, exists=True )
        # Return: 1 //
    ```

    ---
    - Args:
        - attribute (at): Specify either the long or short name of the attribute.
        - forceDelete (fd): If this flag is set and turned ON then data values for the extension attributes are all deleted without confirmation. If it's set and turned OFF then any extension attributes that have non-default values set on any node will remain in
            place. If this flag is not set at all then the user will be asked if they wish to preserve non-default values on this attribute.
        - nodeType (nt): The name of the node type.
    """
@overload #Overload for deleteExtension in ['create']
def deleteExtension(at: str = ..., fd: bool = ..., nt: str = ...) -> int:
    """deleteExtension is NOT undoable, NOT queryable, and NOT editable.
    
    This command is used to delete an extension attribute from a node type. The
    attribute can be specified by using either the long or short name. Only one
    extension attribute can be deleted at a time. Children of a compound attribute
    cannot be deleted, you must delete the complete compound attribute. This
    command has no undo, edit, or query capabilities.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.addExtension( nodeType='planet', longName='martians', shortName='mr', attributeType='double' )
        cmds.createNode( 'planet', name='jupiter' )
        cmds.createNode( 'planet', name='mars' )
        cmds.setAttr( 'mars.mr', 35 )
        # Delete an extension attribute named mr/martians.
        # Only returns 1 since the planet node 'jupiter'
        # does not have a non-default value on the extension.
        cmds.deleteExtension( nodeType='planet', forceDelete=True, attribute='martians' )
        # Return: 1 //
        # The attribute is gone since it was forced out
        cmds.attributeQuery( type='planet', attribute='mr', query=True, exists=True )
        # Return: 0 //
        # Re-add and delete the extension again, forcing the
        # attribute to remain if non-default values exist.
        cmds.addExtension( nodeType='planet', longName='martians', shortName='mr', attributeType='double' )
        cmds.setAttr( 'mars.mr', 35 )
        cmds.deleteExtension( nodeType='planet', forceDelete=False, attribute='mr' )
        # Return: 0 //
        # The attribute still exists since it had some non-default values
        cmds.attributeQuery( type='planet', attribute='mr', query=True, exists=True )
        # Return: 1 //
        cmds.attributeQuery( name='jupiter', attribute='mr', query=True, exists=True )
        # Return: 1 //
    ```

    ---
    - Args:
        - attribute (at): Specify either the long or short name of the attribute.
        - forceDelete (fd): If this flag is set and turned ON then data values for the extension attributes are all deleted without confirmation. If it's set and turned OFF then any extension attributes that have non-default values set on any node will remain in
            place. If this flag is not set at all then the user will be asked if they wish to preserve non-default values on this attribute.
        - nodeType (nt): The name of the node type.
    """
@overload #Overload for deleteExtension in ['create']
def deleteExtension(attribute: str = ..., at: str = ..., forceDelete: bool = ..., fd: bool = ..., nodeType: str = ..., nt: str = ...) -> int:
    """deleteExtension is NOT undoable, NOT queryable, and NOT editable.
    
    This command is used to delete an extension attribute from a node type. The
    attribute can be specified by using either the long or short name. Only one
    extension attribute can be deleted at a time. Children of a compound attribute
    cannot be deleted, you must delete the complete compound attribute. This
    command has no undo, edit, or query capabilities.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.addExtension( nodeType='planet', longName='martians', shortName='mr', attributeType='double' )
        cmds.createNode( 'planet', name='jupiter' )
        cmds.createNode( 'planet', name='mars' )
        cmds.setAttr( 'mars.mr', 35 )
        # Delete an extension attribute named mr/martians.
        # Only returns 1 since the planet node 'jupiter'
        # does not have a non-default value on the extension.
        cmds.deleteExtension( nodeType='planet', forceDelete=True, attribute='martians' )
        # Return: 1 //
        # The attribute is gone since it was forced out
        cmds.attributeQuery( type='planet', attribute='mr', query=True, exists=True )
        # Return: 0 //
        # Re-add and delete the extension again, forcing the
        # attribute to remain if non-default values exist.
        cmds.addExtension( nodeType='planet', longName='martians', shortName='mr', attributeType='double' )
        cmds.setAttr( 'mars.mr', 35 )
        cmds.deleteExtension( nodeType='planet', forceDelete=False, attribute='mr' )
        # Return: 0 //
        # The attribute still exists since it had some non-default values
        cmds.attributeQuery( type='planet', attribute='mr', query=True, exists=True )
        # Return: 1 //
        cmds.attributeQuery( name='jupiter', attribute='mr', query=True, exists=True )
        # Return: 1 //
    ```

    ---
    - Args:
        - attribute (at): Specify either the long or short name of the attribute.
        - forceDelete (fd): If this flag is set and turned ON then data values for the extension attributes are all deleted without confirmation. If it's set and turned OFF then any extension attributes that have non-default values set on any node will remain in
            place. If this flag is not set at all then the user will be asked if they wish to preserve non-default values on this attribute.
        - nodeType (nt): The name of the node type.
    """
