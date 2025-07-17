"""Stub files for General category in Maya commands, command: transformLimits."""

from typing import Any, overload

@overload #Overload for transformLimits in ['create']
def transformLimits([object]: [object], remove: bool = ...) -> None:
    """transformLimits is undoable, queryable, and editable.
    
    The transformLimits command allows us to set, edit, or query the limits of the
    transformation that can be applied to objects.
    
    We can also turn any limits off which may have been previously set. When an
    object is first created, all the transformation limits are off by default.
    
    Transformation limits allow us to control how much an object can be
    transformed. This is most useful for joints, although it can be used any place
    we would like to limit the movement of an object.
    
    Default values are:
    ( -1, 1) for translation, ( -1, 1) for scaling, and (-45,45) for rotation.

    Example:
    ```python
        import maya.cmds as cmds
        # Create an object, e.g.
        cmds.cone()
        # 1. To set the limits for the translation of the cone to within
        # a unit volume centered at the origin
        cmds.transformLimits( tx=(-1, 1), ty=(-1, 1), tz=(-1, 1) )
        # 2. To disable the lower limits
        cmds.transformLimits( etx=(False, True), ety=(False, True), etz=(False, True ) )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - remove (rm): turn all the limits off and reset them to their default values
    """
@overload #Overload for transformLimits in ['create']
def transformLimits([object]: [object], rm: bool = ...) -> None:
    """transformLimits is undoable, queryable, and editable.
    
    The transformLimits command allows us to set, edit, or query the limits of the
    transformation that can be applied to objects.
    
    We can also turn any limits off which may have been previously set. When an
    object is first created, all the transformation limits are off by default.
    
    Transformation limits allow us to control how much an object can be
    transformed. This is most useful for joints, although it can be used any place
    we would like to limit the movement of an object.
    
    Default values are:
    ( -1, 1) for translation, ( -1, 1) for scaling, and (-45,45) for rotation.

    Example:
    ```python
        import maya.cmds as cmds
        # Create an object, e.g.
        cmds.cone()
        # 1. To set the limits for the translation of the cone to within
        # a unit volume centered at the origin
        cmds.transformLimits( tx=(-1, 1), ty=(-1, 1), tz=(-1, 1) )
        # 2. To disable the lower limits
        cmds.transformLimits( etx=(False, True), ety=(False, True), etz=(False, True ) )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - remove (rm): turn all the limits off and reset them to their default values
    """
@overload #Overload for transformLimits in ['create']
def transformLimits([object]: [object], remove: bool = ..., rm: bool = ...) -> None:
    """transformLimits is undoable, queryable, and editable.
    
    The transformLimits command allows us to set, edit, or query the limits of the
    transformation that can be applied to objects.
    
    We can also turn any limits off which may have been previously set. When an
    object is first created, all the transformation limits are off by default.
    
    Transformation limits allow us to control how much an object can be
    transformed. This is most useful for joints, although it can be used any place
    we would like to limit the movement of an object.
    
    Default values are:
    ( -1, 1) for translation, ( -1, 1) for scaling, and (-45,45) for rotation.

    Example:
    ```python
        import maya.cmds as cmds
        # Create an object, e.g.
        cmds.cone()
        # 1. To set the limits for the translation of the cone to within
        # a unit volume centered at the origin
        cmds.transformLimits( tx=(-1, 1), ty=(-1, 1), tz=(-1, 1) )
        # 2. To disable the lower limits
        cmds.transformLimits( etx=(False, True), ety=(False, True), etz=(False, True ) )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - remove (rm): turn all the limits off and reset them to their default values
    """
@overload #Overload for transformLimits in ['query']
def transformLimits([object]: [object], enableRotationX: [boolean, boolean] = ..., enableRotationY: [boolean, boolean] = ..., enableRotationZ: [boolean, boolean] = ..., enableScaleX: [boolean, boolean] = ..., enableScaleY: [boolean, boolean] = ..., enableScaleZ: [boolean, boolean] = ..., enableTranslationX: [boolean, boolean] = ..., enableTranslationY: [boolean, boolean] = ..., enableTranslationZ: [boolean, boolean] = ..., rotationX: [angle, angle] = ..., rotationY: [angle, angle] = ..., rotationZ: [angle, angle] = ..., scaleX: [float, float] = ..., scaleY: [float, float] = ..., scaleZ: [float, float] = ..., translationX: [linear, linear] = ..., translationY: [linear, linear] = ..., translationZ: [linear, linear] = ..., query: bool = ...) -> None:
    """transformLimits is undoable, queryable, and editable.
    
    The transformLimits command allows us to set, edit, or query the limits of the
    transformation that can be applied to objects.
    
    We can also turn any limits off which may have been previously set. When an
    object is first created, all the transformation limits are off by default.
    
    Transformation limits allow us to control how much an object can be
    transformed. This is most useful for joints, although it can be used any place
    we would like to limit the movement of an object.
    
    Default values are:
    ( -1, 1) for translation, ( -1, 1) for scaling, and (-45,45) for rotation.

    Example:
    ```python
        import maya.cmds as cmds
        # Create an object, e.g.
        cmds.cone()
        # 1. To set the limits for the translation of the cone to within
        # a unit volume centered at the origin
        cmds.transformLimits( tx=(-1, 1), ty=(-1, 1), tz=(-1, 1) )
        # 2. To disable the lower limits
        cmds.transformLimits( etx=(False, True), ety=(False, True), etz=(False, True ) )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - enableRotationX (erx): enable/disable the lower and upper x-rotation limitsWhen queried, it returnsboolean boolean
        - enableRotationY (ery): enable/disable the lower and upper y-rotation limitsWhen queried, it returnsboolean boolean
        - enableRotationZ (erz): enable/disable the lower and upper z-rotation limitsWhen queried, it returnsboolean boolean
        - enableScaleX (esx): enable/disable the lower and upper x-scale limitsWhen queried, it returnsboolean boolean
        - enableScaleY (esy): enable/disable the lower and upper y-scale limitsWhen queried, it returnsboolean boolean
        - enableScaleZ (esz): enable/disable the lower and upper z-scale limitsWhen queried, it returnsboolean boolean
        - enableTranslationX (etx): enable/disable the  ower and upper x-translation limitsWhen queried, it returnsboolean boolean
        - enableTranslationY (ety): enable/disable the lower and upper y-translation limitsWhen queried, it returnsboolean boolean
        - enableTranslationZ (etz): enable/disable the lower and upper z-translation limitsWhen queried, it returnsboolean boolean
        - rotationX (rx): set the lower and upper x-rotation limitsWhen queried, it returnsangle angle
        - rotationY (ry): set the lower and upper y-rotation limitsWhen queried, it returnsangle angle
        - rotationZ (rz): set the lower and upper z-rotation limitsWhen queried, it returnsangle angle
        - scaleX (sx): set the lower and upper x-scale limitsWhen queried, it returnsfloat float
        - scaleY (sy): set the lower and upper y-scale limitsWhen queried, it returnsfloat float
        - scaleZ (sz): set the lower and upper z-scale limitsWhen queried, it returnsfloat float
        - translationX (tx): set the lower and upper x-translation limitsWhen queried, it returnslinear linear
        - translationY (ty): set the lower and upper y-translation limitsWhen queried, it returnslinear linear
        - translationZ (tz): set the lower and upper z-translation limitsWhen queried, it returnslinear linear
        - query (q): Query mode flag
    """
@overload #Overload for transformLimits in ['query']
def transformLimits([object]: [object], erx: [boolean, boolean] = ..., ery: [boolean, boolean] = ..., erz: [boolean, boolean] = ..., esx: [boolean, boolean] = ..., esy: [boolean, boolean] = ..., esz: [boolean, boolean] = ..., etx: [boolean, boolean] = ..., ety: [boolean, boolean] = ..., etz: [boolean, boolean] = ..., rx: [angle, angle] = ..., ry: [angle, angle] = ..., rz: [angle, angle] = ..., sx: [float, float] = ..., sy: [float, float] = ..., sz: [float, float] = ..., tx: [linear, linear] = ..., ty: [linear, linear] = ..., tz: [linear, linear] = ..., q: bool = ...) -> None:
    """transformLimits is undoable, queryable, and editable.
    
    The transformLimits command allows us to set, edit, or query the limits of the
    transformation that can be applied to objects.
    
    We can also turn any limits off which may have been previously set. When an
    object is first created, all the transformation limits are off by default.
    
    Transformation limits allow us to control how much an object can be
    transformed. This is most useful for joints, although it can be used any place
    we would like to limit the movement of an object.
    
    Default values are:
    ( -1, 1) for translation, ( -1, 1) for scaling, and (-45,45) for rotation.

    Example:
    ```python
        import maya.cmds as cmds
        # Create an object, e.g.
        cmds.cone()
        # 1. To set the limits for the translation of the cone to within
        # a unit volume centered at the origin
        cmds.transformLimits( tx=(-1, 1), ty=(-1, 1), tz=(-1, 1) )
        # 2. To disable the lower limits
        cmds.transformLimits( etx=(False, True), ety=(False, True), etz=(False, True ) )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - enableRotationX (erx): enable/disable the lower and upper x-rotation limitsWhen queried, it returnsboolean boolean
        - enableRotationY (ery): enable/disable the lower and upper y-rotation limitsWhen queried, it returnsboolean boolean
        - enableRotationZ (erz): enable/disable the lower and upper z-rotation limitsWhen queried, it returnsboolean boolean
        - enableScaleX (esx): enable/disable the lower and upper x-scale limitsWhen queried, it returnsboolean boolean
        - enableScaleY (esy): enable/disable the lower and upper y-scale limitsWhen queried, it returnsboolean boolean
        - enableScaleZ (esz): enable/disable the lower and upper z-scale limitsWhen queried, it returnsboolean boolean
        - enableTranslationX (etx): enable/disable the  ower and upper x-translation limitsWhen queried, it returnsboolean boolean
        - enableTranslationY (ety): enable/disable the lower and upper y-translation limitsWhen queried, it returnsboolean boolean
        - enableTranslationZ (etz): enable/disable the lower and upper z-translation limitsWhen queried, it returnsboolean boolean
        - rotationX (rx): set the lower and upper x-rotation limitsWhen queried, it returnsangle angle
        - rotationY (ry): set the lower and upper y-rotation limitsWhen queried, it returnsangle angle
        - rotationZ (rz): set the lower and upper z-rotation limitsWhen queried, it returnsangle angle
        - scaleX (sx): set the lower and upper x-scale limitsWhen queried, it returnsfloat float
        - scaleY (sy): set the lower and upper y-scale limitsWhen queried, it returnsfloat float
        - scaleZ (sz): set the lower and upper z-scale limitsWhen queried, it returnsfloat float
        - translationX (tx): set the lower and upper x-translation limitsWhen queried, it returnslinear linear
        - translationY (ty): set the lower and upper y-translation limitsWhen queried, it returnslinear linear
        - translationZ (tz): set the lower and upper z-translation limitsWhen queried, it returnslinear linear
        - query (q): Query mode flag
    """
@overload #Overload for transformLimits in ['query']
def transformLimits([object]: [object], enableRotationX: [boolean, boolean] = ..., erx: [boolean, boolean] = ..., enableRotationY: [boolean, boolean] = ..., ery: [boolean, boolean] = ..., enableRotationZ: [boolean, boolean] = ..., erz: [boolean, boolean] = ..., enableScaleX: [boolean, boolean] = ..., esx: [boolean, boolean] = ..., enableScaleY: [boolean, boolean] = ..., esy: [boolean, boolean] = ..., enableScaleZ: [boolean, boolean] = ..., esz: [boolean, boolean] = ..., enableTranslationX: [boolean, boolean] = ..., etx: [boolean, boolean] = ..., enableTranslationY: [boolean, boolean] = ..., ety: [boolean, boolean] = ..., enableTranslationZ: [boolean, boolean] = ..., etz: [boolean, boolean] = ..., rotationX: [angle, angle] = ..., rx: [angle, angle] = ..., rotationY: [angle, angle] = ..., ry: [angle, angle] = ..., rotationZ: [angle, angle] = ..., rz: [angle, angle] = ..., scaleX: [float, float] = ..., sx: [float, float] = ..., scaleY: [float, float] = ..., sy: [float, float] = ..., scaleZ: [float, float] = ..., sz: [float, float] = ..., translationX: [linear, linear] = ..., tx: [linear, linear] = ..., translationY: [linear, linear] = ..., ty: [linear, linear] = ..., translationZ: [linear, linear] = ..., tz: [linear, linear] = ..., query: bool = ..., q: bool = ...) -> None:
    """transformLimits is undoable, queryable, and editable.
    
    The transformLimits command allows us to set, edit, or query the limits of the
    transformation that can be applied to objects.
    
    We can also turn any limits off which may have been previously set. When an
    object is first created, all the transformation limits are off by default.
    
    Transformation limits allow us to control how much an object can be
    transformed. This is most useful for joints, although it can be used any place
    we would like to limit the movement of an object.
    
    Default values are:
    ( -1, 1) for translation, ( -1, 1) for scaling, and (-45,45) for rotation.

    Example:
    ```python
        import maya.cmds as cmds
        # Create an object, e.g.
        cmds.cone()
        # 1. To set the limits for the translation of the cone to within
        # a unit volume centered at the origin
        cmds.transformLimits( tx=(-1, 1), ty=(-1, 1), tz=(-1, 1) )
        # 2. To disable the lower limits
        cmds.transformLimits( etx=(False, True), ety=(False, True), etz=(False, True ) )
    ```

    ---
    - Args:
        - [object]: Input item(s).
        - enableRotationX (erx): enable/disable the lower and upper x-rotation limitsWhen queried, it returnsboolean boolean
        - enableRotationY (ery): enable/disable the lower and upper y-rotation limitsWhen queried, it returnsboolean boolean
        - enableRotationZ (erz): enable/disable the lower and upper z-rotation limitsWhen queried, it returnsboolean boolean
        - enableScaleX (esx): enable/disable the lower and upper x-scale limitsWhen queried, it returnsboolean boolean
        - enableScaleY (esy): enable/disable the lower and upper y-scale limitsWhen queried, it returnsboolean boolean
        - enableScaleZ (esz): enable/disable the lower and upper z-scale limitsWhen queried, it returnsboolean boolean
        - enableTranslationX (etx): enable/disable the  ower and upper x-translation limitsWhen queried, it returnsboolean boolean
        - enableTranslationY (ety): enable/disable the lower and upper y-translation limitsWhen queried, it returnsboolean boolean
        - enableTranslationZ (etz): enable/disable the lower and upper z-translation limitsWhen queried, it returnsboolean boolean
        - rotationX (rx): set the lower and upper x-rotation limitsWhen queried, it returnsangle angle
        - rotationY (ry): set the lower and upper y-rotation limitsWhen queried, it returnsangle angle
        - rotationZ (rz): set the lower and upper z-rotation limitsWhen queried, it returnsangle angle
        - scaleX (sx): set the lower and upper x-scale limitsWhen queried, it returnsfloat float
        - scaleY (sy): set the lower and upper y-scale limitsWhen queried, it returnsfloat float
        - scaleZ (sz): set the lower and upper z-scale limitsWhen queried, it returnsfloat float
        - translationX (tx): set the lower and upper x-translation limitsWhen queried, it returnslinear linear
        - translationY (ty): set the lower and upper y-translation limitsWhen queried, it returnslinear linear
        - translationZ (tz): set the lower and upper z-translation limitsWhen queried, it returnslinear linear
        - query (q): Query mode flag
    """
