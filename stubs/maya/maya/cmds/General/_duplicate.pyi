"""Stub files for General category in Maya commands, command: duplicate."""

from typing import Any, overload

@overload #Overload for duplicate in ['create']
def duplicate([objects...]: [objects...], fullPath: bool = ..., inputConnections: bool = ..., instanceLeaf: bool = ..., name: str = ..., parentOnly: bool = ..., renameChildren: bool = ..., returnRootsOnly: bool = ..., smartTransform: bool = ..., transformsOnly: bool = ..., upstreamNodes: bool = ...) -> list[str]:
    """duplicate is undoable, NOT queryable, and NOT editable.
    
    This command duplicates the given objects. If no objects are given, then the
    selected list is duplicated.
    
    The smart transform feature allows duplicate to transform newly duplicated
    objects based on previous transformations between duplications.
    
    Example: Duplicate an object and move it to a new location. Duplicate it again
    with the smart duplicate flag. It should have moved once again the distance
    you had previously moved it.
    
    Note: changing the selected list between smart duplications will cause the
    transform information to be deleted
    
    The upstream Nodes option forces duplication of all upstream nodes leading
    upto the selected objects.. Upstream nodes are defined as all nodes feeding
    into selected nodes. During traversal of Dependency graph, if another
    dagObject is encountered, then that node and all it's parent transforms are
    also duplicated.
    
    The inputConnections option forces the duplication of input connections to the
    nodes that are to be duplicated. This is very useful especially in cases where
    two nodes that are connected to each other are specified as nodes to be
    duplicated. In that situation, the connection between the nodes is also
    duplicated.
    
    See also: instance

    Example:
    ```python
        import maya.cmds as cmds
        # Create a hierarchy of two spheres;
        cmds.sphere( n='sphere1' )
        cmds.move( 3, 0, 0 )
        cmds.sphere( n='sphere2' )
        cmds.move( -3, 0, 0 )
        cmds.group( 'sphere1', 'sphere2', n='group1' )
        cmds.circle( n='circle1' )
        # Create a duplicate of the group
        cmds.duplicate( 'group1' )
        # Result: group2 sphere1 sphere2 #
        cmds.undo()
        cmds.duplicate( 'group1', rr=True )
        # Result: group2 #
        # Create a row of 4 circles equally spaced using
        # the -smartTransform flag.
        cmds.duplicate( 'circle1' )
        cmds.move( 3, 0, 0 )
        cmds.duplicate( st=True )
        cmds.duplicate( st=True )
        # Duplicate a sphere along with its input connections.
        # If animCurves were feeding into original transforms of the
        # sphere, they will feed into the duplicated ones also.
        # If the sphere has history (in this case it does),
        # then the history is connected to the duplicate. Note that
        # changing the radius for the makeNurbSphere for the sphere1
        # affects the duplicated sphere.
        #
        cmds.duplicate( 'group1|sphere1', ic=True )
        cmds.move( 0, 0, 0 )
        cmds.setAttr( 'makeNurbSphere1.radius', 2 )
        # Duplicate selected objects along with their upstream nodes
        # and connections. This will duplicate the history.
        cmds.select( 'group1|sphere2' )
        cmds.duplicate( un=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - fullPath (f): ADDED 2023 Return full pathnames instead of object names.
        - inputConnections (ic): Input connections to the node to be duplicated, are also duplicated. This would result in a fan-out scenario as the nodes at the input side are not duplicated (unlike the -un option).
        - instanceLeaf (ilf): instead of duplicating leaf DAG nodes, instance them.
        - name (n): name to give duplicated object(s)
        - parentOnly (po): Duplicate only the specified DAG node and not any of its children.
        - renameChildren (rc): rename the child nodes of the hierarchy, to make them unique.
        - returnRootsOnly (rr): return only the root nodes of the new hierarchy. When used with upstreamNodes flag, the upstream nodes will be omitted in the result.  This flag controls only what is returned in the output string[], and it does NOT change the behaviour of
            the duplicate command.
        - smartTransform (st): remembers last transformation and applies it to duplicated object(s)
        - transformsOnly (to): Duplicate only transform nodes and not any shapes.
        - upstreamNodes (un): the upstream nodes leading upto the selected nodes (along with their connections) are also duplicated.
    """
@overload #Overload for duplicate in ['create']
def duplicate([objects...]: [objects...], f: bool = ..., ic: bool = ..., ilf: bool = ..., n: str = ..., po: bool = ..., rc: bool = ..., rr: bool = ..., st: bool = ..., to: bool = ..., un: bool = ...) -> list[str]:
    """duplicate is undoable, NOT queryable, and NOT editable.
    
    This command duplicates the given objects. If no objects are given, then the
    selected list is duplicated.
    
    The smart transform feature allows duplicate to transform newly duplicated
    objects based on previous transformations between duplications.
    
    Example: Duplicate an object and move it to a new location. Duplicate it again
    with the smart duplicate flag. It should have moved once again the distance
    you had previously moved it.
    
    Note: changing the selected list between smart duplications will cause the
    transform information to be deleted
    
    The upstream Nodes option forces duplication of all upstream nodes leading
    upto the selected objects.. Upstream nodes are defined as all nodes feeding
    into selected nodes. During traversal of Dependency graph, if another
    dagObject is encountered, then that node and all it's parent transforms are
    also duplicated.
    
    The inputConnections option forces the duplication of input connections to the
    nodes that are to be duplicated. This is very useful especially in cases where
    two nodes that are connected to each other are specified as nodes to be
    duplicated. In that situation, the connection between the nodes is also
    duplicated.
    
    See also: instance

    Example:
    ```python
        import maya.cmds as cmds
        # Create a hierarchy of two spheres;
        cmds.sphere( n='sphere1' )
        cmds.move( 3, 0, 0 )
        cmds.sphere( n='sphere2' )
        cmds.move( -3, 0, 0 )
        cmds.group( 'sphere1', 'sphere2', n='group1' )
        cmds.circle( n='circle1' )
        # Create a duplicate of the group
        cmds.duplicate( 'group1' )
        # Result: group2 sphere1 sphere2 #
        cmds.undo()
        cmds.duplicate( 'group1', rr=True )
        # Result: group2 #
        # Create a row of 4 circles equally spaced using
        # the -smartTransform flag.
        cmds.duplicate( 'circle1' )
        cmds.move( 3, 0, 0 )
        cmds.duplicate( st=True )
        cmds.duplicate( st=True )
        # Duplicate a sphere along with its input connections.
        # If animCurves were feeding into original transforms of the
        # sphere, they will feed into the duplicated ones also.
        # If the sphere has history (in this case it does),
        # then the history is connected to the duplicate. Note that
        # changing the radius for the makeNurbSphere for the sphere1
        # affects the duplicated sphere.
        #
        cmds.duplicate( 'group1|sphere1', ic=True )
        cmds.move( 0, 0, 0 )
        cmds.setAttr( 'makeNurbSphere1.radius', 2 )
        # Duplicate selected objects along with their upstream nodes
        # and connections. This will duplicate the history.
        cmds.select( 'group1|sphere2' )
        cmds.duplicate( un=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - fullPath (f): ADDED 2023 Return full pathnames instead of object names.
        - inputConnections (ic): Input connections to the node to be duplicated, are also duplicated. This would result in a fan-out scenario as the nodes at the input side are not duplicated (unlike the -un option).
        - instanceLeaf (ilf): instead of duplicating leaf DAG nodes, instance them.
        - name (n): name to give duplicated object(s)
        - parentOnly (po): Duplicate only the specified DAG node and not any of its children.
        - renameChildren (rc): rename the child nodes of the hierarchy, to make them unique.
        - returnRootsOnly (rr): return only the root nodes of the new hierarchy. When used with upstreamNodes flag, the upstream nodes will be omitted in the result.  This flag controls only what is returned in the output string[], and it does NOT change the behaviour of
            the duplicate command.
        - smartTransform (st): remembers last transformation and applies it to duplicated object(s)
        - transformsOnly (to): Duplicate only transform nodes and not any shapes.
        - upstreamNodes (un): the upstream nodes leading upto the selected nodes (along with their connections) are also duplicated.
    """
@overload #Overload for duplicate in ['create']
def duplicate([objects...]: [objects...], fullPath: bool = ..., f: bool = ..., inputConnections: bool = ..., ic: bool = ..., instanceLeaf: bool = ..., ilf: bool = ..., name: str = ..., n: str = ..., parentOnly: bool = ..., po: bool = ..., renameChildren: bool = ..., rc: bool = ..., returnRootsOnly: bool = ..., rr: bool = ..., smartTransform: bool = ..., st: bool = ..., transformsOnly: bool = ..., to: bool = ..., upstreamNodes: bool = ..., un: bool = ...) -> list[str]:
    """duplicate is undoable, NOT queryable, and NOT editable.
    
    This command duplicates the given objects. If no objects are given, then the
    selected list is duplicated.
    
    The smart transform feature allows duplicate to transform newly duplicated
    objects based on previous transformations between duplications.
    
    Example: Duplicate an object and move it to a new location. Duplicate it again
    with the smart duplicate flag. It should have moved once again the distance
    you had previously moved it.
    
    Note: changing the selected list between smart duplications will cause the
    transform information to be deleted
    
    The upstream Nodes option forces duplication of all upstream nodes leading
    upto the selected objects.. Upstream nodes are defined as all nodes feeding
    into selected nodes. During traversal of Dependency graph, if another
    dagObject is encountered, then that node and all it's parent transforms are
    also duplicated.
    
    The inputConnections option forces the duplication of input connections to the
    nodes that are to be duplicated. This is very useful especially in cases where
    two nodes that are connected to each other are specified as nodes to be
    duplicated. In that situation, the connection between the nodes is also
    duplicated.
    
    See also: instance

    Example:
    ```python
        import maya.cmds as cmds
        # Create a hierarchy of two spheres;
        cmds.sphere( n='sphere1' )
        cmds.move( 3, 0, 0 )
        cmds.sphere( n='sphere2' )
        cmds.move( -3, 0, 0 )
        cmds.group( 'sphere1', 'sphere2', n='group1' )
        cmds.circle( n='circle1' )
        # Create a duplicate of the group
        cmds.duplicate( 'group1' )
        # Result: group2 sphere1 sphere2 #
        cmds.undo()
        cmds.duplicate( 'group1', rr=True )
        # Result: group2 #
        # Create a row of 4 circles equally spaced using
        # the -smartTransform flag.
        cmds.duplicate( 'circle1' )
        cmds.move( 3, 0, 0 )
        cmds.duplicate( st=True )
        cmds.duplicate( st=True )
        # Duplicate a sphere along with its input connections.
        # If animCurves were feeding into original transforms of the
        # sphere, they will feed into the duplicated ones also.
        # If the sphere has history (in this case it does),
        # then the history is connected to the duplicate. Note that
        # changing the radius for the makeNurbSphere for the sphere1
        # affects the duplicated sphere.
        #
        cmds.duplicate( 'group1|sphere1', ic=True )
        cmds.move( 0, 0, 0 )
        cmds.setAttr( 'makeNurbSphere1.radius', 2 )
        # Duplicate selected objects along with their upstream nodes
        # and connections. This will duplicate the history.
        cmds.select( 'group1|sphere2' )
        cmds.duplicate( un=True )
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - fullPath (f): ADDED 2023 Return full pathnames instead of object names.
        - inputConnections (ic): Input connections to the node to be duplicated, are also duplicated. This would result in a fan-out scenario as the nodes at the input side are not duplicated (unlike the -un option).
        - instanceLeaf (ilf): instead of duplicating leaf DAG nodes, instance them.
        - name (n): name to give duplicated object(s)
        - parentOnly (po): Duplicate only the specified DAG node and not any of its children.
        - renameChildren (rc): rename the child nodes of the hierarchy, to make them unique.
        - returnRootsOnly (rr): return only the root nodes of the new hierarchy. When used with upstreamNodes flag, the upstream nodes will be omitted in the result.  This flag controls only what is returned in the output string[], and it does NOT change the behaviour of
            the duplicate command.
        - smartTransform (st): remembers last transformation and applies it to duplicated object(s)
        - transformsOnly (to): Duplicate only transform nodes and not any shapes.
        - upstreamNodes (un): the upstream nodes leading upto the selected nodes (along with their connections) are also duplicated.
    """
