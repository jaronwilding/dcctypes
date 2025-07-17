"""Stub files for Attributes category in Maya commands, command: aliasAttr."""

from typing import Any, overload

@overload  # Overload for aliasAttr in ['create']
def aliasAttr(*, remove: bool = ...) -> list[str]:
    """aliasAttr is undoable, queryable, and editable.

    Allows aliases (alternate names) to be defined for any attribute of a
    specified node. When an attribute is aliased, the alias will be used by the
    system to display information about the attribute. The user may, however,
    freely use either the alias or the original name of the attribute. Only a
    single alias can be specified for an attribute so setting an alias on an
    already-aliased attribute destroys the old alias.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'blendShape', n='blender' )
        #
        # Define intuitive names for the weights of a blendShape.
        # The blendShape command does this automatically to allow you
        # to refer to the weight corresponding to a target shape by the name
        # of that shape.
        #
        cmds.aliasAttr( 'smile', 'blender.w[0]', 'frown', 'blender.w[1]' )
        # Result: 2 #
        #
        # List all the attribute aliases for the node blendShape1
        #
        cmds.aliasAttr( 'blender', query=True )
        # Result: smile weight[0] frown weight[1] #
        #
        # Allow the X rotation on a joint to be called its "roll"
        #
        cmds.createNode( 'joint', n='elbow' )
        cmds.aliasAttr( 'roll', 'elbow.rx' )
        # Result: 1 #
        cmds.aliasAttr( 'tuck', 'elbow.ry' )
        # Result: 1 #
        #
        # Remove the roll alias defined above.
        #
        cmds.aliasAttr( 'elbow.roll', rm=True )
        #
        # Remove the tuck alias defined above.
        #
        cmds.aliasAttr( 'elbow.ry', rm=True )
    ```

    ---
    - Args:
        - remove (rm): Specifies that aliases listed should be removed (otherwise new aliases are added).
    """

@overload  # Overload for aliasAttr in ['create']
def aliasAttr(*, rm: bool = ...) -> list[str]:
    """aliasAttr is undoable, queryable, and editable.

    Allows aliases (alternate names) to be defined for any attribute of a
    specified node. When an attribute is aliased, the alias will be used by the
    system to display information about the attribute. The user may, however,
    freely use either the alias or the original name of the attribute. Only a
    single alias can be specified for an attribute so setting an alias on an
    already-aliased attribute destroys the old alias.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'blendShape', n='blender' )
        #
        # Define intuitive names for the weights of a blendShape.
        # The blendShape command does this automatically to allow you
        # to refer to the weight corresponding to a target shape by the name
        # of that shape.
        #
        cmds.aliasAttr( 'smile', 'blender.w[0]', 'frown', 'blender.w[1]' )
        # Result: 2 #
        #
        # List all the attribute aliases for the node blendShape1
        #
        cmds.aliasAttr( 'blender', query=True )
        # Result: smile weight[0] frown weight[1] #
        #
        # Allow the X rotation on a joint to be called its "roll"
        #
        cmds.createNode( 'joint', n='elbow' )
        cmds.aliasAttr( 'roll', 'elbow.rx' )
        # Result: 1 #
        cmds.aliasAttr( 'tuck', 'elbow.ry' )
        # Result: 1 #
        #
        # Remove the roll alias defined above.
        #
        cmds.aliasAttr( 'elbow.roll', rm=True )
        #
        # Remove the tuck alias defined above.
        #
        cmds.aliasAttr( 'elbow.ry', rm=True )
    ```

    ---
    - Args:
        - remove (rm): Specifies that aliases listed should be removed (otherwise new aliases are added).
    """

@overload  # Overload for aliasAttr in ['create']
def aliasAttr(*, remove: bool = ..., rm: bool = ...) -> list[str]:
    """aliasAttr is undoable, queryable, and editable.

    Allows aliases (alternate names) to be defined for any attribute of a
    specified node. When an attribute is aliased, the alias will be used by the
    system to display information about the attribute. The user may, however,
    freely use either the alias or the original name of the attribute. Only a
    single alias can be specified for an attribute so setting an alias on an
    already-aliased attribute destroys the old alias.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.createNode( 'blendShape', n='blender' )
        #
        # Define intuitive names for the weights of a blendShape.
        # The blendShape command does this automatically to allow you
        # to refer to the weight corresponding to a target shape by the name
        # of that shape.
        #
        cmds.aliasAttr( 'smile', 'blender.w[0]', 'frown', 'blender.w[1]' )
        # Result: 2 #
        #
        # List all the attribute aliases for the node blendShape1
        #
        cmds.aliasAttr( 'blender', query=True )
        # Result: smile weight[0] frown weight[1] #
        #
        # Allow the X rotation on a joint to be called its "roll"
        #
        cmds.createNode( 'joint', n='elbow' )
        cmds.aliasAttr( 'roll', 'elbow.rx' )
        # Result: 1 #
        cmds.aliasAttr( 'tuck', 'elbow.ry' )
        # Result: 1 #
        #
        # Remove the roll alias defined above.
        #
        cmds.aliasAttr( 'elbow.roll', rm=True )
        #
        # Remove the tuck alias defined above.
        #
        cmds.aliasAttr( 'elbow.ry', rm=True )
    ```

    ---
    - Args:
        - remove (rm): Specifies that aliases listed should be removed (otherwise new aliases are added).
    """
