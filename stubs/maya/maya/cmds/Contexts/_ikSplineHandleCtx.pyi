"""Stub files for Contexts category in Maya commands, command: ikSplineHandleCtx."""

from typing import Any, overload

@overload #Overload for ikSplineHandleCtx in ['create']
def ikSplineHandleCtx(object: object, autoPriorityH: bool = ..., createCurve: bool = ..., exists: bool = ..., forceSolverH: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., poWeightH: float = ..., priorityH: int = ..., snapHandleH: bool = ..., solverTypeH: str = ..., stickyH: str = ..., weightH: float = ...) -> str:
    """ikSplineHandleCtx is undoable, queryable, and editable.
    
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
    ikSplineHandle tool. The options for the tool will be set to the flags the
    user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Edit an existing context to create an ikSplineHandle with
        #    the curve parented to the corresponding joint.
        #
        if cmds.ikSplineHandleCtx( 'ikSplineHandleCtx', q=True, ex=True ):
        cmds.ikSplineHandleCtx('ikSplineHandleCtx', e=True, parentCurve=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - autoPriorityH (apH): Specifies that this handle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createCurve (ccv): Specifies if a curve should be automatically created for the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - forceSolverH (fsH): Specifies if the ikSolver is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - snapHandleH (snH): Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.C: The default solver is the ikSplineSolver.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver.C: The default is "off".Q: When queried, this flag returns a string.
        - weightH (wH): Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx.C: The default is 1.Q: When queried, this flag returns a float.
    """
@overload #Overload for ikSplineHandleCtx in ['create']
def ikSplineHandleCtx(object: object, apH: bool = ..., ccv: bool = ..., ex: bool = ..., fsH: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., pwH: float = ..., pH: int = ..., snH: bool = ..., stH: str = ..., sH: str = ..., wH: float = ...) -> str:
    """ikSplineHandleCtx is undoable, queryable, and editable.
    
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
    ikSplineHandle tool. The options for the tool will be set to the flags the
    user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Edit an existing context to create an ikSplineHandle with
        #    the curve parented to the corresponding joint.
        #
        if cmds.ikSplineHandleCtx( 'ikSplineHandleCtx', q=True, ex=True ):
        cmds.ikSplineHandleCtx('ikSplineHandleCtx', e=True, parentCurve=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - autoPriorityH (apH): Specifies that this handle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createCurve (ccv): Specifies if a curve should be automatically created for the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - forceSolverH (fsH): Specifies if the ikSolver is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - snapHandleH (snH): Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.C: The default solver is the ikSplineSolver.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver.C: The default is "off".Q: When queried, this flag returns a string.
        - weightH (wH): Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx.C: The default is 1.Q: When queried, this flag returns a float.
    """
@overload #Overload for ikSplineHandleCtx in ['create']
def ikSplineHandleCtx(object: object, autoPriorityH: bool = ..., apH: bool = ..., createCurve: bool = ..., ccv: bool = ..., exists: bool = ..., ex: bool = ..., forceSolverH: bool = ..., fsH: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., poWeightH: float = ..., pwH: float = ..., priorityH: int = ..., pH: int = ..., snapHandleH: bool = ..., snH: bool = ..., solverTypeH: str = ..., stH: str = ..., stickyH: str = ..., sH: str = ..., weightH: float = ..., wH: float = ...) -> str:
    """ikSplineHandleCtx is undoable, queryable, and editable.
    
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
    ikSplineHandle tool. The options for the tool will be set to the flags the
    user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Edit an existing context to create an ikSplineHandle with
        #    the curve parented to the corresponding joint.
        #
        if cmds.ikSplineHandleCtx( 'ikSplineHandleCtx', q=True, ex=True ):
        cmds.ikSplineHandleCtx('ikSplineHandleCtx', e=True, parentCurve=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - autoPriorityH (apH): Specifies that this handle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createCurve (ccv): Specifies if a curve should be automatically created for the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - forceSolverH (fsH): Specifies if the ikSolver is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - snapHandleH (snH): Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.C: The default solver is the ikSplineSolver.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver.C: The default is "off".Q: When queried, this flag returns a string.
        - weightH (wH): Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx.C: The default is 1.Q: When queried, this flag returns a float.
    """
@overload #Overload for ikSplineHandleCtx in ['query']
def ikSplineHandleCtx(object: object, autoPriorityH: bool = ..., createCurve: bool = ..., forceSolverH: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., poWeightH: float = ..., priorityH: int = ..., snapHandleH: bool = ..., solverTypeH: str = ..., stickyH: str = ..., weightH: float = ..., query: bool = ...) -> str:
    """ikSplineHandleCtx is undoable, queryable, and editable.
    
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
    ikSplineHandle tool. The options for the tool will be set to the flags the
    user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Edit an existing context to create an ikSplineHandle with
        #    the curve parented to the corresponding joint.
        #
        if cmds.ikSplineHandleCtx( 'ikSplineHandleCtx', q=True, ex=True ):
        cmds.ikSplineHandleCtx('ikSplineHandleCtx', e=True, parentCurve=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - autoPriorityH (apH): Specifies that this handle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createCurve (ccv): Specifies if a curve should be automatically created for the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - forceSolverH (fsH): Specifies if the ikSolver is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - snapHandleH (snH): Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.C: The default solver is the ikSplineSolver.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver.C: The default is "off".Q: When queried, this flag returns a string.
        - weightH (wH): Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx.C: The default is 1.Q: When queried, this flag returns a float.
        - query (q): Query mode flag
    """
@overload #Overload for ikSplineHandleCtx in ['query']
def ikSplineHandleCtx(object: object, apH: bool = ..., ccv: bool = ..., fsH: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., pwH: float = ..., pH: int = ..., snH: bool = ..., stH: str = ..., sH: str = ..., wH: float = ..., q: bool = ...) -> str:
    """ikSplineHandleCtx is undoable, queryable, and editable.
    
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
    ikSplineHandle tool. The options for the tool will be set to the flags the
    user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Edit an existing context to create an ikSplineHandle with
        #    the curve parented to the corresponding joint.
        #
        if cmds.ikSplineHandleCtx( 'ikSplineHandleCtx', q=True, ex=True ):
        cmds.ikSplineHandleCtx('ikSplineHandleCtx', e=True, parentCurve=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - autoPriorityH (apH): Specifies that this handle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createCurve (ccv): Specifies if a curve should be automatically created for the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - forceSolverH (fsH): Specifies if the ikSolver is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - snapHandleH (snH): Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.C: The default solver is the ikSplineSolver.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver.C: The default is "off".Q: When queried, this flag returns a string.
        - weightH (wH): Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx.C: The default is 1.Q: When queried, this flag returns a float.
        - query (q): Query mode flag
    """
@overload #Overload for ikSplineHandleCtx in ['query']
def ikSplineHandleCtx(object: object, autoPriorityH: bool = ..., apH: bool = ..., createCurve: bool = ..., ccv: bool = ..., forceSolverH: bool = ..., fsH: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., poWeightH: float = ..., pwH: float = ..., priorityH: int = ..., pH: int = ..., snapHandleH: bool = ..., snH: bool = ..., solverTypeH: str = ..., stH: str = ..., stickyH: str = ..., sH: str = ..., weightH: float = ..., wH: float = ..., query: bool = ..., q: bool = ...) -> str:
    """ikSplineHandleCtx is undoable, queryable, and editable.
    
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
    ikSplineHandle tool. The options for the tool will be set to the flags the
    user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Edit an existing context to create an ikSplineHandle with
        #    the curve parented to the corresponding joint.
        #
        if cmds.ikSplineHandleCtx( 'ikSplineHandleCtx', q=True, ex=True ):
        cmds.ikSplineHandleCtx('ikSplineHandleCtx', e=True, parentCurve=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - autoPriorityH (apH): Specifies that this handle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createCurve (ccv): Specifies if a curve should be automatically created for the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - forceSolverH (fsH): Specifies if the ikSolver is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - snapHandleH (snH): Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.C: The default solver is the ikSplineSolver.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver.C: The default is "off".Q: When queried, this flag returns a string.
        - weightH (wH): Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx.C: The default is 1.Q: When queried, this flag returns a float.
        - query (q): Query mode flag
    """
@overload #Overload for ikSplineHandleCtx in ['edit']
def ikSplineHandleCtx(object: object, autoPriorityH: bool = ..., createCurve: bool = ..., createRootAxis: bool = ..., forceSolverH: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., numSpans: int = ..., parentCurve: bool = ..., poWeightH: float = ..., priorityH: int = ..., rootOnCurve: bool = ..., rootTwistMode: bool = ..., simplifyCurve: bool = ..., snapCurve: bool = ..., snapHandleH: bool = ..., solverTypeH: str = ..., stickyH: str = ..., twistType: str = ..., weightH: float = ..., edit: bool = ...) -> str:
    """ikSplineHandleCtx is undoable, queryable, and editable.
    
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
    ikSplineHandle tool. The options for the tool will be set to the flags the
    user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Edit an existing context to create an ikSplineHandle with
        #    the curve parented to the corresponding joint.
        #
        if cmds.ikSplineHandleCtx( 'ikSplineHandleCtx', q=True, ex=True ):
        cmds.ikSplineHandleCtx('ikSplineHandleCtx', e=True, parentCurve=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - autoPriorityH (apH): Specifies that this handle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createCurve (ccv): Specifies if a curve should be automatically created for the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - createRootAxis (cra): Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path.C: The default is off.Q: When queried, this flag
            returns an int.
        - forceSolverH (fsH): Specifies if the ikSolver is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - numSpans (ns): Specifies the number of spans in the automatically generated curve of the ikSplineHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - parentCurve (pcv): Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - rootOnCurve (roc): Specifies if the root is locked onto the curve of the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - rootTwistMode (rtm): Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types. C: The default is off.Q: When queried, this flag returns an int.
        - simplifyCurve (scv): Specifies if the ikSplineHandle curve should be simplified.C: The default is on.Q: When queried, this returns an int.
        - snapCurve (snc): Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle.C: The default is off.Q: When queried, this flag returns an int.
        - snapHandleH (snH): Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.C: The default solver is the ikSplineSolver.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver.C: The default is "off".Q: When queried, this flag returns a string.
        - twistType (tws): Specifies the type of interpolation to be used by the ikSplineHandle.The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".C: The default is "linear".Q: When queried, this flag returns a string.
        - weightH (wH): Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx.C: The default is 1.Q: When queried, this flag returns a float.
        - edit (e): Edit mode flag
    """
@overload #Overload for ikSplineHandleCtx in ['edit']
def ikSplineHandleCtx(object: object, apH: bool = ..., ccv: bool = ..., cra: bool = ..., fsH: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., ns: int = ..., pcv: bool = ..., pwH: float = ..., pH: int = ..., roc: bool = ..., rtm: bool = ..., scv: bool = ..., snc: bool = ..., snH: bool = ..., stH: str = ..., sH: str = ..., tws: str = ..., wH: float = ..., e: bool = ...) -> str:
    """ikSplineHandleCtx is undoable, queryable, and editable.
    
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
    ikSplineHandle tool. The options for the tool will be set to the flags the
    user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Edit an existing context to create an ikSplineHandle with
        #    the curve parented to the corresponding joint.
        #
        if cmds.ikSplineHandleCtx( 'ikSplineHandleCtx', q=True, ex=True ):
        cmds.ikSplineHandleCtx('ikSplineHandleCtx', e=True, parentCurve=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - autoPriorityH (apH): Specifies that this handle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createCurve (ccv): Specifies if a curve should be automatically created for the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - createRootAxis (cra): Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path.C: The default is off.Q: When queried, this flag
            returns an int.
        - forceSolverH (fsH): Specifies if the ikSolver is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - numSpans (ns): Specifies the number of spans in the automatically generated curve of the ikSplineHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - parentCurve (pcv): Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - rootOnCurve (roc): Specifies if the root is locked onto the curve of the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - rootTwistMode (rtm): Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types. C: The default is off.Q: When queried, this flag returns an int.
        - simplifyCurve (scv): Specifies if the ikSplineHandle curve should be simplified.C: The default is on.Q: When queried, this returns an int.
        - snapCurve (snc): Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle.C: The default is off.Q: When queried, this flag returns an int.
        - snapHandleH (snH): Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.C: The default solver is the ikSplineSolver.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver.C: The default is "off".Q: When queried, this flag returns a string.
        - twistType (tws): Specifies the type of interpolation to be used by the ikSplineHandle.The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".C: The default is "linear".Q: When queried, this flag returns a string.
        - weightH (wH): Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx.C: The default is 1.Q: When queried, this flag returns a float.
        - edit (e): Edit mode flag
    """
@overload #Overload for ikSplineHandleCtx in ['edit']
def ikSplineHandleCtx(object: object, autoPriorityH: bool = ..., apH: bool = ..., createCurve: bool = ..., ccv: bool = ..., createRootAxis: bool = ..., cra: bool = ..., forceSolverH: bool = ..., fsH: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., numSpans: int = ..., ns: int = ..., parentCurve: bool = ..., pcv: bool = ..., poWeightH: float = ..., pwH: float = ..., priorityH: int = ..., pH: int = ..., rootOnCurve: bool = ..., roc: bool = ..., rootTwistMode: bool = ..., rtm: bool = ..., simplifyCurve: bool = ..., scv: bool = ..., snapCurve: bool = ..., snc: bool = ..., snapHandleH: bool = ..., snH: bool = ..., solverTypeH: str = ..., stH: str = ..., stickyH: str = ..., sH: str = ..., twistType: str = ..., tws: str = ..., weightH: float = ..., wH: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """ikSplineHandleCtx is undoable, queryable, and editable.
    
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of
    ikSplineHandle tool. The options for the tool will be set to the flags the
    user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Edit an existing context to create an ikSplineHandle with
        #    the curve parented to the corresponding joint.
        #
        if cmds.ikSplineHandleCtx( 'ikSplineHandleCtx', q=True, ex=True ):
        cmds.ikSplineHandleCtx('ikSplineHandleCtx', e=True, parentCurve=True)
    ```

    ---
    - Args:
        - object: Input item(s).
        - autoPriorityH (apH): Specifies that this handle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createCurve (ccv): Specifies if a curve should be automatically created for the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - createRootAxis (cra): Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path.C: The default is off.Q: When queried, this flag
            returns an int.
        - forceSolverH (fsH): Specifies if the ikSolver is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - numSpans (ns): Specifies the number of spans in the automatically generated curve of the ikSplineHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - parentCurve (pcv): Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is 1.Q: When queried, this flag returns an int.
        - rootOnCurve (roc): Specifies if the root is locked onto the curve of the ikSplineHandle.C: The default is on.Q: When queried, this flag returns an int.
        - rootTwistMode (rtm): Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types. C: The default is off.Q: When queried, this flag returns an int.
        - simplifyCurve (scv): Specifies if the ikSplineHandle curve should be simplified.C: The default is on.Q: When queried, this returns an int.
        - snapCurve (snc): Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle.C: The default is off.Q: When queried, this flag returns an int.
        - snapHandleH (snH): Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.C: The default solver is the ikSplineSolver.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver.C: The default is "off".Q: When queried, this flag returns a string.
        - twistType (tws): Specifies the type of interpolation to be used by the ikSplineHandle.The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".C: The default is "linear".Q: When queried, this flag returns a string.
        - weightH (wH): Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx.C: The default is 1.Q: When queried, this flag returns a float.
        - edit (e): Edit mode flag
    """
