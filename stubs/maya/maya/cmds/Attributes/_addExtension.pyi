"""Stub files for Attributes category in Maya commands, command: addExtension."""

from typing import Any, overload

@overload #Overload for addExtension in ['create']
def addExtension(attributeType: str = ..., binaryTag: str = ..., cachedInternally: bool = ..., category: str = ..., dataType: str = ..., defaultValue: float = ..., disconnectBehaviour: int = ..., enforcingUniqueName: bool = ..., enumName: str = ..., exists: bool = ..., fromPlugin: bool = ..., hasMaxValue: bool = ..., hasMinValue: bool = ..., hasSoftMaxValue: bool = ..., hasSoftMinValue: bool = ..., hidden: bool = ..., indexMatters: bool = ..., internalSet: bool = ..., keyable: bool = ..., longName: str = ..., maxValue: float = ..., minValue: float = ..., multi: bool = ..., niceName: str = ..., nodeType: str = ..., numberOfChildren: int = ..., parent: str = ..., proxy: str = ..., readable: bool = ..., shortName: str = ..., softMaxValue: float = ..., softMinValue: float = ..., storable: bool = ..., usedAsColor: bool = ..., usedAsFilename: bool = ..., usedAsProxy: bool = ..., worldSpace: bool = ..., writable: bool = ...) -> None:
    """addExtension is NOT undoable, queryable, and editable.
    
    This command is used to add an extension attribute to a node type. Either the
    longName or the shortName or both must be specified. If neither a dataType nor
    an attributeType is specified, a double attribute will be added. The dataType
    flag can be specified more than once indicating that any of the supplied types
    will be accepted (logical-or).
    
    To add a non-double attribute the following criteria can be used to determine
    whether the dataType or the attributeType flag is appropriate. Some types,
    such as double3 can use either. In these cases the -dt flag should be used
    when you only wish to access the data as an atomic entity (eg. you never want
    to access the three individual values that make up a double3). In general it
    is best to use the -at in these cases for maximum flexibility. In most cases
    the -dt version will not display in the attribute editor as it is an atomic
    type and you are not allowed to change individual parts of it.
    
    All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created). See
    the EXAMPLES section for more details.
    
    Type of attribute |  Flag and argument to use
    ---|---
    boolean |  -at bool
    32 bit integer |  -at long
    16 bit integer |  -at short
    8 bit integer |  -at byte
    char |  -at char
    enum |  -at enum (specify the enum names using the enumName flag)
    float |  -at "float" (use quotes since float is a mel keyword)
    double |  -at double
    angle value |  -at doubleAngle
    linear value |  -at doubleLinear
    string |  -dt "string" (use quotes since string is a mel keyword)
    array of strings |  -dt stringArray
    compound |  -at compound
    message (no data) |  -at message
    time |  -at time
    4x4 double matrix |  -dt "matrix" (use quotes since matrix is a mel keyword)
    4x4 float matrix |  -at fltMatrix
    reflectance |  -dt reflectanceRGB
    reflectance (compound) |  -at reflectance
    spectrum |  -dt spectrumRGB
    spectrum (compound) |  -at spectrum
    2 floats |  -dt float2
    2 floats (compound) |  -at float2
    3 floats |  -dt float3
    3 floats (compound) |  -at float3
    2 doubles |  -dt double2
    2 doubles (compound) |  -at double2
    3 doubles |  -dt double3
    3 doubles (compound) |  -at double3
    2 32-bit integers |  -dt long2
    2 32-bit integers (compound) |  -at long2
    3 32-bit integers |  -dt long3
    3 32-bit integers (compound) |  -at long3
    2 16-bit integers |  -dt short2
    2 16-bit integers (compound) |  -at short2
    3 16-bit integers |  -dt short3
    3 16-bit integers (compound) |  -at short3
    array of doubles |  -dt doubleArray
    array of floats |  -dt floatArray
    array of 32-bit ints |  -dt Int32Array
    array of vectors |  -dt vectorArray
    nurbs curve |  -dt nurbsCurve
    nurbs surface |  -dt nurbsSurface
    polygonal mesh |  -dt mesh
    lattice |  -dt lattice
    array of double 4D points |  -dt pointArray

    ---
    - Args:
        - attributeType (at): Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        - binaryTag (bt): This flag is obsolete and does not do anything any more
        - cachedInternally (ci): Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached
            as this will make it impossible to set keyframes.
        - category (ct): An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however
            categories can not be removed once associated.
        - dataType (dt): Specifies the data type.  See "setAttr" for more information on data type names.
        - defaultValue (dv): Specifies the default value for the attribute (can only be used for numeric attributes).
        - disconnectBehaviour (dcb): defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        - enforcingUniqueName (eun): Sets whether this attribute will enforce to have a unique name in the attribute tree.
        - enumName (en): Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers
            starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would
            produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers
            inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        - exists (ex): Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        - fromPlugin (fp): Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        - hasMaxValue (hxv): Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        - hasMinValue (hnv): Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        - hasSoftMaxValue (hsx): Flag indicating whether a numeric attribute has a soft maximum.
        - hasSoftMinValue (hsn): Flag indicating whether a numeric attribute has a soft minimum.
        - hidden (h): Will this attribute be hidden from the UI?
        - indexMatters (im): Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        - internalSet: Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        - keyable (k): Is the attribute keyable by default?
        - longName (ln): Sets the long name of the attribute.
        - maxValue (max): Specifies the maximum value for the attribute (can only be used for numeric attributes).
        - minValue (min): Specifies the minimum value for the attribute (can only be used for numeric attributes).
        - multi (m): Makes the new attribute a multi-attribute.
        - niceName (nn): Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands
            "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        - nodeType (nt): Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        - numberOfChildren (nc): How many children will the new attribute have?
        - parent (p): Attribute that is to be the new attribute's parent.
        - proxy (pxy): Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        - readable (r): Can outgoing connections be made from this attribute?
        - shortName (sn): Sets the short name of the attribute.
        - softMaxValue (smx): Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        - softMinValue (smn): Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        - storable (s): Can the attribute be stored out to a file?
        - usedAsColor (uac): Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt"
            as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        - usedAsFilename (uaf): Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        - usedAsProxy (uap): Set if the specified attribute should be treated as a proxy to another attributes.
        - worldSpace (ws): Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that
            affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only
            be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection. Otherwise, the attribute will not get computed and will not get dirty again.
        - writable (w): Can incoming connections be made to this attribute?
    """
@overload #Overload for addExtension in ['create']
def addExtension(at: str = ..., bt: str = ..., ci: bool = ..., ct: str = ..., dt: str = ..., dv: float = ..., dcb: int = ..., eun: bool = ..., en: str = ..., ex: bool = ..., fp: bool = ..., hxv: bool = ..., hnv: bool = ..., hsx: bool = ..., hsn: bool = ..., h: bool = ..., im: bool = ..., k: bool = ..., ln: str = ..., max: float = ..., min: float = ..., m: bool = ..., nn: str = ..., nt: str = ..., nc: int = ..., p: str = ..., pxy: str = ..., r: bool = ..., sn: str = ..., smx: float = ..., smn: float = ..., s: bool = ..., uac: bool = ..., uaf: bool = ..., uap: bool = ..., ws: bool = ..., w: bool = ...) -> None:
    """addExtension is NOT undoable, queryable, and editable.
    
    This command is used to add an extension attribute to a node type. Either the
    longName or the shortName or both must be specified. If neither a dataType nor
    an attributeType is specified, a double attribute will be added. The dataType
    flag can be specified more than once indicating that any of the supplied types
    will be accepted (logical-or).
    
    To add a non-double attribute the following criteria can be used to determine
    whether the dataType or the attributeType flag is appropriate. Some types,
    such as double3 can use either. In these cases the -dt flag should be used
    when you only wish to access the data as an atomic entity (eg. you never want
    to access the three individual values that make up a double3). In general it
    is best to use the -at in these cases for maximum flexibility. In most cases
    the -dt version will not display in the attribute editor as it is an atomic
    type and you are not allowed to change individual parts of it.
    
    All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created). See
    the EXAMPLES section for more details.
    
    Type of attribute |  Flag and argument to use
    ---|---
    boolean |  -at bool
    32 bit integer |  -at long
    16 bit integer |  -at short
    8 bit integer |  -at byte
    char |  -at char
    enum |  -at enum (specify the enum names using the enumName flag)
    float |  -at "float" (use quotes since float is a mel keyword)
    double |  -at double
    angle value |  -at doubleAngle
    linear value |  -at doubleLinear
    string |  -dt "string" (use quotes since string is a mel keyword)
    array of strings |  -dt stringArray
    compound |  -at compound
    message (no data) |  -at message
    time |  -at time
    4x4 double matrix |  -dt "matrix" (use quotes since matrix is a mel keyword)
    4x4 float matrix |  -at fltMatrix
    reflectance |  -dt reflectanceRGB
    reflectance (compound) |  -at reflectance
    spectrum |  -dt spectrumRGB
    spectrum (compound) |  -at spectrum
    2 floats |  -dt float2
    2 floats (compound) |  -at float2
    3 floats |  -dt float3
    3 floats (compound) |  -at float3
    2 doubles |  -dt double2
    2 doubles (compound) |  -at double2
    3 doubles |  -dt double3
    3 doubles (compound) |  -at double3
    2 32-bit integers |  -dt long2
    2 32-bit integers (compound) |  -at long2
    3 32-bit integers |  -dt long3
    3 32-bit integers (compound) |  -at long3
    2 16-bit integers |  -dt short2
    2 16-bit integers (compound) |  -at short2
    3 16-bit integers |  -dt short3
    3 16-bit integers (compound) |  -at short3
    array of doubles |  -dt doubleArray
    array of floats |  -dt floatArray
    array of 32-bit ints |  -dt Int32Array
    array of vectors |  -dt vectorArray
    nurbs curve |  -dt nurbsCurve
    nurbs surface |  -dt nurbsSurface
    polygonal mesh |  -dt mesh
    lattice |  -dt lattice
    array of double 4D points |  -dt pointArray

    ---
    - Args:
        - attributeType (at): Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        - binaryTag (bt): This flag is obsolete and does not do anything any more
        - cachedInternally (ci): Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached
            as this will make it impossible to set keyframes.
        - category (ct): An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however
            categories can not be removed once associated.
        - dataType (dt): Specifies the data type.  See "setAttr" for more information on data type names.
        - defaultValue (dv): Specifies the default value for the attribute (can only be used for numeric attributes).
        - disconnectBehaviour (dcb): defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        - enforcingUniqueName (eun): Sets whether this attribute will enforce to have a unique name in the attribute tree.
        - enumName (en): Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers
            starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would
            produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers
            inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        - exists (ex): Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        - fromPlugin (fp): Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        - hasMaxValue (hxv): Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        - hasMinValue (hnv): Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        - hasSoftMaxValue (hsx): Flag indicating whether a numeric attribute has a soft maximum.
        - hasSoftMinValue (hsn): Flag indicating whether a numeric attribute has a soft minimum.
        - hidden (h): Will this attribute be hidden from the UI?
        - indexMatters (im): Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        - internalSet: Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        - keyable (k): Is the attribute keyable by default?
        - longName (ln): Sets the long name of the attribute.
        - maxValue (max): Specifies the maximum value for the attribute (can only be used for numeric attributes).
        - minValue (min): Specifies the minimum value for the attribute (can only be used for numeric attributes).
        - multi (m): Makes the new attribute a multi-attribute.
        - niceName (nn): Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands
            "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        - nodeType (nt): Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        - numberOfChildren (nc): How many children will the new attribute have?
        - parent (p): Attribute that is to be the new attribute's parent.
        - proxy (pxy): Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        - readable (r): Can outgoing connections be made from this attribute?
        - shortName (sn): Sets the short name of the attribute.
        - softMaxValue (smx): Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        - softMinValue (smn): Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        - storable (s): Can the attribute be stored out to a file?
        - usedAsColor (uac): Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt"
            as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        - usedAsFilename (uaf): Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        - usedAsProxy (uap): Set if the specified attribute should be treated as a proxy to another attributes.
        - worldSpace (ws): Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that
            affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only
            be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection. Otherwise, the attribute will not get computed and will not get dirty again.
        - writable (w): Can incoming connections be made to this attribute?
    """
@overload #Overload for addExtension in ['create']
def addExtension(attributeType: str = ..., at: str = ..., binaryTag: str = ..., bt: str = ..., cachedInternally: bool = ..., ci: bool = ..., category: str = ..., ct: str = ..., dataType: str = ..., dt: str = ..., defaultValue: float = ..., dv: float = ..., disconnectBehaviour: int = ..., dcb: int = ..., enforcingUniqueName: bool = ..., eun: bool = ..., enumName: str = ..., en: str = ..., exists: bool = ..., ex: bool = ..., fromPlugin: bool = ..., fp: bool = ..., hasMaxValue: bool = ..., hxv: bool = ..., hasMinValue: bool = ..., hnv: bool = ..., hasSoftMaxValue: bool = ..., hsx: bool = ..., hasSoftMinValue: bool = ..., hsn: bool = ..., hidden: bool = ..., h: bool = ..., indexMatters: bool = ..., im: bool = ..., internalSet: bool = ..., keyable: bool = ..., k: bool = ..., longName: str = ..., ln: str = ..., maxValue: float = ..., max: float = ..., minValue: float = ..., min: float = ..., multi: bool = ..., m: bool = ..., niceName: str = ..., nn: str = ..., nodeType: str = ..., nt: str = ..., numberOfChildren: int = ..., nc: int = ..., parent: str = ..., p: str = ..., proxy: str = ..., pxy: str = ..., readable: bool = ..., r: bool = ..., shortName: str = ..., sn: str = ..., softMaxValue: float = ..., smx: float = ..., softMinValue: float = ..., smn: float = ..., storable: bool = ..., s: bool = ..., usedAsColor: bool = ..., uac: bool = ..., usedAsFilename: bool = ..., uaf: bool = ..., usedAsProxy: bool = ..., uap: bool = ..., worldSpace: bool = ..., ws: bool = ..., writable: bool = ..., w: bool = ...) -> None:
    """addExtension is NOT undoable, queryable, and editable.
    
    This command is used to add an extension attribute to a node type. Either the
    longName or the shortName or both must be specified. If neither a dataType nor
    an attributeType is specified, a double attribute will be added. The dataType
    flag can be specified more than once indicating that any of the supplied types
    will be accepted (logical-or).
    
    To add a non-double attribute the following criteria can be used to determine
    whether the dataType or the attributeType flag is appropriate. Some types,
    such as double3 can use either. In these cases the -dt flag should be used
    when you only wish to access the data as an atomic entity (eg. you never want
    to access the three individual values that make up a double3). In general it
    is best to use the -at in these cases for maximum flexibility. In most cases
    the -dt version will not display in the attribute editor as it is an atomic
    type and you are not allowed to change individual parts of it.
    
    All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created). See
    the EXAMPLES section for more details.
    
    Type of attribute |  Flag and argument to use
    ---|---
    boolean |  -at bool
    32 bit integer |  -at long
    16 bit integer |  -at short
    8 bit integer |  -at byte
    char |  -at char
    enum |  -at enum (specify the enum names using the enumName flag)
    float |  -at "float" (use quotes since float is a mel keyword)
    double |  -at double
    angle value |  -at doubleAngle
    linear value |  -at doubleLinear
    string |  -dt "string" (use quotes since string is a mel keyword)
    array of strings |  -dt stringArray
    compound |  -at compound
    message (no data) |  -at message
    time |  -at time
    4x4 double matrix |  -dt "matrix" (use quotes since matrix is a mel keyword)
    4x4 float matrix |  -at fltMatrix
    reflectance |  -dt reflectanceRGB
    reflectance (compound) |  -at reflectance
    spectrum |  -dt spectrumRGB
    spectrum (compound) |  -at spectrum
    2 floats |  -dt float2
    2 floats (compound) |  -at float2
    3 floats |  -dt float3
    3 floats (compound) |  -at float3
    2 doubles |  -dt double2
    2 doubles (compound) |  -at double2
    3 doubles |  -dt double3
    3 doubles (compound) |  -at double3
    2 32-bit integers |  -dt long2
    2 32-bit integers (compound) |  -at long2
    3 32-bit integers |  -dt long3
    3 32-bit integers (compound) |  -at long3
    2 16-bit integers |  -dt short2
    2 16-bit integers (compound) |  -at short2
    3 16-bit integers |  -dt short3
    3 16-bit integers (compound) |  -at short3
    array of doubles |  -dt doubleArray
    array of floats |  -dt floatArray
    array of 32-bit ints |  -dt Int32Array
    array of vectors |  -dt vectorArray
    nurbs curve |  -dt nurbsCurve
    nurbs surface |  -dt nurbsSurface
    polygonal mesh |  -dt mesh
    lattice |  -dt lattice
    array of double 4D points |  -dt pointArray

    ---
    - Args:
        - attributeType (at): Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        - binaryTag (bt): This flag is obsolete and does not do anything any more
        - cachedInternally (ci): Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached
            as this will make it impossible to set keyframes.
        - category (ct): An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however
            categories can not be removed once associated.
        - dataType (dt): Specifies the data type.  See "setAttr" for more information on data type names.
        - defaultValue (dv): Specifies the default value for the attribute (can only be used for numeric attributes).
        - disconnectBehaviour (dcb): defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        - enforcingUniqueName (eun): Sets whether this attribute will enforce to have a unique name in the attribute tree.
        - enumName (en): Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers
            starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would
            produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers
            inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        - exists (ex): Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        - fromPlugin (fp): Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        - hasMaxValue (hxv): Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        - hasMinValue (hnv): Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        - hasSoftMaxValue (hsx): Flag indicating whether a numeric attribute has a soft maximum.
        - hasSoftMinValue (hsn): Flag indicating whether a numeric attribute has a soft minimum.
        - hidden (h): Will this attribute be hidden from the UI?
        - indexMatters (im): Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        - internalSet: Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        - keyable (k): Is the attribute keyable by default?
        - longName (ln): Sets the long name of the attribute.
        - maxValue (max): Specifies the maximum value for the attribute (can only be used for numeric attributes).
        - minValue (min): Specifies the minimum value for the attribute (can only be used for numeric attributes).
        - multi (m): Makes the new attribute a multi-attribute.
        - niceName (nn): Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands
            "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        - nodeType (nt): Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        - numberOfChildren (nc): How many children will the new attribute have?
        - parent (p): Attribute that is to be the new attribute's parent.
        - proxy (pxy): Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        - readable (r): Can outgoing connections be made from this attribute?
        - shortName (sn): Sets the short name of the attribute.
        - softMaxValue (smx): Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        - softMinValue (smn): Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        - storable (s): Can the attribute be stored out to a file?
        - usedAsColor (uac): Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt"
            as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        - usedAsFilename (uaf): Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        - usedAsProxy (uap): Set if the specified attribute should be treated as a proxy to another attributes.
        - worldSpace (ws): Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that
            affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only
            be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection. Otherwise, the attribute will not get computed and will not get dirty again.
        - writable (w): Can incoming connections be made to this attribute?
    """
@overload #Overload for addExtension in ['query']
def addExtension(attributeType: str = ..., binaryTag: str = ..., cachedInternally: bool = ..., category: str = ..., dataType: str = ..., defaultValue: float = ..., disconnectBehaviour: int = ..., enforcingUniqueName: bool = ..., enumName: str = ..., exists: bool = ..., fromPlugin: bool = ..., hasMaxValue: bool = ..., hasMinValue: bool = ..., hasSoftMaxValue: bool = ..., hasSoftMinValue: bool = ..., hidden: bool = ..., indexMatters: bool = ..., internalSet: bool = ..., keyable: bool = ..., longName: str = ..., maxValue: float = ..., minValue: float = ..., multi: bool = ..., niceName: str = ..., nodeType: str = ..., numberOfChildren: int = ..., parent: str = ..., proxy: str = ..., readable: bool = ..., shortName: str = ..., softMaxValue: float = ..., softMinValue: float = ..., storable: bool = ..., usedAsColor: bool = ..., usedAsFilename: bool = ..., usedAsProxy: bool = ..., worldSpace: bool = ..., writable: bool = ..., query: bool = ...) -> None:
    """addExtension is NOT undoable, queryable, and editable.
    
    This command is used to add an extension attribute to a node type. Either the
    longName or the shortName or both must be specified. If neither a dataType nor
    an attributeType is specified, a double attribute will be added. The dataType
    flag can be specified more than once indicating that any of the supplied types
    will be accepted (logical-or).
    
    To add a non-double attribute the following criteria can be used to determine
    whether the dataType or the attributeType flag is appropriate. Some types,
    such as double3 can use either. In these cases the -dt flag should be used
    when you only wish to access the data as an atomic entity (eg. you never want
    to access the three individual values that make up a double3). In general it
    is best to use the -at in these cases for maximum flexibility. In most cases
    the -dt version will not display in the attribute editor as it is an atomic
    type and you are not allowed to change individual parts of it.
    
    All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created). See
    the EXAMPLES section for more details.
    
    Type of attribute |  Flag and argument to use
    ---|---
    boolean |  -at bool
    32 bit integer |  -at long
    16 bit integer |  -at short
    8 bit integer |  -at byte
    char |  -at char
    enum |  -at enum (specify the enum names using the enumName flag)
    float |  -at "float" (use quotes since float is a mel keyword)
    double |  -at double
    angle value |  -at doubleAngle
    linear value |  -at doubleLinear
    string |  -dt "string" (use quotes since string is a mel keyword)
    array of strings |  -dt stringArray
    compound |  -at compound
    message (no data) |  -at message
    time |  -at time
    4x4 double matrix |  -dt "matrix" (use quotes since matrix is a mel keyword)
    4x4 float matrix |  -at fltMatrix
    reflectance |  -dt reflectanceRGB
    reflectance (compound) |  -at reflectance
    spectrum |  -dt spectrumRGB
    spectrum (compound) |  -at spectrum
    2 floats |  -dt float2
    2 floats (compound) |  -at float2
    3 floats |  -dt float3
    3 floats (compound) |  -at float3
    2 doubles |  -dt double2
    2 doubles (compound) |  -at double2
    3 doubles |  -dt double3
    3 doubles (compound) |  -at double3
    2 32-bit integers |  -dt long2
    2 32-bit integers (compound) |  -at long2
    3 32-bit integers |  -dt long3
    3 32-bit integers (compound) |  -at long3
    2 16-bit integers |  -dt short2
    2 16-bit integers (compound) |  -at short2
    3 16-bit integers |  -dt short3
    3 16-bit integers (compound) |  -at short3
    array of doubles |  -dt doubleArray
    array of floats |  -dt floatArray
    array of 32-bit ints |  -dt Int32Array
    array of vectors |  -dt vectorArray
    nurbs curve |  -dt nurbsCurve
    nurbs surface |  -dt nurbsSurface
    polygonal mesh |  -dt mesh
    lattice |  -dt lattice
    array of double 4D points |  -dt pointArray

    ---
    - Args:
        - attributeType (at): Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        - binaryTag (bt): This flag is obsolete and does not do anything any more
        - cachedInternally (ci): Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached
            as this will make it impossible to set keyframes.
        - category (ct): An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however
            categories can not be removed once associated.
        - dataType (dt): Specifies the data type.  See "setAttr" for more information on data type names.
        - defaultValue (dv): Specifies the default value for the attribute (can only be used for numeric attributes).
        - disconnectBehaviour (dcb): defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        - enforcingUniqueName (eun): Sets whether this attribute will enforce to have a unique name in the attribute tree.
        - enumName (en): Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers
            starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would
            produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers
            inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        - exists (ex): Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        - fromPlugin (fp): Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        - hasMaxValue (hxv): Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        - hasMinValue (hnv): Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        - hasSoftMaxValue (hsx): Flag indicating whether a numeric attribute has a soft maximum.
        - hasSoftMinValue (hsn): Flag indicating whether a numeric attribute has a soft minimum.
        - hidden (h): Will this attribute be hidden from the UI?
        - indexMatters (im): Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        - internalSet: Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        - keyable (k): Is the attribute keyable by default?
        - longName (ln): Sets the long name of the attribute.
        - maxValue (max): Specifies the maximum value for the attribute (can only be used for numeric attributes).
        - minValue (min): Specifies the minimum value for the attribute (can only be used for numeric attributes).
        - multi (m): Makes the new attribute a multi-attribute.
        - niceName (nn): Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands
            "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        - nodeType (nt): Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        - numberOfChildren (nc): How many children will the new attribute have?
        - parent (p): Attribute that is to be the new attribute's parent.
        - proxy (pxy): Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        - readable (r): Can outgoing connections be made from this attribute?
        - shortName (sn): Sets the short name of the attribute.
        - softMaxValue (smx): Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        - softMinValue (smn): Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        - storable (s): Can the attribute be stored out to a file?
        - usedAsColor (uac): Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt"
            as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        - usedAsFilename (uaf): Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        - usedAsProxy (uap): Set if the specified attribute should be treated as a proxy to another attributes.
        - worldSpace (ws): Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that
            affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only
            be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection. Otherwise, the attribute will not get computed and will not get dirty again.
        - writable (w): Can incoming connections be made to this attribute?
        - query (q): Query mode flag
    """
@overload #Overload for addExtension in ['query']
def addExtension(at: str = ..., bt: str = ..., ci: bool = ..., ct: str = ..., dt: str = ..., dv: float = ..., dcb: int = ..., eun: bool = ..., en: str = ..., ex: bool = ..., fp: bool = ..., hxv: bool = ..., hnv: bool = ..., hsx: bool = ..., hsn: bool = ..., h: bool = ..., im: bool = ..., k: bool = ..., ln: str = ..., max: float = ..., min: float = ..., m: bool = ..., nn: str = ..., nt: str = ..., nc: int = ..., p: str = ..., pxy: str = ..., r: bool = ..., sn: str = ..., smx: float = ..., smn: float = ..., s: bool = ..., uac: bool = ..., uaf: bool = ..., uap: bool = ..., ws: bool = ..., w: bool = ..., q: bool = ...) -> None:
    """addExtension is NOT undoable, queryable, and editable.
    
    This command is used to add an extension attribute to a node type. Either the
    longName or the shortName or both must be specified. If neither a dataType nor
    an attributeType is specified, a double attribute will be added. The dataType
    flag can be specified more than once indicating that any of the supplied types
    will be accepted (logical-or).
    
    To add a non-double attribute the following criteria can be used to determine
    whether the dataType or the attributeType flag is appropriate. Some types,
    such as double3 can use either. In these cases the -dt flag should be used
    when you only wish to access the data as an atomic entity (eg. you never want
    to access the three individual values that make up a double3). In general it
    is best to use the -at in these cases for maximum flexibility. In most cases
    the -dt version will not display in the attribute editor as it is an atomic
    type and you are not allowed to change individual parts of it.
    
    All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created). See
    the EXAMPLES section for more details.
    
    Type of attribute |  Flag and argument to use
    ---|---
    boolean |  -at bool
    32 bit integer |  -at long
    16 bit integer |  -at short
    8 bit integer |  -at byte
    char |  -at char
    enum |  -at enum (specify the enum names using the enumName flag)
    float |  -at "float" (use quotes since float is a mel keyword)
    double |  -at double
    angle value |  -at doubleAngle
    linear value |  -at doubleLinear
    string |  -dt "string" (use quotes since string is a mel keyword)
    array of strings |  -dt stringArray
    compound |  -at compound
    message (no data) |  -at message
    time |  -at time
    4x4 double matrix |  -dt "matrix" (use quotes since matrix is a mel keyword)
    4x4 float matrix |  -at fltMatrix
    reflectance |  -dt reflectanceRGB
    reflectance (compound) |  -at reflectance
    spectrum |  -dt spectrumRGB
    spectrum (compound) |  -at spectrum
    2 floats |  -dt float2
    2 floats (compound) |  -at float2
    3 floats |  -dt float3
    3 floats (compound) |  -at float3
    2 doubles |  -dt double2
    2 doubles (compound) |  -at double2
    3 doubles |  -dt double3
    3 doubles (compound) |  -at double3
    2 32-bit integers |  -dt long2
    2 32-bit integers (compound) |  -at long2
    3 32-bit integers |  -dt long3
    3 32-bit integers (compound) |  -at long3
    2 16-bit integers |  -dt short2
    2 16-bit integers (compound) |  -at short2
    3 16-bit integers |  -dt short3
    3 16-bit integers (compound) |  -at short3
    array of doubles |  -dt doubleArray
    array of floats |  -dt floatArray
    array of 32-bit ints |  -dt Int32Array
    array of vectors |  -dt vectorArray
    nurbs curve |  -dt nurbsCurve
    nurbs surface |  -dt nurbsSurface
    polygonal mesh |  -dt mesh
    lattice |  -dt lattice
    array of double 4D points |  -dt pointArray

    ---
    - Args:
        - attributeType (at): Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        - binaryTag (bt): This flag is obsolete and does not do anything any more
        - cachedInternally (ci): Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached
            as this will make it impossible to set keyframes.
        - category (ct): An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however
            categories can not be removed once associated.
        - dataType (dt): Specifies the data type.  See "setAttr" for more information on data type names.
        - defaultValue (dv): Specifies the default value for the attribute (can only be used for numeric attributes).
        - disconnectBehaviour (dcb): defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        - enforcingUniqueName (eun): Sets whether this attribute will enforce to have a unique name in the attribute tree.
        - enumName (en): Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers
            starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would
            produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers
            inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        - exists (ex): Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        - fromPlugin (fp): Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        - hasMaxValue (hxv): Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        - hasMinValue (hnv): Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        - hasSoftMaxValue (hsx): Flag indicating whether a numeric attribute has a soft maximum.
        - hasSoftMinValue (hsn): Flag indicating whether a numeric attribute has a soft minimum.
        - hidden (h): Will this attribute be hidden from the UI?
        - indexMatters (im): Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        - internalSet: Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        - keyable (k): Is the attribute keyable by default?
        - longName (ln): Sets the long name of the attribute.
        - maxValue (max): Specifies the maximum value for the attribute (can only be used for numeric attributes).
        - minValue (min): Specifies the minimum value for the attribute (can only be used for numeric attributes).
        - multi (m): Makes the new attribute a multi-attribute.
        - niceName (nn): Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands
            "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        - nodeType (nt): Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        - numberOfChildren (nc): How many children will the new attribute have?
        - parent (p): Attribute that is to be the new attribute's parent.
        - proxy (pxy): Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        - readable (r): Can outgoing connections be made from this attribute?
        - shortName (sn): Sets the short name of the attribute.
        - softMaxValue (smx): Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        - softMinValue (smn): Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        - storable (s): Can the attribute be stored out to a file?
        - usedAsColor (uac): Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt"
            as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        - usedAsFilename (uaf): Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        - usedAsProxy (uap): Set if the specified attribute should be treated as a proxy to another attributes.
        - worldSpace (ws): Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that
            affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only
            be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection. Otherwise, the attribute will not get computed and will not get dirty again.
        - writable (w): Can incoming connections be made to this attribute?
        - query (q): Query mode flag
    """
@overload #Overload for addExtension in ['query']
def addExtension(attributeType: str = ..., at: str = ..., binaryTag: str = ..., bt: str = ..., cachedInternally: bool = ..., ci: bool = ..., category: str = ..., ct: str = ..., dataType: str = ..., dt: str = ..., defaultValue: float = ..., dv: float = ..., disconnectBehaviour: int = ..., dcb: int = ..., enforcingUniqueName: bool = ..., eun: bool = ..., enumName: str = ..., en: str = ..., exists: bool = ..., ex: bool = ..., fromPlugin: bool = ..., fp: bool = ..., hasMaxValue: bool = ..., hxv: bool = ..., hasMinValue: bool = ..., hnv: bool = ..., hasSoftMaxValue: bool = ..., hsx: bool = ..., hasSoftMinValue: bool = ..., hsn: bool = ..., hidden: bool = ..., h: bool = ..., indexMatters: bool = ..., im: bool = ..., internalSet: bool = ..., keyable: bool = ..., k: bool = ..., longName: str = ..., ln: str = ..., maxValue: float = ..., max: float = ..., minValue: float = ..., min: float = ..., multi: bool = ..., m: bool = ..., niceName: str = ..., nn: str = ..., nodeType: str = ..., nt: str = ..., numberOfChildren: int = ..., nc: int = ..., parent: str = ..., p: str = ..., proxy: str = ..., pxy: str = ..., readable: bool = ..., r: bool = ..., shortName: str = ..., sn: str = ..., softMaxValue: float = ..., smx: float = ..., softMinValue: float = ..., smn: float = ..., storable: bool = ..., s: bool = ..., usedAsColor: bool = ..., uac: bool = ..., usedAsFilename: bool = ..., uaf: bool = ..., usedAsProxy: bool = ..., uap: bool = ..., worldSpace: bool = ..., ws: bool = ..., writable: bool = ..., w: bool = ..., query: bool = ..., q: bool = ...) -> None:
    """addExtension is NOT undoable, queryable, and editable.
    
    This command is used to add an extension attribute to a node type. Either the
    longName or the shortName or both must be specified. If neither a dataType nor
    an attributeType is specified, a double attribute will be added. The dataType
    flag can be specified more than once indicating that any of the supplied types
    will be accepted (logical-or).
    
    To add a non-double attribute the following criteria can be used to determine
    whether the dataType or the attributeType flag is appropriate. Some types,
    such as double3 can use either. In these cases the -dt flag should be used
    when you only wish to access the data as an atomic entity (eg. you never want
    to access the three individual values that make up a double3). In general it
    is best to use the -at in these cases for maximum flexibility. In most cases
    the -dt version will not display in the attribute editor as it is an atomic
    type and you are not allowed to change individual parts of it.
    
    All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created). See
    the EXAMPLES section for more details.
    
    Type of attribute |  Flag and argument to use
    ---|---
    boolean |  -at bool
    32 bit integer |  -at long
    16 bit integer |  -at short
    8 bit integer |  -at byte
    char |  -at char
    enum |  -at enum (specify the enum names using the enumName flag)
    float |  -at "float" (use quotes since float is a mel keyword)
    double |  -at double
    angle value |  -at doubleAngle
    linear value |  -at doubleLinear
    string |  -dt "string" (use quotes since string is a mel keyword)
    array of strings |  -dt stringArray
    compound |  -at compound
    message (no data) |  -at message
    time |  -at time
    4x4 double matrix |  -dt "matrix" (use quotes since matrix is a mel keyword)
    4x4 float matrix |  -at fltMatrix
    reflectance |  -dt reflectanceRGB
    reflectance (compound) |  -at reflectance
    spectrum |  -dt spectrumRGB
    spectrum (compound) |  -at spectrum
    2 floats |  -dt float2
    2 floats (compound) |  -at float2
    3 floats |  -dt float3
    3 floats (compound) |  -at float3
    2 doubles |  -dt double2
    2 doubles (compound) |  -at double2
    3 doubles |  -dt double3
    3 doubles (compound) |  -at double3
    2 32-bit integers |  -dt long2
    2 32-bit integers (compound) |  -at long2
    3 32-bit integers |  -dt long3
    3 32-bit integers (compound) |  -at long3
    2 16-bit integers |  -dt short2
    2 16-bit integers (compound) |  -at short2
    3 16-bit integers |  -dt short3
    3 16-bit integers (compound) |  -at short3
    array of doubles |  -dt doubleArray
    array of floats |  -dt floatArray
    array of 32-bit ints |  -dt Int32Array
    array of vectors |  -dt vectorArray
    nurbs curve |  -dt nurbsCurve
    nurbs surface |  -dt nurbsSurface
    polygonal mesh |  -dt mesh
    lattice |  -dt lattice
    array of double 4D points |  -dt pointArray

    ---
    - Args:
        - attributeType (at): Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        - binaryTag (bt): This flag is obsolete and does not do anything any more
        - cachedInternally (ci): Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached
            as this will make it impossible to set keyframes.
        - category (ct): An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however
            categories can not be removed once associated.
        - dataType (dt): Specifies the data type.  See "setAttr" for more information on data type names.
        - defaultValue (dv): Specifies the default value for the attribute (can only be used for numeric attributes).
        - disconnectBehaviour (dcb): defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        - enforcingUniqueName (eun): Sets whether this attribute will enforce to have a unique name in the attribute tree.
        - enumName (en): Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers
            starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would
            produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers
            inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        - exists (ex): Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        - fromPlugin (fp): Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        - hasMaxValue (hxv): Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        - hasMinValue (hnv): Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        - hasSoftMaxValue (hsx): Flag indicating whether a numeric attribute has a soft maximum.
        - hasSoftMinValue (hsn): Flag indicating whether a numeric attribute has a soft minimum.
        - hidden (h): Will this attribute be hidden from the UI?
        - indexMatters (im): Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        - internalSet: Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        - keyable (k): Is the attribute keyable by default?
        - longName (ln): Sets the long name of the attribute.
        - maxValue (max): Specifies the maximum value for the attribute (can only be used for numeric attributes).
        - minValue (min): Specifies the minimum value for the attribute (can only be used for numeric attributes).
        - multi (m): Makes the new attribute a multi-attribute.
        - niceName (nn): Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands
            "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        - nodeType (nt): Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        - numberOfChildren (nc): How many children will the new attribute have?
        - parent (p): Attribute that is to be the new attribute's parent.
        - proxy (pxy): Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        - readable (r): Can outgoing connections be made from this attribute?
        - shortName (sn): Sets the short name of the attribute.
        - softMaxValue (smx): Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        - softMinValue (smn): Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        - storable (s): Can the attribute be stored out to a file?
        - usedAsColor (uac): Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt"
            as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        - usedAsFilename (uaf): Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        - usedAsProxy (uap): Set if the specified attribute should be treated as a proxy to another attributes.
        - worldSpace (ws): Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that
            affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only
            be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection. Otherwise, the attribute will not get computed and will not get dirty again.
        - writable (w): Can incoming connections be made to this attribute?
        - query (q): Query mode flag
    """
@overload #Overload for addExtension in ['edit']
def addExtension(attributeType: str = ..., binaryTag: str = ..., cachedInternally: bool = ..., category: str = ..., dataType: str = ..., defaultValue: float = ..., disconnectBehaviour: int = ..., enforcingUniqueName: bool = ..., enumName: str = ..., exists: bool = ..., fromPlugin: bool = ..., hasMaxValue: bool = ..., hasMinValue: bool = ..., hasSoftMaxValue: bool = ..., hasSoftMinValue: bool = ..., hidden: bool = ..., indexMatters: bool = ..., internalSet: bool = ..., keyable: bool = ..., longName: str = ..., maxValue: float = ..., minValue: float = ..., multi: bool = ..., niceName: str = ..., nodeType: str = ..., numberOfChildren: int = ..., parent: str = ..., proxy: str = ..., readable: bool = ..., shortName: str = ..., softMaxValue: float = ..., softMinValue: float = ..., storable: bool = ..., usedAsColor: bool = ..., usedAsFilename: bool = ..., usedAsProxy: bool = ..., worldSpace: bool = ..., writable: bool = ..., edit: bool = ...) -> None:
    """addExtension is NOT undoable, queryable, and editable.
    
    This command is used to add an extension attribute to a node type. Either the
    longName or the shortName or both must be specified. If neither a dataType nor
    an attributeType is specified, a double attribute will be added. The dataType
    flag can be specified more than once indicating that any of the supplied types
    will be accepted (logical-or).
    
    To add a non-double attribute the following criteria can be used to determine
    whether the dataType or the attributeType flag is appropriate. Some types,
    such as double3 can use either. In these cases the -dt flag should be used
    when you only wish to access the data as an atomic entity (eg. you never want
    to access the three individual values that make up a double3). In general it
    is best to use the -at in these cases for maximum flexibility. In most cases
    the -dt version will not display in the attribute editor as it is an atomic
    type and you are not allowed to change individual parts of it.
    
    All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created). See
    the EXAMPLES section for more details.
    
    Type of attribute |  Flag and argument to use
    ---|---
    boolean |  -at bool
    32 bit integer |  -at long
    16 bit integer |  -at short
    8 bit integer |  -at byte
    char |  -at char
    enum |  -at enum (specify the enum names using the enumName flag)
    float |  -at "float" (use quotes since float is a mel keyword)
    double |  -at double
    angle value |  -at doubleAngle
    linear value |  -at doubleLinear
    string |  -dt "string" (use quotes since string is a mel keyword)
    array of strings |  -dt stringArray
    compound |  -at compound
    message (no data) |  -at message
    time |  -at time
    4x4 double matrix |  -dt "matrix" (use quotes since matrix is a mel keyword)
    4x4 float matrix |  -at fltMatrix
    reflectance |  -dt reflectanceRGB
    reflectance (compound) |  -at reflectance
    spectrum |  -dt spectrumRGB
    spectrum (compound) |  -at spectrum
    2 floats |  -dt float2
    2 floats (compound) |  -at float2
    3 floats |  -dt float3
    3 floats (compound) |  -at float3
    2 doubles |  -dt double2
    2 doubles (compound) |  -at double2
    3 doubles |  -dt double3
    3 doubles (compound) |  -at double3
    2 32-bit integers |  -dt long2
    2 32-bit integers (compound) |  -at long2
    3 32-bit integers |  -dt long3
    3 32-bit integers (compound) |  -at long3
    2 16-bit integers |  -dt short2
    2 16-bit integers (compound) |  -at short2
    3 16-bit integers |  -dt short3
    3 16-bit integers (compound) |  -at short3
    array of doubles |  -dt doubleArray
    array of floats |  -dt floatArray
    array of 32-bit ints |  -dt Int32Array
    array of vectors |  -dt vectorArray
    nurbs curve |  -dt nurbsCurve
    nurbs surface |  -dt nurbsSurface
    polygonal mesh |  -dt mesh
    lattice |  -dt lattice
    array of double 4D points |  -dt pointArray

    ---
    - Args:
        - attributeType (at): Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        - binaryTag (bt): This flag is obsolete and does not do anything any more
        - cachedInternally (ci): Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached
            as this will make it impossible to set keyframes.
        - category (ct): An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however
            categories can not be removed once associated.
        - dataType (dt): Specifies the data type.  See "setAttr" for more information on data type names.
        - defaultValue (dv): Specifies the default value for the attribute (can only be used for numeric attributes).
        - disconnectBehaviour (dcb): defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        - enforcingUniqueName (eun): Sets whether this attribute will enforce to have a unique name in the attribute tree.
        - enumName (en): Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers
            starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would
            produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers
            inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        - exists (ex): Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        - fromPlugin (fp): Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        - hasMaxValue (hxv): Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        - hasMinValue (hnv): Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        - hasSoftMaxValue (hsx): Flag indicating whether a numeric attribute has a soft maximum.
        - hasSoftMinValue (hsn): Flag indicating whether a numeric attribute has a soft minimum.
        - hidden (h): Will this attribute be hidden from the UI?
        - indexMatters (im): Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        - internalSet: Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        - keyable (k): Is the attribute keyable by default?
        - longName (ln): Sets the long name of the attribute.
        - maxValue (max): Specifies the maximum value for the attribute (can only be used for numeric attributes).
        - minValue (min): Specifies the minimum value for the attribute (can only be used for numeric attributes).
        - multi (m): Makes the new attribute a multi-attribute.
        - niceName (nn): Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands
            "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        - nodeType (nt): Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        - numberOfChildren (nc): How many children will the new attribute have?
        - parent (p): Attribute that is to be the new attribute's parent.
        - proxy (pxy): Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        - readable (r): Can outgoing connections be made from this attribute?
        - shortName (sn): Sets the short name of the attribute.
        - softMaxValue (smx): Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        - softMinValue (smn): Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        - storable (s): Can the attribute be stored out to a file?
        - usedAsColor (uac): Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt"
            as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        - usedAsFilename (uaf): Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        - usedAsProxy (uap): Set if the specified attribute should be treated as a proxy to another attributes.
        - worldSpace (ws): Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that
            affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only
            be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection. Otherwise, the attribute will not get computed and will not get dirty again.
        - writable (w): Can incoming connections be made to this attribute?
        - edit (e): Edit mode flag
    """
@overload #Overload for addExtension in ['edit']
def addExtension(at: str = ..., bt: str = ..., ci: bool = ..., ct: str = ..., dt: str = ..., dv: float = ..., dcb: int = ..., eun: bool = ..., en: str = ..., ex: bool = ..., fp: bool = ..., hxv: bool = ..., hnv: bool = ..., hsx: bool = ..., hsn: bool = ..., h: bool = ..., im: bool = ..., k: bool = ..., ln: str = ..., max: float = ..., min: float = ..., m: bool = ..., nn: str = ..., nt: str = ..., nc: int = ..., p: str = ..., pxy: str = ..., r: bool = ..., sn: str = ..., smx: float = ..., smn: float = ..., s: bool = ..., uac: bool = ..., uaf: bool = ..., uap: bool = ..., ws: bool = ..., w: bool = ..., e: bool = ...) -> None:
    """addExtension is NOT undoable, queryable, and editable.
    
    This command is used to add an extension attribute to a node type. Either the
    longName or the shortName or both must be specified. If neither a dataType nor
    an attributeType is specified, a double attribute will be added. The dataType
    flag can be specified more than once indicating that any of the supplied types
    will be accepted (logical-or).
    
    To add a non-double attribute the following criteria can be used to determine
    whether the dataType or the attributeType flag is appropriate. Some types,
    such as double3 can use either. In these cases the -dt flag should be used
    when you only wish to access the data as an atomic entity (eg. you never want
    to access the three individual values that make up a double3). In general it
    is best to use the -at in these cases for maximum flexibility. In most cases
    the -dt version will not display in the attribute editor as it is an atomic
    type and you are not allowed to change individual parts of it.
    
    All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created). See
    the EXAMPLES section for more details.
    
    Type of attribute |  Flag and argument to use
    ---|---
    boolean |  -at bool
    32 bit integer |  -at long
    16 bit integer |  -at short
    8 bit integer |  -at byte
    char |  -at char
    enum |  -at enum (specify the enum names using the enumName flag)
    float |  -at "float" (use quotes since float is a mel keyword)
    double |  -at double
    angle value |  -at doubleAngle
    linear value |  -at doubleLinear
    string |  -dt "string" (use quotes since string is a mel keyword)
    array of strings |  -dt stringArray
    compound |  -at compound
    message (no data) |  -at message
    time |  -at time
    4x4 double matrix |  -dt "matrix" (use quotes since matrix is a mel keyword)
    4x4 float matrix |  -at fltMatrix
    reflectance |  -dt reflectanceRGB
    reflectance (compound) |  -at reflectance
    spectrum |  -dt spectrumRGB
    spectrum (compound) |  -at spectrum
    2 floats |  -dt float2
    2 floats (compound) |  -at float2
    3 floats |  -dt float3
    3 floats (compound) |  -at float3
    2 doubles |  -dt double2
    2 doubles (compound) |  -at double2
    3 doubles |  -dt double3
    3 doubles (compound) |  -at double3
    2 32-bit integers |  -dt long2
    2 32-bit integers (compound) |  -at long2
    3 32-bit integers |  -dt long3
    3 32-bit integers (compound) |  -at long3
    2 16-bit integers |  -dt short2
    2 16-bit integers (compound) |  -at short2
    3 16-bit integers |  -dt short3
    3 16-bit integers (compound) |  -at short3
    array of doubles |  -dt doubleArray
    array of floats |  -dt floatArray
    array of 32-bit ints |  -dt Int32Array
    array of vectors |  -dt vectorArray
    nurbs curve |  -dt nurbsCurve
    nurbs surface |  -dt nurbsSurface
    polygonal mesh |  -dt mesh
    lattice |  -dt lattice
    array of double 4D points |  -dt pointArray

    ---
    - Args:
        - attributeType (at): Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        - binaryTag (bt): This flag is obsolete and does not do anything any more
        - cachedInternally (ci): Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached
            as this will make it impossible to set keyframes.
        - category (ct): An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however
            categories can not be removed once associated.
        - dataType (dt): Specifies the data type.  See "setAttr" for more information on data type names.
        - defaultValue (dv): Specifies the default value for the attribute (can only be used for numeric attributes).
        - disconnectBehaviour (dcb): defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        - enforcingUniqueName (eun): Sets whether this attribute will enforce to have a unique name in the attribute tree.
        - enumName (en): Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers
            starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would
            produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers
            inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        - exists (ex): Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        - fromPlugin (fp): Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        - hasMaxValue (hxv): Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        - hasMinValue (hnv): Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        - hasSoftMaxValue (hsx): Flag indicating whether a numeric attribute has a soft maximum.
        - hasSoftMinValue (hsn): Flag indicating whether a numeric attribute has a soft minimum.
        - hidden (h): Will this attribute be hidden from the UI?
        - indexMatters (im): Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        - internalSet: Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        - keyable (k): Is the attribute keyable by default?
        - longName (ln): Sets the long name of the attribute.
        - maxValue (max): Specifies the maximum value for the attribute (can only be used for numeric attributes).
        - minValue (min): Specifies the minimum value for the attribute (can only be used for numeric attributes).
        - multi (m): Makes the new attribute a multi-attribute.
        - niceName (nn): Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands
            "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        - nodeType (nt): Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        - numberOfChildren (nc): How many children will the new attribute have?
        - parent (p): Attribute that is to be the new attribute's parent.
        - proxy (pxy): Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        - readable (r): Can outgoing connections be made from this attribute?
        - shortName (sn): Sets the short name of the attribute.
        - softMaxValue (smx): Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        - softMinValue (smn): Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        - storable (s): Can the attribute be stored out to a file?
        - usedAsColor (uac): Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt"
            as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        - usedAsFilename (uaf): Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        - usedAsProxy (uap): Set if the specified attribute should be treated as a proxy to another attributes.
        - worldSpace (ws): Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that
            affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only
            be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection. Otherwise, the attribute will not get computed and will not get dirty again.
        - writable (w): Can incoming connections be made to this attribute?
        - edit (e): Edit mode flag
    """
@overload #Overload for addExtension in ['edit']
def addExtension(attributeType: str = ..., at: str = ..., binaryTag: str = ..., bt: str = ..., cachedInternally: bool = ..., ci: bool = ..., category: str = ..., ct: str = ..., dataType: str = ..., dt: str = ..., defaultValue: float = ..., dv: float = ..., disconnectBehaviour: int = ..., dcb: int = ..., enforcingUniqueName: bool = ..., eun: bool = ..., enumName: str = ..., en: str = ..., exists: bool = ..., ex: bool = ..., fromPlugin: bool = ..., fp: bool = ..., hasMaxValue: bool = ..., hxv: bool = ..., hasMinValue: bool = ..., hnv: bool = ..., hasSoftMaxValue: bool = ..., hsx: bool = ..., hasSoftMinValue: bool = ..., hsn: bool = ..., hidden: bool = ..., h: bool = ..., indexMatters: bool = ..., im: bool = ..., internalSet: bool = ..., keyable: bool = ..., k: bool = ..., longName: str = ..., ln: str = ..., maxValue: float = ..., max: float = ..., minValue: float = ..., min: float = ..., multi: bool = ..., m: bool = ..., niceName: str = ..., nn: str = ..., nodeType: str = ..., nt: str = ..., numberOfChildren: int = ..., nc: int = ..., parent: str = ..., p: str = ..., proxy: str = ..., pxy: str = ..., readable: bool = ..., r: bool = ..., shortName: str = ..., sn: str = ..., softMaxValue: float = ..., smx: float = ..., softMinValue: float = ..., smn: float = ..., storable: bool = ..., s: bool = ..., usedAsColor: bool = ..., uac: bool = ..., usedAsFilename: bool = ..., uaf: bool = ..., usedAsProxy: bool = ..., uap: bool = ..., worldSpace: bool = ..., ws: bool = ..., writable: bool = ..., w: bool = ..., edit: bool = ..., e: bool = ...) -> None:
    """addExtension is NOT undoable, queryable, and editable.
    
    This command is used to add an extension attribute to a node type. Either the
    longName or the shortName or both must be specified. If neither a dataType nor
    an attributeType is specified, a double attribute will be added. The dataType
    flag can be specified more than once indicating that any of the supplied types
    will be accepted (logical-or).
    
    To add a non-double attribute the following criteria can be used to determine
    whether the dataType or the attributeType flag is appropriate. Some types,
    such as double3 can use either. In these cases the -dt flag should be used
    when you only wish to access the data as an atomic entity (eg. you never want
    to access the three individual values that make up a double3). In general it
    is best to use the -at in these cases for maximum flexibility. In most cases
    the -dt version will not display in the attribute editor as it is an atomic
    type and you are not allowed to change individual parts of it.
    
    All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created). See
    the EXAMPLES section for more details.
    
    Type of attribute |  Flag and argument to use
    ---|---
    boolean |  -at bool
    32 bit integer |  -at long
    16 bit integer |  -at short
    8 bit integer |  -at byte
    char |  -at char
    enum |  -at enum (specify the enum names using the enumName flag)
    float |  -at "float" (use quotes since float is a mel keyword)
    double |  -at double
    angle value |  -at doubleAngle
    linear value |  -at doubleLinear
    string |  -dt "string" (use quotes since string is a mel keyword)
    array of strings |  -dt stringArray
    compound |  -at compound
    message (no data) |  -at message
    time |  -at time
    4x4 double matrix |  -dt "matrix" (use quotes since matrix is a mel keyword)
    4x4 float matrix |  -at fltMatrix
    reflectance |  -dt reflectanceRGB
    reflectance (compound) |  -at reflectance
    spectrum |  -dt spectrumRGB
    spectrum (compound) |  -at spectrum
    2 floats |  -dt float2
    2 floats (compound) |  -at float2
    3 floats |  -dt float3
    3 floats (compound) |  -at float3
    2 doubles |  -dt double2
    2 doubles (compound) |  -at double2
    3 doubles |  -dt double3
    3 doubles (compound) |  -at double3
    2 32-bit integers |  -dt long2
    2 32-bit integers (compound) |  -at long2
    3 32-bit integers |  -dt long3
    3 32-bit integers (compound) |  -at long3
    2 16-bit integers |  -dt short2
    2 16-bit integers (compound) |  -at short2
    3 16-bit integers |  -dt short3
    3 16-bit integers (compound) |  -at short3
    array of doubles |  -dt doubleArray
    array of floats |  -dt floatArray
    array of 32-bit ints |  -dt Int32Array
    array of vectors |  -dt vectorArray
    nurbs curve |  -dt nurbsCurve
    nurbs surface |  -dt nurbsSurface
    polygonal mesh |  -dt mesh
    lattice |  -dt lattice
    array of double 4D points |  -dt pointArray

    ---
    - Args:
        - attributeType (at): Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        - binaryTag (bt): This flag is obsolete and does not do anything any more
        - cachedInternally (ci): Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached
            as this will make it impossible to set keyframes.
        - category (ct): An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however
            categories can not be removed once associated.
        - dataType (dt): Specifies the data type.  See "setAttr" for more information on data type names.
        - defaultValue (dv): Specifies the default value for the attribute (can only be used for numeric attributes).
        - disconnectBehaviour (dcb): defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        - enforcingUniqueName (eun): Sets whether this attribute will enforce to have a unique name in the attribute tree.
        - enumName (en): Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers
            starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would
            produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers
            inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        - exists (ex): Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        - fromPlugin (fp): Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        - hasMaxValue (hxv): Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        - hasMinValue (hnv): Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        - hasSoftMaxValue (hsx): Flag indicating whether a numeric attribute has a soft maximum.
        - hasSoftMinValue (hsn): Flag indicating whether a numeric attribute has a soft minimum.
        - hidden (h): Will this attribute be hidden from the UI?
        - indexMatters (im): Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        - internalSet: Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        - keyable (k): Is the attribute keyable by default?
        - longName (ln): Sets the long name of the attribute.
        - maxValue (max): Specifies the maximum value for the attribute (can only be used for numeric attributes).
        - minValue (min): Specifies the minimum value for the attribute (can only be used for numeric attributes).
        - multi (m): Makes the new attribute a multi-attribute.
        - niceName (nn): Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands
            "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        - nodeType (nt): Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        - numberOfChildren (nc): How many children will the new attribute have?
        - parent (p): Attribute that is to be the new attribute's parent.
        - proxy (pxy): Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        - readable (r): Can outgoing connections be made from this attribute?
        - shortName (sn): Sets the short name of the attribute.
        - softMaxValue (smx): Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        - softMinValue (smn): Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        - storable (s): Can the attribute be stored out to a file?
        - usedAsColor (uac): Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt"
            as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        - usedAsFilename (uaf): Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        - usedAsProxy (uap): Set if the specified attribute should be treated as a proxy to another attributes.
        - worldSpace (ws): Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that
            affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only
            be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection. Otherwise, the attribute will not get computed and will not get dirty again.
        - writable (w): Can incoming connections be made to this attribute?
        - edit (e): Edit mode flag
    """
