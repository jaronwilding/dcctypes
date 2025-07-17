"""Stub files for Selection category in Maya commands, command: selectKey."""

from typing import Any, overload

@overload #Overload for selectKey in ['create']
def selectKey([targetList]: [targetList], addTo: bool = ..., animation: str = ..., attribute: str = ..., clear: bool = ..., controlPoints: bool = ..., float: floatrange = ..., hierarchy: str = ..., inTangent: bool = ..., includeUpperBound: bool = ..., index: int = ..., keyframe: bool = ..., outTangent: bool = ..., remove: bool = ..., replace: bool = ..., shape: bool = ..., time: timerange = ..., toggle: bool = ..., unsnappedKeys: float = ...) -> int:
    """selectKey is undoable, NOT queryable, and NOT editable.
    
    This command operates on a keyset. A keyset is defined as a group of keys
    within a specified time range on one or more animation curves.
    
    The animation curves comprising a keyset depend on the value of the
    "-animation" flag:
    
    * keysOrObjects:
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or
    
    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
    
    * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
    
    * objects: Only act on specified objects. If there are no objects specified, don't do anything.
    
    Note that the "-animation" flag can be used to override the curves uniquely
    identified by the multi-use "-attribute" flag, which takes an argument of the
    form attributeName, such as "translateX".
    
    Keys on animation curves are identified by either their time values or their
    indices. Times and indices can be given individually or as part of a list or
    range (see Examples).
    
    This command places keyframes and/or keyframe tangents on the active list.

    Example:
    ```python
        import maya.cmds as cmds
        # Keys on animation curves are identified by either
        # their time values or their indices.  Times and indices can
        # be given as a range or list of ranges.
        # time=('10pal','10pal') means the key at frame 10 (PAL format).
        # time=[('1.0sec','1.0sec'),('15ntsc','15ntsc'),(20,20)] means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
        # time=(10,20) means all keys in the range from 10 to 20, inclusive, in the current time unit.
        # Omitting one end of a range means "go to infinity", as in the following examples:
        # time=(10,None) means all keys from time 10 (in the current time unit) onwards.
        # time=(10,) means the same as (10,10)
        # time=(0,10) means all keys up to (and including) time 10 (in the current time unit).
        # time=(None,None) is a short form to specify all keys.
        # index=(0,0) means the first key of each animation curve. (Indices are 0-based.)
        # index=[(2,2),(5,5),(7,7)] means the 3rd, 6th, and 8th keys.
        # index=(1,5) means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
        # Select all translateX keyframes on nurbsSphere1 in the range 10 to 20.
        #
        cmds.selectKey( 'nurbsSphere1', time=(10,20), attribute='translateX' )
        # select all the animation of the active objects, range 0-30
        #
        cmds.selectKey( time=(0,30) )
    ```

    ---
    - Args:
        - [targetList]: Input item(s).
        - addTo (add): Add to the current selection of keyframes/tangents
        - animation (an): Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - clear (cl): Remove all keyframes and tangents from the active list.
        - controlPoints (cp): This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - float (f): value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")In query mode, this flag
            needs a value.
        - hierarchy (hi): Hierarchy expansion options.  Valid values are "above," "below," "both," and "none."(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - inTangent (it): Select in-tangents of keyframes in the specified time range
        - includeUpperBound (iub): When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time
            flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."
            This flag has no effect on the curve pasted from the clipboard.)
        - index: index of a key on an animCurveIn query mode, this flag needs a value.
        - keyframe (k): select only keyframes (cannot be combined with -in/-out)
        - outTangent (ot): Select out-tangents of keyframes in the specified time range
        - remove (rm): Remove from the current selection of keyframes/tangents
        - replace (r): Replace the current selection of keyframes/tangents
        - shape (s): Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - time (t): time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.In query mode, this flag needs a value.
        - toggle (tgl): Toggle the picked state of the specified keyset
        - unsnappedKeys (uk): Select only keys that have times that are not a multiple of the specified numeric value.
    """
@overload #Overload for selectKey in ['create']
def selectKey([targetList]: [targetList], add: bool = ..., an: str = ..., at: str = ..., cl: bool = ..., cp: bool = ..., f: floatrange = ..., hi: str = ..., it: bool = ..., iub: bool = ..., k: bool = ..., ot: bool = ..., rm: bool = ..., r: bool = ..., s: bool = ..., t: timerange = ..., tgl: bool = ..., uk: float = ...) -> int:
    """selectKey is undoable, NOT queryable, and NOT editable.
    
    This command operates on a keyset. A keyset is defined as a group of keys
    within a specified time range on one or more animation curves.
    
    The animation curves comprising a keyset depend on the value of the
    "-animation" flag:
    
    * keysOrObjects:
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or
    
    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
    
    * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
    
    * objects: Only act on specified objects. If there are no objects specified, don't do anything.
    
    Note that the "-animation" flag can be used to override the curves uniquely
    identified by the multi-use "-attribute" flag, which takes an argument of the
    form attributeName, such as "translateX".
    
    Keys on animation curves are identified by either their time values or their
    indices. Times and indices can be given individually or as part of a list or
    range (see Examples).
    
    This command places keyframes and/or keyframe tangents on the active list.

    Example:
    ```python
        import maya.cmds as cmds
        # Keys on animation curves are identified by either
        # their time values or their indices.  Times and indices can
        # be given as a range or list of ranges.
        # time=('10pal','10pal') means the key at frame 10 (PAL format).
        # time=[('1.0sec','1.0sec'),('15ntsc','15ntsc'),(20,20)] means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
        # time=(10,20) means all keys in the range from 10 to 20, inclusive, in the current time unit.
        # Omitting one end of a range means "go to infinity", as in the following examples:
        # time=(10,None) means all keys from time 10 (in the current time unit) onwards.
        # time=(10,) means the same as (10,10)
        # time=(0,10) means all keys up to (and including) time 10 (in the current time unit).
        # time=(None,None) is a short form to specify all keys.
        # index=(0,0) means the first key of each animation curve. (Indices are 0-based.)
        # index=[(2,2),(5,5),(7,7)] means the 3rd, 6th, and 8th keys.
        # index=(1,5) means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
        # Select all translateX keyframes on nurbsSphere1 in the range 10 to 20.
        #
        cmds.selectKey( 'nurbsSphere1', time=(10,20), attribute='translateX' )
        # select all the animation of the active objects, range 0-30
        #
        cmds.selectKey( time=(0,30) )
    ```

    ---
    - Args:
        - [targetList]: Input item(s).
        - addTo (add): Add to the current selection of keyframes/tangents
        - animation (an): Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - clear (cl): Remove all keyframes and tangents from the active list.
        - controlPoints (cp): This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - float (f): value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")In query mode, this flag
            needs a value.
        - hierarchy (hi): Hierarchy expansion options.  Valid values are "above," "below," "both," and "none."(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - inTangent (it): Select in-tangents of keyframes in the specified time range
        - includeUpperBound (iub): When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time
            flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."
            This flag has no effect on the curve pasted from the clipboard.)
        - index: index of a key on an animCurveIn query mode, this flag needs a value.
        - keyframe (k): select only keyframes (cannot be combined with -in/-out)
        - outTangent (ot): Select out-tangents of keyframes in the specified time range
        - remove (rm): Remove from the current selection of keyframes/tangents
        - replace (r): Replace the current selection of keyframes/tangents
        - shape (s): Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - time (t): time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.In query mode, this flag needs a value.
        - toggle (tgl): Toggle the picked state of the specified keyset
        - unsnappedKeys (uk): Select only keys that have times that are not a multiple of the specified numeric value.
    """
@overload #Overload for selectKey in ['create']
def selectKey([targetList]: [targetList], addTo: bool = ..., add: bool = ..., animation: str = ..., an: str = ..., attribute: str = ..., at: str = ..., clear: bool = ..., cl: bool = ..., controlPoints: bool = ..., cp: bool = ..., float: floatrange = ..., f: floatrange = ..., hierarchy: str = ..., hi: str = ..., inTangent: bool = ..., it: bool = ..., includeUpperBound: bool = ..., iub: bool = ..., index: int = ..., keyframe: bool = ..., k: bool = ..., outTangent: bool = ..., ot: bool = ..., remove: bool = ..., rm: bool = ..., replace: bool = ..., r: bool = ..., shape: bool = ..., s: bool = ..., time: timerange = ..., t: timerange = ..., toggle: bool = ..., tgl: bool = ..., unsnappedKeys: float = ..., uk: float = ...) -> int:
    """selectKey is undoable, NOT queryable, and NOT editable.
    
    This command operates on a keyset. A keyset is defined as a group of keys
    within a specified time range on one or more animation curves.
    
    The animation curves comprising a keyset depend on the value of the
    "-animation" flag:
    
    * keysOrObjects:
    1. Any active keys, when no target objects or -attribute flags appear on the command line, or
    
    2. All animation curves connected to all keyframable attributes of objects specified as the command line's targetList, when there are no active keys.
    
    * keys: Only act on active keys or tangents. If there are no active keys or tangents, don't do anything.
    
    * objects: Only act on specified objects. If there are no objects specified, don't do anything.
    
    Note that the "-animation" flag can be used to override the curves uniquely
    identified by the multi-use "-attribute" flag, which takes an argument of the
    form attributeName, such as "translateX".
    
    Keys on animation curves are identified by either their time values or their
    indices. Times and indices can be given individually or as part of a list or
    range (see Examples).
    
    This command places keyframes and/or keyframe tangents on the active list.

    Example:
    ```python
        import maya.cmds as cmds
        # Keys on animation curves are identified by either
        # their time values or their indices.  Times and indices can
        # be given as a range or list of ranges.
        # time=('10pal','10pal') means the key at frame 10 (PAL format).
        # time=[('1.0sec','1.0sec'),('15ntsc','15ntsc'),(20,20)] means the keys at time 1.0 second, frame 15 (in NTSC format), and time 20 (in the currently defined global time unit).
        # time=(10,20) means all keys in the range from 10 to 20, inclusive, in the current time unit.
        # Omitting one end of a range means "go to infinity", as in the following examples:
        # time=(10,None) means all keys from time 10 (in the current time unit) onwards.
        # time=(10,) means the same as (10,10)
        # time=(0,10) means all keys up to (and including) time 10 (in the current time unit).
        # time=(None,None) is a short form to specify all keys.
        # index=(0,0) means the first key of each animation curve. (Indices are 0-based.)
        # index=[(2,2),(5,5),(7,7)] means the 3rd, 6th, and 8th keys.
        # index=(1,5) means the 2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
        # Select all translateX keyframes on nurbsSphere1 in the range 10 to 20.
        #
        cmds.selectKey( 'nurbsSphere1', time=(10,20), attribute='translateX' )
        # select all the animation of the active objects, range 0-30
        #
        cmds.selectKey( time=(0,30) )
    ```

    ---
    - Args:
        - [targetList]: Input item(s).
        - addTo (add): Add to the current selection of keyframes/tangents
        - animation (an): Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        - attribute (at): List of attributes to selectIn query mode, this flag needs a value.
        - clear (cl): Remove all keyframes and tangents from the active list.
        - controlPoints (cp): This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - float (f): value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")In query mode, this flag
            needs a value.
        - hierarchy (hi): Hierarchy expansion options.  Valid values are "above," "below," "both," and "none."(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - inTangent (it): Select in-tangents of keyframes in the specified time range
        - includeUpperBound (iub): When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time
            flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."
            This flag has no effect on the curve pasted from the clipboard.)
        - index: index of a key on an animCurveIn query mode, this flag needs a value.
        - keyframe (k): select only keyframes (cannot be combined with -in/-out)
        - outTangent (ot): Select out-tangents of keyframes in the specified time range
        - remove (rm): Remove from the current selection of keyframes/tangents
        - replace (r): Replace the current selection of keyframes/tangents
        - shape (s): Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.(Not valid for "pasteKey" cmd.)In query mode, this flag needs a value.
        - time (t): time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.In query mode, this flag needs a value.
        - toggle (tgl): Toggle the picked state of the specified keyset
        - unsnappedKeys (uk): Select only keys that have times that are not a multiple of the specified numeric value.
    """
