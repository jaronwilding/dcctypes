"""Stub files for Attributes category in Maya commands, command: disconnectAttr."""

from typing import Any, overload

@overload #Overload for disconnectAttr in ['create']
def disconnectAttr(attribute attribute: attribute attribute, nextAvailable: bool = ...) -> str:
    """disconnectAttr is undoable, NOT queryable, and NOT editable.
    
    Disconnects two connected attributes. First argument is the source attribute,
    second is the destination.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a sphere and cone and connect their rotate attribute.
        #
        sph = cmds.sphere()
        con = cmds.cone()
        sphereR = '%s.r' % sph[0]
        coneR = '%s.r' % con[0]
        cmds.connectAttr(sphereR, coneR)
        #    Break the connection between the rotate attributes.
        #
        cmds.disconnectAttr(sphereR, coneR)
    ```

    ---
    - Args:
        - attribute attribute: Input item(s).
        - nextAvailable (na): If the destination multi-attribute has set the indexMatters to be false, the command will disconnect the first matching connection.  No index needs to be specified.
    """
@overload #Overload for disconnectAttr in ['create']
def disconnectAttr(attribute attribute: attribute attribute, na: bool = ...) -> str:
    """disconnectAttr is undoable, NOT queryable, and NOT editable.
    
    Disconnects two connected attributes. First argument is the source attribute,
    second is the destination.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a sphere and cone and connect their rotate attribute.
        #
        sph = cmds.sphere()
        con = cmds.cone()
        sphereR = '%s.r' % sph[0]
        coneR = '%s.r' % con[0]
        cmds.connectAttr(sphereR, coneR)
        #    Break the connection between the rotate attributes.
        #
        cmds.disconnectAttr(sphereR, coneR)
    ```

    ---
    - Args:
        - attribute attribute: Input item(s).
        - nextAvailable (na): If the destination multi-attribute has set the indexMatters to be false, the command will disconnect the first matching connection.  No index needs to be specified.
    """
@overload #Overload for disconnectAttr in ['create']
def disconnectAttr(attribute attribute: attribute attribute, nextAvailable: bool = ..., na: bool = ...) -> str:
    """disconnectAttr is undoable, NOT queryable, and NOT editable.
    
    Disconnects two connected attributes. First argument is the source attribute,
    second is the destination.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a sphere and cone and connect their rotate attribute.
        #
        sph = cmds.sphere()
        con = cmds.cone()
        sphereR = '%s.r' % sph[0]
        coneR = '%s.r' % con[0]
        cmds.connectAttr(sphereR, coneR)
        #    Break the connection between the rotate attributes.
        #
        cmds.disconnectAttr(sphereR, coneR)
    ```

    ---
    - Args:
        - attribute attribute: Input item(s).
        - nextAvailable (na): If the destination multi-attribute has set the indexMatters to be false, the command will disconnect the first matching connection.  No index needs to be specified.
    """
