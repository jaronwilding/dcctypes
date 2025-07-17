"""Stub files for General category in Maya commands, command: lockNode."""

from typing import Any, overload

@overload #Overload for lockNode in ['create']
def lockNode(ignoreComponents: bool = ..., lock: bool = ..., lockName: bool = ..., lockUnpublished: bool = ...) -> boolean[]:
    """lockNode is undoable, queryable, and NOT editable.
    
    Locks or unlocks one or more dependency nodes. A locked node is restricted in
    the following ways:
    
    * It may not be deleted.
    * It may not be renamed.
    * Its parenting may not be changed.
    * Attributes may not be added to or removed from it.
    * Locked attributes may not be unlocked.
    * Unlocked attributes may not be locked.
    
    Note that an unlocked attribute of a locked node may still have its value set,
    or connections to it made or broken. For more information on attribute
    locking, see the setAttr command.
    
    If no node names are specified then the current selection list is used.
    
    There are a few special behaviors when locking containers. Containers are
    automatically expanded to their constituent objects. When a container is
    locked, members of the container may not be unlocked and the container
    membership may not be modified. Containers may also be set to lock unpublished
    attributes. When in this state, unpublished member attributes may not have
    existing connections broken, new connections cannot be made, and values on
    unconnected attributes may not be modified. Parenting is allowed to change on
    members of locked containers that have been published as parent or child
    anchors.

    Example:
    ```python
        import maya.cmds as cmds
        # create a sphere, lock it, then try to delete it.
        cmds.sphere( n='sphere1' )
        cmds.lockNode( 'sphere1' )
        cmds.delete( 'sphere1' )
        # Error: Cannot delete locked nodes.
        # Unlock the sphere, then it can be deleted.
        cmds.lockNode( 'sphere1', lock=False )
        cmds.delete( 'sphere1' )
    ```

    ---
    - Args:
        - ignoreComponents (ic): Normally, the presence of a component in the list of objects to be locked will cause the command to fail with an error. But if this flag is supplied then components will be silently ignored.
        - lock (l): Specifies the new lock state for the node. The default is true.
        - lockName (ln): Specifies the new lock state for the node's name.
        - lockUnpublished (lu): Used in conjunction with the lock flag. On a container, lock or unlock all unpublished attributes on the members of the container. For non-containers, lock or unlock unpublished attributes on the specified node.
    """
@overload #Overload for lockNode in ['create']
def lockNode(ic: bool = ..., l: bool = ..., ln: bool = ..., lu: bool = ...) -> boolean[]:
    """lockNode is undoable, queryable, and NOT editable.
    
    Locks or unlocks one or more dependency nodes. A locked node is restricted in
    the following ways:
    
    * It may not be deleted.
    * It may not be renamed.
    * Its parenting may not be changed.
    * Attributes may not be added to or removed from it.
    * Locked attributes may not be unlocked.
    * Unlocked attributes may not be locked.
    
    Note that an unlocked attribute of a locked node may still have its value set,
    or connections to it made or broken. For more information on attribute
    locking, see the setAttr command.
    
    If no node names are specified then the current selection list is used.
    
    There are a few special behaviors when locking containers. Containers are
    automatically expanded to their constituent objects. When a container is
    locked, members of the container may not be unlocked and the container
    membership may not be modified. Containers may also be set to lock unpublished
    attributes. When in this state, unpublished member attributes may not have
    existing connections broken, new connections cannot be made, and values on
    unconnected attributes may not be modified. Parenting is allowed to change on
    members of locked containers that have been published as parent or child
    anchors.

    Example:
    ```python
        import maya.cmds as cmds
        # create a sphere, lock it, then try to delete it.
        cmds.sphere( n='sphere1' )
        cmds.lockNode( 'sphere1' )
        cmds.delete( 'sphere1' )
        # Error: Cannot delete locked nodes.
        # Unlock the sphere, then it can be deleted.
        cmds.lockNode( 'sphere1', lock=False )
        cmds.delete( 'sphere1' )
    ```

    ---
    - Args:
        - ignoreComponents (ic): Normally, the presence of a component in the list of objects to be locked will cause the command to fail with an error. But if this flag is supplied then components will be silently ignored.
        - lock (l): Specifies the new lock state for the node. The default is true.
        - lockName (ln): Specifies the new lock state for the node's name.
        - lockUnpublished (lu): Used in conjunction with the lock flag. On a container, lock or unlock all unpublished attributes on the members of the container. For non-containers, lock or unlock unpublished attributes on the specified node.
    """
@overload #Overload for lockNode in ['create']
def lockNode(ignoreComponents: bool = ..., ic: bool = ..., lock: bool = ..., l: bool = ..., lockName: bool = ..., ln: bool = ..., lockUnpublished: bool = ..., lu: bool = ...) -> boolean[]:
    """lockNode is undoable, queryable, and NOT editable.
    
    Locks or unlocks one or more dependency nodes. A locked node is restricted in
    the following ways:
    
    * It may not be deleted.
    * It may not be renamed.
    * Its parenting may not be changed.
    * Attributes may not be added to or removed from it.
    * Locked attributes may not be unlocked.
    * Unlocked attributes may not be locked.
    
    Note that an unlocked attribute of a locked node may still have its value set,
    or connections to it made or broken. For more information on attribute
    locking, see the setAttr command.
    
    If no node names are specified then the current selection list is used.
    
    There are a few special behaviors when locking containers. Containers are
    automatically expanded to their constituent objects. When a container is
    locked, members of the container may not be unlocked and the container
    membership may not be modified. Containers may also be set to lock unpublished
    attributes. When in this state, unpublished member attributes may not have
    existing connections broken, new connections cannot be made, and values on
    unconnected attributes may not be modified. Parenting is allowed to change on
    members of locked containers that have been published as parent or child
    anchors.

    Example:
    ```python
        import maya.cmds as cmds
        # create a sphere, lock it, then try to delete it.
        cmds.sphere( n='sphere1' )
        cmds.lockNode( 'sphere1' )
        cmds.delete( 'sphere1' )
        # Error: Cannot delete locked nodes.
        # Unlock the sphere, then it can be deleted.
        cmds.lockNode( 'sphere1', lock=False )
        cmds.delete( 'sphere1' )
    ```

    ---
    - Args:
        - ignoreComponents (ic): Normally, the presence of a component in the list of objects to be locked will cause the command to fail with an error. But if this flag is supplied then components will be silently ignored.
        - lock (l): Specifies the new lock state for the node. The default is true.
        - lockName (ln): Specifies the new lock state for the node's name.
        - lockUnpublished (lu): Used in conjunction with the lock flag. On a container, lock or unlock all unpublished attributes on the members of the container. For non-containers, lock or unlock unpublished attributes on the specified node.
    """
@overload #Overload for lockNode in ['query']
def lockNode(ignoreComponents: bool = ..., lock: bool = ..., lockName: bool = ..., lockUnpublished: bool = ..., query: bool = ...) -> boolean[]:
    """lockNode is undoable, queryable, and NOT editable.
    
    Locks or unlocks one or more dependency nodes. A locked node is restricted in
    the following ways:
    
    * It may not be deleted.
    * It may not be renamed.
    * Its parenting may not be changed.
    * Attributes may not be added to or removed from it.
    * Locked attributes may not be unlocked.
    * Unlocked attributes may not be locked.
    
    Note that an unlocked attribute of a locked node may still have its value set,
    or connections to it made or broken. For more information on attribute
    locking, see the setAttr command.
    
    If no node names are specified then the current selection list is used.
    
    There are a few special behaviors when locking containers. Containers are
    automatically expanded to their constituent objects. When a container is
    locked, members of the container may not be unlocked and the container
    membership may not be modified. Containers may also be set to lock unpublished
    attributes. When in this state, unpublished member attributes may not have
    existing connections broken, new connections cannot be made, and values on
    unconnected attributes may not be modified. Parenting is allowed to change on
    members of locked containers that have been published as parent or child
    anchors.

    Example:
    ```python
        import maya.cmds as cmds
        # create a sphere, lock it, then try to delete it.
        cmds.sphere( n='sphere1' )
        cmds.lockNode( 'sphere1' )
        cmds.delete( 'sphere1' )
        # Error: Cannot delete locked nodes.
        # Unlock the sphere, then it can be deleted.
        cmds.lockNode( 'sphere1', lock=False )
        cmds.delete( 'sphere1' )
    ```

    ---
    - Args:
        - ignoreComponents (ic): Normally, the presence of a component in the list of objects to be locked will cause the command to fail with an error. But if this flag is supplied then components will be silently ignored.
        - lock (l): Specifies the new lock state for the node. The default is true.
        - lockName (ln): Specifies the new lock state for the node's name.
        - lockUnpublished (lu): Used in conjunction with the lock flag. On a container, lock or unlock all unpublished attributes on the members of the container. For non-containers, lock or unlock unpublished attributes on the specified node.
        - query (q): Query mode flag
    """
@overload #Overload for lockNode in ['query']
def lockNode(ic: bool = ..., l: bool = ..., ln: bool = ..., lu: bool = ..., q: bool = ...) -> boolean[]:
    """lockNode is undoable, queryable, and NOT editable.
    
    Locks or unlocks one or more dependency nodes. A locked node is restricted in
    the following ways:
    
    * It may not be deleted.
    * It may not be renamed.
    * Its parenting may not be changed.
    * Attributes may not be added to or removed from it.
    * Locked attributes may not be unlocked.
    * Unlocked attributes may not be locked.
    
    Note that an unlocked attribute of a locked node may still have its value set,
    or connections to it made or broken. For more information on attribute
    locking, see the setAttr command.
    
    If no node names are specified then the current selection list is used.
    
    There are a few special behaviors when locking containers. Containers are
    automatically expanded to their constituent objects. When a container is
    locked, members of the container may not be unlocked and the container
    membership may not be modified. Containers may also be set to lock unpublished
    attributes. When in this state, unpublished member attributes may not have
    existing connections broken, new connections cannot be made, and values on
    unconnected attributes may not be modified. Parenting is allowed to change on
    members of locked containers that have been published as parent or child
    anchors.

    Example:
    ```python
        import maya.cmds as cmds
        # create a sphere, lock it, then try to delete it.
        cmds.sphere( n='sphere1' )
        cmds.lockNode( 'sphere1' )
        cmds.delete( 'sphere1' )
        # Error: Cannot delete locked nodes.
        # Unlock the sphere, then it can be deleted.
        cmds.lockNode( 'sphere1', lock=False )
        cmds.delete( 'sphere1' )
    ```

    ---
    - Args:
        - ignoreComponents (ic): Normally, the presence of a component in the list of objects to be locked will cause the command to fail with an error. But if this flag is supplied then components will be silently ignored.
        - lock (l): Specifies the new lock state for the node. The default is true.
        - lockName (ln): Specifies the new lock state for the node's name.
        - lockUnpublished (lu): Used in conjunction with the lock flag. On a container, lock or unlock all unpublished attributes on the members of the container. For non-containers, lock or unlock unpublished attributes on the specified node.
        - query (q): Query mode flag
    """
@overload #Overload for lockNode in ['query']
def lockNode(ignoreComponents: bool = ..., ic: bool = ..., lock: bool = ..., l: bool = ..., lockName: bool = ..., ln: bool = ..., lockUnpublished: bool = ..., lu: bool = ..., query: bool = ..., q: bool = ...) -> boolean[]:
    """lockNode is undoable, queryable, and NOT editable.
    
    Locks or unlocks one or more dependency nodes. A locked node is restricted in
    the following ways:
    
    * It may not be deleted.
    * It may not be renamed.
    * Its parenting may not be changed.
    * Attributes may not be added to or removed from it.
    * Locked attributes may not be unlocked.
    * Unlocked attributes may not be locked.
    
    Note that an unlocked attribute of a locked node may still have its value set,
    or connections to it made or broken. For more information on attribute
    locking, see the setAttr command.
    
    If no node names are specified then the current selection list is used.
    
    There are a few special behaviors when locking containers. Containers are
    automatically expanded to their constituent objects. When a container is
    locked, members of the container may not be unlocked and the container
    membership may not be modified. Containers may also be set to lock unpublished
    attributes. When in this state, unpublished member attributes may not have
    existing connections broken, new connections cannot be made, and values on
    unconnected attributes may not be modified. Parenting is allowed to change on
    members of locked containers that have been published as parent or child
    anchors.

    Example:
    ```python
        import maya.cmds as cmds
        # create a sphere, lock it, then try to delete it.
        cmds.sphere( n='sphere1' )
        cmds.lockNode( 'sphere1' )
        cmds.delete( 'sphere1' )
        # Error: Cannot delete locked nodes.
        # Unlock the sphere, then it can be deleted.
        cmds.lockNode( 'sphere1', lock=False )
        cmds.delete( 'sphere1' )
    ```

    ---
    - Args:
        - ignoreComponents (ic): Normally, the presence of a component in the list of objects to be locked will cause the command to fail with an error. But if this flag is supplied then components will be silently ignored.
        - lock (l): Specifies the new lock state for the node. The default is true.
        - lockName (ln): Specifies the new lock state for the node's name.
        - lockUnpublished (lu): Used in conjunction with the lock flag. On a container, lock or unlock all unpublished attributes on the members of the container. For non-containers, lock or unlock unpublished attributes on the specified node.
        - query (q): Query mode flag
    """
