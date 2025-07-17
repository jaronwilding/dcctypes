"""Stub files for Selection category in Maya commands, command: select."""

from typing import Any, overload

@overload #Overload for select in ['create']
def select([objects...]: [objects...], add: bool = ..., addFirst: bool = ..., all: bool = ..., allDagObjects: bool = ..., allDependencyNodes: bool = ..., clear: bool = ..., containerCentric: bool = ..., deselect: bool = ..., hierarchy: bool = ..., noExpand: bool = ..., replace: bool = ..., symmetry: bool = ..., symmetrySide: int = ..., toggle: bool = ..., visible: bool = ...) -> None:
    """select is undoable, NOT queryable, and NOT editable.
    
    This command is used to put objects onto or off of the active list. If none of
    the five flags [-add, -af, -r, -d, -tgl] are specified, the default is to
    replace the objects on the active list with the given list of objects.
    
    When selecting a set as in "select set1", the behaviour is for all the members
    of the set to become selected instead of the set itself. If you want to select
    a set, the "-ne/noExpand" flag must be used.
    
    With the advent of namespaces, selection by name may be confusing. To clarify,
    without a qualified namespace, name lookup is limited to objects in the root
    namespace ":". There are really two parts of a name: the namespace and the
    name itself which is unique within the namespace. If you want to select
    objects in a specific namespace, you need to include the namespace separator
    ":".
    
    For example, 'select -r "foo*"' is trying to look for an object with the "foo"
    prefix in the root namespace. It is not trying to look for all objects in the
    namespace with the "foo" prefix. If you want to select all objects in a
    namespace (foo), use 'select "foo:*"'.
    
    Note: When the application starts up, there are several dependency nodes
    created by the system which must exist. These objects are not deletable but
    are selectable. All objects (dag and dependency nodes) in the scene can be
    obtained using the "ls" command without any arguments. When using the "-all",
    "adn/allDependencyNodes" or "-ado/allDagObjects" flags, only the deletable
    objects are selected. The non deletable object can still be selected by
    explicitly specifying their name as in "select time1;".

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects and add them to a set
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sets( 'sphere1', 'sphere2', n='set1' )
        # select all dag objects and all dependency nodes
        cmds.select( all=True )
        # clear the active list
        cmds.select( clear=True )
        # select sphere2 only if it is visible
        cmds.select( 'sphere2', visible=True )
        # select a couple of objects regardless of visibilty
        cmds.select( 'sphere1', r=True )
        cmds.select( 'sphere2', add=True )
        # remove one of the spheres from the active list (using toggle)
        cmds.select( 'sphere1', tgl=True )
        # remove the other sphere from the active list
        cmds.select( 'sphere2', d=True )
        # the following selects all the members of set1
        cmds.select( 'set1' )
        # this selects set1 itself
        cmds.select( 'set1', ne=True )
        # Some examples selecting with namespaces:
        # create a namespace and an object in the namespace
        cmds.namespace( add='foo' )
        cmds.namespace( set='foo' )
        cmds.sphere( n='bar' )
        # 'select bar' will not select "bar" unless bar is in the
        # root namespace. You need to qualify the name with the
        # namespace (shown below).
        cmds.select( 'foo:bar' )
        # select all the objects in a namespace
        cmds.select( 'foo:*' )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - add: Indicates that the specified items should be added to the active list without removing existing items from the active list.
        - addFirst (af): Indicates that the specified items should be added to the front of the active list without removing existing items from the active list.
        - all: Indicates that all deletable root level dag objects and all deletable non-dag dependency nodes should be selected.
        - allDagObjects (ado): Indicates that all deletable root level dag objects should be selected.
        - allDependencyNodes (adn): Indicates that all deletable dependency nodes including all deletable dag objects should be selected.
        - clear (cl): Clears the active list.  This is more efficient than "select -d;".  Also "select -d;" will not remove sets from the active list unless the "-ne" flag is also specified.
        - containerCentric (cc): Specifies that the same selection rules as apply to selection in the main viewport will also be applied to the select command. In particular, if the specified objects are members of a black-boxed container and are not published as nodes,
            Maya will not select them. Instead, their first parent valid for selection will be selected.
        - deselect (d): Indicates that the specified items should be removed from the active list if they are on the active list.
        - hierarchy (hi): Indicates that all children, grandchildren, ... of the specified dag objects should also be selected.
        - noExpand (ne): Indicates that any set which is among the specified items should not be expanded to its list of members. This allows sets to be selected as opposed to the members of sets which is the default behaviour.
        - replace (r): Indicates that the specified items should replace the existing items on the active list.
        - symmetry (sym): Specifies that components should be selected symmetrically using the current symmetricModelling command settings. If symmetric modeling is not enabled then this flag has no effect.
        - symmetrySide (sys): Indicates that components involved in the current symmetry object should be selected, according to the supplied parameter. Valid values for the parameter are:-1 : Select components in the unsymmetrical region.0 : Select components on the
            symmetry seam.1 : Select components on side 1.2 : Select components on side 2. If symmetric modeling is not enabled then this flag has no effect. Note: currently only works for topological symmetry.
        - toggle (tgl): Indicates that those items on the given list which are on the active list should be removed from the active list and those items on the given list which are not on the active list should be added to the active list.
        - visible (vis): Indicates that of the specified items only those that are visible should be affected.
    """
@overload #Overload for select in ['create']
def select([objects...]: [objects...], af: bool = ..., ado: bool = ..., adn: bool = ..., cl: bool = ..., cc: bool = ..., d: bool = ..., hi: bool = ..., ne: bool = ..., r: bool = ..., sym: bool = ..., sys: int = ..., tgl: bool = ..., vis: bool = ...) -> None:
    """select is undoable, NOT queryable, and NOT editable.
    
    This command is used to put objects onto or off of the active list. If none of
    the five flags [-add, -af, -r, -d, -tgl] are specified, the default is to
    replace the objects on the active list with the given list of objects.
    
    When selecting a set as in "select set1", the behaviour is for all the members
    of the set to become selected instead of the set itself. If you want to select
    a set, the "-ne/noExpand" flag must be used.
    
    With the advent of namespaces, selection by name may be confusing. To clarify,
    without a qualified namespace, name lookup is limited to objects in the root
    namespace ":". There are really two parts of a name: the namespace and the
    name itself which is unique within the namespace. If you want to select
    objects in a specific namespace, you need to include the namespace separator
    ":".
    
    For example, 'select -r "foo*"' is trying to look for an object with the "foo"
    prefix in the root namespace. It is not trying to look for all objects in the
    namespace with the "foo" prefix. If you want to select all objects in a
    namespace (foo), use 'select "foo:*"'.
    
    Note: When the application starts up, there are several dependency nodes
    created by the system which must exist. These objects are not deletable but
    are selectable. All objects (dag and dependency nodes) in the scene can be
    obtained using the "ls" command without any arguments. When using the "-all",
    "adn/allDependencyNodes" or "-ado/allDagObjects" flags, only the deletable
    objects are selected. The non deletable object can still be selected by
    explicitly specifying their name as in "select time1;".

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects and add them to a set
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sets( 'sphere1', 'sphere2', n='set1' )
        # select all dag objects and all dependency nodes
        cmds.select( all=True )
        # clear the active list
        cmds.select( clear=True )
        # select sphere2 only if it is visible
        cmds.select( 'sphere2', visible=True )
        # select a couple of objects regardless of visibilty
        cmds.select( 'sphere1', r=True )
        cmds.select( 'sphere2', add=True )
        # remove one of the spheres from the active list (using toggle)
        cmds.select( 'sphere1', tgl=True )
        # remove the other sphere from the active list
        cmds.select( 'sphere2', d=True )
        # the following selects all the members of set1
        cmds.select( 'set1' )
        # this selects set1 itself
        cmds.select( 'set1', ne=True )
        # Some examples selecting with namespaces:
        # create a namespace and an object in the namespace
        cmds.namespace( add='foo' )
        cmds.namespace( set='foo' )
        cmds.sphere( n='bar' )
        # 'select bar' will not select "bar" unless bar is in the
        # root namespace. You need to qualify the name with the
        # namespace (shown below).
        cmds.select( 'foo:bar' )
        # select all the objects in a namespace
        cmds.select( 'foo:*' )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - add: Indicates that the specified items should be added to the active list without removing existing items from the active list.
        - addFirst (af): Indicates that the specified items should be added to the front of the active list without removing existing items from the active list.
        - all: Indicates that all deletable root level dag objects and all deletable non-dag dependency nodes should be selected.
        - allDagObjects (ado): Indicates that all deletable root level dag objects should be selected.
        - allDependencyNodes (adn): Indicates that all deletable dependency nodes including all deletable dag objects should be selected.
        - clear (cl): Clears the active list.  This is more efficient than "select -d;".  Also "select -d;" will not remove sets from the active list unless the "-ne" flag is also specified.
        - containerCentric (cc): Specifies that the same selection rules as apply to selection in the main viewport will also be applied to the select command. In particular, if the specified objects are members of a black-boxed container and are not published as nodes,
            Maya will not select them. Instead, their first parent valid for selection will be selected.
        - deselect (d): Indicates that the specified items should be removed from the active list if they are on the active list.
        - hierarchy (hi): Indicates that all children, grandchildren, ... of the specified dag objects should also be selected.
        - noExpand (ne): Indicates that any set which is among the specified items should not be expanded to its list of members. This allows sets to be selected as opposed to the members of sets which is the default behaviour.
        - replace (r): Indicates that the specified items should replace the existing items on the active list.
        - symmetry (sym): Specifies that components should be selected symmetrically using the current symmetricModelling command settings. If symmetric modeling is not enabled then this flag has no effect.
        - symmetrySide (sys): Indicates that components involved in the current symmetry object should be selected, according to the supplied parameter. Valid values for the parameter are:-1 : Select components in the unsymmetrical region.0 : Select components on the
            symmetry seam.1 : Select components on side 1.2 : Select components on side 2. If symmetric modeling is not enabled then this flag has no effect. Note: currently only works for topological symmetry.
        - toggle (tgl): Indicates that those items on the given list which are on the active list should be removed from the active list and those items on the given list which are not on the active list should be added to the active list.
        - visible (vis): Indicates that of the specified items only those that are visible should be affected.
    """
@overload #Overload for select in ['create']
def select([objects...]: [objects...], add: bool = ..., addFirst: bool = ..., af: bool = ..., all: bool = ..., allDagObjects: bool = ..., ado: bool = ..., allDependencyNodes: bool = ..., adn: bool = ..., clear: bool = ..., cl: bool = ..., containerCentric: bool = ..., cc: bool = ..., deselect: bool = ..., d: bool = ..., hierarchy: bool = ..., hi: bool = ..., noExpand: bool = ..., ne: bool = ..., replace: bool = ..., r: bool = ..., symmetry: bool = ..., sym: bool = ..., symmetrySide: int = ..., sys: int = ..., toggle: bool = ..., tgl: bool = ..., visible: bool = ..., vis: bool = ...) -> None:
    """select is undoable, NOT queryable, and NOT editable.
    
    This command is used to put objects onto or off of the active list. If none of
    the five flags [-add, -af, -r, -d, -tgl] are specified, the default is to
    replace the objects on the active list with the given list of objects.
    
    When selecting a set as in "select set1", the behaviour is for all the members
    of the set to become selected instead of the set itself. If you want to select
    a set, the "-ne/noExpand" flag must be used.
    
    With the advent of namespaces, selection by name may be confusing. To clarify,
    without a qualified namespace, name lookup is limited to objects in the root
    namespace ":". There are really two parts of a name: the namespace and the
    name itself which is unique within the namespace. If you want to select
    objects in a specific namespace, you need to include the namespace separator
    ":".
    
    For example, 'select -r "foo*"' is trying to look for an object with the "foo"
    prefix in the root namespace. It is not trying to look for all objects in the
    namespace with the "foo" prefix. If you want to select all objects in a
    namespace (foo), use 'select "foo:*"'.
    
    Note: When the application starts up, there are several dependency nodes
    created by the system which must exist. These objects are not deletable but
    are selectable. All objects (dag and dependency nodes) in the scene can be
    obtained using the "ls" command without any arguments. When using the "-all",
    "adn/allDependencyNodes" or "-ado/allDagObjects" flags, only the deletable
    objects are selected. The non deletable object can still be selected by
    explicitly specifying their name as in "select time1;".

    Example:
    ```python
        import maya.cmds as cmds
        # create some objects and add them to a set
        cmds.sphere( n='sphere1' )
        cmds.sphere( n='sphere2' )
        cmds.sets( 'sphere1', 'sphere2', n='set1' )
        # select all dag objects and all dependency nodes
        cmds.select( all=True )
        # clear the active list
        cmds.select( clear=True )
        # select sphere2 only if it is visible
        cmds.select( 'sphere2', visible=True )
        # select a couple of objects regardless of visibilty
        cmds.select( 'sphere1', r=True )
        cmds.select( 'sphere2', add=True )
        # remove one of the spheres from the active list (using toggle)
        cmds.select( 'sphere1', tgl=True )
        # remove the other sphere from the active list
        cmds.select( 'sphere2', d=True )
        # the following selects all the members of set1
        cmds.select( 'set1' )
        # this selects set1 itself
        cmds.select( 'set1', ne=True )
        # Some examples selecting with namespaces:
        # create a namespace and an object in the namespace
        cmds.namespace( add='foo' )
        cmds.namespace( set='foo' )
        cmds.sphere( n='bar' )
        # 'select bar' will not select "bar" unless bar is in the
        # root namespace. You need to qualify the name with the
        # namespace (shown below).
        cmds.select( 'foo:bar' )
        # select all the objects in a namespace
        cmds.select( 'foo:*' )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - add: Indicates that the specified items should be added to the active list without removing existing items from the active list.
        - addFirst (af): Indicates that the specified items should be added to the front of the active list without removing existing items from the active list.
        - all: Indicates that all deletable root level dag objects and all deletable non-dag dependency nodes should be selected.
        - allDagObjects (ado): Indicates that all deletable root level dag objects should be selected.
        - allDependencyNodes (adn): Indicates that all deletable dependency nodes including all deletable dag objects should be selected.
        - clear (cl): Clears the active list.  This is more efficient than "select -d;".  Also "select -d;" will not remove sets from the active list unless the "-ne" flag is also specified.
        - containerCentric (cc): Specifies that the same selection rules as apply to selection in the main viewport will also be applied to the select command. In particular, if the specified objects are members of a black-boxed container and are not published as nodes,
            Maya will not select them. Instead, their first parent valid for selection will be selected.
        - deselect (d): Indicates that the specified items should be removed from the active list if they are on the active list.
        - hierarchy (hi): Indicates that all children, grandchildren, ... of the specified dag objects should also be selected.
        - noExpand (ne): Indicates that any set which is among the specified items should not be expanded to its list of members. This allows sets to be selected as opposed to the members of sets which is the default behaviour.
        - replace (r): Indicates that the specified items should replace the existing items on the active list.
        - symmetry (sym): Specifies that components should be selected symmetrically using the current symmetricModelling command settings. If symmetric modeling is not enabled then this flag has no effect.
        - symmetrySide (sys): Indicates that components involved in the current symmetry object should be selected, according to the supplied parameter. Valid values for the parameter are:-1 : Select components in the unsymmetrical region.0 : Select components on the
            symmetry seam.1 : Select components on side 1.2 : Select components on side 2. If symmetric modeling is not enabled then this flag has no effect. Note: currently only works for topological symmetry.
        - toggle (tgl): Indicates that those items on the given list which are on the active list should be removed from the active list and those items on the given list which are not on the active list should be added to the active list.
        - visible (vis): Indicates that of the specified items only those that are visible should be affected.
    """
