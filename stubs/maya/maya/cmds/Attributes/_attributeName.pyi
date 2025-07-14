"""Stub files for Attributes category in Maya commands, command: attributeName."""

from typing import Any, overload

@overload #Overload for attributeName in ['create']
def attributeName(leaf: bool = ..., long: bool = ..., nice: bool = ..., short: bool = ...) -> str:
    """attributeName is NOT undoable, NOT queryable, and NOT editable.
    
    This command takes one "node.attribute"-style specifier on the command line
    and returns either the attribute's long, short, or nice name. (The "nice"
    name, or UI name, is the name used to display the attribute in Maya's
    interface, and may be localized when running Maya in a language other than
    English.) If more than one "node.attribute" specifier is given on the command
    line, only the first valid specifier is processed.

    ---
    - Args:
        - leaf (lf): When false, shows parent multi attributes (like "controlPoints[2].xValue").  When true, shows only the leaf-level attribute name (like "xValue").  Default is true. Note that for incomplete attribute strings, like a missing multi-parent
            index ("controlPoints.xValue") or an incorrectly named compound (cntrlPnts[2].xValue), this flag defaults to true and provides a result as long as the named leaf-level attribute is defined for the node.
        - long (l): Returns names in "long name" format like "translateX"
        - nice (n): Returns names in "nice name" format like "Translate X"
        - short (s): Returns names in "short name" format like "tx"
    """
@overload #Overload for attributeName in ['create']
def attributeName(lf: bool = ..., l: bool = ..., n: bool = ..., s: bool = ...) -> str:
    """attributeName is NOT undoable, NOT queryable, and NOT editable.
    
    This command takes one "node.attribute"-style specifier on the command line
    and returns either the attribute's long, short, or nice name. (The "nice"
    name, or UI name, is the name used to display the attribute in Maya's
    interface, and may be localized when running Maya in a language other than
    English.) If more than one "node.attribute" specifier is given on the command
    line, only the first valid specifier is processed.

    ---
    - Args:
        - leaf (lf): When false, shows parent multi attributes (like "controlPoints[2].xValue").  When true, shows only the leaf-level attribute name (like "xValue").  Default is true. Note that for incomplete attribute strings, like a missing multi-parent
            index ("controlPoints.xValue") or an incorrectly named compound (cntrlPnts[2].xValue), this flag defaults to true and provides a result as long as the named leaf-level attribute is defined for the node.
        - long (l): Returns names in "long name" format like "translateX"
        - nice (n): Returns names in "nice name" format like "Translate X"
        - short (s): Returns names in "short name" format like "tx"
    """
@overload #Overload for attributeName in ['create']
def attributeName(leaf: bool = ..., lf: bool = ..., long: bool = ..., l: bool = ..., nice: bool = ..., n: bool = ..., short: bool = ..., s: bool = ...) -> str:
    """attributeName is NOT undoable, NOT queryable, and NOT editable.
    
    This command takes one "node.attribute"-style specifier on the command line
    and returns either the attribute's long, short, or nice name. (The "nice"
    name, or UI name, is the name used to display the attribute in Maya's
    interface, and may be localized when running Maya in a language other than
    English.) If more than one "node.attribute" specifier is given on the command
    line, only the first valid specifier is processed.

    ---
    - Args:
        - leaf (lf): When false, shows parent multi attributes (like "controlPoints[2].xValue").  When true, shows only the leaf-level attribute name (like "xValue").  Default is true. Note that for incomplete attribute strings, like a missing multi-parent
            index ("controlPoints.xValue") or an incorrectly named compound (cntrlPnts[2].xValue), this flag defaults to true and provides a result as long as the named leaf-level attribute is defined for the node.
        - long (l): Returns names in "long name" format like "translateX"
        - nice (n): Returns names in "nice name" format like "Translate X"
        - short (s): Returns names in "short name" format like "tx"
    """
