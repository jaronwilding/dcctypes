"""Stub files for Attributes category in Maya commands, command: listHistory."""

from typing import Any, overload

@overload #Overload for listHistory in ['create']
def listHistory(objects: objects, allConnections: bool = ..., allFuture: bool = ..., allGraphs: bool = ..., breadthFirst: bool = ..., fastIteration: bool = ..., fullNodeName: bool = ..., future: bool = ..., groupLevels: bool = ..., interestLevel: int = ..., leaf: bool = ..., levels: int = ..., pruneDagObjects: bool = ...) -> list[str]:
    """listHistory is undoable, queryable, and NOT editable.
    
    This command traverses backwards or forwards in the graph from the specified
    node and returns all of the nodes whose construction history it passes
    through. The construction history consists of connections to specific
    attributes of a node defined as the creators and results of the node's main
    data, eg. the curve for a Nurbs Curve node.
    
    For information on history connections through specific plugs use the
    "listConnections" command first to find where the history begins then use this
    command on the resulting node.

    ---
    - Args:
        - objects: Input item(s).
        - allConnections (ac): If specified, the traversal that searches for the history or future will not restrict its traversal across nodes to only dependent plugs. Thus it will reach all upstream nodes (or all downstream nodes for f/future).
        - allFuture (af): If listing the future, list all of it. Otherwise if a shape has an attribute that represents its output geometry data, and that plug is connected, only list the future history downstream from that connection.
        - allGraphs (ag): This flag is obsolete and has no effect.
        - breadthFirst (bf): The breadth first traversal will return the closest nodes in the traversal first. The depth first traversal will follow a complete path away from the node, then return to any other paths from the node. Default is depth first.
        - fastIteration (fi): This flag enables a faster iteration mode that offers more scalable performance, especially when traversing nodes with numerous connections.  However, the results can be slightly different, especially in cases with transitive dependencies
            between attributes (attribute A is affected by B which is affected by C, but A is not directly affected by C).
        - fullNodeName (fnn): Return full node name in result.
        - future (f): List the future instead of the history.
        - groupLevels (gl): The node names are grouped depending on the level.  > 1 is the lead, the rest are grouped with it.
        - interestLevel (il): If this flag is set, only nodes whose historicallyInteresting attribute value is not less than the value will be listed. The historicallyInteresting attribute is 0 on nodes which are not of interest to non-programmers.  1 for the TDs, 2 for
            the users.
        - leaf (lf): If transform is selected, show history for its leaf shape. Default is true.
        - levels (lv): Levels deep to traverse. Setting the number of levels to 0 means do all levels. All levels is the default.
        - pruneDagObjects (pdo): If this flag is set, prune at dag objects.
    """
@overload #Overload for listHistory in ['create']
def listHistory(objects: objects, ac: bool = ..., af: bool = ..., ag: bool = ..., bf: bool = ..., fi: bool = ..., fnn: bool = ..., f: bool = ..., gl: bool = ..., il: int = ..., lf: bool = ..., lv: int = ..., pdo: bool = ...) -> list[str]:
    """listHistory is undoable, queryable, and NOT editable.
    
    This command traverses backwards or forwards in the graph from the specified
    node and returns all of the nodes whose construction history it passes
    through. The construction history consists of connections to specific
    attributes of a node defined as the creators and results of the node's main
    data, eg. the curve for a Nurbs Curve node.
    
    For information on history connections through specific plugs use the
    "listConnections" command first to find where the history begins then use this
    command on the resulting node.

    ---
    - Args:
        - objects: Input item(s).
        - allConnections (ac): If specified, the traversal that searches for the history or future will not restrict its traversal across nodes to only dependent plugs. Thus it will reach all upstream nodes (or all downstream nodes for f/future).
        - allFuture (af): If listing the future, list all of it. Otherwise if a shape has an attribute that represents its output geometry data, and that plug is connected, only list the future history downstream from that connection.
        - allGraphs (ag): This flag is obsolete and has no effect.
        - breadthFirst (bf): The breadth first traversal will return the closest nodes in the traversal first. The depth first traversal will follow a complete path away from the node, then return to any other paths from the node. Default is depth first.
        - fastIteration (fi): This flag enables a faster iteration mode that offers more scalable performance, especially when traversing nodes with numerous connections.  However, the results can be slightly different, especially in cases with transitive dependencies
            between attributes (attribute A is affected by B which is affected by C, but A is not directly affected by C).
        - fullNodeName (fnn): Return full node name in result.
        - future (f): List the future instead of the history.
        - groupLevels (gl): The node names are grouped depending on the level.  > 1 is the lead, the rest are grouped with it.
        - interestLevel (il): If this flag is set, only nodes whose historicallyInteresting attribute value is not less than the value will be listed. The historicallyInteresting attribute is 0 on nodes which are not of interest to non-programmers.  1 for the TDs, 2 for
            the users.
        - leaf (lf): If transform is selected, show history for its leaf shape. Default is true.
        - levels (lv): Levels deep to traverse. Setting the number of levels to 0 means do all levels. All levels is the default.
        - pruneDagObjects (pdo): If this flag is set, prune at dag objects.
    """
@overload #Overload for listHistory in ['create']
def listHistory(objects: objects, allConnections: bool = ..., ac: bool = ..., allFuture: bool = ..., af: bool = ..., allGraphs: bool = ..., ag: bool = ..., breadthFirst: bool = ..., bf: bool = ..., fastIteration: bool = ..., fi: bool = ..., fullNodeName: bool = ..., fnn: bool = ..., future: bool = ..., f: bool = ..., groupLevels: bool = ..., gl: bool = ..., interestLevel: int = ..., il: int = ..., leaf: bool = ..., lf: bool = ..., levels: int = ..., lv: int = ..., pruneDagObjects: bool = ..., pdo: bool = ...) -> list[str]:
    """listHistory is undoable, queryable, and NOT editable.
    
    This command traverses backwards or forwards in the graph from the specified
    node and returns all of the nodes whose construction history it passes
    through. The construction history consists of connections to specific
    attributes of a node defined as the creators and results of the node's main
    data, eg. the curve for a Nurbs Curve node.
    
    For information on history connections through specific plugs use the
    "listConnections" command first to find where the history begins then use this
    command on the resulting node.

    ---
    - Args:
        - objects: Input item(s).
        - allConnections (ac): If specified, the traversal that searches for the history or future will not restrict its traversal across nodes to only dependent plugs. Thus it will reach all upstream nodes (or all downstream nodes for f/future).
        - allFuture (af): If listing the future, list all of it. Otherwise if a shape has an attribute that represents its output geometry data, and that plug is connected, only list the future history downstream from that connection.
        - allGraphs (ag): This flag is obsolete and has no effect.
        - breadthFirst (bf): The breadth first traversal will return the closest nodes in the traversal first. The depth first traversal will follow a complete path away from the node, then return to any other paths from the node. Default is depth first.
        - fastIteration (fi): This flag enables a faster iteration mode that offers more scalable performance, especially when traversing nodes with numerous connections.  However, the results can be slightly different, especially in cases with transitive dependencies
            between attributes (attribute A is affected by B which is affected by C, but A is not directly affected by C).
        - fullNodeName (fnn): Return full node name in result.
        - future (f): List the future instead of the history.
        - groupLevels (gl): The node names are grouped depending on the level.  > 1 is the lead, the rest are grouped with it.
        - interestLevel (il): If this flag is set, only nodes whose historicallyInteresting attribute value is not less than the value will be listed. The historicallyInteresting attribute is 0 on nodes which are not of interest to non-programmers.  1 for the TDs, 2 for
            the users.
        - leaf (lf): If transform is selected, show history for its leaf shape. Default is true.
        - levels (lv): Levels deep to traverse. Setting the number of levels to 0 means do all levels. All levels is the default.
        - pruneDagObjects (pdo): If this flag is set, prune at dag objects.
    """
@overload #Overload for listHistory in ['query']
def listHistory(objects: objects, futureLocalAttr: bool = ..., futureWorldAttr: bool = ..., historyAttr: bool = ..., query: bool = ...) -> list[str]:
    """listHistory is undoable, queryable, and NOT editable.
    
    This command traverses backwards or forwards in the graph from the specified
    node and returns all of the nodes whose construction history it passes
    through. The construction history consists of connections to specific
    attributes of a node defined as the creators and results of the node's main
    data, eg. the curve for a Nurbs Curve node.
    
    For information on history connections through specific plugs use the
    "listConnections" command first to find where the history begins then use this
    command on the resulting node.

    ---
    - Args:
        - objects: Input item(s).
        - futureLocalAttr (fl): This flag allows querying of the local-space future-related attribute(s) on shape nodes.
        - futureWorldAttr (fw): This flag allows querying of the world-space future-related attribute(s) on shape nodes.
        - historyAttr (ha): This flag allows querying of the attribute where history connects on shape nodes.
        - query (q): Query mode flag
    """
@overload #Overload for listHistory in ['query']
def listHistory(objects: objects, fl: bool = ..., fw: bool = ..., ha: bool = ..., q: bool = ...) -> list[str]:
    """listHistory is undoable, queryable, and NOT editable.
    
    This command traverses backwards or forwards in the graph from the specified
    node and returns all of the nodes whose construction history it passes
    through. The construction history consists of connections to specific
    attributes of a node defined as the creators and results of the node's main
    data, eg. the curve for a Nurbs Curve node.
    
    For information on history connections through specific plugs use the
    "listConnections" command first to find where the history begins then use this
    command on the resulting node.

    ---
    - Args:
        - objects: Input item(s).
        - futureLocalAttr (fl): This flag allows querying of the local-space future-related attribute(s) on shape nodes.
        - futureWorldAttr (fw): This flag allows querying of the world-space future-related attribute(s) on shape nodes.
        - historyAttr (ha): This flag allows querying of the attribute where history connects on shape nodes.
        - query (q): Query mode flag
    """
@overload #Overload for listHistory in ['query']
def listHistory(objects: objects, futureLocalAttr: bool = ..., fl: bool = ..., futureWorldAttr: bool = ..., fw: bool = ..., historyAttr: bool = ..., ha: bool = ..., query: bool = ..., q: bool = ...) -> list[str]:
    """listHistory is undoable, queryable, and NOT editable.
    
    This command traverses backwards or forwards in the graph from the specified
    node and returns all of the nodes whose construction history it passes
    through. The construction history consists of connections to specific
    attributes of a node defined as the creators and results of the node's main
    data, eg. the curve for a Nurbs Curve node.
    
    For information on history connections through specific plugs use the
    "listConnections" command first to find where the history begins then use this
    command on the resulting node.

    ---
    - Args:
        - objects: Input item(s).
        - futureLocalAttr (fl): This flag allows querying of the local-space future-related attribute(s) on shape nodes.
        - futureWorldAttr (fw): This flag allows querying of the world-space future-related attribute(s) on shape nodes.
        - historyAttr (ha): This flag allows querying of the attribute where history connects on shape nodes.
        - query (q): Query mode flag
    """
