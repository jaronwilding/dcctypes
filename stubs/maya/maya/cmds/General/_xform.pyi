"""Stub files for General category in Maya commands, command: xform."""

from typing import Any, overload

@overload #Overload for xform in ['create']
def xform([objects...]: [objects...], absolute: bool = ..., centerPivots: bool = ..., centerPivotsOnComponents: bool = ..., deletePriorHistory: bool = ..., euler: bool = ..., matrix: [float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float] = ..., objectSpace: bool = ..., parentSpace: bool = ..., pivots: [linear, linear, linear] = ..., preserve: bool = ..., preserveUV: bool = ..., reflection: bool = ..., reflectionAboutBBox: bool = ..., reflectionAboutOrigin: bool = ..., reflectionAboutX: bool = ..., reflectionAboutY: bool = ..., reflectionAboutZ: bool = ..., reflectionTolerance: float = ..., relative: bool = ..., rotateAxis: [angle, angle, angle] = ..., rotateOrder: str = ..., rotatePivot: [linear, linear, linear] = ..., rotateTranslation: [linear, linear, linear] = ..., rotation: [angle, angle, angle] = ..., scale: [float, float, float] = ..., scalePivot: [linear, linear, linear] = ..., scaleTranslation: [linear, linear, linear] = ..., shear: [float, float, float] = ..., translation: [linear, linear, linear] = ..., worldSpace: bool = ..., worldSpaceDistance: bool = ..., zeroTransformPivots: bool = ...) -> None:
    """xform is undoable, queryable, and NOT editable.
    
    This command can be used query/set any element in a transformation node. It
    can also be used to query some values that cannot be set directly such as the
    transformation matrix or the bounding box. It can also set both pivot points
    to convenient values.
    
    All values are specified in transformation coordinates. (attribute-space)
    
    In addition, the attributes are applied/returned in the order in which they
    appear in the flags section. (which corresponds to the order they appear in
    the transformation matrix as given below)
    
    See also: move, rotate, scale
    
    ## Notes
    
    The transformation matrix for a node is built by post-multiplying the
    following matrices in the given order (Note: rotations are applied according
    to the rotation order parameter and the 6 different rotation possibilities are
    not shown below)
    
    
    
    //                        -1                       -1
    //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
    //
    //where:
    //
    //[sp] = |  1      0        0       0 | = scale pivot matrix
    //       |  0      1        0       0 |
    //       |  0      0        1       0 |
    //       | -spx   -spy     -spz     1 |
    //
    //[s]  = |  sx     0        0       0 | = scale matrix
    //       |  0      sy       0       0 |
    //       |  0      0        sz      0 |
    //       |  0      0        0       1 |
    //
    //
    //[sh] = |  1      0        0       0 | = shear matrix
    //       |  xy     1        0       0 |
    //       |  xz     yz       1       0 |
    //       |  0      0        0       1 |
    //
    //   -1
    //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  spx     spy     spz     1 |
    //
    //[st] = |  1       0       0       0 | = scale translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  stx     sty     stz     1 |
    //
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       | -rpx    -rpy    -rpz     1 |
    //
    //[ar] = |  *       *       *       0 | = axis rotation matrix
    //       |  *       *       *       0 |   (composite rotation,
    //       |  *       *       *       0 |    see [rx], [ry], [rz]
    //       |  0       0       0       1 |    below for details)
    //
    //[rx] = |  1       0       0       0 | = rotate X matrix
    //       |  0       cos(x)  sin(x)  0 |
    //       |  0      -sin(x)  cos(x)  0 |
    //       |  0       0       0       1 |
    //
    //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
    //       |  0       1       0       0 |
    //       |  sin(y)  0       cos(y)  0 |
    //       |  0       0       0       1 |
    //
    //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
    //       | -sin(z)  cos(z)  0       0 |
    //       |  0       0       1       0 |
    //       |  0       0       0       1 |
    //
    //   -1
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rpx     rpy     rpz     1 |
    //
    //[rt] = |  1       0       0       0 | = rotate translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rtx     rty     rtz     1 |
    //
    //[t]  = |  1       0       0       0 | = translation matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  tx      ty      tz      1 |

    Example:
    ```python
        //                        -1                       -1
        //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
        //
        //where:
        //
        //[sp] = |  1      0        0       0 | = scale pivot matrix
        //       |  0      1        0       0 |
        //       |  0      0        1       0 |
        //       | -spx   -spy     -spz     1 |
        //
        //[s]  = |  sx     0        0       0 | = scale matrix
        //       |  0      sy       0       0 |
        //       |  0      0        sz      0 |
        //       |  0      0        0       1 |
        //
        //
        //[sh] = |  1      0        0       0 | = shear matrix
        //       |  xy     1        0       0 |
        //       |  xz     yz       1       0 |
        //       |  0      0        0       1 |
        //
        //   -1
        //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  spx     spy     spz     1 |
        //
        //[st] = |  1       0       0       0 | = scale translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  stx     sty     stz     1 |
        //
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       | -rpx    -rpy    -rpz     1 |
        //
        //[ar] = |  *       *       *       0 | = axis rotation matrix
        //       |  *       *       *       0 |   (composite rotation,
        //       |  *       *       *       0 |    see [rx], [ry], [rz]
        //       |  0       0       0       1 |    below for details)
        //
        //[rx] = |  1       0       0       0 | = rotate X matrix
        //       |  0       cos(x)  sin(x)  0 |
        //       |  0      -sin(x)  cos(x)  0 |
        //       |  0       0       0       1 |
        //
        //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
        //       |  0       1       0       0 |
        //       |  sin(y)  0       cos(y)  0 |
        //       |  0       0       0       1 |
        //
        //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
        //       | -sin(z)  cos(z)  0       0 |
        //       |  0       0       1       0 |
        //       |  0       0       0       1 |
        //
        //   -1
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rpx     rpy     rpz     1 |
        //
        //[rt] = |  1       0       0       0 | = rotate translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rtx     rty     rtz     1 |
        //
        //[t]  = |  1       0       0       0 | = translation matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  tx      ty      tz      1 |
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - absolute (a): perform absolute transformation (default)
        - centerPivots (cp): Set pivot points to the center of the object's bounding box. (see -p flag)
        - centerPivotsOnComponents (cpc): Set pivot points to the center of the component's bounding box. (see -p flag)
        - deletePriorHistory (dph): If true then delete the construction history before the operation is performed.
        - euler (eu): modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.
        - matrix (m): Sets/returns the composite transformation matrix. *Note* the matrix is represented by 16 double arguments that are specified in row order.
        - objectSpace (os): treat values as object-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - parentSpace (ps): treat values as parent-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - pivots (piv): convenience method that changes both the rotate and scale pivots simultaneously. (see -rp -sp flags for more info)
        - preserve (p): preserve overall transformation. used to prevent object from "jumping" when changing pivots or rotation order. the default value is true. (used with -sp, -rp, -roo, -cp, -ra)
        - preserveUV (puv): When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices.
            Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): perform relative transformation
        - rotateAxis (ra): rotation axis orientation (when used with the -p flag the overall rotation is preserved by modifying the rotation to compensate for the axis rotation)
        - rotateOrder (roo): rotation order (when used with the -p flag the overall rotation is preserved by modifying the local rotation to be quivalent to the old one) Valid values for this flag are <xyz | yzx | zxy | xzy | yxz | zyx>
        - rotatePivot (rp): rotate pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the rotation translation)
        - rotateTranslation (rt): rotation translation
        - rotation (ro): rotation transformation
        - scale (s): scale transformation
        - scalePivot (sp): scale pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the scale translation)
        - scaleTranslation (st): scale translation
        - shear (sh): shear transformation. The values represent the shear <xy,xz,yz>
        - translation (t): translation
        - worldSpace (ws): (works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags). Note that, when querying the scale, that this calculation is cumulative and is only valid if there are all uniform scales and no rotation. In a
            hierarchy with non-uniform scale and rotation, this value may not correspond entirely with the perceived global scale.
        - worldSpaceDistance (wd): Values for -sp, -rp, -st, -rt, -t, -piv flags are treated as world space distances to move along the local axis. (where the local axis depends on whether the command is operating in local-space or object-space. This flag has no effect for
            world space.
        - zeroTransformPivots (ztp): reset pivot points and pivot translations without changing the overall matrix by applying these values into the translation channel.
    """
@overload #Overload for xform in ['create']
def xform([objects...]: [objects...], a: bool = ..., cp: bool = ..., cpc: bool = ..., dph: bool = ..., eu: bool = ..., m: [float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float] = ..., os: bool = ..., ps: bool = ..., piv: [linear, linear, linear] = ..., p: bool = ..., puv: bool = ..., rfl: bool = ..., rab: bool = ..., rao: bool = ..., rax: bool = ..., ray: bool = ..., raz: bool = ..., rft: float = ..., r: bool = ..., ra: [angle, angle, angle] = ..., roo: str = ..., rp: [linear, linear, linear] = ..., rt: [linear, linear, linear] = ..., ro: [angle, angle, angle] = ..., s: [float, float, float] = ..., sp: [linear, linear, linear] = ..., st: [linear, linear, linear] = ..., sh: [float, float, float] = ..., t: [linear, linear, linear] = ..., ws: bool = ..., wd: bool = ..., ztp: bool = ...) -> None:
    """xform is undoable, queryable, and NOT editable.
    
    This command can be used query/set any element in a transformation node. It
    can also be used to query some values that cannot be set directly such as the
    transformation matrix or the bounding box. It can also set both pivot points
    to convenient values.
    
    All values are specified in transformation coordinates. (attribute-space)
    
    In addition, the attributes are applied/returned in the order in which they
    appear in the flags section. (which corresponds to the order they appear in
    the transformation matrix as given below)
    
    See also: move, rotate, scale
    
    ## Notes
    
    The transformation matrix for a node is built by post-multiplying the
    following matrices in the given order (Note: rotations are applied according
    to the rotation order parameter and the 6 different rotation possibilities are
    not shown below)
    
    
    
    //                        -1                       -1
    //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
    //
    //where:
    //
    //[sp] = |  1      0        0       0 | = scale pivot matrix
    //       |  0      1        0       0 |
    //       |  0      0        1       0 |
    //       | -spx   -spy     -spz     1 |
    //
    //[s]  = |  sx     0        0       0 | = scale matrix
    //       |  0      sy       0       0 |
    //       |  0      0        sz      0 |
    //       |  0      0        0       1 |
    //
    //
    //[sh] = |  1      0        0       0 | = shear matrix
    //       |  xy     1        0       0 |
    //       |  xz     yz       1       0 |
    //       |  0      0        0       1 |
    //
    //   -1
    //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  spx     spy     spz     1 |
    //
    //[st] = |  1       0       0       0 | = scale translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  stx     sty     stz     1 |
    //
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       | -rpx    -rpy    -rpz     1 |
    //
    //[ar] = |  *       *       *       0 | = axis rotation matrix
    //       |  *       *       *       0 |   (composite rotation,
    //       |  *       *       *       0 |    see [rx], [ry], [rz]
    //       |  0       0       0       1 |    below for details)
    //
    //[rx] = |  1       0       0       0 | = rotate X matrix
    //       |  0       cos(x)  sin(x)  0 |
    //       |  0      -sin(x)  cos(x)  0 |
    //       |  0       0       0       1 |
    //
    //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
    //       |  0       1       0       0 |
    //       |  sin(y)  0       cos(y)  0 |
    //       |  0       0       0       1 |
    //
    //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
    //       | -sin(z)  cos(z)  0       0 |
    //       |  0       0       1       0 |
    //       |  0       0       0       1 |
    //
    //   -1
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rpx     rpy     rpz     1 |
    //
    //[rt] = |  1       0       0       0 | = rotate translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rtx     rty     rtz     1 |
    //
    //[t]  = |  1       0       0       0 | = translation matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  tx      ty      tz      1 |

    Example:
    ```python
        //                        -1                       -1
        //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
        //
        //where:
        //
        //[sp] = |  1      0        0       0 | = scale pivot matrix
        //       |  0      1        0       0 |
        //       |  0      0        1       0 |
        //       | -spx   -spy     -spz     1 |
        //
        //[s]  = |  sx     0        0       0 | = scale matrix
        //       |  0      sy       0       0 |
        //       |  0      0        sz      0 |
        //       |  0      0        0       1 |
        //
        //
        //[sh] = |  1      0        0       0 | = shear matrix
        //       |  xy     1        0       0 |
        //       |  xz     yz       1       0 |
        //       |  0      0        0       1 |
        //
        //   -1
        //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  spx     spy     spz     1 |
        //
        //[st] = |  1       0       0       0 | = scale translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  stx     sty     stz     1 |
        //
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       | -rpx    -rpy    -rpz     1 |
        //
        //[ar] = |  *       *       *       0 | = axis rotation matrix
        //       |  *       *       *       0 |   (composite rotation,
        //       |  *       *       *       0 |    see [rx], [ry], [rz]
        //       |  0       0       0       1 |    below for details)
        //
        //[rx] = |  1       0       0       0 | = rotate X matrix
        //       |  0       cos(x)  sin(x)  0 |
        //       |  0      -sin(x)  cos(x)  0 |
        //       |  0       0       0       1 |
        //
        //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
        //       |  0       1       0       0 |
        //       |  sin(y)  0       cos(y)  0 |
        //       |  0       0       0       1 |
        //
        //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
        //       | -sin(z)  cos(z)  0       0 |
        //       |  0       0       1       0 |
        //       |  0       0       0       1 |
        //
        //   -1
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rpx     rpy     rpz     1 |
        //
        //[rt] = |  1       0       0       0 | = rotate translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rtx     rty     rtz     1 |
        //
        //[t]  = |  1       0       0       0 | = translation matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  tx      ty      tz      1 |
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - absolute (a): perform absolute transformation (default)
        - centerPivots (cp): Set pivot points to the center of the object's bounding box. (see -p flag)
        - centerPivotsOnComponents (cpc): Set pivot points to the center of the component's bounding box. (see -p flag)
        - deletePriorHistory (dph): If true then delete the construction history before the operation is performed.
        - euler (eu): modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.
        - matrix (m): Sets/returns the composite transformation matrix. *Note* the matrix is represented by 16 double arguments that are specified in row order.
        - objectSpace (os): treat values as object-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - parentSpace (ps): treat values as parent-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - pivots (piv): convenience method that changes both the rotate and scale pivots simultaneously. (see -rp -sp flags for more info)
        - preserve (p): preserve overall transformation. used to prevent object from "jumping" when changing pivots or rotation order. the default value is true. (used with -sp, -rp, -roo, -cp, -ra)
        - preserveUV (puv): When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices.
            Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): perform relative transformation
        - rotateAxis (ra): rotation axis orientation (when used with the -p flag the overall rotation is preserved by modifying the rotation to compensate for the axis rotation)
        - rotateOrder (roo): rotation order (when used with the -p flag the overall rotation is preserved by modifying the local rotation to be quivalent to the old one) Valid values for this flag are <xyz | yzx | zxy | xzy | yxz | zyx>
        - rotatePivot (rp): rotate pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the rotation translation)
        - rotateTranslation (rt): rotation translation
        - rotation (ro): rotation transformation
        - scale (s): scale transformation
        - scalePivot (sp): scale pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the scale translation)
        - scaleTranslation (st): scale translation
        - shear (sh): shear transformation. The values represent the shear <xy,xz,yz>
        - translation (t): translation
        - worldSpace (ws): (works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags). Note that, when querying the scale, that this calculation is cumulative and is only valid if there are all uniform scales and no rotation. In a
            hierarchy with non-uniform scale and rotation, this value may not correspond entirely with the perceived global scale.
        - worldSpaceDistance (wd): Values for -sp, -rp, -st, -rt, -t, -piv flags are treated as world space distances to move along the local axis. (where the local axis depends on whether the command is operating in local-space or object-space. This flag has no effect for
            world space.
        - zeroTransformPivots (ztp): reset pivot points and pivot translations without changing the overall matrix by applying these values into the translation channel.
    """
@overload #Overload for xform in ['create']
def xform([objects...]: [objects...], absolute: bool = ..., a: bool = ..., centerPivots: bool = ..., cp: bool = ..., centerPivotsOnComponents: bool = ..., cpc: bool = ..., deletePriorHistory: bool = ..., dph: bool = ..., euler: bool = ..., eu: bool = ..., matrix: [float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float] = ..., m: [float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float] = ..., objectSpace: bool = ..., os: bool = ..., parentSpace: bool = ..., ps: bool = ..., pivots: [linear, linear, linear] = ..., piv: [linear, linear, linear] = ..., preserve: bool = ..., p: bool = ..., preserveUV: bool = ..., puv: bool = ..., reflection: bool = ..., rfl: bool = ..., reflectionAboutBBox: bool = ..., rab: bool = ..., reflectionAboutOrigin: bool = ..., rao: bool = ..., reflectionAboutX: bool = ..., rax: bool = ..., reflectionAboutY: bool = ..., ray: bool = ..., reflectionAboutZ: bool = ..., raz: bool = ..., reflectionTolerance: float = ..., rft: float = ..., relative: bool = ..., r: bool = ..., rotateAxis: [angle, angle, angle] = ..., ra: [angle, angle, angle] = ..., rotateOrder: str = ..., roo: str = ..., rotatePivot: [linear, linear, linear] = ..., rp: [linear, linear, linear] = ..., rotateTranslation: [linear, linear, linear] = ..., rt: [linear, linear, linear] = ..., rotation: [angle, angle, angle] = ..., ro: [angle, angle, angle] = ..., scale: [float, float, float] = ..., s: [float, float, float] = ..., scalePivot: [linear, linear, linear] = ..., sp: [linear, linear, linear] = ..., scaleTranslation: [linear, linear, linear] = ..., st: [linear, linear, linear] = ..., shear: [float, float, float] = ..., sh: [float, float, float] = ..., translation: [linear, linear, linear] = ..., t: [linear, linear, linear] = ..., worldSpace: bool = ..., ws: bool = ..., worldSpaceDistance: bool = ..., wd: bool = ..., zeroTransformPivots: bool = ..., ztp: bool = ...) -> None:
    """xform is undoable, queryable, and NOT editable.
    
    This command can be used query/set any element in a transformation node. It
    can also be used to query some values that cannot be set directly such as the
    transformation matrix or the bounding box. It can also set both pivot points
    to convenient values.
    
    All values are specified in transformation coordinates. (attribute-space)
    
    In addition, the attributes are applied/returned in the order in which they
    appear in the flags section. (which corresponds to the order they appear in
    the transformation matrix as given below)
    
    See also: move, rotate, scale
    
    ## Notes
    
    The transformation matrix for a node is built by post-multiplying the
    following matrices in the given order (Note: rotations are applied according
    to the rotation order parameter and the 6 different rotation possibilities are
    not shown below)
    
    
    
    //                        -1                       -1
    //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
    //
    //where:
    //
    //[sp] = |  1      0        0       0 | = scale pivot matrix
    //       |  0      1        0       0 |
    //       |  0      0        1       0 |
    //       | -spx   -spy     -spz     1 |
    //
    //[s]  = |  sx     0        0       0 | = scale matrix
    //       |  0      sy       0       0 |
    //       |  0      0        sz      0 |
    //       |  0      0        0       1 |
    //
    //
    //[sh] = |  1      0        0       0 | = shear matrix
    //       |  xy     1        0       0 |
    //       |  xz     yz       1       0 |
    //       |  0      0        0       1 |
    //
    //   -1
    //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  spx     spy     spz     1 |
    //
    //[st] = |  1       0       0       0 | = scale translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  stx     sty     stz     1 |
    //
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       | -rpx    -rpy    -rpz     1 |
    //
    //[ar] = |  *       *       *       0 | = axis rotation matrix
    //       |  *       *       *       0 |   (composite rotation,
    //       |  *       *       *       0 |    see [rx], [ry], [rz]
    //       |  0       0       0       1 |    below for details)
    //
    //[rx] = |  1       0       0       0 | = rotate X matrix
    //       |  0       cos(x)  sin(x)  0 |
    //       |  0      -sin(x)  cos(x)  0 |
    //       |  0       0       0       1 |
    //
    //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
    //       |  0       1       0       0 |
    //       |  sin(y)  0       cos(y)  0 |
    //       |  0       0       0       1 |
    //
    //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
    //       | -sin(z)  cos(z)  0       0 |
    //       |  0       0       1       0 |
    //       |  0       0       0       1 |
    //
    //   -1
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rpx     rpy     rpz     1 |
    //
    //[rt] = |  1       0       0       0 | = rotate translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rtx     rty     rtz     1 |
    //
    //[t]  = |  1       0       0       0 | = translation matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  tx      ty      tz      1 |

    Example:
    ```python
        //                        -1                       -1
        //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
        //
        //where:
        //
        //[sp] = |  1      0        0       0 | = scale pivot matrix
        //       |  0      1        0       0 |
        //       |  0      0        1       0 |
        //       | -spx   -spy     -spz     1 |
        //
        //[s]  = |  sx     0        0       0 | = scale matrix
        //       |  0      sy       0       0 |
        //       |  0      0        sz      0 |
        //       |  0      0        0       1 |
        //
        //
        //[sh] = |  1      0        0       0 | = shear matrix
        //       |  xy     1        0       0 |
        //       |  xz     yz       1       0 |
        //       |  0      0        0       1 |
        //
        //   -1
        //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  spx     spy     spz     1 |
        //
        //[st] = |  1       0       0       0 | = scale translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  stx     sty     stz     1 |
        //
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       | -rpx    -rpy    -rpz     1 |
        //
        //[ar] = |  *       *       *       0 | = axis rotation matrix
        //       |  *       *       *       0 |   (composite rotation,
        //       |  *       *       *       0 |    see [rx], [ry], [rz]
        //       |  0       0       0       1 |    below for details)
        //
        //[rx] = |  1       0       0       0 | = rotate X matrix
        //       |  0       cos(x)  sin(x)  0 |
        //       |  0      -sin(x)  cos(x)  0 |
        //       |  0       0       0       1 |
        //
        //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
        //       |  0       1       0       0 |
        //       |  sin(y)  0       cos(y)  0 |
        //       |  0       0       0       1 |
        //
        //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
        //       | -sin(z)  cos(z)  0       0 |
        //       |  0       0       1       0 |
        //       |  0       0       0       1 |
        //
        //   -1
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rpx     rpy     rpz     1 |
        //
        //[rt] = |  1       0       0       0 | = rotate translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rtx     rty     rtz     1 |
        //
        //[t]  = |  1       0       0       0 | = translation matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  tx      ty      tz      1 |
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - absolute (a): perform absolute transformation (default)
        - centerPivots (cp): Set pivot points to the center of the object's bounding box. (see -p flag)
        - centerPivotsOnComponents (cpc): Set pivot points to the center of the component's bounding box. (see -p flag)
        - deletePriorHistory (dph): If true then delete the construction history before the operation is performed.
        - euler (eu): modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.
        - matrix (m): Sets/returns the composite transformation matrix. *Note* the matrix is represented by 16 double arguments that are specified in row order.
        - objectSpace (os): treat values as object-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - parentSpace (ps): treat values as parent-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - pivots (piv): convenience method that changes both the rotate and scale pivots simultaneously. (see -rp -sp flags for more info)
        - preserve (p): preserve overall transformation. used to prevent object from "jumping" when changing pivots or rotation order. the default value is true. (used with -sp, -rp, -roo, -cp, -ra)
        - preserveUV (puv): When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices.
            Default is false.
        - reflection (rfl): To move the corresponding symmetric components also.
        - reflectionAboutBBox (rab): Sets the position of the reflection axis  at the geometry bounding box
        - reflectionAboutOrigin (rao): Sets the position of the reflection axis  at the origin
        - reflectionAboutX (rax): Specifies the X=0 as reflection plane
        - reflectionAboutY (ray): Specifies the Y=0 as reflection plane
        - reflectionAboutZ (raz): Specifies the Z=0 as reflection plane
        - reflectionTolerance (rft): Specifies the tolerance to findout the corresponding reflected components
        - relative (r): perform relative transformation
        - rotateAxis (ra): rotation axis orientation (when used with the -p flag the overall rotation is preserved by modifying the rotation to compensate for the axis rotation)
        - rotateOrder (roo): rotation order (when used with the -p flag the overall rotation is preserved by modifying the local rotation to be quivalent to the old one) Valid values for this flag are <xyz | yzx | zxy | xzy | yxz | zyx>
        - rotatePivot (rp): rotate pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the rotation translation)
        - rotateTranslation (rt): rotation translation
        - rotation (ro): rotation transformation
        - scale (s): scale transformation
        - scalePivot (sp): scale pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the scale translation)
        - scaleTranslation (st): scale translation
        - shear (sh): shear transformation. The values represent the shear <xy,xz,yz>
        - translation (t): translation
        - worldSpace (ws): (works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags). Note that, when querying the scale, that this calculation is cumulative and is only valid if there are all uniform scales and no rotation. In a
            hierarchy with non-uniform scale and rotation, this value may not correspond entirely with the perceived global scale.
        - worldSpaceDistance (wd): Values for -sp, -rp, -st, -rt, -t, -piv flags are treated as world space distances to move along the local axis. (where the local axis depends on whether the command is operating in local-space or object-space. This flag has no effect for
            world space.
        - zeroTransformPivots (ztp): reset pivot points and pivot translations without changing the overall matrix by applying these values into the translation channel.
    """
@overload #Overload for xform in ['query']
def xform([objects...]: [objects...], boundingBox: bool = ..., boundingBoxInvisible: bool = ..., matrix: [float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float] = ..., objectSpace: bool = ..., parentSpace: bool = ..., pivots: [linear, linear, linear] = ..., rotateAxis: [angle, angle, angle] = ..., rotateOrder: str = ..., rotatePivot: [linear, linear, linear] = ..., rotateTranslation: [linear, linear, linear] = ..., rotation: [angle, angle, angle] = ..., scale: [float, float, float] = ..., scalePivot: [linear, linear, linear] = ..., scaleTranslation: [linear, linear, linear] = ..., shear: [float, float, float] = ..., translation: [linear, linear, linear] = ..., worldSpace: bool = ..., worldSpaceDistance: bool = ..., query: bool = ...) -> None:
    """xform is undoable, queryable, and NOT editable.
    
    This command can be used query/set any element in a transformation node. It
    can also be used to query some values that cannot be set directly such as the
    transformation matrix or the bounding box. It can also set both pivot points
    to convenient values.
    
    All values are specified in transformation coordinates. (attribute-space)
    
    In addition, the attributes are applied/returned in the order in which they
    appear in the flags section. (which corresponds to the order they appear in
    the transformation matrix as given below)
    
    See also: move, rotate, scale
    
    ## Notes
    
    The transformation matrix for a node is built by post-multiplying the
    following matrices in the given order (Note: rotations are applied according
    to the rotation order parameter and the 6 different rotation possibilities are
    not shown below)
    
    
    
    //                        -1                       -1
    //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
    //
    //where:
    //
    //[sp] = |  1      0        0       0 | = scale pivot matrix
    //       |  0      1        0       0 |
    //       |  0      0        1       0 |
    //       | -spx   -spy     -spz     1 |
    //
    //[s]  = |  sx     0        0       0 | = scale matrix
    //       |  0      sy       0       0 |
    //       |  0      0        sz      0 |
    //       |  0      0        0       1 |
    //
    //
    //[sh] = |  1      0        0       0 | = shear matrix
    //       |  xy     1        0       0 |
    //       |  xz     yz       1       0 |
    //       |  0      0        0       1 |
    //
    //   -1
    //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  spx     spy     spz     1 |
    //
    //[st] = |  1       0       0       0 | = scale translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  stx     sty     stz     1 |
    //
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       | -rpx    -rpy    -rpz     1 |
    //
    //[ar] = |  *       *       *       0 | = axis rotation matrix
    //       |  *       *       *       0 |   (composite rotation,
    //       |  *       *       *       0 |    see [rx], [ry], [rz]
    //       |  0       0       0       1 |    below for details)
    //
    //[rx] = |  1       0       0       0 | = rotate X matrix
    //       |  0       cos(x)  sin(x)  0 |
    //       |  0      -sin(x)  cos(x)  0 |
    //       |  0       0       0       1 |
    //
    //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
    //       |  0       1       0       0 |
    //       |  sin(y)  0       cos(y)  0 |
    //       |  0       0       0       1 |
    //
    //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
    //       | -sin(z)  cos(z)  0       0 |
    //       |  0       0       1       0 |
    //       |  0       0       0       1 |
    //
    //   -1
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rpx     rpy     rpz     1 |
    //
    //[rt] = |  1       0       0       0 | = rotate translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rtx     rty     rtz     1 |
    //
    //[t]  = |  1       0       0       0 | = translation matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  tx      ty      tz      1 |

    Example:
    ```python
        //                        -1                       -1
        //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
        //
        //where:
        //
        //[sp] = |  1      0        0       0 | = scale pivot matrix
        //       |  0      1        0       0 |
        //       |  0      0        1       0 |
        //       | -spx   -spy     -spz     1 |
        //
        //[s]  = |  sx     0        0       0 | = scale matrix
        //       |  0      sy       0       0 |
        //       |  0      0        sz      0 |
        //       |  0      0        0       1 |
        //
        //
        //[sh] = |  1      0        0       0 | = shear matrix
        //       |  xy     1        0       0 |
        //       |  xz     yz       1       0 |
        //       |  0      0        0       1 |
        //
        //   -1
        //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  spx     spy     spz     1 |
        //
        //[st] = |  1       0       0       0 | = scale translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  stx     sty     stz     1 |
        //
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       | -rpx    -rpy    -rpz     1 |
        //
        //[ar] = |  *       *       *       0 | = axis rotation matrix
        //       |  *       *       *       0 |   (composite rotation,
        //       |  *       *       *       0 |    see [rx], [ry], [rz]
        //       |  0       0       0       1 |    below for details)
        //
        //[rx] = |  1       0       0       0 | = rotate X matrix
        //       |  0       cos(x)  sin(x)  0 |
        //       |  0      -sin(x)  cos(x)  0 |
        //       |  0       0       0       1 |
        //
        //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
        //       |  0       1       0       0 |
        //       |  sin(y)  0       cos(y)  0 |
        //       |  0       0       0       1 |
        //
        //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
        //       | -sin(z)  cos(z)  0       0 |
        //       |  0       0       1       0 |
        //       |  0       0       0       1 |
        //
        //   -1
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rpx     rpy     rpz     1 |
        //
        //[rt] = |  1       0       0       0 | = rotate translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rtx     rty     rtz     1 |
        //
        //[t]  = |  1       0       0       0 | = translation matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  tx      ty      tz      1 |
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - boundingBox (bb): Returns the bounding box of an object. The values returned are in the following order: xmin ymin zmin xmax ymax zmax.
        - boundingBoxInvisible (bbi): Returns the bounding box of an object. This includes the bounding boxes of all invisible children which are not included using the boundingBox flag. The values returned are in following order: xmin ymin zmin xmax ymax zmax.
        - matrix (m): Sets/returns the composite transformation matrix. *Note* the matrix is represented by 16 double arguments that are specified in row order.
        - objectSpace (os): treat values as object-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - parentSpace (ps): treat values as parent-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - pivots (piv): convenience method that changes both the rotate and scale pivots simultaneously. (see -rp -sp flags for more info)
        - rotateAxis (ra): rotation axis orientation (when used with the -p flag the overall rotation is preserved by modifying the rotation to compensate for the axis rotation)
        - rotateOrder (roo): rotation order (when used with the -p flag the overall rotation is preserved by modifying the local rotation to be quivalent to the old one) Valid values for this flag are <xyz | yzx | zxy | xzy | yxz | zyx>
        - rotatePivot (rp): rotate pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the rotation translation)
        - rotateTranslation (rt): rotation translation
        - rotation (ro): rotation transformation
        - scale (s): scale transformation
        - scalePivot (sp): scale pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the scale translation)
        - scaleTranslation (st): scale translation
        - shear (sh): shear transformation. The values represent the shear <xy,xz,yz>
        - translation (t): translation
        - worldSpace (ws): (works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags). Note that, when querying the scale, that this calculation is cumulative and is only valid if there are all uniform scales and no rotation. In a
            hierarchy with non-uniform scale and rotation, this value may not correspond entirely with the perceived global scale.
        - worldSpaceDistance (wd): Values for -sp, -rp, -st, -rt, -t, -piv flags are treated as world space distances to move along the local axis. (where the local axis depends on whether the command is operating in local-space or object-space. This flag has no effect for
            world space.
        - query (q): Query mode flag
    """
@overload #Overload for xform in ['query']
def xform([objects...]: [objects...], bb: bool = ..., bbi: bool = ..., m: [float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float] = ..., os: bool = ..., ps: bool = ..., piv: [linear, linear, linear] = ..., ra: [angle, angle, angle] = ..., roo: str = ..., rp: [linear, linear, linear] = ..., rt: [linear, linear, linear] = ..., ro: [angle, angle, angle] = ..., s: [float, float, float] = ..., sp: [linear, linear, linear] = ..., st: [linear, linear, linear] = ..., sh: [float, float, float] = ..., t: [linear, linear, linear] = ..., ws: bool = ..., wd: bool = ..., q: bool = ...) -> None:
    """xform is undoable, queryable, and NOT editable.
    
    This command can be used query/set any element in a transformation node. It
    can also be used to query some values that cannot be set directly such as the
    transformation matrix or the bounding box. It can also set both pivot points
    to convenient values.
    
    All values are specified in transformation coordinates. (attribute-space)
    
    In addition, the attributes are applied/returned in the order in which they
    appear in the flags section. (which corresponds to the order they appear in
    the transformation matrix as given below)
    
    See also: move, rotate, scale
    
    ## Notes
    
    The transformation matrix for a node is built by post-multiplying the
    following matrices in the given order (Note: rotations are applied according
    to the rotation order parameter and the 6 different rotation possibilities are
    not shown below)
    
    
    
    //                        -1                       -1
    //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
    //
    //where:
    //
    //[sp] = |  1      0        0       0 | = scale pivot matrix
    //       |  0      1        0       0 |
    //       |  0      0        1       0 |
    //       | -spx   -spy     -spz     1 |
    //
    //[s]  = |  sx     0        0       0 | = scale matrix
    //       |  0      sy       0       0 |
    //       |  0      0        sz      0 |
    //       |  0      0        0       1 |
    //
    //
    //[sh] = |  1      0        0       0 | = shear matrix
    //       |  xy     1        0       0 |
    //       |  xz     yz       1       0 |
    //       |  0      0        0       1 |
    //
    //   -1
    //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  spx     spy     spz     1 |
    //
    //[st] = |  1       0       0       0 | = scale translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  stx     sty     stz     1 |
    //
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       | -rpx    -rpy    -rpz     1 |
    //
    //[ar] = |  *       *       *       0 | = axis rotation matrix
    //       |  *       *       *       0 |   (composite rotation,
    //       |  *       *       *       0 |    see [rx], [ry], [rz]
    //       |  0       0       0       1 |    below for details)
    //
    //[rx] = |  1       0       0       0 | = rotate X matrix
    //       |  0       cos(x)  sin(x)  0 |
    //       |  0      -sin(x)  cos(x)  0 |
    //       |  0       0       0       1 |
    //
    //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
    //       |  0       1       0       0 |
    //       |  sin(y)  0       cos(y)  0 |
    //       |  0       0       0       1 |
    //
    //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
    //       | -sin(z)  cos(z)  0       0 |
    //       |  0       0       1       0 |
    //       |  0       0       0       1 |
    //
    //   -1
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rpx     rpy     rpz     1 |
    //
    //[rt] = |  1       0       0       0 | = rotate translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rtx     rty     rtz     1 |
    //
    //[t]  = |  1       0       0       0 | = translation matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  tx      ty      tz      1 |

    Example:
    ```python
        //                        -1                       -1
        //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
        //
        //where:
        //
        //[sp] = |  1      0        0       0 | = scale pivot matrix
        //       |  0      1        0       0 |
        //       |  0      0        1       0 |
        //       | -spx   -spy     -spz     1 |
        //
        //[s]  = |  sx     0        0       0 | = scale matrix
        //       |  0      sy       0       0 |
        //       |  0      0        sz      0 |
        //       |  0      0        0       1 |
        //
        //
        //[sh] = |  1      0        0       0 | = shear matrix
        //       |  xy     1        0       0 |
        //       |  xz     yz       1       0 |
        //       |  0      0        0       1 |
        //
        //   -1
        //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  spx     spy     spz     1 |
        //
        //[st] = |  1       0       0       0 | = scale translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  stx     sty     stz     1 |
        //
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       | -rpx    -rpy    -rpz     1 |
        //
        //[ar] = |  *       *       *       0 | = axis rotation matrix
        //       |  *       *       *       0 |   (composite rotation,
        //       |  *       *       *       0 |    see [rx], [ry], [rz]
        //       |  0       0       0       1 |    below for details)
        //
        //[rx] = |  1       0       0       0 | = rotate X matrix
        //       |  0       cos(x)  sin(x)  0 |
        //       |  0      -sin(x)  cos(x)  0 |
        //       |  0       0       0       1 |
        //
        //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
        //       |  0       1       0       0 |
        //       |  sin(y)  0       cos(y)  0 |
        //       |  0       0       0       1 |
        //
        //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
        //       | -sin(z)  cos(z)  0       0 |
        //       |  0       0       1       0 |
        //       |  0       0       0       1 |
        //
        //   -1
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rpx     rpy     rpz     1 |
        //
        //[rt] = |  1       0       0       0 | = rotate translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rtx     rty     rtz     1 |
        //
        //[t]  = |  1       0       0       0 | = translation matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  tx      ty      tz      1 |
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - boundingBox (bb): Returns the bounding box of an object. The values returned are in the following order: xmin ymin zmin xmax ymax zmax.
        - boundingBoxInvisible (bbi): Returns the bounding box of an object. This includes the bounding boxes of all invisible children which are not included using the boundingBox flag. The values returned are in following order: xmin ymin zmin xmax ymax zmax.
        - matrix (m): Sets/returns the composite transformation matrix. *Note* the matrix is represented by 16 double arguments that are specified in row order.
        - objectSpace (os): treat values as object-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - parentSpace (ps): treat values as parent-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - pivots (piv): convenience method that changes both the rotate and scale pivots simultaneously. (see -rp -sp flags for more info)
        - rotateAxis (ra): rotation axis orientation (when used with the -p flag the overall rotation is preserved by modifying the rotation to compensate for the axis rotation)
        - rotateOrder (roo): rotation order (when used with the -p flag the overall rotation is preserved by modifying the local rotation to be quivalent to the old one) Valid values for this flag are <xyz | yzx | zxy | xzy | yxz | zyx>
        - rotatePivot (rp): rotate pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the rotation translation)
        - rotateTranslation (rt): rotation translation
        - rotation (ro): rotation transformation
        - scale (s): scale transformation
        - scalePivot (sp): scale pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the scale translation)
        - scaleTranslation (st): scale translation
        - shear (sh): shear transformation. The values represent the shear <xy,xz,yz>
        - translation (t): translation
        - worldSpace (ws): (works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags). Note that, when querying the scale, that this calculation is cumulative and is only valid if there are all uniform scales and no rotation. In a
            hierarchy with non-uniform scale and rotation, this value may not correspond entirely with the perceived global scale.
        - worldSpaceDistance (wd): Values for -sp, -rp, -st, -rt, -t, -piv flags are treated as world space distances to move along the local axis. (where the local axis depends on whether the command is operating in local-space or object-space. This flag has no effect for
            world space.
        - query (q): Query mode flag
    """
@overload #Overload for xform in ['query']
def xform([objects...]: [objects...], boundingBox: bool = ..., bb: bool = ..., boundingBoxInvisible: bool = ..., bbi: bool = ..., matrix: [float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float] = ..., m: [float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float] = ..., objectSpace: bool = ..., os: bool = ..., parentSpace: bool = ..., ps: bool = ..., pivots: [linear, linear, linear] = ..., piv: [linear, linear, linear] = ..., rotateAxis: [angle, angle, angle] = ..., ra: [angle, angle, angle] = ..., rotateOrder: str = ..., roo: str = ..., rotatePivot: [linear, linear, linear] = ..., rp: [linear, linear, linear] = ..., rotateTranslation: [linear, linear, linear] = ..., rt: [linear, linear, linear] = ..., rotation: [angle, angle, angle] = ..., ro: [angle, angle, angle] = ..., scale: [float, float, float] = ..., s: [float, float, float] = ..., scalePivot: [linear, linear, linear] = ..., sp: [linear, linear, linear] = ..., scaleTranslation: [linear, linear, linear] = ..., st: [linear, linear, linear] = ..., shear: [float, float, float] = ..., sh: [float, float, float] = ..., translation: [linear, linear, linear] = ..., t: [linear, linear, linear] = ..., worldSpace: bool = ..., ws: bool = ..., worldSpaceDistance: bool = ..., wd: bool = ..., query: bool = ..., q: bool = ...) -> None:
    """xform is undoable, queryable, and NOT editable.
    
    This command can be used query/set any element in a transformation node. It
    can also be used to query some values that cannot be set directly such as the
    transformation matrix or the bounding box. It can also set both pivot points
    to convenient values.
    
    All values are specified in transformation coordinates. (attribute-space)
    
    In addition, the attributes are applied/returned in the order in which they
    appear in the flags section. (which corresponds to the order they appear in
    the transformation matrix as given below)
    
    See also: move, rotate, scale
    
    ## Notes
    
    The transformation matrix for a node is built by post-multiplying the
    following matrices in the given order (Note: rotations are applied according
    to the rotation order parameter and the 6 different rotation possibilities are
    not shown below)
    
    
    
    //                        -1                       -1
    //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
    //
    //where:
    //
    //[sp] = |  1      0        0       0 | = scale pivot matrix
    //       |  0      1        0       0 |
    //       |  0      0        1       0 |
    //       | -spx   -spy     -spz     1 |
    //
    //[s]  = |  sx     0        0       0 | = scale matrix
    //       |  0      sy       0       0 |
    //       |  0      0        sz      0 |
    //       |  0      0        0       1 |
    //
    //
    //[sh] = |  1      0        0       0 | = shear matrix
    //       |  xy     1        0       0 |
    //       |  xz     yz       1       0 |
    //       |  0      0        0       1 |
    //
    //   -1
    //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  spx     spy     spz     1 |
    //
    //[st] = |  1       0       0       0 | = scale translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  stx     sty     stz     1 |
    //
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       | -rpx    -rpy    -rpz     1 |
    //
    //[ar] = |  *       *       *       0 | = axis rotation matrix
    //       |  *       *       *       0 |   (composite rotation,
    //       |  *       *       *       0 |    see [rx], [ry], [rz]
    //       |  0       0       0       1 |    below for details)
    //
    //[rx] = |  1       0       0       0 | = rotate X matrix
    //       |  0       cos(x)  sin(x)  0 |
    //       |  0      -sin(x)  cos(x)  0 |
    //       |  0       0       0       1 |
    //
    //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
    //       |  0       1       0       0 |
    //       |  sin(y)  0       cos(y)  0 |
    //       |  0       0       0       1 |
    //
    //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
    //       | -sin(z)  cos(z)  0       0 |
    //       |  0       0       1       0 |
    //       |  0       0       0       1 |
    //
    //   -1
    //[rp] = |  1       0       0       0 | = rotate pivot matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rpx     rpy     rpz     1 |
    //
    //[rt] = |  1       0       0       0 | = rotate translate matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  rtx     rty     rtz     1 |
    //
    //[t]  = |  1       0       0       0 | = translation matrix
    //       |  0       1       0       0 |
    //       |  0       0       1       0 |
    //       |  tx      ty      tz      1 |

    Example:
    ```python
        //                        -1                       -1
        //[M]  = [sp]x[s]x[sh]x[sp]x[st]x[rp]x[ar]x[ro]x[rp]x[rt]x[t]
        //
        //where:
        //
        //[sp] = |  1      0        0       0 | = scale pivot matrix
        //       |  0      1        0       0 |
        //       |  0      0        1       0 |
        //       | -spx   -spy     -spz     1 |
        //
        //[s]  = |  sx     0        0       0 | = scale matrix
        //       |  0      sy       0       0 |
        //       |  0      0        sz      0 |
        //       |  0      0        0       1 |
        //
        //
        //[sh] = |  1      0        0       0 | = shear matrix
        //       |  xy     1        0       0 |
        //       |  xz     yz       1       0 |
        //       |  0      0        0       1 |
        //
        //   -1
        //[sp] = |  1       0       0       0 | = scale pivot inverse matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  spx     spy     spz     1 |
        //
        //[st] = |  1       0       0       0 | = scale translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  stx     sty     stz     1 |
        //
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       | -rpx    -rpy    -rpz     1 |
        //
        //[ar] = |  *       *       *       0 | = axis rotation matrix
        //       |  *       *       *       0 |   (composite rotation,
        //       |  *       *       *       0 |    see [rx], [ry], [rz]
        //       |  0       0       0       1 |    below for details)
        //
        //[rx] = |  1       0       0       0 | = rotate X matrix
        //       |  0       cos(x)  sin(x)  0 |
        //       |  0      -sin(x)  cos(x)  0 |
        //       |  0       0       0       1 |
        //
        //[ry] = |  cos(y)  0      -sin(y)  0 | = rotate Y matrix
        //       |  0       1       0       0 |
        //       |  sin(y)  0       cos(y)  0 |
        //       |  0       0       0       1 |
        //
        //[rz] = |  cos(z)  sin(z)  0       0 | = rotate Z matrix
        //       | -sin(z)  cos(z)  0       0 |
        //       |  0       0       1       0 |
        //       |  0       0       0       1 |
        //
        //   -1
        //[rp] = |  1       0       0       0 | = rotate pivot matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rpx     rpy     rpz     1 |
        //
        //[rt] = |  1       0       0       0 | = rotate translate matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  rtx     rty     rtz     1 |
        //
        //[t]  = |  1       0       0       0 | = translation matrix
        //       |  0       1       0       0 |
        //       |  0       0       1       0 |
        //       |  tx      ty      tz      1 |
    ```

    ---
    - Args:
        - [objects...]: Input item(s).
        - boundingBox (bb): Returns the bounding box of an object. The values returned are in the following order: xmin ymin zmin xmax ymax zmax.
        - boundingBoxInvisible (bbi): Returns the bounding box of an object. This includes the bounding boxes of all invisible children which are not included using the boundingBox flag. The values returned are in following order: xmin ymin zmin xmax ymax zmax.
        - matrix (m): Sets/returns the composite transformation matrix. *Note* the matrix is represented by 16 double arguments that are specified in row order.
        - objectSpace (os): treat values as object-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - parentSpace (ps): treat values as parent-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        - pivots (piv): convenience method that changes both the rotate and scale pivots simultaneously. (see -rp -sp flags for more info)
        - rotateAxis (ra): rotation axis orientation (when used with the -p flag the overall rotation is preserved by modifying the rotation to compensate for the axis rotation)
        - rotateOrder (roo): rotation order (when used with the -p flag the overall rotation is preserved by modifying the local rotation to be quivalent to the old one) Valid values for this flag are <xyz | yzx | zxy | xzy | yxz | zyx>
        - rotatePivot (rp): rotate pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the rotation translation)
        - rotateTranslation (rt): rotation translation
        - rotation (ro): rotation transformation
        - scale (s): scale transformation
        - scalePivot (sp): scale pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the scale translation)
        - scaleTranslation (st): scale translation
        - shear (sh): shear transformation. The values represent the shear <xy,xz,yz>
        - translation (t): translation
        - worldSpace (ws): (works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags). Note that, when querying the scale, that this calculation is cumulative and is only valid if there are all uniform scales and no rotation. In a
            hierarchy with non-uniform scale and rotation, this value may not correspond entirely with the perceived global scale.
        - worldSpaceDistance (wd): Values for -sp, -rp, -st, -rt, -t, -piv flags are treated as world space distances to move along the local axis. (where the local axis depends on whether the command is operating in local-space or object-space. This flag has no effect for
            world space.
        - query (q): Query mode flag
    """
