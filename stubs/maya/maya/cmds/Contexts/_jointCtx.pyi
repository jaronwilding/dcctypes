"""Stub files for Contexts category in Maya commands, command: jointCtx."""

from typing import Any, overload

@overload #Overload for jointCtx in ['create']
def jointCtx([object]: [object], autoJointOrient: str = ..., autoOrientSecondaryAxis: bool = ..., autoPriorityH: bool = ..., createIKHandle: bool = ..., degreeOfFreedomJ: str = ..., exists: bool = ..., forceSolverH: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., jointAutoLimits: bool = ..., jointOrientationJ: [angle, angle, angle] = ..., largeBoneLength: float = ..., largeBoneRadius: float = ..., poWeightH: float = ..., priorityH: int = ..., scaleCompensateJ: bool = ..., scaleJ: [float, float, float] = ..., scaleOrientationJ: [angle, angle, angle] = ..., secondaryAxisOrient: str = ..., smallBoneLength: float = ..., smallBoneRadius: float = ..., snapHandleH: bool = ..., solverTypeH: str = ..., stickyH: str = ..., symmetry: bool = ..., symmetryAxis: str = ..., variableBoneSize: bool = ..., weightH: float = ...) -> str:
    """jointCtx is undoable, queryable, and editable.
    
    The joint context command (jointCtx) updates the parameters of the joint tool.
    The options for the tool will be set by the flags the user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a joint context that makes a ikHandle with an ikRPSolver.
        #    The use the tool.
        #
        cmds.jointCtx( 'myJointContext', createIKHandle=True, solverTypeH='ikRPsolver' )
        cmds.setToolTo( 'myJointContext' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - autoJointOrient (ajo): Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone.C: The default is "xyz".Q: When queried,
            this flag returns a string.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - autoPriorityH (apH): Specifies if the ikHandle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createIKHandle (ikh): Enables the joint tool to create an ikHandle when the tool is completed.C: The default is off.Q: When queried, this flag returns an int.
        - degreeOfFreedomJ (dJ): Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none".C: The default is "xyz".Q: When queried, this flag returns a string.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - forceSolverH (fsH): Specifies if the ikSolver for the ikHandle is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jointAutoLimits (jal): Automatically computes the joint limits based on the kind of joint created.C: The default is off.Q: When queried, this flag returns an int.
        - jointOrientationJ (joJ): Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - largeBoneLength (lbl): Specifies the length above which bones should be assigned the largeBoneRadius.
        - largeBoneRadius (lbr): Specifies the radius for bones whose length is above the largeBoneLength
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - scaleCompensateJ (scJ): Specifies if scale compensate is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - scaleJ (sJ): Sets the scale for the joints created by the tool.C: The default is 1 1 1.Q: When queried, this flag returns an array of three floats.
        - scaleOrientationJ (soJ): Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - secondaryAxisOrient (sao): Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".
        - smallBoneLength (sbl): Specifies the length below which bones should be assigned the smallBoneRadius.
        - smallBoneRadius (sbr): Specifies the radius for bones whose length is below the smallBoneLength.
        - snapHandleH (snH): Sepcifies if snapping is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Sets the name of the solver to use with the ikHandle.C: The default is the solver set to the default in the user preferences.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off.C: The default is "off".Q: When queried, this flag returns a string.
        - symmetry (sym): Automaticaly create a symmetry joint based if symmetry is on.C: The default is off.Q: When queried, this flag returns an int.
        - symmetryAxis (sa): Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.C: The default is x.Q: When queried, this flag returns a string.
        - variableBoneSize (vbs): Specifies whether or not variable bone length and radius settings should be used.
        - weightH (wH): Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene.C: The default is 1.Q: When queried, this flag returns a float.
    """
@overload #Overload for jointCtx in ['create']
def jointCtx([object]: [object], ajo: str = ..., aos: bool = ..., apH: bool = ..., ikh: bool = ..., dJ: str = ..., ex: bool = ..., fsH: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., jal: bool = ..., joJ: [angle, angle, angle] = ..., lbl: float = ..., lbr: float = ..., pwH: float = ..., pH: int = ..., scJ: bool = ..., sJ: [float, float, float] = ..., soJ: [angle, angle, angle] = ..., sao: str = ..., sbl: float = ..., sbr: float = ..., snH: bool = ..., stH: str = ..., sH: str = ..., sym: bool = ..., sa: str = ..., vbs: bool = ..., wH: float = ...) -> str:
    """jointCtx is undoable, queryable, and editable.
    
    The joint context command (jointCtx) updates the parameters of the joint tool.
    The options for the tool will be set by the flags the user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a joint context that makes a ikHandle with an ikRPSolver.
        #    The use the tool.
        #
        cmds.jointCtx( 'myJointContext', createIKHandle=True, solverTypeH='ikRPsolver' )
        cmds.setToolTo( 'myJointContext' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - autoJointOrient (ajo): Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone.C: The default is "xyz".Q: When queried,
            this flag returns a string.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - autoPriorityH (apH): Specifies if the ikHandle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createIKHandle (ikh): Enables the joint tool to create an ikHandle when the tool is completed.C: The default is off.Q: When queried, this flag returns an int.
        - degreeOfFreedomJ (dJ): Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none".C: The default is "xyz".Q: When queried, this flag returns a string.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - forceSolverH (fsH): Specifies if the ikSolver for the ikHandle is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jointAutoLimits (jal): Automatically computes the joint limits based on the kind of joint created.C: The default is off.Q: When queried, this flag returns an int.
        - jointOrientationJ (joJ): Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - largeBoneLength (lbl): Specifies the length above which bones should be assigned the largeBoneRadius.
        - largeBoneRadius (lbr): Specifies the radius for bones whose length is above the largeBoneLength
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - scaleCompensateJ (scJ): Specifies if scale compensate is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - scaleJ (sJ): Sets the scale for the joints created by the tool.C: The default is 1 1 1.Q: When queried, this flag returns an array of three floats.
        - scaleOrientationJ (soJ): Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - secondaryAxisOrient (sao): Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".
        - smallBoneLength (sbl): Specifies the length below which bones should be assigned the smallBoneRadius.
        - smallBoneRadius (sbr): Specifies the radius for bones whose length is below the smallBoneLength.
        - snapHandleH (snH): Sepcifies if snapping is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Sets the name of the solver to use with the ikHandle.C: The default is the solver set to the default in the user preferences.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off.C: The default is "off".Q: When queried, this flag returns a string.
        - symmetry (sym): Automaticaly create a symmetry joint based if symmetry is on.C: The default is off.Q: When queried, this flag returns an int.
        - symmetryAxis (sa): Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.C: The default is x.Q: When queried, this flag returns a string.
        - variableBoneSize (vbs): Specifies whether or not variable bone length and radius settings should be used.
        - weightH (wH): Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene.C: The default is 1.Q: When queried, this flag returns a float.
    """
@overload #Overload for jointCtx in ['create']
def jointCtx([object]: [object], autoJointOrient: str = ..., ajo: str = ..., autoOrientSecondaryAxis: bool = ..., aos: bool = ..., autoPriorityH: bool = ..., apH: bool = ..., createIKHandle: bool = ..., ikh: bool = ..., degreeOfFreedomJ: str = ..., dJ: str = ..., exists: bool = ..., ex: bool = ..., forceSolverH: bool = ..., fsH: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., jointAutoLimits: bool = ..., jal: bool = ..., jointOrientationJ: [angle, angle, angle] = ..., joJ: [angle, angle, angle] = ..., largeBoneLength: float = ..., lbl: float = ..., largeBoneRadius: float = ..., lbr: float = ..., poWeightH: float = ..., pwH: float = ..., priorityH: int = ..., pH: int = ..., scaleCompensateJ: bool = ..., scJ: bool = ..., scaleJ: [float, float, float] = ..., sJ: [float, float, float] = ..., scaleOrientationJ: [angle, angle, angle] = ..., soJ: [angle, angle, angle] = ..., secondaryAxisOrient: str = ..., sao: str = ..., smallBoneLength: float = ..., sbl: float = ..., smallBoneRadius: float = ..., sbr: float = ..., snapHandleH: bool = ..., snH: bool = ..., solverTypeH: str = ..., stH: str = ..., stickyH: str = ..., sH: str = ..., symmetry: bool = ..., sym: bool = ..., symmetryAxis: str = ..., sa: str = ..., variableBoneSize: bool = ..., vbs: bool = ..., weightH: float = ..., wH: float = ...) -> str:
    """jointCtx is undoable, queryable, and editable.
    
    The joint context command (jointCtx) updates the parameters of the joint tool.
    The options for the tool will be set by the flags the user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a joint context that makes a ikHandle with an ikRPSolver.
        #    The use the tool.
        #
        cmds.jointCtx( 'myJointContext', createIKHandle=True, solverTypeH='ikRPsolver' )
        cmds.setToolTo( 'myJointContext' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - autoJointOrient (ajo): Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone.C: The default is "xyz".Q: When queried,
            this flag returns a string.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - autoPriorityH (apH): Specifies if the ikHandle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createIKHandle (ikh): Enables the joint tool to create an ikHandle when the tool is completed.C: The default is off.Q: When queried, this flag returns an int.
        - degreeOfFreedomJ (dJ): Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none".C: The default is "xyz".Q: When queried, this flag returns a string.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - forceSolverH (fsH): Specifies if the ikSolver for the ikHandle is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jointAutoLimits (jal): Automatically computes the joint limits based on the kind of joint created.C: The default is off.Q: When queried, this flag returns an int.
        - jointOrientationJ (joJ): Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - largeBoneLength (lbl): Specifies the length above which bones should be assigned the largeBoneRadius.
        - largeBoneRadius (lbr): Specifies the radius for bones whose length is above the largeBoneLength
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - scaleCompensateJ (scJ): Specifies if scale compensate is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - scaleJ (sJ): Sets the scale for the joints created by the tool.C: The default is 1 1 1.Q: When queried, this flag returns an array of three floats.
        - scaleOrientationJ (soJ): Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - secondaryAxisOrient (sao): Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".
        - smallBoneLength (sbl): Specifies the length below which bones should be assigned the smallBoneRadius.
        - smallBoneRadius (sbr): Specifies the radius for bones whose length is below the smallBoneLength.
        - snapHandleH (snH): Sepcifies if snapping is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Sets the name of the solver to use with the ikHandle.C: The default is the solver set to the default in the user preferences.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off.C: The default is "off".Q: When queried, this flag returns a string.
        - symmetry (sym): Automaticaly create a symmetry joint based if symmetry is on.C: The default is off.Q: When queried, this flag returns an int.
        - symmetryAxis (sa): Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.C: The default is x.Q: When queried, this flag returns a string.
        - variableBoneSize (vbs): Specifies whether or not variable bone length and radius settings should be used.
        - weightH (wH): Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene.C: The default is 1.Q: When queried, this flag returns a float.
    """
@overload #Overload for jointCtx in ['query']
def jointCtx([object]: [object], autoJointOrient: str = ..., autoOrientSecondaryAxis: bool = ..., autoPriorityH: bool = ..., createIKHandle: bool = ..., degreeOfFreedomJ: str = ..., forceSolverH: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., jointAutoLimits: bool = ..., jointOrientationJ: [angle, angle, angle] = ..., largeBoneLength: float = ..., largeBoneRadius: float = ..., poWeightH: float = ..., priorityH: int = ..., scaleCompensateJ: bool = ..., scaleJ: [float, float, float] = ..., scaleOrientationJ: [angle, angle, angle] = ..., secondaryAxisOrient: str = ..., smallBoneLength: float = ..., smallBoneRadius: float = ..., snapHandleH: bool = ..., solverTypeH: str = ..., stickyH: str = ..., symmetry: bool = ..., symmetryAxis: str = ..., variableBoneSize: bool = ..., weightH: float = ..., query: bool = ...) -> str:
    """jointCtx is undoable, queryable, and editable.
    
    The joint context command (jointCtx) updates the parameters of the joint tool.
    The options for the tool will be set by the flags the user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a joint context that makes a ikHandle with an ikRPSolver.
        #    The use the tool.
        #
        cmds.jointCtx( 'myJointContext', createIKHandle=True, solverTypeH='ikRPsolver' )
        cmds.setToolTo( 'myJointContext' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - autoJointOrient (ajo): Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone.C: The default is "xyz".Q: When queried,
            this flag returns a string.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - autoPriorityH (apH): Specifies if the ikHandle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createIKHandle (ikh): Enables the joint tool to create an ikHandle when the tool is completed.C: The default is off.Q: When queried, this flag returns an int.
        - degreeOfFreedomJ (dJ): Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none".C: The default is "xyz".Q: When queried, this flag returns a string.
        - forceSolverH (fsH): Specifies if the ikSolver for the ikHandle is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jointAutoLimits (jal): Automatically computes the joint limits based on the kind of joint created.C: The default is off.Q: When queried, this flag returns an int.
        - jointOrientationJ (joJ): Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - largeBoneLength (lbl): Specifies the length above which bones should be assigned the largeBoneRadius.
        - largeBoneRadius (lbr): Specifies the radius for bones whose length is above the largeBoneLength
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - scaleCompensateJ (scJ): Specifies if scale compensate is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - scaleJ (sJ): Sets the scale for the joints created by the tool.C: The default is 1 1 1.Q: When queried, this flag returns an array of three floats.
        - scaleOrientationJ (soJ): Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - secondaryAxisOrient (sao): Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".
        - smallBoneLength (sbl): Specifies the length below which bones should be assigned the smallBoneRadius.
        - smallBoneRadius (sbr): Specifies the radius for bones whose length is below the smallBoneLength.
        - snapHandleH (snH): Sepcifies if snapping is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Sets the name of the solver to use with the ikHandle.C: The default is the solver set to the default in the user preferences.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off.C: The default is "off".Q: When queried, this flag returns a string.
        - symmetry (sym): Automaticaly create a symmetry joint based if symmetry is on.C: The default is off.Q: When queried, this flag returns an int.
        - symmetryAxis (sa): Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.C: The default is x.Q: When queried, this flag returns a string.
        - variableBoneSize (vbs): Specifies whether or not variable bone length and radius settings should be used.
        - weightH (wH): Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene.C: The default is 1.Q: When queried, this flag returns a float.
        - query (q): Query mode flag
    """
@overload #Overload for jointCtx in ['query']
def jointCtx([object]: [object], ajo: str = ..., aos: bool = ..., apH: bool = ..., ikh: bool = ..., dJ: str = ..., fsH: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., jal: bool = ..., joJ: [angle, angle, angle] = ..., lbl: float = ..., lbr: float = ..., pwH: float = ..., pH: int = ..., scJ: bool = ..., sJ: [float, float, float] = ..., soJ: [angle, angle, angle] = ..., sao: str = ..., sbl: float = ..., sbr: float = ..., snH: bool = ..., stH: str = ..., sH: str = ..., sym: bool = ..., sa: str = ..., vbs: bool = ..., wH: float = ..., q: bool = ...) -> str:
    """jointCtx is undoable, queryable, and editable.
    
    The joint context command (jointCtx) updates the parameters of the joint tool.
    The options for the tool will be set by the flags the user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a joint context that makes a ikHandle with an ikRPSolver.
        #    The use the tool.
        #
        cmds.jointCtx( 'myJointContext', createIKHandle=True, solverTypeH='ikRPsolver' )
        cmds.setToolTo( 'myJointContext' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - autoJointOrient (ajo): Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone.C: The default is "xyz".Q: When queried,
            this flag returns a string.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - autoPriorityH (apH): Specifies if the ikHandle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createIKHandle (ikh): Enables the joint tool to create an ikHandle when the tool is completed.C: The default is off.Q: When queried, this flag returns an int.
        - degreeOfFreedomJ (dJ): Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none".C: The default is "xyz".Q: When queried, this flag returns a string.
        - forceSolverH (fsH): Specifies if the ikSolver for the ikHandle is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jointAutoLimits (jal): Automatically computes the joint limits based on the kind of joint created.C: The default is off.Q: When queried, this flag returns an int.
        - jointOrientationJ (joJ): Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - largeBoneLength (lbl): Specifies the length above which bones should be assigned the largeBoneRadius.
        - largeBoneRadius (lbr): Specifies the radius for bones whose length is above the largeBoneLength
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - scaleCompensateJ (scJ): Specifies if scale compensate is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - scaleJ (sJ): Sets the scale for the joints created by the tool.C: The default is 1 1 1.Q: When queried, this flag returns an array of three floats.
        - scaleOrientationJ (soJ): Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - secondaryAxisOrient (sao): Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".
        - smallBoneLength (sbl): Specifies the length below which bones should be assigned the smallBoneRadius.
        - smallBoneRadius (sbr): Specifies the radius for bones whose length is below the smallBoneLength.
        - snapHandleH (snH): Sepcifies if snapping is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Sets the name of the solver to use with the ikHandle.C: The default is the solver set to the default in the user preferences.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off.C: The default is "off".Q: When queried, this flag returns a string.
        - symmetry (sym): Automaticaly create a symmetry joint based if symmetry is on.C: The default is off.Q: When queried, this flag returns an int.
        - symmetryAxis (sa): Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.C: The default is x.Q: When queried, this flag returns a string.
        - variableBoneSize (vbs): Specifies whether or not variable bone length and radius settings should be used.
        - weightH (wH): Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene.C: The default is 1.Q: When queried, this flag returns a float.
        - query (q): Query mode flag
    """
@overload #Overload for jointCtx in ['query']
def jointCtx([object]: [object], autoJointOrient: str = ..., ajo: str = ..., autoOrientSecondaryAxis: bool = ..., aos: bool = ..., autoPriorityH: bool = ..., apH: bool = ..., createIKHandle: bool = ..., ikh: bool = ..., degreeOfFreedomJ: str = ..., dJ: str = ..., forceSolverH: bool = ..., fsH: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., jointAutoLimits: bool = ..., jal: bool = ..., jointOrientationJ: [angle, angle, angle] = ..., joJ: [angle, angle, angle] = ..., largeBoneLength: float = ..., lbl: float = ..., largeBoneRadius: float = ..., lbr: float = ..., poWeightH: float = ..., pwH: float = ..., priorityH: int = ..., pH: int = ..., scaleCompensateJ: bool = ..., scJ: bool = ..., scaleJ: [float, float, float] = ..., sJ: [float, float, float] = ..., scaleOrientationJ: [angle, angle, angle] = ..., soJ: [angle, angle, angle] = ..., secondaryAxisOrient: str = ..., sao: str = ..., smallBoneLength: float = ..., sbl: float = ..., smallBoneRadius: float = ..., sbr: float = ..., snapHandleH: bool = ..., snH: bool = ..., solverTypeH: str = ..., stH: str = ..., stickyH: str = ..., sH: str = ..., symmetry: bool = ..., sym: bool = ..., symmetryAxis: str = ..., sa: str = ..., variableBoneSize: bool = ..., vbs: bool = ..., weightH: float = ..., wH: float = ..., query: bool = ..., q: bool = ...) -> str:
    """jointCtx is undoable, queryable, and editable.
    
    The joint context command (jointCtx) updates the parameters of the joint tool.
    The options for the tool will be set by the flags the user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a joint context that makes a ikHandle with an ikRPSolver.
        #    The use the tool.
        #
        cmds.jointCtx( 'myJointContext', createIKHandle=True, solverTypeH='ikRPsolver' )
        cmds.setToolTo( 'myJointContext' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - autoJointOrient (ajo): Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone.C: The default is "xyz".Q: When queried,
            this flag returns a string.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - autoPriorityH (apH): Specifies if the ikHandle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createIKHandle (ikh): Enables the joint tool to create an ikHandle when the tool is completed.C: The default is off.Q: When queried, this flag returns an int.
        - degreeOfFreedomJ (dJ): Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none".C: The default is "xyz".Q: When queried, this flag returns a string.
        - forceSolverH (fsH): Specifies if the ikSolver for the ikHandle is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jointAutoLimits (jal): Automatically computes the joint limits based on the kind of joint created.C: The default is off.Q: When queried, this flag returns an int.
        - jointOrientationJ (joJ): Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - largeBoneLength (lbl): Specifies the length above which bones should be assigned the largeBoneRadius.
        - largeBoneRadius (lbr): Specifies the radius for bones whose length is above the largeBoneLength
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - scaleCompensateJ (scJ): Specifies if scale compensate is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - scaleJ (sJ): Sets the scale for the joints created by the tool.C: The default is 1 1 1.Q: When queried, this flag returns an array of three floats.
        - scaleOrientationJ (soJ): Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - secondaryAxisOrient (sao): Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".
        - smallBoneLength (sbl): Specifies the length below which bones should be assigned the smallBoneRadius.
        - smallBoneRadius (sbr): Specifies the radius for bones whose length is below the smallBoneLength.
        - snapHandleH (snH): Sepcifies if snapping is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Sets the name of the solver to use with the ikHandle.C: The default is the solver set to the default in the user preferences.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off.C: The default is "off".Q: When queried, this flag returns a string.
        - symmetry (sym): Automaticaly create a symmetry joint based if symmetry is on.C: The default is off.Q: When queried, this flag returns an int.
        - symmetryAxis (sa): Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.C: The default is x.Q: When queried, this flag returns a string.
        - variableBoneSize (vbs): Specifies whether or not variable bone length and radius settings should be used.
        - weightH (wH): Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene.C: The default is 1.Q: When queried, this flag returns a float.
        - query (q): Query mode flag
    """
@overload #Overload for jointCtx in ['edit']
def jointCtx([object]: [object], autoJointOrient: str = ..., autoOrientSecondaryAxis: bool = ..., autoPriorityH: bool = ..., createIKHandle: bool = ..., degreeOfFreedomJ: str = ..., forceSolverH: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., jointAutoLimits: bool = ..., jointOrientationJ: [angle, angle, angle] = ..., largeBoneLength: float = ..., largeBoneRadius: float = ..., poWeightH: float = ..., priorityH: int = ..., scaleCompensateJ: bool = ..., scaleJ: [float, float, float] = ..., scaleOrientationJ: [angle, angle, angle] = ..., secondaryAxisOrient: str = ..., smallBoneLength: float = ..., smallBoneRadius: float = ..., snapHandleH: bool = ..., solverTypeH: str = ..., stickyH: str = ..., symmetry: bool = ..., symmetryAxis: str = ..., variableBoneSize: bool = ..., weightH: float = ..., edit: bool = ...) -> str:
    """jointCtx is undoable, queryable, and editable.
    
    The joint context command (jointCtx) updates the parameters of the joint tool.
    The options for the tool will be set by the flags the user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a joint context that makes a ikHandle with an ikRPSolver.
        #    The use the tool.
        #
        cmds.jointCtx( 'myJointContext', createIKHandle=True, solverTypeH='ikRPsolver' )
        cmds.setToolTo( 'myJointContext' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - autoJointOrient (ajo): Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone.C: The default is "xyz".Q: When queried,
            this flag returns a string.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - autoPriorityH (apH): Specifies if the ikHandle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createIKHandle (ikh): Enables the joint tool to create an ikHandle when the tool is completed.C: The default is off.Q: When queried, this flag returns an int.
        - degreeOfFreedomJ (dJ): Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none".C: The default is "xyz".Q: When queried, this flag returns a string.
        - forceSolverH (fsH): Specifies if the ikSolver for the ikHandle is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jointAutoLimits (jal): Automatically computes the joint limits based on the kind of joint created.C: The default is off.Q: When queried, this flag returns an int.
        - jointOrientationJ (joJ): Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - largeBoneLength (lbl): Specifies the length above which bones should be assigned the largeBoneRadius.
        - largeBoneRadius (lbr): Specifies the radius for bones whose length is above the largeBoneLength
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - scaleCompensateJ (scJ): Specifies if scale compensate is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - scaleJ (sJ): Sets the scale for the joints created by the tool.C: The default is 1 1 1.Q: When queried, this flag returns an array of three floats.
        - scaleOrientationJ (soJ): Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - secondaryAxisOrient (sao): Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".
        - smallBoneLength (sbl): Specifies the length below which bones should be assigned the smallBoneRadius.
        - smallBoneRadius (sbr): Specifies the radius for bones whose length is below the smallBoneLength.
        - snapHandleH (snH): Sepcifies if snapping is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Sets the name of the solver to use with the ikHandle.C: The default is the solver set to the default in the user preferences.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off.C: The default is "off".Q: When queried, this flag returns a string.
        - symmetry (sym): Automaticaly create a symmetry joint based if symmetry is on.C: The default is off.Q: When queried, this flag returns an int.
        - symmetryAxis (sa): Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.C: The default is x.Q: When queried, this flag returns a string.
        - variableBoneSize (vbs): Specifies whether or not variable bone length and radius settings should be used.
        - weightH (wH): Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene.C: The default is 1.Q: When queried, this flag returns a float.
        - edit (e): Edit mode flag
    """
@overload #Overload for jointCtx in ['edit']
def jointCtx([object]: [object], ajo: str = ..., aos: bool = ..., apH: bool = ..., ikh: bool = ..., dJ: str = ..., fsH: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., jal: bool = ..., joJ: [angle, angle, angle] = ..., lbl: float = ..., lbr: float = ..., pwH: float = ..., pH: int = ..., scJ: bool = ..., sJ: [float, float, float] = ..., soJ: [angle, angle, angle] = ..., sao: str = ..., sbl: float = ..., sbr: float = ..., snH: bool = ..., stH: str = ..., sH: str = ..., sym: bool = ..., sa: str = ..., vbs: bool = ..., wH: float = ..., e: bool = ...) -> str:
    """jointCtx is undoable, queryable, and editable.
    
    The joint context command (jointCtx) updates the parameters of the joint tool.
    The options for the tool will be set by the flags the user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a joint context that makes a ikHandle with an ikRPSolver.
        #    The use the tool.
        #
        cmds.jointCtx( 'myJointContext', createIKHandle=True, solverTypeH='ikRPsolver' )
        cmds.setToolTo( 'myJointContext' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - autoJointOrient (ajo): Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone.C: The default is "xyz".Q: When queried,
            this flag returns a string.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - autoPriorityH (apH): Specifies if the ikHandle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createIKHandle (ikh): Enables the joint tool to create an ikHandle when the tool is completed.C: The default is off.Q: When queried, this flag returns an int.
        - degreeOfFreedomJ (dJ): Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none".C: The default is "xyz".Q: When queried, this flag returns a string.
        - forceSolverH (fsH): Specifies if the ikSolver for the ikHandle is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jointAutoLimits (jal): Automatically computes the joint limits based on the kind of joint created.C: The default is off.Q: When queried, this flag returns an int.
        - jointOrientationJ (joJ): Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - largeBoneLength (lbl): Specifies the length above which bones should be assigned the largeBoneRadius.
        - largeBoneRadius (lbr): Specifies the radius for bones whose length is above the largeBoneLength
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - scaleCompensateJ (scJ): Specifies if scale compensate is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - scaleJ (sJ): Sets the scale for the joints created by the tool.C: The default is 1 1 1.Q: When queried, this flag returns an array of three floats.
        - scaleOrientationJ (soJ): Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - secondaryAxisOrient (sao): Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".
        - smallBoneLength (sbl): Specifies the length below which bones should be assigned the smallBoneRadius.
        - smallBoneRadius (sbr): Specifies the radius for bones whose length is below the smallBoneLength.
        - snapHandleH (snH): Sepcifies if snapping is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Sets the name of the solver to use with the ikHandle.C: The default is the solver set to the default in the user preferences.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off.C: The default is "off".Q: When queried, this flag returns a string.
        - symmetry (sym): Automaticaly create a symmetry joint based if symmetry is on.C: The default is off.Q: When queried, this flag returns an int.
        - symmetryAxis (sa): Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.C: The default is x.Q: When queried, this flag returns a string.
        - variableBoneSize (vbs): Specifies whether or not variable bone length and radius settings should be used.
        - weightH (wH): Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene.C: The default is 1.Q: When queried, this flag returns a float.
        - edit (e): Edit mode flag
    """
@overload #Overload for jointCtx in ['edit']
def jointCtx([object]: [object], autoJointOrient: str = ..., ajo: str = ..., autoOrientSecondaryAxis: bool = ..., aos: bool = ..., autoPriorityH: bool = ..., apH: bool = ..., createIKHandle: bool = ..., ikh: bool = ..., degreeOfFreedomJ: str = ..., dJ: str = ..., forceSolverH: bool = ..., fsH: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., jointAutoLimits: bool = ..., jal: bool = ..., jointOrientationJ: [angle, angle, angle] = ..., joJ: [angle, angle, angle] = ..., largeBoneLength: float = ..., lbl: float = ..., largeBoneRadius: float = ..., lbr: float = ..., poWeightH: float = ..., pwH: float = ..., priorityH: int = ..., pH: int = ..., scaleCompensateJ: bool = ..., scJ: bool = ..., scaleJ: [float, float, float] = ..., sJ: [float, float, float] = ..., scaleOrientationJ: [angle, angle, angle] = ..., soJ: [angle, angle, angle] = ..., secondaryAxisOrient: str = ..., sao: str = ..., smallBoneLength: float = ..., sbl: float = ..., smallBoneRadius: float = ..., sbr: float = ..., snapHandleH: bool = ..., snH: bool = ..., solverTypeH: str = ..., stH: str = ..., stickyH: str = ..., sH: str = ..., symmetry: bool = ..., sym: bool = ..., symmetryAxis: str = ..., sa: str = ..., variableBoneSize: bool = ..., vbs: bool = ..., weightH: float = ..., wH: float = ..., edit: bool = ..., e: bool = ...) -> str:
    """jointCtx is undoable, queryable, and editable.
    
    The joint context command (jointCtx) updates the parameters of the joint tool.
    The options for the tool will be set by the flags the user specifies.

    Example:
    ```python
        import maya.cmds as cmds
        #    Create a joint context that makes a ikHandle with an ikRPSolver.
        #    The use the tool.
        #
        cmds.jointCtx( 'myJointContext', createIKHandle=True, solverTypeH='ikRPsolver' )
        cmds.setToolTo( 'myJointContext' )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - autoJointOrient (ajo): Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone.C: The default is "xyz".Q: When queried,
            this flag returns a string.
        - autoOrientSecondaryAxis (aos): This flag is used in conjunction with the -sao/secondaryAxisOrient flag. If this flag is enabled the secondary axis will be oriented using the plane defined by neighboring joints and pointing in the same direction as the secondary axis. If
            no such plane exists the joint will be oriented using the secondary axis alone.
        - autoPriorityH (apH): Specifies if the ikHandle's priority is assigned automatically.C: The default is off.Q: When queried, this flag returns an int.
        - createIKHandle (ikh): Enables the joint tool to create an ikHandle when the tool is completed.C: The default is off.Q: When queried, this flag returns an int.
        - degreeOfFreedomJ (dJ): Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none".C: The default is "xyz".Q: When queried, this flag returns a string.
        - forceSolverH (fsH): Specifies if the ikSolver for the ikHandle is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - jointAutoLimits (jal): Automatically computes the joint limits based on the kind of joint created.C: The default is off.Q: When queried, this flag returns an int.
        - jointOrientationJ (joJ): Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - largeBoneLength (lbl): Specifies the length above which bones should be assigned the largeBoneRadius.
        - largeBoneRadius (lbr): Specifies the radius for bones whose length is above the largeBoneLength
        - poWeightH (pwH): Specifies the position/orientation weight of the ikHandle.C: The default is 1.Q: When queried, this flag returns a float.
        - priorityH (pH): Specifies the priority of the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - scaleCompensateJ (scJ): Specifies if scale compensate is enabled.C: The default is on.Q: When queried, this flag returns an int.
        - scaleJ (sJ): Sets the scale for the joints created by the tool.C: The default is 1 1 1.Q: When queried, this flag returns an array of three floats.
        - scaleOrientationJ (soJ): Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored.C: The default is 0 0 0.Q: When queried, this flag returns an array of three floats.
        - secondaryAxisOrient (sao): Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".
        - smallBoneLength (sbl): Specifies the length below which bones should be assigned the smallBoneRadius.
        - smallBoneRadius (sbr): Specifies the radius for bones whose length is below the smallBoneLength.
        - snapHandleH (snH): Sepcifies if snapping is enabled for the ikHandle.C: The default is on.Q: When queried, this flag returns an int.
        - solverTypeH (stH): Sets the name of the solver to use with the ikHandle.C: The default is the solver set to the default in the user preferences.Q: When queried, this flag returns a string.
        - stickyH (sH): Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off.C: The default is "off".Q: When queried, this flag returns a string.
        - symmetry (sym): Automaticaly create a symmetry joint based if symmetry is on.C: The default is off.Q: When queried, this flag returns an int.
        - symmetryAxis (sa): Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.C: The default is x.Q: When queried, this flag returns a string.
        - variableBoneSize (vbs): Specifies whether or not variable bone length and radius settings should be used.
        - weightH (wH): Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene.C: The default is 1.Q: When queried, this flag returns a float.
        - edit (e): Edit mode flag
    """
