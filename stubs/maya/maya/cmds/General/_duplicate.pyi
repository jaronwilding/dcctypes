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
