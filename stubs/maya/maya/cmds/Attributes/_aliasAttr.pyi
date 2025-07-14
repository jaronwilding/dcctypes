"""Stub files for Attributes category in Maya commands, command: aliasAttr."""

from typing import Any, overload

@overload #Overload for aliasAttr in ['create']
def aliasAttr(remove: bool = ...) -> list[str]:
    """aliasAttr is undoable, queryable, and editable.
    
    Allows aliases (alternate names) to be defined for any attribute of a
    specified node. When an attribute is aliased, the alias will be used by the
    system to display information about the attribute. The user may, however,
    freely use either the alias or the original name of the attribute. Only a
    single alias can be specified for an attribute so setting an alias on an
    already-aliased attribute destroys the old alias.

    ---
    - Args:
        - remove (rm): Specifies that aliases listed should be removed (otherwise new aliases are added).
    """
@overload #Overload for aliasAttr in ['create']
def aliasAttr(rm: bool = ...) -> list[str]:
    """aliasAttr is undoable, queryable, and editable.
    
    Allows aliases (alternate names) to be defined for any attribute of a
    specified node. When an attribute is aliased, the alias will be used by the
    system to display information about the attribute. The user may, however,
    freely use either the alias or the original name of the attribute. Only a
    single alias can be specified for an attribute so setting an alias on an
    already-aliased attribute destroys the old alias.

    ---
    - Args:
        - remove (rm): Specifies that aliases listed should be removed (otherwise new aliases are added).
    """
@overload #Overload for aliasAttr in ['create']
def aliasAttr(remove: bool = ..., rm: bool = ...) -> list[str]:
    """aliasAttr is undoable, queryable, and editable.
    
    Allows aliases (alternate names) to be defined for any attribute of a
    specified node. When an attribute is aliased, the alias will be used by the
    system to display information about the attribute. The user may, however,
    freely use either the alias or the original name of the attribute. Only a
    single alias can be specified for an attribute so setting an alias on an
    already-aliased attribute destroys the old alias.

    ---
    - Args:
        - remove (rm): Specifies that aliases listed should be removed (otherwise new aliases are added).
    """
