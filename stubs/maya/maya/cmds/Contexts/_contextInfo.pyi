"""Stub files for Contexts category in Maya commands, command: contextInfo."""

from typing import Any, overload

@overload #Overload for contextInfo in ['create']
def contextInfo([context name]: [context name], c: bool = ..., escapeContext: bool = ..., exists: bool = ..., image1: bool = ..., image2: bool = ..., image3: bool = ..., title: bool = ...) -> str:
    """contextInfo is undoable, queryable, and editable.
    
    This command allows you to get information on named contexts.

    ---
    - Args:
        - [context name]: Input item(s).
        - c: Return the class type of the named context.
        - escapeContext (esc): Return the command string that will allow you to exit the current tool.
        - exists (ex): Return true if the context exists, false if it does not exists (or is internal and therefore untouchable)
        - image1 (i1): Returns the name of an xpm associated with the named context.
        - image2 (i2): Returns the name of an xpm associated with the named context.
        - image3 (i3): Returns the name of an xpm associated with the named context.
        - title (t): Return the title string of the named context.
    """
@overload #Overload for contextInfo in ['create']
def contextInfo([context name]: [context name], esc: bool = ..., ex: bool = ..., i1: bool = ..., i2: bool = ..., i3: bool = ..., t: bool = ...) -> str:
    """contextInfo is undoable, queryable, and editable.
    
    This command allows you to get information on named contexts.

    ---
    - Args:
        - [context name]: Input item(s).
        - c: Return the class type of the named context.
        - escapeContext (esc): Return the command string that will allow you to exit the current tool.
        - exists (ex): Return true if the context exists, false if it does not exists (or is internal and therefore untouchable)
        - image1 (i1): Returns the name of an xpm associated with the named context.
        - image2 (i2): Returns the name of an xpm associated with the named context.
        - image3 (i3): Returns the name of an xpm associated with the named context.
        - title (t): Return the title string of the named context.
    """
@overload #Overload for contextInfo in ['create']
def contextInfo([context name]: [context name], c: bool = ..., escapeContext: bool = ..., esc: bool = ..., exists: bool = ..., ex: bool = ..., image1: bool = ..., i1: bool = ..., image2: bool = ..., i2: bool = ..., image3: bool = ..., i3: bool = ..., title: bool = ..., t: bool = ...) -> str:
    """contextInfo is undoable, queryable, and editable.
    
    This command allows you to get information on named contexts.

    ---
    - Args:
        - [context name]: Input item(s).
        - c: Return the class type of the named context.
        - escapeContext (esc): Return the command string that will allow you to exit the current tool.
        - exists (ex): Return true if the context exists, false if it does not exists (or is internal and therefore untouchable)
        - image1 (i1): Returns the name of an xpm associated with the named context.
        - image2 (i2): Returns the name of an xpm associated with the named context.
        - image3 (i3): Returns the name of an xpm associated with the named context.
        - title (t): Return the title string of the named context.
    """
