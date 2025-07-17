"""Stub files for General category in Maya commands, command: makeIdentity."""

from typing import Any, overload

@overload #Overload for makeIdentity in ['create']
def makeIdentity([dagObject]: [dagObject], apply: bool = ..., jointOrient: bool = ..., normal: int = ..., preserveNormals: bool = ..., rotate: bool = ..., scale: bool = ..., translate: bool = ...) -> None:
    """makeIdentity is undoable, NOT queryable, and NOT editable.
    
    The makeIdentity command is a quick way to reset the selected transform and
    all of its children down to the shape level by the identity transformation.
    You can also specify which of transform, rotate or scale is applied down from
    the selected transform. The identity transformation means:
    
    * translate = 0, 0, 0
    * rotate = 0, 0, 0
    * scale = 1, 1, 1
    * shear = 1, 1, 1
    
    If a transform is a joint, then the "translate" attribute may not be 0, but
    will be used to position the joints so that they preserve their world space
    positions. The translate flag doesn't apply to joints, since joints must
    preserve their world space positions. Only the rotate and scale flags are
    meaningful when applied to joints.
    
    If the -a/apply flag is true, then the transforms that are reset are
    accumulated and applied to the all shapes below the modified transforms, so
    that the shapes will not move. The pivot positions are recalculated so that
    they also will not move in world space. If this flag is false, then the
    transformations are reset to identity, without any changes to preserve
    position.

    Example:
    ```python
        import maya.cmds as cmds
        # Example 1:  Create a hierarchical object, for example a
        # car. Scale the tires, translate the doors into place, rotate the
        # steering wheel, then select the group node above the car, and type:
        cmds.makeIdentity( apply=True )
        # The car should not move.
        cmds.move( 3, 0, 0 )
        # The car should move exactly 3 units to (3, 0, 0), since
        # the previous makeIdentity command set its translation to (0, 0, 0).
        cmds.makeIdentity()
        # The car should return to the same position as before the move.
        # Example 2:  Create a curve and translate, rotate and scale it.
        # Then group it and translate, rotate and scale the group.
        cmds.makeIdentity( 'group1', apply=True, translate=True )
        # The curve will not move, but both the curve transform's and group
        # transform's translation will be set to 0, 0, 0. The rotation and
        # scale will remain the same.
        cmds.makeIdentity( 'group1', apply=True, rotate=True )
        # The curve will not move, but both the curve transform's and group
        # transform's rotation will be set to 0, 0, 0. The translation and
        # scale will remain the same.
        cmds.makeIdentity( 'group1', apply=True, scale=True )
        # The curve will not move, but both the curve transform's and group
        # transform's scale will be set to 1, 1, 1. The translation and rotation
        # will remain the same.
        cmds.makeIdentity( 'group1', apply=True, translate=True, rotate=True )
        # The curve will not move, but both the curve transform's and group
        # transform's translation and rotation will be set to 0, 0, 0.
        # The scale will remain the same.
        cmds.makeIdentity( 'group1', apply=False, translate=True )
        # The curve transform and group transform will have their translation
        # set to 0, 0, 0. The curve will probably move, since the apply
        # flag is false.
        cmds.makeIdentity( apply=True, translate=True, rotate=True, scale=True )
        # This is the same as "makeIdentity -apply true".
        # Example 3:  Create a polyCube and translate, rotate and scale it.
        # And then freeze the normals.
        cmds.polyCube()
        cmds.rotate( 30, 45, 0 )
        cmds.move( 2, 0, 2, r=True )
        cmds.scale( 2, 1, 2, r=True )
        cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )
    ```

    ---
    - Args:
        - [dagObject]: Input item(s).
        - apply (a): If this flag is true, the accumulated transforms are applied to the shape after the transforms are made identity, such that the world space positions of the transforms pivots are preserved, and the shapes do not move. The default is false.
        - jointOrient (jo): If this flag is set, the joint orient on joints will be reset to align with worldspace.
        - normal (n): If this flag is set to 1, the normals on polygonal objects will be frozen.  This flag is valid only when the -apply flag is on. If this flag is set to 2, the normals on polygonal objects will be frozen only if its a non-rigid transformation
            matrix. ie, a transformation that does not contain shear, skew or non-proportional scaling. The default behaviour is not to freeze normals.
        - preserveNormals (pn): If this flag is true, the normals on polygonal objects will be reversed if the objects are negatively scaled (reflection). This flag is valid only when the -apply flag is on.
        - rotate (r): If this flag is true, only the rotation is applied to the shape. The rotation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
        - scale (s): If this flag is true, only the scale is applied to the shape. The scale factor will be changed to 1, 1, 1. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
        - translate (t): If this flag is true, only the translation is applied to the shape. The translation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s)  are applied.  (Note: the translate flag is
            not meaningful when applied to joints, since joints are made to preserve their world space position.  This flag will have no effect on joints.)
    """
@overload #Overload for makeIdentity in ['create']
def makeIdentity([dagObject]: [dagObject], a: bool = ..., jo: bool = ..., n: int = ..., pn: bool = ..., r: bool = ..., s: bool = ..., t: bool = ...) -> None:
    """makeIdentity is undoable, NOT queryable, and NOT editable.
    
    The makeIdentity command is a quick way to reset the selected transform and
    all of its children down to the shape level by the identity transformation.
    You can also specify which of transform, rotate or scale is applied down from
    the selected transform. The identity transformation means:
    
    * translate = 0, 0, 0
    * rotate = 0, 0, 0
    * scale = 1, 1, 1
    * shear = 1, 1, 1
    
    If a transform is a joint, then the "translate" attribute may not be 0, but
    will be used to position the joints so that they preserve their world space
    positions. The translate flag doesn't apply to joints, since joints must
    preserve their world space positions. Only the rotate and scale flags are
    meaningful when applied to joints.
    
    If the -a/apply flag is true, then the transforms that are reset are
    accumulated and applied to the all shapes below the modified transforms, so
    that the shapes will not move. The pivot positions are recalculated so that
    they also will not move in world space. If this flag is false, then the
    transformations are reset to identity, without any changes to preserve
    position.

    Example:
    ```python
        import maya.cmds as cmds
        # Example 1:  Create a hierarchical object, for example a
        # car. Scale the tires, translate the doors into place, rotate the
        # steering wheel, then select the group node above the car, and type:
        cmds.makeIdentity( apply=True )
        # The car should not move.
        cmds.move( 3, 0, 0 )
        # The car should move exactly 3 units to (3, 0, 0), since
        # the previous makeIdentity command set its translation to (0, 0, 0).
        cmds.makeIdentity()
        # The car should return to the same position as before the move.
        # Example 2:  Create a curve and translate, rotate and scale it.
        # Then group it and translate, rotate and scale the group.
        cmds.makeIdentity( 'group1', apply=True, translate=True )
        # The curve will not move, but both the curve transform's and group
        # transform's translation will be set to 0, 0, 0. The rotation and
        # scale will remain the same.
        cmds.makeIdentity( 'group1', apply=True, rotate=True )
        # The curve will not move, but both the curve transform's and group
        # transform's rotation will be set to 0, 0, 0. The translation and
        # scale will remain the same.
        cmds.makeIdentity( 'group1', apply=True, scale=True )
        # The curve will not move, but both the curve transform's and group
        # transform's scale will be set to 1, 1, 1. The translation and rotation
        # will remain the same.
        cmds.makeIdentity( 'group1', apply=True, translate=True, rotate=True )
        # The curve will not move, but both the curve transform's and group
        # transform's translation and rotation will be set to 0, 0, 0.
        # The scale will remain the same.
        cmds.makeIdentity( 'group1', apply=False, translate=True )
        # The curve transform and group transform will have their translation
        # set to 0, 0, 0. The curve will probably move, since the apply
        # flag is false.
        cmds.makeIdentity( apply=True, translate=True, rotate=True, scale=True )
        # This is the same as "makeIdentity -apply true".
        # Example 3:  Create a polyCube and translate, rotate and scale it.
        # And then freeze the normals.
        cmds.polyCube()
        cmds.rotate( 30, 45, 0 )
        cmds.move( 2, 0, 2, r=True )
        cmds.scale( 2, 1, 2, r=True )
        cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )
    ```

    ---
    - Args:
        - [dagObject]: Input item(s).
        - apply (a): If this flag is true, the accumulated transforms are applied to the shape after the transforms are made identity, such that the world space positions of the transforms pivots are preserved, and the shapes do not move. The default is false.
        - jointOrient (jo): If this flag is set, the joint orient on joints will be reset to align with worldspace.
        - normal (n): If this flag is set to 1, the normals on polygonal objects will be frozen.  This flag is valid only when the -apply flag is on. If this flag is set to 2, the normals on polygonal objects will be frozen only if its a non-rigid transformation
            matrix. ie, a transformation that does not contain shear, skew or non-proportional scaling. The default behaviour is not to freeze normals.
        - preserveNormals (pn): If this flag is true, the normals on polygonal objects will be reversed if the objects are negatively scaled (reflection). This flag is valid only when the -apply flag is on.
        - rotate (r): If this flag is true, only the rotation is applied to the shape. The rotation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
        - scale (s): If this flag is true, only the scale is applied to the shape. The scale factor will be changed to 1, 1, 1. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
        - translate (t): If this flag is true, only the translation is applied to the shape. The translation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s)  are applied.  (Note: the translate flag is
            not meaningful when applied to joints, since joints are made to preserve their world space position.  This flag will have no effect on joints.)
    """
@overload #Overload for makeIdentity in ['create']
def makeIdentity([dagObject]: [dagObject], apply: bool = ..., a: bool = ..., jointOrient: bool = ..., jo: bool = ..., normal: int = ..., n: int = ..., preserveNormals: bool = ..., pn: bool = ..., rotate: bool = ..., r: bool = ..., scale: bool = ..., s: bool = ..., translate: bool = ..., t: bool = ...) -> None:
    """makeIdentity is undoable, NOT queryable, and NOT editable.
    
    The makeIdentity command is a quick way to reset the selected transform and
    all of its children down to the shape level by the identity transformation.
    You can also specify which of transform, rotate or scale is applied down from
    the selected transform. The identity transformation means:
    
    * translate = 0, 0, 0
    * rotate = 0, 0, 0
    * scale = 1, 1, 1
    * shear = 1, 1, 1
    
    If a transform is a joint, then the "translate" attribute may not be 0, but
    will be used to position the joints so that they preserve their world space
    positions. The translate flag doesn't apply to joints, since joints must
    preserve their world space positions. Only the rotate and scale flags are
    meaningful when applied to joints.
    
    If the -a/apply flag is true, then the transforms that are reset are
    accumulated and applied to the all shapes below the modified transforms, so
    that the shapes will not move. The pivot positions are recalculated so that
    they also will not move in world space. If this flag is false, then the
    transformations are reset to identity, without any changes to preserve
    position.

    Example:
    ```python
        import maya.cmds as cmds
        # Example 1:  Create a hierarchical object, for example a
        # car. Scale the tires, translate the doors into place, rotate the
        # steering wheel, then select the group node above the car, and type:
        cmds.makeIdentity( apply=True )
        # The car should not move.
        cmds.move( 3, 0, 0 )
        # The car should move exactly 3 units to (3, 0, 0), since
        # the previous makeIdentity command set its translation to (0, 0, 0).
        cmds.makeIdentity()
        # The car should return to the same position as before the move.
        # Example 2:  Create a curve and translate, rotate and scale it.
        # Then group it and translate, rotate and scale the group.
        cmds.makeIdentity( 'group1', apply=True, translate=True )
        # The curve will not move, but both the curve transform's and group
        # transform's translation will be set to 0, 0, 0. The rotation and
        # scale will remain the same.
        cmds.makeIdentity( 'group1', apply=True, rotate=True )
        # The curve will not move, but both the curve transform's and group
        # transform's rotation will be set to 0, 0, 0. The translation and
        # scale will remain the same.
        cmds.makeIdentity( 'group1', apply=True, scale=True )
        # The curve will not move, but both the curve transform's and group
        # transform's scale will be set to 1, 1, 1. The translation and rotation
        # will remain the same.
        cmds.makeIdentity( 'group1', apply=True, translate=True, rotate=True )
        # The curve will not move, but both the curve transform's and group
        # transform's translation and rotation will be set to 0, 0, 0.
        # The scale will remain the same.
        cmds.makeIdentity( 'group1', apply=False, translate=True )
        # The curve transform and group transform will have their translation
        # set to 0, 0, 0. The curve will probably move, since the apply
        # flag is false.
        cmds.makeIdentity( apply=True, translate=True, rotate=True, scale=True )
        # This is the same as "makeIdentity -apply true".
        # Example 3:  Create a polyCube and translate, rotate and scale it.
        # And then freeze the normals.
        cmds.polyCube()
        cmds.rotate( 30, 45, 0 )
        cmds.move( 2, 0, 2, r=True )
        cmds.scale( 2, 1, 2, r=True )
        cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )
    ```

    ---
    - Args:
        - [dagObject]: Input item(s).
        - apply (a): If this flag is true, the accumulated transforms are applied to the shape after the transforms are made identity, such that the world space positions of the transforms pivots are preserved, and the shapes do not move. The default is false.
        - jointOrient (jo): If this flag is set, the joint orient on joints will be reset to align with worldspace.
        - normal (n): If this flag is set to 1, the normals on polygonal objects will be frozen.  This flag is valid only when the -apply flag is on. If this flag is set to 2, the normals on polygonal objects will be frozen only if its a non-rigid transformation
            matrix. ie, a transformation that does not contain shear, skew or non-proportional scaling. The default behaviour is not to freeze normals.
        - preserveNormals (pn): If this flag is true, the normals on polygonal objects will be reversed if the objects are negatively scaled (reflection). This flag is valid only when the -apply flag is on.
        - rotate (r): If this flag is true, only the rotation is applied to the shape. The rotation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
        - scale (s): If this flag is true, only the scale is applied to the shape. The scale factor will be changed to 1, 1, 1. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
        - translate (t): If this flag is true, only the translation is applied to the shape. The translation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s)  are applied.  (Note: the translate flag is
            not meaningful when applied to joints, since joints are made to preserve their world space position.  This flag will have no effect on joints.)
    """
