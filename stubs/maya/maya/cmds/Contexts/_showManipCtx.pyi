"""Stub files for Contexts category in Maya commands, command: showManipCtx."""

from typing import Any, overload

@overload #Overload for showManipCtx in ['create']
def showManipCtx(string: str, exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., incSnap: [uint, boolean] = ..., incSnapRelative: [uint, boolean] = ..., incSnapValue: [uint, float] = ..., lockSelection: bool = ..., name: str = ..., toggleIncSnap: bool = ..., toolFinish: script = ..., toolStart: script = ...) -> str:
    """showManipCtx is undoable, queryable, and editable.
    
    This command can be used to create a show manip context. The show manip
    context will display manips for all selected objects that have valid manips
    defined for them.

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a new show manip context.
        cmds.showManipCtx()
    ```

    ---
    - Args:
        - string: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - incSnap: If true, the manipulator owned by the context will use incremental snapping for specified mode.
        - incSnapRelative (isr): If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
        - incSnapValue (isv): Supply the step value which the manipulator owned by the context will use for specified mode.
        - lockSelection (ls): If true, this context will never change the current selection. By default this is set to false.
        - name (n): If this is a tool command, name the tool appropriately.
        - toggleIncSnap (tis): Toggles (enables/disables) snapping for all modes.
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
    """
@overload #Overload for showManipCtx in ['create']
def showManipCtx(string: str, ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., isr: [uint, boolean] = ..., isv: [uint, float] = ..., ls: bool = ..., n: str = ..., tis: bool = ..., tf: script = ..., ts: script = ...) -> str:
    """showManipCtx is undoable, queryable, and editable.
    
    This command can be used to create a show manip context. The show manip
    context will display manips for all selected objects that have valid manips
    defined for them.

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a new show manip context.
        cmds.showManipCtx()
    ```

    ---
    - Args:
        - string: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - incSnap: If true, the manipulator owned by the context will use incremental snapping for specified mode.
        - incSnapRelative (isr): If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
        - incSnapValue (isv): Supply the step value which the manipulator owned by the context will use for specified mode.
        - lockSelection (ls): If true, this context will never change the current selection. By default this is set to false.
        - name (n): If this is a tool command, name the tool appropriately.
        - toggleIncSnap (tis): Toggles (enables/disables) snapping for all modes.
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
    """
@overload #Overload for showManipCtx in ['create']
def showManipCtx(string: str, exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., incSnap: [uint, boolean] = ..., incSnapRelative: [uint, boolean] = ..., isr: [uint, boolean] = ..., incSnapValue: [uint, float] = ..., isv: [uint, float] = ..., lockSelection: bool = ..., ls: bool = ..., name: str = ..., n: str = ..., toggleIncSnap: bool = ..., tis: bool = ..., toolFinish: script = ..., tf: script = ..., toolStart: script = ..., ts: script = ...) -> str:
    """showManipCtx is undoable, queryable, and editable.
    
    This command can be used to create a show manip context. The show manip
    context will display manips for all selected objects that have valid manips
    defined for them.

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a new show manip context.
        cmds.showManipCtx()
    ```

    ---
    - Args:
        - string: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - incSnap: If true, the manipulator owned by the context will use incremental snapping for specified mode.
        - incSnapRelative (isr): If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
        - incSnapValue (isv): Supply the step value which the manipulator owned by the context will use for specified mode.
        - lockSelection (ls): If true, this context will never change the current selection. By default this is set to false.
        - name (n): If this is a tool command, name the tool appropriately.
        - toggleIncSnap (tis): Toggles (enables/disables) snapping for all modes.
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
    """
@overload #Overload for showManipCtx in ['query']
def showManipCtx(string: str, currentNodeName: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., incSnap: [uint, boolean] = ..., incSnapRelative: [uint, boolean] = ..., incSnapUI: bool = ..., incSnapValue: [uint, float] = ..., iveVisible: bool = ..., lockSelection: bool = ..., selectedAttributes: bool = ..., toolFinish: script = ..., toolStart: script = ..., query: bool = ...) -> str:
    """showManipCtx is undoable, queryable, and editable.
    
    This command can be used to create a show manip context. The show manip
    context will display manips for all selected objects that have valid manips
    defined for them.

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a new show manip context.
        cmds.showManipCtx()
    ```

    ---
    - Args:
        - string: Input item(s).
        - currentNodeName (cnn): Returns the name of the first node that the context is attached to.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - incSnap: If true, the manipulator owned by the context will use incremental snapping for specified mode.
        - incSnapRelative (isr): If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
        - incSnapUI (isu): Returns an array of elements indicating what kind of incremental snap UI is required by the manipulator owned by the context. If no UI is required, the result array will contain a single element of with the value 0. The other values and
            their meanings are:1 - UI for linear incremental translate2 - UI for incremental rotate3 - UI for inclremental scale
        - incSnapValue (isv): Supply the step value which the manipulator owned by the context will use for specified mode.
        - iveVisible (iv): Set the In View Editor visible or not.
        - lockSelection (ls): If true, this context will never change the current selection. By default this is set to false.
        - selectedAttributes (sa): Returns a list of the names of the attributes that are currently visible in the In View Editor.
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - query (q): Query mode flag
    """
@overload #Overload for showManipCtx in ['query']
def showManipCtx(string: str, cnn: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., isr: [uint, boolean] = ..., isu: bool = ..., isv: [uint, float] = ..., iv: bool = ..., ls: bool = ..., sa: bool = ..., tf: script = ..., ts: script = ..., q: bool = ...) -> str:
    """showManipCtx is undoable, queryable, and editable.
    
    This command can be used to create a show manip context. The show manip
    context will display manips for all selected objects that have valid manips
    defined for them.

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a new show manip context.
        cmds.showManipCtx()
    ```

    ---
    - Args:
        - string: Input item(s).
        - currentNodeName (cnn): Returns the name of the first node that the context is attached to.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - incSnap: If true, the manipulator owned by the context will use incremental snapping for specified mode.
        - incSnapRelative (isr): If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
        - incSnapUI (isu): Returns an array of elements indicating what kind of incremental snap UI is required by the manipulator owned by the context. If no UI is required, the result array will contain a single element of with the value 0. The other values and
            their meanings are:1 - UI for linear incremental translate2 - UI for incremental rotate3 - UI for inclremental scale
        - incSnapValue (isv): Supply the step value which the manipulator owned by the context will use for specified mode.
        - iveVisible (iv): Set the In View Editor visible or not.
        - lockSelection (ls): If true, this context will never change the current selection. By default this is set to false.
        - selectedAttributes (sa): Returns a list of the names of the attributes that are currently visible in the In View Editor.
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - query (q): Query mode flag
    """
@overload #Overload for showManipCtx in ['query']
def showManipCtx(string: str, currentNodeName: bool = ..., cnn: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., incSnap: [uint, boolean] = ..., incSnapRelative: [uint, boolean] = ..., isr: [uint, boolean] = ..., incSnapUI: bool = ..., isu: bool = ..., incSnapValue: [uint, float] = ..., isv: [uint, float] = ..., iveVisible: bool = ..., iv: bool = ..., lockSelection: bool = ..., ls: bool = ..., selectedAttributes: bool = ..., sa: bool = ..., toolFinish: script = ..., tf: script = ..., toolStart: script = ..., ts: script = ..., query: bool = ..., q: bool = ...) -> str:
    """showManipCtx is undoable, queryable, and editable.
    
    This command can be used to create a show manip context. The show manip
    context will display manips for all selected objects that have valid manips
    defined for them.

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a new show manip context.
        cmds.showManipCtx()
    ```

    ---
    - Args:
        - string: Input item(s).
        - currentNodeName (cnn): Returns the name of the first node that the context is attached to.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - incSnap: If true, the manipulator owned by the context will use incremental snapping for specified mode.
        - incSnapRelative (isr): If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
        - incSnapUI (isu): Returns an array of elements indicating what kind of incremental snap UI is required by the manipulator owned by the context. If no UI is required, the result array will contain a single element of with the value 0. The other values and
            their meanings are:1 - UI for linear incremental translate2 - UI for incremental rotate3 - UI for inclremental scale
        - incSnapValue (isv): Supply the step value which the manipulator owned by the context will use for specified mode.
        - iveVisible (iv): Set the In View Editor visible or not.
        - lockSelection (ls): If true, this context will never change the current selection. By default this is set to false.
        - selectedAttributes (sa): Returns a list of the names of the attributes that are currently visible in the In View Editor.
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - query (q): Query mode flag
    """
@overload #Overload for showManipCtx in ['edit']
def showManipCtx(string: str, addAttr: str = ..., image1: str = ..., image2: str = ..., image3: str = ..., incSnap: [uint, boolean] = ..., incSnapRelative: [uint, boolean] = ..., incSnapValue: [uint, float] = ..., iveVisible: bool = ..., lockSelection: bool = ..., moveActiveAttrDown: bool = ..., moveActiveAttrToTop: bool = ..., moveActiveAttrUp: bool = ..., removeAttr: str = ..., resetActiveAttr: bool = ..., setAttrActive: str = ..., setNextAttrActive: bool = ..., setPreviousAttrActive: bool = ..., toggleIncSnap: bool = ..., toolFinish: script = ..., toolStart: script = ..., edit: bool = ...) -> str:
    """showManipCtx is undoable, queryable, and editable.
    
    This command can be used to create a show manip context. The show manip
    context will display manips for all selected objects that have valid manips
    defined for them.

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a new show manip context.
        cmds.showManipCtx()
    ```

    ---
    - Args:
        - string: Input item(s).
        - addAttr (aa): Add a specific attribute to the In View Editor attribute list.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - incSnap: If true, the manipulator owned by the context will use incremental snapping for specified mode.
        - incSnapRelative (isr): If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
        - incSnapValue (isv): Supply the step value which the manipulator owned by the context will use for specified mode.
        - iveVisible (iv): Set the In View Editor visible or not.
        - lockSelection (ls): If true, this context will never change the current selection. By default this is set to false.
        - moveActiveAttrDown (md): Move the In View Editor active attribute down one in the list.
        - moveActiveAttrToTop (mtt): Move the In View Editor active attribute to the top of the list.
        - moveActiveAttrUp (mu): Move the In View Editor active attribute up one in the list.
        - removeAttr (ra): Remove a specific attribute from the In View Editor attribute list.
        - resetActiveAttr (raa): Reset the In View Editor active attribute to its default value.
        - setAttrActive (saa): Set a specific attribute from the In View Editor attribute list active.
        - setNextAttrActive (sna): Set the next attribute in the In View Editor attribute list active.
        - setPreviousAttrActive (spa): Set the previous attribute in the In View Editor attribute list active.
        - toggleIncSnap (tis): Toggles (enables/disables) snapping for all modes.
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - edit (e): Edit mode flag
    """
@overload #Overload for showManipCtx in ['edit']
def showManipCtx(string: str, aa: str = ..., i1: str = ..., i2: str = ..., i3: str = ..., isr: [uint, boolean] = ..., isv: [uint, float] = ..., iv: bool = ..., ls: bool = ..., md: bool = ..., mtt: bool = ..., mu: bool = ..., ra: str = ..., raa: bool = ..., saa: str = ..., sna: bool = ..., spa: bool = ..., tis: bool = ..., tf: script = ..., ts: script = ..., e: bool = ...) -> str:
    """showManipCtx is undoable, queryable, and editable.
    
    This command can be used to create a show manip context. The show manip
    context will display manips for all selected objects that have valid manips
    defined for them.

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a new show manip context.
        cmds.showManipCtx()
    ```

    ---
    - Args:
        - string: Input item(s).
        - addAttr (aa): Add a specific attribute to the In View Editor attribute list.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - incSnap: If true, the manipulator owned by the context will use incremental snapping for specified mode.
        - incSnapRelative (isr): If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
        - incSnapValue (isv): Supply the step value which the manipulator owned by the context will use for specified mode.
        - iveVisible (iv): Set the In View Editor visible or not.
        - lockSelection (ls): If true, this context will never change the current selection. By default this is set to false.
        - moveActiveAttrDown (md): Move the In View Editor active attribute down one in the list.
        - moveActiveAttrToTop (mtt): Move the In View Editor active attribute to the top of the list.
        - moveActiveAttrUp (mu): Move the In View Editor active attribute up one in the list.
        - removeAttr (ra): Remove a specific attribute from the In View Editor attribute list.
        - resetActiveAttr (raa): Reset the In View Editor active attribute to its default value.
        - setAttrActive (saa): Set a specific attribute from the In View Editor attribute list active.
        - setNextAttrActive (sna): Set the next attribute in the In View Editor attribute list active.
        - setPreviousAttrActive (spa): Set the previous attribute in the In View Editor attribute list active.
        - toggleIncSnap (tis): Toggles (enables/disables) snapping for all modes.
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - edit (e): Edit mode flag
    """
@overload #Overload for showManipCtx in ['edit']
def showManipCtx(string: str, addAttr: str = ..., aa: str = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., incSnap: [uint, boolean] = ..., incSnapRelative: [uint, boolean] = ..., isr: [uint, boolean] = ..., incSnapValue: [uint, float] = ..., isv: [uint, float] = ..., iveVisible: bool = ..., iv: bool = ..., lockSelection: bool = ..., ls: bool = ..., moveActiveAttrDown: bool = ..., md: bool = ..., moveActiveAttrToTop: bool = ..., mtt: bool = ..., moveActiveAttrUp: bool = ..., mu: bool = ..., removeAttr: str = ..., ra: str = ..., resetActiveAttr: bool = ..., raa: bool = ..., setAttrActive: str = ..., saa: str = ..., setNextAttrActive: bool = ..., sna: bool = ..., setPreviousAttrActive: bool = ..., spa: bool = ..., toggleIncSnap: bool = ..., tis: bool = ..., toolFinish: script = ..., tf: script = ..., toolStart: script = ..., ts: script = ..., edit: bool = ..., e: bool = ...) -> str:
    """showManipCtx is undoable, queryable, and editable.
    
    This command can be used to create a show manip context. The show manip
    context will display manips for all selected objects that have valid manips
    defined for them.

    Example:
    ```python
        import maya.cmds as cmds
        # Creates a new show manip context.
        cmds.showManipCtx()
    ```

    ---
    - Args:
        - string: Input item(s).
        - addAttr (aa): Add a specific attribute to the In View Editor attribute list.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - incSnap: If true, the manipulator owned by the context will use incremental snapping for specified mode.
        - incSnapRelative (isr): If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
        - incSnapValue (isv): Supply the step value which the manipulator owned by the context will use for specified mode.
        - iveVisible (iv): Set the In View Editor visible or not.
        - lockSelection (ls): If true, this context will never change the current selection. By default this is set to false.
        - moveActiveAttrDown (md): Move the In View Editor active attribute down one in the list.
        - moveActiveAttrToTop (mtt): Move the In View Editor active attribute to the top of the list.
        - moveActiveAttrUp (mu): Move the In View Editor active attribute up one in the list.
        - removeAttr (ra): Remove a specific attribute from the In View Editor attribute list.
        - resetActiveAttr (raa): Reset the In View Editor active attribute to its default value.
        - setAttrActive (saa): Set a specific attribute from the In View Editor attribute list active.
        - setNextAttrActive (sna): Set the next attribute in the In View Editor attribute list active.
        - setPreviousAttrActive (spa): Set the previous attribute in the In View Editor attribute list active.
        - toggleIncSnap (tis): Toggles (enables/disables) snapping for all modes.
        - toolFinish (tf): Supply the script that will be run when the user exits the script.
        - toolStart (ts): Supply the script that will be run when the user first enters the script
        - edit (e): Edit mode flag
    """
