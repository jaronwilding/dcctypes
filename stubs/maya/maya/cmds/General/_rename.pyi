"""Stub files for General category in Maya commands, command: rename."""

from typing import Any, overload

@overload #Overload for rename in ['create']
def rename([object] string: [object] string, ignoreShape: bool = ..., uuid: bool = ...) -> str:
    """rename is undoable, NOT queryable, and NOT editable.
    
    Renames the given object to have the new name. If only one argument is
    supplied the command will rename the (first) selected object. If the new name
    conflicts with an existing name, the object will be given a unique name based
    on the supplied name. It is not legal to rename an object to the empty string.
    
    When a transform is renamed then any shape nodes beneath the transform that
    have the same prefix as the old transform name are renamed. For example,
    "rename nurbsSphere1 ball" would rename "nurbsSphere1|nurbsSphereShape1" to
    "ball|ballShape".
    
    If the new name ends in a single '#' then the rename command will replace the
    trailing '#' with a number that ensures the new name is unique.
    
    ## Notes
    
    If the name has an absolute namespace part, it will be considered. Namespaces
    that do not exist will be created automatically as needed. If the name has a
    relative namespace part, it will be ignored. In that case, the object will be
    put under the current namespace. (see example below).

    Example:
    ```python
        import maya.cmds as cmds
        # create two namespaces under the root namespace and create
        # a sphere under the root namespace and a sphere under one
        # of the new namespaces.
        cmds.namespace( set=':' )
        cmds.sphere( n='sphere1' )
        cmds.namespace( add='nsA' )
        cmds.namespace( add='nsB' )
        cmds.namespace( set='nsA' )
        cmds.sphere( n='sphere2' )
        cmds.namespace( set=':' )
        # change name of sphere1
        cmds.rename('sphere1', 'spinning_ball')
        # change name of spinning_ball back to sphere1
        cmds.select( 'spinning_ball', r=True )
        cmds.rename( 'sphere1' )
        # move sphere2 to namespace nsB
        cmds.rename( 'nsA:sphere2', 'nsB:sphere2' )
        # Result: nsB:sphere2 #
        # move sphere2 back to namespace nsA when not in the root namespace
        # Note the ":" appearing in front of the new name to indicate
        # we want to move the object to namespace nsA under the root namespace.
        cmds.namespace( set='nsB' )
        cmds.rename( 'nsB:sphere2', ':nsA:sphere2' )
        # Result: nsA:sphere2 #
        # Let's try this without the leading ":" in the new name.
        # Since we are namespace nsA, in affect, what we are trying to do
        # is rename :nsB:sphere2 to :nsA:nsB:sphere3. Since there isn't a
        # nsB namespace under the namespace nsA, the namespace specification
        # on new name is ignored and a warning is issued.
        cmds.namespace( set=':nsA' )
        cmds.rename( 'nsA:sphere2', 'nsB:sphere3' )
        # Warning: Removing invalid characters from name. #
        # Result: nsA:sphere3 #
        # rename an object when not in the root namespace
        # and move the object to current namespace
        cmds.namespace( set=':nsB' )
        cmds.rename( 'nsA:sphere3', 'sphere4' )
        # Result: nsB:sphere4 #
        # rename an object with an absolute name to move it into a new namespace.
        # The namespace does not exist so will be created.
        cmds.namespace( set=':nsB' )
        cmds.rename( 'nsA:sphere3', ':nsC:sphere4' )
        # Result: nsC:sphere4 #
    ```

    ---
    - Args:
        - [object] string: Input item(s).
        - ignoreShape: Indicates that renaming of shape nodes below transform nodes should be prevented.
        - uuid (uid): Indicates that the new name is actually a UUID, and that the command should change the node's UUID. (In which case its name remains unchanged.)
    """
@overload #Overload for rename in ['create']
def rename([object] string: [object] string, uid: bool = ...) -> str:
    """rename is undoable, NOT queryable, and NOT editable.
    
    Renames the given object to have the new name. If only one argument is
    supplied the command will rename the (first) selected object. If the new name
    conflicts with an existing name, the object will be given a unique name based
    on the supplied name. It is not legal to rename an object to the empty string.
    
    When a transform is renamed then any shape nodes beneath the transform that
    have the same prefix as the old transform name are renamed. For example,
    "rename nurbsSphere1 ball" would rename "nurbsSphere1|nurbsSphereShape1" to
    "ball|ballShape".
    
    If the new name ends in a single '#' then the rename command will replace the
    trailing '#' with a number that ensures the new name is unique.
    
    ## Notes
    
    If the name has an absolute namespace part, it will be considered. Namespaces
    that do not exist will be created automatically as needed. If the name has a
    relative namespace part, it will be ignored. In that case, the object will be
    put under the current namespace. (see example below).

    Example:
    ```python
        import maya.cmds as cmds
        # create two namespaces under the root namespace and create
        # a sphere under the root namespace and a sphere under one
        # of the new namespaces.
        cmds.namespace( set=':' )
        cmds.sphere( n='sphere1' )
        cmds.namespace( add='nsA' )
        cmds.namespace( add='nsB' )
        cmds.namespace( set='nsA' )
        cmds.sphere( n='sphere2' )
        cmds.namespace( set=':' )
        # change name of sphere1
        cmds.rename('sphere1', 'spinning_ball')
        # change name of spinning_ball back to sphere1
        cmds.select( 'spinning_ball', r=True )
        cmds.rename( 'sphere1' )
        # move sphere2 to namespace nsB
        cmds.rename( 'nsA:sphere2', 'nsB:sphere2' )
        # Result: nsB:sphere2 #
        # move sphere2 back to namespace nsA when not in the root namespace
        # Note the ":" appearing in front of the new name to indicate
        # we want to move the object to namespace nsA under the root namespace.
        cmds.namespace( set='nsB' )
        cmds.rename( 'nsB:sphere2', ':nsA:sphere2' )
        # Result: nsA:sphere2 #
        # Let's try this without the leading ":" in the new name.
        # Since we are namespace nsA, in affect, what we are trying to do
        # is rename :nsB:sphere2 to :nsA:nsB:sphere3. Since there isn't a
        # nsB namespace under the namespace nsA, the namespace specification
        # on new name is ignored and a warning is issued.
        cmds.namespace( set=':nsA' )
        cmds.rename( 'nsA:sphere2', 'nsB:sphere3' )
        # Warning: Removing invalid characters from name. #
        # Result: nsA:sphere3 #
        # rename an object when not in the root namespace
        # and move the object to current namespace
        cmds.namespace( set=':nsB' )
        cmds.rename( 'nsA:sphere3', 'sphere4' )
        # Result: nsB:sphere4 #
        # rename an object with an absolute name to move it into a new namespace.
        # The namespace does not exist so will be created.
        cmds.namespace( set=':nsB' )
        cmds.rename( 'nsA:sphere3', ':nsC:sphere4' )
        # Result: nsC:sphere4 #
    ```

    ---
    - Args:
        - [object] string: Input item(s).
        - ignoreShape: Indicates that renaming of shape nodes below transform nodes should be prevented.
        - uuid (uid): Indicates that the new name is actually a UUID, and that the command should change the node's UUID. (In which case its name remains unchanged.)
    """
@overload #Overload for rename in ['create']
def rename([object] string: [object] string, ignoreShape: bool = ..., uuid: bool = ..., uid: bool = ...) -> str:
    """rename is undoable, NOT queryable, and NOT editable.
    
    Renames the given object to have the new name. If only one argument is
    supplied the command will rename the (first) selected object. If the new name
    conflicts with an existing name, the object will be given a unique name based
    on the supplied name. It is not legal to rename an object to the empty string.
    
    When a transform is renamed then any shape nodes beneath the transform that
    have the same prefix as the old transform name are renamed. For example,
    "rename nurbsSphere1 ball" would rename "nurbsSphere1|nurbsSphereShape1" to
    "ball|ballShape".
    
    If the new name ends in a single '#' then the rename command will replace the
    trailing '#' with a number that ensures the new name is unique.
    
    ## Notes
    
    If the name has an absolute namespace part, it will be considered. Namespaces
    that do not exist will be created automatically as needed. If the name has a
    relative namespace part, it will be ignored. In that case, the object will be
    put under the current namespace. (see example below).

    Example:
    ```python
        import maya.cmds as cmds
        # create two namespaces under the root namespace and create
        # a sphere under the root namespace and a sphere under one
        # of the new namespaces.
        cmds.namespace( set=':' )
        cmds.sphere( n='sphere1' )
        cmds.namespace( add='nsA' )
        cmds.namespace( add='nsB' )
        cmds.namespace( set='nsA' )
        cmds.sphere( n='sphere2' )
        cmds.namespace( set=':' )
        # change name of sphere1
        cmds.rename('sphere1', 'spinning_ball')
        # change name of spinning_ball back to sphere1
        cmds.select( 'spinning_ball', r=True )
        cmds.rename( 'sphere1' )
        # move sphere2 to namespace nsB
        cmds.rename( 'nsA:sphere2', 'nsB:sphere2' )
        # Result: nsB:sphere2 #
        # move sphere2 back to namespace nsA when not in the root namespace
        # Note the ":" appearing in front of the new name to indicate
        # we want to move the object to namespace nsA under the root namespace.
        cmds.namespace( set='nsB' )
        cmds.rename( 'nsB:sphere2', ':nsA:sphere2' )
        # Result: nsA:sphere2 #
        # Let's try this without the leading ":" in the new name.
        # Since we are namespace nsA, in affect, what we are trying to do
        # is rename :nsB:sphere2 to :nsA:nsB:sphere3. Since there isn't a
        # nsB namespace under the namespace nsA, the namespace specification
        # on new name is ignored and a warning is issued.
        cmds.namespace( set=':nsA' )
        cmds.rename( 'nsA:sphere2', 'nsB:sphere3' )
        # Warning: Removing invalid characters from name. #
        # Result: nsA:sphere3 #
        # rename an object when not in the root namespace
        # and move the object to current namespace
        cmds.namespace( set=':nsB' )
        cmds.rename( 'nsA:sphere3', 'sphere4' )
        # Result: nsB:sphere4 #
        # rename an object with an absolute name to move it into a new namespace.
        # The namespace does not exist so will be created.
        cmds.namespace( set=':nsB' )
        cmds.rename( 'nsA:sphere3', ':nsC:sphere4' )
        # Result: nsC:sphere4 #
    ```

    ---
    - Args:
        - [object] string: Input item(s).
        - ignoreShape: Indicates that renaming of shape nodes below transform nodes should be prevented.
        - uuid (uid): Indicates that the new name is actually a UUID, and that the command should change the node's UUID. (In which case its name remains unchanged.)
    """
