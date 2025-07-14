"""Stub files for General category in Maya commands, command: delete."""

from typing import Any, overload

@overload #Overload for delete in ['create']
def delete(objects: objects, all: bool = ..., attribute: str = ..., channels: bool = ..., constraints: bool = ..., constructionHistory: bool = ..., controlPoints: bool = ..., expressions: bool = ..., hierarchy: str = ..., inputConnectionsAndNodes: bool = ..., motionPaths: bool = ..., shape: bool = ..., staticChannels: bool = ..., timeAnimationCurves: bool = ..., unitlessAnimationCurves: bool = ...) -> None:
    """delete is undoable, NOT queryable, and NOT editable.
    
    This command is used to delete selected objects, or all objects, or objects
    specified along with the command. Flags are available to filter the type of
    objects that the command acts on.
    
    At times, more than just specified items will be deleted. For example,
    deleting two CVs in the same "row" on a NURBS surface will delete the whole
    row.

    ---
    - Args:
        - objects: Input item(s).
        - all: Remove all objects of specified kind, in the scene. This flag is to be used in conjunction with the following flags.
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - channels (c): Remove animation channels in the scene. Either all channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - constraints (cn): Remove selected constraints and constraints attached to the selected nodes, or remove all constraints in the scene.
        - constructionHistory (ch): Remove the construction history on the objects specified or selected.
        - controlPoints (cp): This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - expressions (e): Remove expressions in the scene. Either all expressions can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - hierarchy (hi): Hierarchy expansion options.  Valid values are "above," "below," "both," and "none."(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - inputConnectionsAndNodes (icn): Break input connection to specified attribute and delete all unconnected nodes that are left behind. The graph will be traversed until a node that cannot be deleted is encountered.
        - motionPaths (mp): Remove motion paths in the scene. Either all motion paths can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - shape (s): Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - staticChannels (sc): Remove static animation channels in the scene. Either all static channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - timeAnimationCurves (tac): Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to time-input animation curves (for instance, those created by 'setKeyframe' will be deleted.  When false, no time-input animation curves will be
            deleted. Default: true.
        - unitlessAnimationCurves (uac): Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to unitless-input animation curves (for instance, those created by 'setDrivenKeyframe' will be deleted.  When false, no unitless-input animation
            curves will be deleted.  Default: true.
    """
@overload #Overload for delete in ['create']
def delete(objects: objects, at: str = ..., c: bool = ..., cn: bool = ..., ch: bool = ..., cp: bool = ..., e: bool = ..., hi: str = ..., icn: bool = ..., mp: bool = ..., s: bool = ..., sc: bool = ..., tac: bool = ..., uac: bool = ...) -> None:
    """delete is undoable, NOT queryable, and NOT editable.
    
    This command is used to delete selected objects, or all objects, or objects
    specified along with the command. Flags are available to filter the type of
    objects that the command acts on.
    
    At times, more than just specified items will be deleted. For example,
    deleting two CVs in the same "row" on a NURBS surface will delete the whole
    row.

    ---
    - Args:
        - objects: Input item(s).
        - all: Remove all objects of specified kind, in the scene. This flag is to be used in conjunction with the following flags.
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - channels (c): Remove animation channels in the scene. Either all channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - constraints (cn): Remove selected constraints and constraints attached to the selected nodes, or remove all constraints in the scene.
        - constructionHistory (ch): Remove the construction history on the objects specified or selected.
        - controlPoints (cp): This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - expressions (e): Remove expressions in the scene. Either all expressions can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - hierarchy (hi): Hierarchy expansion options.  Valid values are "above," "below," "both," and "none."(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - inputConnectionsAndNodes (icn): Break input connection to specified attribute and delete all unconnected nodes that are left behind. The graph will be traversed until a node that cannot be deleted is encountered.
        - motionPaths (mp): Remove motion paths in the scene. Either all motion paths can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - shape (s): Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - staticChannels (sc): Remove static animation channels in the scene. Either all static channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - timeAnimationCurves (tac): Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to time-input animation curves (for instance, those created by 'setKeyframe' will be deleted.  When false, no time-input animation curves will be
            deleted. Default: true.
        - unitlessAnimationCurves (uac): Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to unitless-input animation curves (for instance, those created by 'setDrivenKeyframe' will be deleted.  When false, no unitless-input animation
            curves will be deleted.  Default: true.
    """
@overload #Overload for delete in ['create']
def delete(objects: objects, all: bool = ..., attribute: str = ..., at: str = ..., channels: bool = ..., c: bool = ..., constraints: bool = ..., cn: bool = ..., constructionHistory: bool = ..., ch: bool = ..., controlPoints: bool = ..., cp: bool = ..., expressions: bool = ..., e: bool = ..., hierarchy: str = ..., hi: str = ..., inputConnectionsAndNodes: bool = ..., icn: bool = ..., motionPaths: bool = ..., mp: bool = ..., shape: bool = ..., s: bool = ..., staticChannels: bool = ..., sc: bool = ..., timeAnimationCurves: bool = ..., tac: bool = ..., unitlessAnimationCurves: bool = ..., uac: bool = ...) -> None:
    """delete is undoable, NOT queryable, and NOT editable.
    
    This command is used to delete selected objects, or all objects, or objects
    specified along with the command. Flags are available to filter the type of
    objects that the command acts on.
    
    At times, more than just specified items will be deleted. For example,
    deleting two CVs in the same "row" on a NURBS surface will delete the whole
    row.

    ---
    - Args:
        - objects: Input item(s).
        - all: Remove all objects of specified kind, in the scene. This flag is to be used in conjunction with the following flags.
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - channels (c): Remove animation channels in the scene. Either all channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - constraints (cn): Remove selected constraints and constraints attached to the selected nodes, or remove all constraints in the scene.
        - constructionHistory (ch): Remove the construction history on the objects specified or selected.
        - controlPoints (cp): This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - expressions (e): Remove expressions in the scene. Either all expressions can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - hierarchy (hi): Hierarchy expansion options.  Valid values are "above," "below," "both," and "none."(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - inputConnectionsAndNodes (icn): Break input connection to specified attribute and delete all unconnected nodes that are left behind. The graph will be traversed until a node that cannot be deleted is encountered.
        - motionPaths (mp): Remove motion paths in the scene. Either all motion paths can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - shape (s): Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - staticChannels (sc): Remove static animation channels in the scene. Either all static channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        - timeAnimationCurves (tac): Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to time-input animation curves (for instance, those created by 'setKeyframe' will be deleted.  When false, no time-input animation curves will be
            deleted. Default: true.
        - unitlessAnimationCurves (uac): Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to unitless-input animation curves (for instance, those created by 'setDrivenKeyframe' will be deleted.  When false, no unitless-input animation
            curves will be deleted.  Default: true.
    """
@overload #Overload for delete in ['query']
def delete(objects: objects, attribute: str = ..., query: bool = ...) -> None:
    """delete is undoable, NOT queryable, and NOT editable.
    
    This command is used to delete selected objects, or all objects, or objects
    specified along with the command. Flags are available to filter the type of
    objects that the command acts on.
    
    At times, more than just specified items will be deleted. For example,
    deleting two CVs in the same "row" on a NURBS surface will delete the whole
    row.

    ---
    - Args:
        - objects: Input item(s).
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - query (q): Query mode flag
    """
@overload #Overload for delete in ['query']
def delete(objects: objects, at: str = ..., q: bool = ...) -> None:
    """delete is undoable, NOT queryable, and NOT editable.
    
    This command is used to delete selected objects, or all objects, or objects
    specified along with the command. Flags are available to filter the type of
    objects that the command acts on.
    
    At times, more than just specified items will be deleted. For example,
    deleting two CVs in the same "row" on a NURBS surface will delete the whole
    row.

    ---
    - Args:
        - objects: Input item(s).
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - query (q): Query mode flag
    """
@overload #Overload for delete in ['query']
def delete(objects: objects, attribute: str = ..., at: str = ..., query: bool = ..., q: bool = ...) -> None:
    """delete is undoable, NOT queryable, and NOT editable.
    
    This command is used to delete selected objects, or all objects, or objects
    specified along with the command. Flags are available to filter the type of
    objects that the command acts on.
    
    At times, more than just specified items will be deleted. For example,
    deleting two CVs in the same "row" on a NURBS surface will delete the whole
    row.

    ---
    - Args:
        - objects: Input item(s).
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - query (q): Query mode flag
    """
@overload #Overload for delete in ['edit']
def delete(objects: objects, attribute: str = ..., edit: bool = ...) -> None:
    """delete is undoable, NOT queryable, and NOT editable.
    
    This command is used to delete selected objects, or all objects, or objects
    specified along with the command. Flags are available to filter the type of
    objects that the command acts on.
    
    At times, more than just specified items will be deleted. For example,
    deleting two CVs in the same "row" on a NURBS surface will delete the whole
    row.

    ---
    - Args:
        - objects: Input item(s).
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - edit (e): Edit mode flag
    """
@overload #Overload for delete in ['edit']
def delete(objects: objects, at: str = ..., e: bool = ...) -> None:
    """delete is undoable, NOT queryable, and NOT editable.
    
    This command is used to delete selected objects, or all objects, or objects
    specified along with the command. Flags are available to filter the type of
    objects that the command acts on.
    
    At times, more than just specified items will be deleted. For example,
    deleting two CVs in the same "row" on a NURBS surface will delete the whole
    row.

    ---
    - Args:
        - objects: Input item(s).
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - edit (e): Edit mode flag
    """
@overload #Overload for delete in ['edit']
def delete(objects: objects, attribute: str = ..., at: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """delete is undoable, NOT queryable, and NOT editable.
    
    This command is used to delete selected objects, or all objects, or objects
    specified along with the command. Flags are available to filter the type of
    objects that the command acts on.
    
    At times, more than just specified items will be deleted. For example,
    deleting two CVs in the same "row" on a NURBS surface will delete the whole
    row.

    ---
    - Args:
        - objects: Input item(s).
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - edit (e): Edit mode flag
    """
