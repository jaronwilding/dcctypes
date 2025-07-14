"""Stub files for Attributes category in Maya commands, command: attributeQuery."""

from typing import Any, overload

@overload #Overload for attributeQuery in ['create']
def attributeQuery(affectsAppearance: bool = ..., affectsWorldspace: bool = ..., attributeType: bool = ..., cachedInternally: bool = ..., categories: bool = ..., channelBox: bool = ..., connectable: bool = ..., enum: bool = ..., exists: bool = ..., hidden: bool = ..., indeterminant: bool = ..., indexMatters: bool = ..., internal: bool = ..., internalGet: bool = ..., internalSet: bool = ..., keyable: bool = ..., listChildren: bool = ..., listDefault: bool = ..., listEnum: bool = ..., listParent: bool = ..., listSiblings: bool = ..., localizedListEnum: bool = ..., longName: bool = ..., maxExists: bool = ..., maximum: bool = ..., message: bool = ..., minExists: bool = ..., minimum: bool = ..., multi: bool = ..., niceName: bool = ..., node: name = ..., numberOfChildren: bool = ..., range: bool = ..., rangeExists: bool = ..., readable: bool = ..., renderSource: bool = ..., shortName: bool = ..., softMax: bool = ..., softMaxExists: bool = ..., softMin: bool = ..., softMinExists: bool = ..., softRange: bool = ..., softRangeExists: bool = ..., storable: bool = ..., type: str = ..., typeExact: str = ..., usedAsColor: bool = ..., usedAsFilename: bool = ..., usesMultiBuilder: bool = ..., worldspace: bool = ..., writable: bool = ...) -> float[] | bool:
    """attributeQuery is NOT undoable, NOT queryable, and NOT editable.
    
    attributeQuery returns information about the configuration of an attribute. It
    handles both boolean flags, returning true or false, as well as other return
    values. Specifying more than one boolean flag will return the logical "and" of
    all the specified boolean flags. You may not specify any two flags when both
    do not provide a boolean return type. (eg. "-internal -hidden" is okay but
    "-range -hidden" or "-range -softRange" is not.)

    ---
    - Args:
        - affectsAppearance (aa): Return true if the attribute affects the appearance of the node
        - affectsWorldspace (aws): Return the status of the attribute flag marking attributes affecting worldspace
        - attributeType (at): Return the name of the attribute type (will be the same type names as described in the addAttr and addExtension commands).
        - cachedInternally (ci): Return whether the attribute is cached within the node as well as in the datablock
        - categories (ct): Return the categories to which the attribute belongs or an empty list if it does not belong to any.
        - channelBox (ch): Return whether the attribute should show up in the channelBox or not
        - connectable (c): Return the connectable status of the attribute
        - enum (e): Return true if the attribute is a enum attribute
        - exists (ex): Return true if the attribute exists
        - hidden (h): Return the hidden status of the attribute
        - indeterminant (idt): Return true if this attribute might be used in evaluation but it's not known for sure until evaluation time
        - indexMatters (im): Return the indexMatters status of the attribute
        - internal (i): Return true if the attribute is either internalSet or internalGet
        - internalGet (ig): Return true if the attribute come from getCachedValue
        - internalSet: Return true if the attribute must be set through setCachedValue
        - keyable (k): Return the keyable status of the attribute
        - listChildren (lc): Return the list of children attributes of the given attribute.
        - listDefault (ld): Return the default values of numeric and compound numeric attributes.
        - listEnum (le): Return the list of enum strings for the given attribute.
        - listParent (lp): Return the parent of the given attribute.
        - listSiblings (ls): Return the list of sibling attributes of the given attribute.
        - localizedListEnum (lz): Return the list of localized enum strings for the given attribute.
        - longName (ln): Return the long name of the attribute.
        - maxExists (mxe): Return true if the attribute has a hard maximum. A min does not have to be present.
        - maximum (max): Return the hard maximum of the attribute's value
        - message (msg): Return true if the attribute is a message attribute
        - minExists (mne): Return true if the attribute has a hard minimum. A max does not have to be present.
        - minimum (min): Return the hard minimum of the attribute's value
        - multi (m): Return true if the attribute is a multi-attribute
        - niceName (nn): Return the nice name (or "UI name") of the attribute.
        - node (n): Use all attributes from node named NAME
        - numberOfChildren (nc): Return the number of children the attribute has
        - range (r): Return the hard range of the attribute's value
        - rangeExists (re): Return true if the attribute has a hard range. Both min and max must be present.
        - readable (rd): Return the readable status of the attribute
        - renderSource (rs): Return whether this attribute is marked as a render source or not
        - shortName (sn): Return the short name of the attribute.
        - softMax (smx): Return the soft max (slider range) of the attribute's value
        - softMaxExists (sxe): Return true if the attribute has a soft maximum. A min does not have to be present.
        - softMin (smn): Return the soft min (slider range) of the attribute's value
        - softMinExists (sme): Return true if the attribute has a soft minimum. A max does not have to be present.
        - softRange (s): Return the soft range (slider range) of the attribute's value
        - softRangeExists (se): Return true if the attribute has a soft range. Both min and max must be present.
        - storable (st): Return true if the attribute is storable
        - type (typ): Use static attributes from nodes of type TYPE.  Includes attributes inherited from parent class nodes.
        - typeExact (tex): Use static attributes only from nodes of type TYPE.  Does not included inherited attributes.
        - usedAsColor (uac): Return true if the attribute should bring up a color picker
        - usedAsFilename (uaf): Return true if the attribute should bring up a file browser
        - usesMultiBuilder (umb): Return true if the attribute is a multi-attribute and it uses the multi-builder to handle its data
        - worldspace (ws): Return the status of the attribute flag marking worldspace attribute
        - writable (w): Return the writable status of the attribute
    """
@overload #Overload for attributeQuery in ['create']
def attributeQuery(aa: bool = ..., aws: bool = ..., at: bool = ..., ci: bool = ..., ct: bool = ..., ch: bool = ..., c: bool = ..., e: bool = ..., ex: bool = ..., h: bool = ..., idt: bool = ..., im: bool = ..., i: bool = ..., ig: bool = ..., k: bool = ..., lc: bool = ..., ld: bool = ..., le: bool = ..., lp: bool = ..., ls: bool = ..., lz: bool = ..., ln: bool = ..., mxe: bool = ..., max: bool = ..., msg: bool = ..., mne: bool = ..., min: bool = ..., m: bool = ..., nn: bool = ..., n: name = ..., nc: bool = ..., r: bool = ..., re: bool = ..., rd: bool = ..., rs: bool = ..., sn: bool = ..., smx: bool = ..., sxe: bool = ..., smn: bool = ..., sme: bool = ..., s: bool = ..., se: bool = ..., st: bool = ..., typ: str = ..., tex: str = ..., uac: bool = ..., uaf: bool = ..., umb: bool = ..., ws: bool = ..., w: bool = ...) -> float[] | bool:
    """attributeQuery is NOT undoable, NOT queryable, and NOT editable.
    
    attributeQuery returns information about the configuration of an attribute. It
    handles both boolean flags, returning true or false, as well as other return
    values. Specifying more than one boolean flag will return the logical "and" of
    all the specified boolean flags. You may not specify any two flags when both
    do not provide a boolean return type. (eg. "-internal -hidden" is okay but
    "-range -hidden" or "-range -softRange" is not.)

    ---
    - Args:
        - affectsAppearance (aa): Return true if the attribute affects the appearance of the node
        - affectsWorldspace (aws): Return the status of the attribute flag marking attributes affecting worldspace
        - attributeType (at): Return the name of the attribute type (will be the same type names as described in the addAttr and addExtension commands).
        - cachedInternally (ci): Return whether the attribute is cached within the node as well as in the datablock
        - categories (ct): Return the categories to which the attribute belongs or an empty list if it does not belong to any.
        - channelBox (ch): Return whether the attribute should show up in the channelBox or not
        - connectable (c): Return the connectable status of the attribute
        - enum (e): Return true if the attribute is a enum attribute
        - exists (ex): Return true if the attribute exists
        - hidden (h): Return the hidden status of the attribute
        - indeterminant (idt): Return true if this attribute might be used in evaluation but it's not known for sure until evaluation time
        - indexMatters (im): Return the indexMatters status of the attribute
        - internal (i): Return true if the attribute is either internalSet or internalGet
        - internalGet (ig): Return true if the attribute come from getCachedValue
        - internalSet: Return true if the attribute must be set through setCachedValue
        - keyable (k): Return the keyable status of the attribute
        - listChildren (lc): Return the list of children attributes of the given attribute.
        - listDefault (ld): Return the default values of numeric and compound numeric attributes.
        - listEnum (le): Return the list of enum strings for the given attribute.
        - listParent (lp): Return the parent of the given attribute.
        - listSiblings (ls): Return the list of sibling attributes of the given attribute.
        - localizedListEnum (lz): Return the list of localized enum strings for the given attribute.
        - longName (ln): Return the long name of the attribute.
        - maxExists (mxe): Return true if the attribute has a hard maximum. A min does not have to be present.
        - maximum (max): Return the hard maximum of the attribute's value
        - message (msg): Return true if the attribute is a message attribute
        - minExists (mne): Return true if the attribute has a hard minimum. A max does not have to be present.
        - minimum (min): Return the hard minimum of the attribute's value
        - multi (m): Return true if the attribute is a multi-attribute
        - niceName (nn): Return the nice name (or "UI name") of the attribute.
        - node (n): Use all attributes from node named NAME
        - numberOfChildren (nc): Return the number of children the attribute has
        - range (r): Return the hard range of the attribute's value
        - rangeExists (re): Return true if the attribute has a hard range. Both min and max must be present.
        - readable (rd): Return the readable status of the attribute
        - renderSource (rs): Return whether this attribute is marked as a render source or not
        - shortName (sn): Return the short name of the attribute.
        - softMax (smx): Return the soft max (slider range) of the attribute's value
        - softMaxExists (sxe): Return true if the attribute has a soft maximum. A min does not have to be present.
        - softMin (smn): Return the soft min (slider range) of the attribute's value
        - softMinExists (sme): Return true if the attribute has a soft minimum. A max does not have to be present.
        - softRange (s): Return the soft range (slider range) of the attribute's value
        - softRangeExists (se): Return true if the attribute has a soft range. Both min and max must be present.
        - storable (st): Return true if the attribute is storable
        - type (typ): Use static attributes from nodes of type TYPE.  Includes attributes inherited from parent class nodes.
        - typeExact (tex): Use static attributes only from nodes of type TYPE.  Does not included inherited attributes.
        - usedAsColor (uac): Return true if the attribute should bring up a color picker
        - usedAsFilename (uaf): Return true if the attribute should bring up a file browser
        - usesMultiBuilder (umb): Return true if the attribute is a multi-attribute and it uses the multi-builder to handle its data
        - worldspace (ws): Return the status of the attribute flag marking worldspace attribute
        - writable (w): Return the writable status of the attribute
    """
@overload #Overload for attributeQuery in ['create']
def attributeQuery(affectsAppearance: bool = ..., aa: bool = ..., affectsWorldspace: bool = ..., aws: bool = ..., attributeType: bool = ..., at: bool = ..., cachedInternally: bool = ..., ci: bool = ..., categories: bool = ..., ct: bool = ..., channelBox: bool = ..., ch: bool = ..., connectable: bool = ..., c: bool = ..., enum: bool = ..., e: bool = ..., exists: bool = ..., ex: bool = ..., hidden: bool = ..., h: bool = ..., indeterminant: bool = ..., idt: bool = ..., indexMatters: bool = ..., im: bool = ..., internal: bool = ..., i: bool = ..., internalGet: bool = ..., ig: bool = ..., internalSet: bool = ..., keyable: bool = ..., k: bool = ..., listChildren: bool = ..., lc: bool = ..., listDefault: bool = ..., ld: bool = ..., listEnum: bool = ..., le: bool = ..., listParent: bool = ..., lp: bool = ..., listSiblings: bool = ..., ls: bool = ..., localizedListEnum: bool = ..., lz: bool = ..., longName: bool = ..., ln: bool = ..., maxExists: bool = ..., mxe: bool = ..., maximum: bool = ..., max: bool = ..., message: bool = ..., msg: bool = ..., minExists: bool = ..., mne: bool = ..., minimum: bool = ..., min: bool = ..., multi: bool = ..., m: bool = ..., niceName: bool = ..., nn: bool = ..., node: name = ..., n: name = ..., numberOfChildren: bool = ..., nc: bool = ..., range: bool = ..., r: bool = ..., rangeExists: bool = ..., re: bool = ..., readable: bool = ..., rd: bool = ..., renderSource: bool = ..., rs: bool = ..., shortName: bool = ..., sn: bool = ..., softMax: bool = ..., smx: bool = ..., softMaxExists: bool = ..., sxe: bool = ..., softMin: bool = ..., smn: bool = ..., softMinExists: bool = ..., sme: bool = ..., softRange: bool = ..., s: bool = ..., softRangeExists: bool = ..., se: bool = ..., storable: bool = ..., st: bool = ..., type: str = ..., typ: str = ..., typeExact: str = ..., tex: str = ..., usedAsColor: bool = ..., uac: bool = ..., usedAsFilename: bool = ..., uaf: bool = ..., usesMultiBuilder: bool = ..., umb: bool = ..., worldspace: bool = ..., ws: bool = ..., writable: bool = ..., w: bool = ...) -> float[] | bool:
    """attributeQuery is NOT undoable, NOT queryable, and NOT editable.
    
    attributeQuery returns information about the configuration of an attribute. It
    handles both boolean flags, returning true or false, as well as other return
    values. Specifying more than one boolean flag will return the logical "and" of
    all the specified boolean flags. You may not specify any two flags when both
    do not provide a boolean return type. (eg. "-internal -hidden" is okay but
    "-range -hidden" or "-range -softRange" is not.)

    ---
    - Args:
        - affectsAppearance (aa): Return true if the attribute affects the appearance of the node
        - affectsWorldspace (aws): Return the status of the attribute flag marking attributes affecting worldspace
        - attributeType (at): Return the name of the attribute type (will be the same type names as described in the addAttr and addExtension commands).
        - cachedInternally (ci): Return whether the attribute is cached within the node as well as in the datablock
        - categories (ct): Return the categories to which the attribute belongs or an empty list if it does not belong to any.
        - channelBox (ch): Return whether the attribute should show up in the channelBox or not
        - connectable (c): Return the connectable status of the attribute
        - enum (e): Return true if the attribute is a enum attribute
        - exists (ex): Return true if the attribute exists
        - hidden (h): Return the hidden status of the attribute
        - indeterminant (idt): Return true if this attribute might be used in evaluation but it's not known for sure until evaluation time
        - indexMatters (im): Return the indexMatters status of the attribute
        - internal (i): Return true if the attribute is either internalSet or internalGet
        - internalGet (ig): Return true if the attribute come from getCachedValue
        - internalSet: Return true if the attribute must be set through setCachedValue
        - keyable (k): Return the keyable status of the attribute
        - listChildren (lc): Return the list of children attributes of the given attribute.
        - listDefault (ld): Return the default values of numeric and compound numeric attributes.
        - listEnum (le): Return the list of enum strings for the given attribute.
        - listParent (lp): Return the parent of the given attribute.
        - listSiblings (ls): Return the list of sibling attributes of the given attribute.
        - localizedListEnum (lz): Return the list of localized enum strings for the given attribute.
        - longName (ln): Return the long name of the attribute.
        - maxExists (mxe): Return true if the attribute has a hard maximum. A min does not have to be present.
        - maximum (max): Return the hard maximum of the attribute's value
        - message (msg): Return true if the attribute is a message attribute
        - minExists (mne): Return true if the attribute has a hard minimum. A max does not have to be present.
        - minimum (min): Return the hard minimum of the attribute's value
        - multi (m): Return true if the attribute is a multi-attribute
        - niceName (nn): Return the nice name (or "UI name") of the attribute.
        - node (n): Use all attributes from node named NAME
        - numberOfChildren (nc): Return the number of children the attribute has
        - range (r): Return the hard range of the attribute's value
        - rangeExists (re): Return true if the attribute has a hard range. Both min and max must be present.
        - readable (rd): Return the readable status of the attribute
        - renderSource (rs): Return whether this attribute is marked as a render source or not
        - shortName (sn): Return the short name of the attribute.
        - softMax (smx): Return the soft max (slider range) of the attribute's value
        - softMaxExists (sxe): Return true if the attribute has a soft maximum. A min does not have to be present.
        - softMin (smn): Return the soft min (slider range) of the attribute's value
        - softMinExists (sme): Return true if the attribute has a soft minimum. A max does not have to be present.
        - softRange (s): Return the soft range (slider range) of the attribute's value
        - softRangeExists (se): Return true if the attribute has a soft range. Both min and max must be present.
        - storable (st): Return true if the attribute is storable
        - type (typ): Use static attributes from nodes of type TYPE.  Includes attributes inherited from parent class nodes.
        - typeExact (tex): Use static attributes only from nodes of type TYPE.  Does not included inherited attributes.
        - usedAsColor (uac): Return true if the attribute should bring up a color picker
        - usedAsFilename (uaf): Return true if the attribute should bring up a file browser
        - usesMultiBuilder (umb): Return true if the attribute is a multi-attribute and it uses the multi-builder to handle its data
        - worldspace (ws): Return the status of the attribute flag marking worldspace attribute
        - writable (w): Return the writable status of the attribute
    """
