"""Stub files for Attributes category in Maya commands, command: createNode."""

from typing import Any, overload

@overload #Overload for createNode in ['create']
def createNode(string: str, name: str = ..., parent: str = ..., shared: bool = ..., skipSelect: bool = ...) -> str:
    """createNode is undoable, NOT queryable, and NOT editable.
    
    This command creates a new node in the dependency graph of the specified type.

    ---
    - Args:
        - string: Input item(s).
        - name (n): Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        - parent (p): Specifies the parent in the DAG under which the new node belongs.
        - shared (s): This node is shared across multiple files, so only create it if it does not already exist.
        - skipSelect (ss): This node is not to be selected after creation, the original selection will be preserved.
    """
@overload #Overload for createNode in ['create']
def createNode(string: str, n: str = ..., p: str = ..., s: bool = ..., ss: bool = ...) -> str:
    """createNode is undoable, NOT queryable, and NOT editable.
    
    This command creates a new node in the dependency graph of the specified type.

    ---
    - Args:
        - string: Input item(s).
        - name (n): Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        - parent (p): Specifies the parent in the DAG under which the new node belongs.
        - shared (s): This node is shared across multiple files, so only create it if it does not already exist.
        - skipSelect (ss): This node is not to be selected after creation, the original selection will be preserved.
    """
@overload #Overload for createNode in ['create']
def createNode(string: str, name: str = ..., n: str = ..., parent: str = ..., p: str = ..., shared: bool = ..., s: bool = ..., skipSelect: bool = ..., ss: bool = ...) -> str:
    """createNode is undoable, NOT queryable, and NOT editable.
    
    This command creates a new node in the dependency graph of the specified type.

    ---
    - Args:
        - string: Input item(s).
        - name (n): Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        - parent (p): Specifies the parent in the DAG under which the new node belongs.
        - shared (s): This node is shared across multiple files, so only create it if it does not already exist.
        - skipSelect (ss): This node is not to be selected after creation, the original selection will be preserved.
    """
