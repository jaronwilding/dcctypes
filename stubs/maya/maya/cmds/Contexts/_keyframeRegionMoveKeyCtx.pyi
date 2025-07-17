"""Stub files for Contexts category in Maya commands, command: keyframeRegionMoveKeyCtx."""

from typing import Any, overload

@overload #Overload for keyframeRegionMoveKeyCtx in ['create']
def keyframeRegionMoveKeyCtx(contextName: contextName, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., option: str = ...) -> str:
    """keyframeRegionMoveKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to move keyframes within the
    keyframe region of the dope sheet editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a move key context which works in insert mode
        # for the dope sheet editor
        #
        cmds.keyframeRegionMoveKeyCtx( 'keyframeRegionMoveKeyContext', option='insert' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - option (o): Valid values are "move," "insert," "over," "segmentOver" and "ripple". Specifies the keyframe -option to use. When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before
            or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option
            only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to
            make room for the segment. When you move a set of keys with "ripple" all keys after the selected ones will be moved by the same amount.
    """
@overload #Overload for keyframeRegionMoveKeyCtx in ['create']
def keyframeRegionMoveKeyCtx(contextName: contextName, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., o: str = ...) -> str:
    """keyframeRegionMoveKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to move keyframes within the
    keyframe region of the dope sheet editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a move key context which works in insert mode
        # for the dope sheet editor
        #
        cmds.keyframeRegionMoveKeyCtx( 'keyframeRegionMoveKeyContext', option='insert' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - option (o): Valid values are "move," "insert," "over," "segmentOver" and "ripple". Specifies the keyframe -option to use. When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before
            or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option
            only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to
            make room for the segment. When you move a set of keys with "ripple" all keys after the selected ones will be moved by the same amount.
    """
@overload #Overload for keyframeRegionMoveKeyCtx in ['create']
def keyframeRegionMoveKeyCtx(contextName: contextName, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., option: str = ..., o: str = ...) -> str:
    """keyframeRegionMoveKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to move keyframes within the
    keyframe region of the dope sheet editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a move key context which works in insert mode
        # for the dope sheet editor
        #
        cmds.keyframeRegionMoveKeyCtx( 'keyframeRegionMoveKeyContext', option='insert' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - option (o): Valid values are "move," "insert," "over," "segmentOver" and "ripple". Specifies the keyframe -option to use. When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before
            or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option
            only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to
            make room for the segment. When you move a set of keys with "ripple" all keys after the selected ones will be moved by the same amount.
    """
@overload #Overload for keyframeRegionMoveKeyCtx in ['query']
def keyframeRegionMoveKeyCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., option: str = ..., query: bool = ...) -> str:
    """keyframeRegionMoveKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to move keyframes within the
    keyframe region of the dope sheet editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a move key context which works in insert mode
        # for the dope sheet editor
        #
        cmds.keyframeRegionMoveKeyCtx( 'keyframeRegionMoveKeyContext', option='insert' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - option (o): Valid values are "move," "insert," "over," "segmentOver" and "ripple". Specifies the keyframe -option to use. When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before
            or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option
            only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to
            make room for the segment. When you move a set of keys with "ripple" all keys after the selected ones will be moved by the same amount.
        - query (q): Query mode flag
    """
@overload #Overload for keyframeRegionMoveKeyCtx in ['query']
def keyframeRegionMoveKeyCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., o: str = ..., q: bool = ...) -> str:
    """keyframeRegionMoveKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to move keyframes within the
    keyframe region of the dope sheet editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a move key context which works in insert mode
        # for the dope sheet editor
        #
        cmds.keyframeRegionMoveKeyCtx( 'keyframeRegionMoveKeyContext', option='insert' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - option (o): Valid values are "move," "insert," "over," "segmentOver" and "ripple". Specifies the keyframe -option to use. When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before
            or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option
            only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to
            make room for the segment. When you move a set of keys with "ripple" all keys after the selected ones will be moved by the same amount.
        - query (q): Query mode flag
    """
@overload #Overload for keyframeRegionMoveKeyCtx in ['query']
def keyframeRegionMoveKeyCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., option: str = ..., o: str = ..., query: bool = ..., q: bool = ...) -> str:
    """keyframeRegionMoveKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to move keyframes within the
    keyframe region of the dope sheet editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a move key context which works in insert mode
        # for the dope sheet editor
        #
        cmds.keyframeRegionMoveKeyCtx( 'keyframeRegionMoveKeyContext', option='insert' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - option (o): Valid values are "move," "insert," "over," "segmentOver" and "ripple". Specifies the keyframe -option to use. When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before
            or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option
            only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to
            make room for the segment. When you move a set of keys with "ripple" all keys after the selected ones will be moved by the same amount.
        - query (q): Query mode flag
    """
@overload #Overload for keyframeRegionMoveKeyCtx in ['edit']
def keyframeRegionMoveKeyCtx(contextName: contextName, image1: str = ..., image2: str = ..., image3: str = ..., option: str = ..., edit: bool = ...) -> str:
    """keyframeRegionMoveKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to move keyframes within the
    keyframe region of the dope sheet editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a move key context which works in insert mode
        # for the dope sheet editor
        #
        cmds.keyframeRegionMoveKeyCtx( 'keyframeRegionMoveKeyContext', option='insert' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - option (o): Valid values are "move," "insert," "over," "segmentOver" and "ripple". Specifies the keyframe -option to use. When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before
            or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option
            only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to
            make room for the segment. When you move a set of keys with "ripple" all keys after the selected ones will be moved by the same amount.
        - edit (e): Edit mode flag
    """
@overload #Overload for keyframeRegionMoveKeyCtx in ['edit']
def keyframeRegionMoveKeyCtx(contextName: contextName, i1: str = ..., i2: str = ..., i3: str = ..., o: str = ..., e: bool = ...) -> str:
    """keyframeRegionMoveKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to move keyframes within the
    keyframe region of the dope sheet editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a move key context which works in insert mode
        # for the dope sheet editor
        #
        cmds.keyframeRegionMoveKeyCtx( 'keyframeRegionMoveKeyContext', option='insert' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - option (o): Valid values are "move," "insert," "over," "segmentOver" and "ripple". Specifies the keyframe -option to use. When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before
            or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option
            only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to
            make room for the segment. When you move a set of keys with "ripple" all keys after the selected ones will be moved by the same amount.
        - edit (e): Edit mode flag
    """
@overload #Overload for keyframeRegionMoveKeyCtx in ['edit']
def keyframeRegionMoveKeyCtx(contextName: contextName, image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., option: str = ..., o: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """keyframeRegionMoveKeyCtx is undoable, queryable, and editable.
    
    This command creates a context which may be used to move keyframes within the
    keyframe region of the dope sheet editor

    Example:
    ```python
        import maya.cmds as cmds
        # Create a move key context which works in insert mode
        # for the dope sheet editor
        #
        cmds.keyframeRegionMoveKeyCtx( 'keyframeRegionMoveKeyContext', option='insert' )
    ```

    ---
    - Args:
        - contextName: Input item(s).
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - option (o): Valid values are "move," "insert," "over," "segmentOver" and "ripple". Specifies the keyframe -option to use. When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before
            or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option
            only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to
            make room for the segment. When you move a set of keys with "ripple" all keys after the selected ones will be moved by the same amount.
        - edit (e): Edit mode flag
    """
