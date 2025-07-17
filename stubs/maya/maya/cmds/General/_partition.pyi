"""Stub files for General category in Maya commands, command: partition."""

from typing import Any, overload

@overload #Overload for partition in ['create']
def partition([string] [string...]: [string] [string...], addSet: name = ..., name: str = ..., removeSet: name = ..., render: bool = ...) -> str:
    """partition is undoable, queryable, and editable.
    
    This command is used to create, query or add/remove sets to a partition. If a
    partition name needs to be specified, it is the first argument, other
    arguments represent the set names.
    
    Without any flags, the command will create a partition with a default name.
    Any sets which are arguments to the command will be added to the partition.
    
    A set can be added to a partition only if none of its members are in any of
    the other sets in the partition. If the -re/render flag is specified when the
    partition is created, only 'renderable' sets can be added to the partition.
    
    Sets can be added and removed from a partition by using the -addSet or
    -removeSet flags.
    
    Note: If a set is already selected, and the partition command is executed, the
    set will be added to the created partition.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a partition calls p1 which contains set1 and set2 ...
        cmds.partition( 'set1', 'set2', n='p1' )
        # To create an empty render partition ...
        cmds.partition( render=True )
        # To add/remove sets from partition p1 ...
        cmds.partition( 'set3', add='p1' )
        cmds.partition( 'set1', rm='p1' )
        # To get a list of all sets in a partition ...
        cmds.partition( 'p1', q=True )
        # To check if the partition is a render partition
        cmds.partition( 'p1', q=True, re=True )
    ```

    ---
    - Args:
        - [string] [string...]: Input item(s).
        - addSet (add): Adds the list of sets to the named partition.
        - name (n): Assigns the given name to new partition. Valid only for create mode.
        - removeSet (rm): Removes the list of sets from the named partition.
        - render (re): New partition can contain render sets. For use in creation mode only. Default is false.  Can also be used with query flag - returns boolean.
    """
@overload #Overload for partition in ['create']
def partition([string] [string...]: [string] [string...], add: name = ..., n: str = ..., rm: name = ..., re: bool = ...) -> str:
    """partition is undoable, queryable, and editable.
    
    This command is used to create, query or add/remove sets to a partition. If a
    partition name needs to be specified, it is the first argument, other
    arguments represent the set names.
    
    Without any flags, the command will create a partition with a default name.
    Any sets which are arguments to the command will be added to the partition.
    
    A set can be added to a partition only if none of its members are in any of
    the other sets in the partition. If the -re/render flag is specified when the
    partition is created, only 'renderable' sets can be added to the partition.
    
    Sets can be added and removed from a partition by using the -addSet or
    -removeSet flags.
    
    Note: If a set is already selected, and the partition command is executed, the
    set will be added to the created partition.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a partition calls p1 which contains set1 and set2 ...
        cmds.partition( 'set1', 'set2', n='p1' )
        # To create an empty render partition ...
        cmds.partition( render=True )
        # To add/remove sets from partition p1 ...
        cmds.partition( 'set3', add='p1' )
        cmds.partition( 'set1', rm='p1' )
        # To get a list of all sets in a partition ...
        cmds.partition( 'p1', q=True )
        # To check if the partition is a render partition
        cmds.partition( 'p1', q=True, re=True )
    ```

    ---
    - Args:
        - [string] [string...]: Input item(s).
        - addSet (add): Adds the list of sets to the named partition.
        - name (n): Assigns the given name to new partition. Valid only for create mode.
        - removeSet (rm): Removes the list of sets from the named partition.
        - render (re): New partition can contain render sets. For use in creation mode only. Default is false.  Can also be used with query flag - returns boolean.
    """
@overload #Overload for partition in ['create']
def partition([string] [string...]: [string] [string...], addSet: name = ..., add: name = ..., name: str = ..., n: str = ..., removeSet: name = ..., rm: name = ..., render: bool = ..., re: bool = ...) -> str:
    """partition is undoable, queryable, and editable.
    
    This command is used to create, query or add/remove sets to a partition. If a
    partition name needs to be specified, it is the first argument, other
    arguments represent the set names.
    
    Without any flags, the command will create a partition with a default name.
    Any sets which are arguments to the command will be added to the partition.
    
    A set can be added to a partition only if none of its members are in any of
    the other sets in the partition. If the -re/render flag is specified when the
    partition is created, only 'renderable' sets can be added to the partition.
    
    Sets can be added and removed from a partition by using the -addSet or
    -removeSet flags.
    
    Note: If a set is already selected, and the partition command is executed, the
    set will be added to the created partition.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a partition calls p1 which contains set1 and set2 ...
        cmds.partition( 'set1', 'set2', n='p1' )
        # To create an empty render partition ...
        cmds.partition( render=True )
        # To add/remove sets from partition p1 ...
        cmds.partition( 'set3', add='p1' )
        cmds.partition( 'set1', rm='p1' )
        # To get a list of all sets in a partition ...
        cmds.partition( 'p1', q=True )
        # To check if the partition is a render partition
        cmds.partition( 'p1', q=True, re=True )
    ```

    ---
    - Args:
        - [string] [string...]: Input item(s).
        - addSet (add): Adds the list of sets to the named partition.
        - name (n): Assigns the given name to new partition. Valid only for create mode.
        - removeSet (rm): Removes the list of sets from the named partition.
        - render (re): New partition can contain render sets. For use in creation mode only. Default is false.  Can also be used with query flag - returns boolean.
    """
@overload #Overload for partition in ['query']
def partition([string] [string...]: [string] [string...], render: bool = ..., query: bool = ...) -> str:
    """partition is undoable, queryable, and editable.
    
    This command is used to create, query or add/remove sets to a partition. If a
    partition name needs to be specified, it is the first argument, other
    arguments represent the set names.
    
    Without any flags, the command will create a partition with a default name.
    Any sets which are arguments to the command will be added to the partition.
    
    A set can be added to a partition only if none of its members are in any of
    the other sets in the partition. If the -re/render flag is specified when the
    partition is created, only 'renderable' sets can be added to the partition.
    
    Sets can be added and removed from a partition by using the -addSet or
    -removeSet flags.
    
    Note: If a set is already selected, and the partition command is executed, the
    set will be added to the created partition.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a partition calls p1 which contains set1 and set2 ...
        cmds.partition( 'set1', 'set2', n='p1' )
        # To create an empty render partition ...
        cmds.partition( render=True )
        # To add/remove sets from partition p1 ...
        cmds.partition( 'set3', add='p1' )
        cmds.partition( 'set1', rm='p1' )
        # To get a list of all sets in a partition ...
        cmds.partition( 'p1', q=True )
        # To check if the partition is a render partition
        cmds.partition( 'p1', q=True, re=True )
    ```

    ---
    - Args:
        - [string] [string...]: Input item(s).
        - render (re): New partition can contain render sets. For use in creation mode only. Default is false.  Can also be used with query flag - returns boolean.
        - query (q): Query mode flag
    """
@overload #Overload for partition in ['query']
def partition([string] [string...]: [string] [string...], re: bool = ..., q: bool = ...) -> str:
    """partition is undoable, queryable, and editable.
    
    This command is used to create, query or add/remove sets to a partition. If a
    partition name needs to be specified, it is the first argument, other
    arguments represent the set names.
    
    Without any flags, the command will create a partition with a default name.
    Any sets which are arguments to the command will be added to the partition.
    
    A set can be added to a partition only if none of its members are in any of
    the other sets in the partition. If the -re/render flag is specified when the
    partition is created, only 'renderable' sets can be added to the partition.
    
    Sets can be added and removed from a partition by using the -addSet or
    -removeSet flags.
    
    Note: If a set is already selected, and the partition command is executed, the
    set will be added to the created partition.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a partition calls p1 which contains set1 and set2 ...
        cmds.partition( 'set1', 'set2', n='p1' )
        # To create an empty render partition ...
        cmds.partition( render=True )
        # To add/remove sets from partition p1 ...
        cmds.partition( 'set3', add='p1' )
        cmds.partition( 'set1', rm='p1' )
        # To get a list of all sets in a partition ...
        cmds.partition( 'p1', q=True )
        # To check if the partition is a render partition
        cmds.partition( 'p1', q=True, re=True )
    ```

    ---
    - Args:
        - [string] [string...]: Input item(s).
        - render (re): New partition can contain render sets. For use in creation mode only. Default is false.  Can also be used with query flag - returns boolean.
        - query (q): Query mode flag
    """
@overload #Overload for partition in ['query']
def partition([string] [string...]: [string] [string...], render: bool = ..., re: bool = ..., query: bool = ..., q: bool = ...) -> str:
    """partition is undoable, queryable, and editable.
    
    This command is used to create, query or add/remove sets to a partition. If a
    partition name needs to be specified, it is the first argument, other
    arguments represent the set names.
    
    Without any flags, the command will create a partition with a default name.
    Any sets which are arguments to the command will be added to the partition.
    
    A set can be added to a partition only if none of its members are in any of
    the other sets in the partition. If the -re/render flag is specified when the
    partition is created, only 'renderable' sets can be added to the partition.
    
    Sets can be added and removed from a partition by using the -addSet or
    -removeSet flags.
    
    Note: If a set is already selected, and the partition command is executed, the
    set will be added to the created partition.

    Example:
    ```python
        import maya.cmds as cmds
        # To create a partition calls p1 which contains set1 and set2 ...
        cmds.partition( 'set1', 'set2', n='p1' )
        # To create an empty render partition ...
        cmds.partition( render=True )
        # To add/remove sets from partition p1 ...
        cmds.partition( 'set3', add='p1' )
        cmds.partition( 'set1', rm='p1' )
        # To get a list of all sets in a partition ...
        cmds.partition( 'p1', q=True )
        # To check if the partition is a render partition
        cmds.partition( 'p1', q=True, re=True )
    ```

    ---
    - Args:
        - [string] [string...]: Input item(s).
        - render (re): New partition can contain render sets. For use in creation mode only. Default is false.  Can also be used with query flag - returns boolean.
        - query (q): Query mode flag
    """
