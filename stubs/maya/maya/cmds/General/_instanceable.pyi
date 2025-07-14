"""Stub files for General category in Maya commands, command: instanceable."""

from typing import Any, overload

@overload #Overload for instanceable in ['create']
def instanceable(allow: bool = ..., recursive: bool = ..., shape: bool = ...) -> boolean[]:
    """instanceable is undoable, queryable, and NOT editable.
    
    Flags one or more DAG nodes so that they can (or cannot) be instanced. This
    command sets an internal state on the specified DAG nodes which is checked
    whenever Maya attempts an instancing operation. If no node names are provided
    on the command line then the current selection list is used.
    
    Sets are automatically expanded to their constituent objects. Nodes which are
    already instanced (or have children which are already instanced) cannot be
    marked as non-instancable.

    ---
    - Args:
        - allow (a): Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).
        - recursive (r): Can be specified with the -allow flag in create or edit mode to recursively apply the -allow setting to all non-shape children of the selected node(s). To also affect shapes, also specify the -shape flag along with -recursive.
        - shape (s): Can be specified with the -allow flag in create or edit mode to apply the -allow setting to all shape children of the selected node(s). This flag can be specified in conjunction with the -recursive flag.
    """
@overload #Overload for instanceable in ['create']
def instanceable(a: bool = ..., r: bool = ..., s: bool = ...) -> boolean[]:
    """instanceable is undoable, queryable, and NOT editable.
    
    Flags one or more DAG nodes so that they can (or cannot) be instanced. This
    command sets an internal state on the specified DAG nodes which is checked
    whenever Maya attempts an instancing operation. If no node names are provided
    on the command line then the current selection list is used.
    
    Sets are automatically expanded to their constituent objects. Nodes which are
    already instanced (or have children which are already instanced) cannot be
    marked as non-instancable.

    ---
    - Args:
        - allow (a): Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).
        - recursive (r): Can be specified with the -allow flag in create or edit mode to recursively apply the -allow setting to all non-shape children of the selected node(s). To also affect shapes, also specify the -shape flag along with -recursive.
        - shape (s): Can be specified with the -allow flag in create or edit mode to apply the -allow setting to all shape children of the selected node(s). This flag can be specified in conjunction with the -recursive flag.
    """
@overload #Overload for instanceable in ['create']
def instanceable(allow: bool = ..., a: bool = ..., recursive: bool = ..., r: bool = ..., shape: bool = ..., s: bool = ...) -> boolean[]:
    """instanceable is undoable, queryable, and NOT editable.
    
    Flags one or more DAG nodes so that they can (or cannot) be instanced. This
    command sets an internal state on the specified DAG nodes which is checked
    whenever Maya attempts an instancing operation. If no node names are provided
    on the command line then the current selection list is used.
    
    Sets are automatically expanded to their constituent objects. Nodes which are
    already instanced (or have children which are already instanced) cannot be
    marked as non-instancable.

    ---
    - Args:
        - allow (a): Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).
        - recursive (r): Can be specified with the -allow flag in create or edit mode to recursively apply the -allow setting to all non-shape children of the selected node(s). To also affect shapes, also specify the -shape flag along with -recursive.
        - shape (s): Can be specified with the -allow flag in create or edit mode to apply the -allow setting to all shape children of the selected node(s). This flag can be specified in conjunction with the -recursive flag.
    """
@overload #Overload for instanceable in ['query']
def instanceable(allow: bool = ..., query: bool = ...) -> boolean[]:
    """instanceable is undoable, queryable, and NOT editable.
    
    Flags one or more DAG nodes so that they can (or cannot) be instanced. This
    command sets an internal state on the specified DAG nodes which is checked
    whenever Maya attempts an instancing operation. If no node names are provided
    on the command line then the current selection list is used.
    
    Sets are automatically expanded to their constituent objects. Nodes which are
    already instanced (or have children which are already instanced) cannot be
    marked as non-instancable.

    ---
    - Args:
        - allow (a): Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).
        - query (q): Query mode flag
    """
@overload #Overload for instanceable in ['query']
def instanceable(a: bool = ..., q: bool = ...) -> boolean[]:
    """instanceable is undoable, queryable, and NOT editable.
    
    Flags one or more DAG nodes so that they can (or cannot) be instanced. This
    command sets an internal state on the specified DAG nodes which is checked
    whenever Maya attempts an instancing operation. If no node names are provided
    on the command line then the current selection list is used.
    
    Sets are automatically expanded to their constituent objects. Nodes which are
    already instanced (or have children which are already instanced) cannot be
    marked as non-instancable.

    ---
    - Args:
        - allow (a): Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).
        - query (q): Query mode flag
    """
@overload #Overload for instanceable in ['query']
def instanceable(allow: bool = ..., a: bool = ..., query: bool = ..., q: bool = ...) -> boolean[]:
    """instanceable is undoable, queryable, and NOT editable.
    
    Flags one or more DAG nodes so that they can (or cannot) be instanced. This
    command sets an internal state on the specified DAG nodes which is checked
    whenever Maya attempts an instancing operation. If no node names are provided
    on the command line then the current selection list is used.
    
    Sets are automatically expanded to their constituent objects. Nodes which are
    already instanced (or have children which are already instanced) cannot be
    marked as non-instancable.

    ---
    - Args:
        - allow (a): Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).
        - query (q): Query mode flag
    """
@overload #Overload for instanceable in ['edit']
def instanceable(allow: bool = ..., edit: bool = ...) -> boolean[]:
    """instanceable is undoable, queryable, and NOT editable.
    
    Flags one or more DAG nodes so that they can (or cannot) be instanced. This
    command sets an internal state on the specified DAG nodes which is checked
    whenever Maya attempts an instancing operation. If no node names are provided
    on the command line then the current selection list is used.
    
    Sets are automatically expanded to their constituent objects. Nodes which are
    already instanced (or have children which are already instanced) cannot be
    marked as non-instancable.

    ---
    - Args:
        - allow (a): Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).
        - edit (e): Edit mode flag
    """
@overload #Overload for instanceable in ['edit']
def instanceable(a: bool = ..., e: bool = ...) -> boolean[]:
    """instanceable is undoable, queryable, and NOT editable.
    
    Flags one or more DAG nodes so that they can (or cannot) be instanced. This
    command sets an internal state on the specified DAG nodes which is checked
    whenever Maya attempts an instancing operation. If no node names are provided
    on the command line then the current selection list is used.
    
    Sets are automatically expanded to their constituent objects. Nodes which are
    already instanced (or have children which are already instanced) cannot be
    marked as non-instancable.

    ---
    - Args:
        - allow (a): Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).
        - edit (e): Edit mode flag
    """
@overload #Overload for instanceable in ['edit']
def instanceable(allow: bool = ..., a: bool = ..., edit: bool = ..., e: bool = ...) -> boolean[]:
    """instanceable is undoable, queryable, and NOT editable.
    
    Flags one or more DAG nodes so that they can (or cannot) be instanced. This
    command sets an internal state on the specified DAG nodes which is checked
    whenever Maya attempts an instancing operation. If no node names are provided
    on the command line then the current selection list is used.
    
    Sets are automatically expanded to their constituent objects. Nodes which are
    already instanced (or have children which are already instanced) cannot be
    marked as non-instancable.

    ---
    - Args:
        - allow (a): Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).
        - edit (e): Edit mode flag
    """
