"""Stub files for Contexts category in Maya commands, command: artAttrTool."""

from typing import Any, overload

@overload #Overload for artAttrTool in ['create']
def artAttrTool(add: str = ..., exists: str = ..., remove: str = ...) -> None:
    """artAttrTool is NOT undoable, queryable, and NOT editable.
    
    The artAttrTool command manages the list of tool types which are used for
    attribute painting. This command supports querying the list contents as well
    as adding new tools to the list. Note that there is a set of built-in tools.
    The list of built-ins can be queried by starting Maya and doing an
    "artAttrTool -q".
    
    The tools which are managed by this command are all intended for attribute
    painting via Artisan: when you create a new context via artAttrCtx you specify
    the tool name via artAttrCtx's -whichTool flag. Typically the user may wish to
    simply use one of the built-in tools. However, if you need to have custom
    Properties and Values sheets asscociated with your tool, you will need to
    define a custom tool via artAttrTool -add "toolName". For an example of a
    custom attribute painting tool, see the devkit example customtoolPaint.mel.

    ---
    - Args:
        - add ()): Adds the named tool to the internal list of tools.
        - exists (ex): Checks if the named tool exists, returning true if found, and false otherwise.
        - remove (rm): Removes the named tool from the internal list of tools.
    """
@overload #Overload for artAttrTool in ['create']
def artAttrTool(): str = ..., ex: str = ..., rm: str = ...) -> None:
    """artAttrTool is NOT undoable, queryable, and NOT editable.
    
    The artAttrTool command manages the list of tool types which are used for
    attribute painting. This command supports querying the list contents as well
    as adding new tools to the list. Note that there is a set of built-in tools.
    The list of built-ins can be queried by starting Maya and doing an
    "artAttrTool -q".
    
    The tools which are managed by this command are all intended for attribute
    painting via Artisan: when you create a new context via artAttrCtx you specify
    the tool name via artAttrCtx's -whichTool flag. Typically the user may wish to
    simply use one of the built-in tools. However, if you need to have custom
    Properties and Values sheets asscociated with your tool, you will need to
    define a custom tool via artAttrTool -add "toolName". For an example of a
    custom attribute painting tool, see the devkit example customtoolPaint.mel.

    ---
    - Args:
        - add ()): Adds the named tool to the internal list of tools.
        - exists (ex): Checks if the named tool exists, returning true if found, and false otherwise.
        - remove (rm): Removes the named tool from the internal list of tools.
    """
@overload #Overload for artAttrTool in ['create']
def artAttrTool(add: str = ..., ): str = ..., exists: str = ..., ex: str = ..., remove: str = ..., rm: str = ...) -> None:
    """artAttrTool is NOT undoable, queryable, and NOT editable.
    
    The artAttrTool command manages the list of tool types which are used for
    attribute painting. This command supports querying the list contents as well
    as adding new tools to the list. Note that there is a set of built-in tools.
    The list of built-ins can be queried by starting Maya and doing an
    "artAttrTool -q".
    
    The tools which are managed by this command are all intended for attribute
    painting via Artisan: when you create a new context via artAttrCtx you specify
    the tool name via artAttrCtx's -whichTool flag. Typically the user may wish to
    simply use one of the built-in tools. However, if you need to have custom
    Properties and Values sheets asscociated with your tool, you will need to
    define a custom tool via artAttrTool -add "toolName". For an example of a
    custom attribute painting tool, see the devkit example customtoolPaint.mel.

    ---
    - Args:
        - add ()): Adds the named tool to the internal list of tools.
        - exists (ex): Checks if the named tool exists, returning true if found, and false otherwise.
        - remove (rm): Removes the named tool from the internal list of tools.
    """
@overload #Overload for artAttrTool in ['query']
def artAttrTool(exists: str = ..., query: bool = ...) -> None:
    """artAttrTool is NOT undoable, queryable, and NOT editable.
    
    The artAttrTool command manages the list of tool types which are used for
    attribute painting. This command supports querying the list contents as well
    as adding new tools to the list. Note that there is a set of built-in tools.
    The list of built-ins can be queried by starting Maya and doing an
    "artAttrTool -q".
    
    The tools which are managed by this command are all intended for attribute
    painting via Artisan: when you create a new context via artAttrCtx you specify
    the tool name via artAttrCtx's -whichTool flag. Typically the user may wish to
    simply use one of the built-in tools. However, if you need to have custom
    Properties and Values sheets asscociated with your tool, you will need to
    define a custom tool via artAttrTool -add "toolName". For an example of a
    custom attribute painting tool, see the devkit example customtoolPaint.mel.

    ---
    - Args:
        - exists (ex): Checks if the named tool exists, returning true if found, and false otherwise.
        - query (q): Query mode flag
    """
@overload #Overload for artAttrTool in ['query']
def artAttrTool(ex: str = ..., q: bool = ...) -> None:
    """artAttrTool is NOT undoable, queryable, and NOT editable.
    
    The artAttrTool command manages the list of tool types which are used for
    attribute painting. This command supports querying the list contents as well
    as adding new tools to the list. Note that there is a set of built-in tools.
    The list of built-ins can be queried by starting Maya and doing an
    "artAttrTool -q".
    
    The tools which are managed by this command are all intended for attribute
    painting via Artisan: when you create a new context via artAttrCtx you specify
    the tool name via artAttrCtx's -whichTool flag. Typically the user may wish to
    simply use one of the built-in tools. However, if you need to have custom
    Properties and Values sheets asscociated with your tool, you will need to
    define a custom tool via artAttrTool -add "toolName". For an example of a
    custom attribute painting tool, see the devkit example customtoolPaint.mel.

    ---
    - Args:
        - exists (ex): Checks if the named tool exists, returning true if found, and false otherwise.
        - query (q): Query mode flag
    """
@overload #Overload for artAttrTool in ['query']
def artAttrTool(exists: str = ..., ex: str = ..., query: bool = ..., q: bool = ...) -> None:
    """artAttrTool is NOT undoable, queryable, and NOT editable.
    
    The artAttrTool command manages the list of tool types which are used for
    attribute painting. This command supports querying the list contents as well
    as adding new tools to the list. Note that there is a set of built-in tools.
    The list of built-ins can be queried by starting Maya and doing an
    "artAttrTool -q".
    
    The tools which are managed by this command are all intended for attribute
    painting via Artisan: when you create a new context via artAttrCtx you specify
    the tool name via artAttrCtx's -whichTool flag. Typically the user may wish to
    simply use one of the built-in tools. However, if you need to have custom
    Properties and Values sheets asscociated with your tool, you will need to
    define a custom tool via artAttrTool -add "toolName". For an example of a
    custom attribute painting tool, see the devkit example customtoolPaint.mel.

    ---
    - Args:
        - exists (ex): Checks if the named tool exists, returning true if found, and false otherwise.
        - query (q): Query mode flag
    """
@overload #Overload for artAttrTool in ['edit']
def artAttrTool(exists: str = ..., edit: bool = ...) -> None:
    """artAttrTool is NOT undoable, queryable, and NOT editable.
    
    The artAttrTool command manages the list of tool types which are used for
    attribute painting. This command supports querying the list contents as well
    as adding new tools to the list. Note that there is a set of built-in tools.
    The list of built-ins can be queried by starting Maya and doing an
    "artAttrTool -q".
    
    The tools which are managed by this command are all intended for attribute
    painting via Artisan: when you create a new context via artAttrCtx you specify
    the tool name via artAttrCtx's -whichTool flag. Typically the user may wish to
    simply use one of the built-in tools. However, if you need to have custom
    Properties and Values sheets asscociated with your tool, you will need to
    define a custom tool via artAttrTool -add "toolName". For an example of a
    custom attribute painting tool, see the devkit example customtoolPaint.mel.

    ---
    - Args:
        - exists (ex): Checks if the named tool exists, returning true if found, and false otherwise.
        - edit (e): Edit mode flag
    """
@overload #Overload for artAttrTool in ['edit']
def artAttrTool(ex: str = ..., e: bool = ...) -> None:
    """artAttrTool is NOT undoable, queryable, and NOT editable.
    
    The artAttrTool command manages the list of tool types which are used for
    attribute painting. This command supports querying the list contents as well
    as adding new tools to the list. Note that there is a set of built-in tools.
    The list of built-ins can be queried by starting Maya and doing an
    "artAttrTool -q".
    
    The tools which are managed by this command are all intended for attribute
    painting via Artisan: when you create a new context via artAttrCtx you specify
    the tool name via artAttrCtx's -whichTool flag. Typically the user may wish to
    simply use one of the built-in tools. However, if you need to have custom
    Properties and Values sheets asscociated with your tool, you will need to
    define a custom tool via artAttrTool -add "toolName". For an example of a
    custom attribute painting tool, see the devkit example customtoolPaint.mel.

    ---
    - Args:
        - exists (ex): Checks if the named tool exists, returning true if found, and false otherwise.
        - edit (e): Edit mode flag
    """
@overload #Overload for artAttrTool in ['edit']
def artAttrTool(exists: str = ..., ex: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """artAttrTool is NOT undoable, queryable, and NOT editable.
    
    The artAttrTool command manages the list of tool types which are used for
    attribute painting. This command supports querying the list contents as well
    as adding new tools to the list. Note that there is a set of built-in tools.
    The list of built-ins can be queried by starting Maya and doing an
    "artAttrTool -q".
    
    The tools which are managed by this command are all intended for attribute
    painting via Artisan: when you create a new context via artAttrCtx you specify
    the tool name via artAttrCtx's -whichTool flag. Typically the user may wish to
    simply use one of the built-in tools. However, if you need to have custom
    Properties and Values sheets asscociated with your tool, you will need to
    define a custom tool via artAttrTool -add "toolName". For an example of a
    custom attribute painting tool, see the devkit example customtoolPaint.mel.

    ---
    - Args:
        - exists (ex): Checks if the named tool exists, returning true if found, and false otherwise.
        - edit (e): Edit mode flag
    """
