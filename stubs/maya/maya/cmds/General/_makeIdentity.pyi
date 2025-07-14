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
