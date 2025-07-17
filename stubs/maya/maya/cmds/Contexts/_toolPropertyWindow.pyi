"""Stub files for Contexts category in Maya commands, command: toolPropertyWindow."""

from typing import Any, overload

@overload #Overload for toolPropertyWindow in ['create']
def toolPropertyWindow(inMainWindow: bool = ..., restore: bool = ...) -> None:
    """toolPropertyWindow is undoable, queryable, and editable.
    
    End users should only call this command as 1. a query (in the custom tool
    property sheet code) or 2. with no arguments to create the default tool
    property sheet. The more complex uses of it are internal.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.toolPropertyWindow()
        pictureObject = cmds.toolPropertyWindow(q=True, icon=True)
    ```

    ---
    - Args:
        - inMainWindow (imw): Specify true if you want the tool settings to appear in the main window rather than a separate window.
        - restore (rs): Reopens the tool settings window. This flag can be used with the flaginMainWindowfor the fall back location if the tool settings can't be restored.
    """
@overload #Overload for toolPropertyWindow in ['create']
def toolPropertyWindow(imw: bool = ..., rs: bool = ...) -> None:
    """toolPropertyWindow is undoable, queryable, and editable.
    
    End users should only call this command as 1. a query (in the custom tool
    property sheet code) or 2. with no arguments to create the default tool
    property sheet. The more complex uses of it are internal.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.toolPropertyWindow()
        pictureObject = cmds.toolPropertyWindow(q=True, icon=True)
    ```

    ---
    - Args:
        - inMainWindow (imw): Specify true if you want the tool settings to appear in the main window rather than a separate window.
        - restore (rs): Reopens the tool settings window. This flag can be used with the flaginMainWindowfor the fall back location if the tool settings can't be restored.
    """
@overload #Overload for toolPropertyWindow in ['create']
def toolPropertyWindow(inMainWindow: bool = ..., imw: bool = ..., restore: bool = ..., rs: bool = ...) -> None:
    """toolPropertyWindow is undoable, queryable, and editable.
    
    End users should only call this command as 1. a query (in the custom tool
    property sheet code) or 2. with no arguments to create the default tool
    property sheet. The more complex uses of it are internal.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.toolPropertyWindow()
        pictureObject = cmds.toolPropertyWindow(q=True, icon=True)
    ```

    ---
    - Args:
        - inMainWindow (imw): Specify true if you want the tool settings to appear in the main window rather than a separate window.
        - restore (rs): Reopens the tool settings window. This flag can be used with the flaginMainWindowfor the fall back location if the tool settings can't be restored.
    """
@overload #Overload for toolPropertyWindow in ['query']
def toolPropertyWindow(field: str = ..., helpButton: str = ..., icon: str = ..., location: str = ..., noviceMode: bool = ..., resetButton: str = ..., selectCommand: str = ..., showCommand: str = ..., query: bool = ...) -> None:
    """toolPropertyWindow is undoable, queryable, and editable.
    
    End users should only call this command as 1. a query (in the custom tool
    property sheet code) or 2. with no arguments to create the default tool
    property sheet. The more complex uses of it are internal.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.toolPropertyWindow()
        pictureObject = cmds.toolPropertyWindow(q=True, icon=True)
    ```

    ---
    - Args:
        - field (fld): Sets/returns the name of the text field used to store the tool name in the property sheet.
        - helpButton (hb): Sets/returns the name of the button used to show help on the tool in the property sheet.
        - icon (icn): Sets/returns the name of the static picture object (used to display the tool icon in the property sheet).
        - location (loc): Sets/returns the location of the current tool property sheet, or an empty string if there is none.
        - noviceMode (nm): Sets/returns the 'novice mode' flag.(unused at the moment)
        - resetButton (rb): Sets/returns the name of the button used to restore the tool settings in the property sheet.
        - selectCommand (sel): Sets/returns the property sheet's select command.
        - showCommand (shw): Sets/returns the property sheet's display command.
        - query (q): Query mode flag
    """
@overload #Overload for toolPropertyWindow in ['query']
def toolPropertyWindow(fld: str = ..., hb: str = ..., icn: str = ..., loc: str = ..., nm: bool = ..., rb: str = ..., sel: str = ..., shw: str = ..., q: bool = ...) -> None:
    """toolPropertyWindow is undoable, queryable, and editable.
    
    End users should only call this command as 1. a query (in the custom tool
    property sheet code) or 2. with no arguments to create the default tool
    property sheet. The more complex uses of it are internal.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.toolPropertyWindow()
        pictureObject = cmds.toolPropertyWindow(q=True, icon=True)
    ```

    ---
    - Args:
        - field (fld): Sets/returns the name of the text field used to store the tool name in the property sheet.
        - helpButton (hb): Sets/returns the name of the button used to show help on the tool in the property sheet.
        - icon (icn): Sets/returns the name of the static picture object (used to display the tool icon in the property sheet).
        - location (loc): Sets/returns the location of the current tool property sheet, or an empty string if there is none.
        - noviceMode (nm): Sets/returns the 'novice mode' flag.(unused at the moment)
        - resetButton (rb): Sets/returns the name of the button used to restore the tool settings in the property sheet.
        - selectCommand (sel): Sets/returns the property sheet's select command.
        - showCommand (shw): Sets/returns the property sheet's display command.
        - query (q): Query mode flag
    """
@overload #Overload for toolPropertyWindow in ['query']
def toolPropertyWindow(field: str = ..., fld: str = ..., helpButton: str = ..., hb: str = ..., icon: str = ..., icn: str = ..., location: str = ..., loc: str = ..., noviceMode: bool = ..., nm: bool = ..., resetButton: str = ..., rb: str = ..., selectCommand: str = ..., sel: str = ..., showCommand: str = ..., shw: str = ..., query: bool = ..., q: bool = ...) -> None:
    """toolPropertyWindow is undoable, queryable, and editable.
    
    End users should only call this command as 1. a query (in the custom tool
    property sheet code) or 2. with no arguments to create the default tool
    property sheet. The more complex uses of it are internal.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.toolPropertyWindow()
        pictureObject = cmds.toolPropertyWindow(q=True, icon=True)
    ```

    ---
    - Args:
        - field (fld): Sets/returns the name of the text field used to store the tool name in the property sheet.
        - helpButton (hb): Sets/returns the name of the button used to show help on the tool in the property sheet.
        - icon (icn): Sets/returns the name of the static picture object (used to display the tool icon in the property sheet).
        - location (loc): Sets/returns the location of the current tool property sheet, or an empty string if there is none.
        - noviceMode (nm): Sets/returns the 'novice mode' flag.(unused at the moment)
        - resetButton (rb): Sets/returns the name of the button used to restore the tool settings in the property sheet.
        - selectCommand (sel): Sets/returns the property sheet's select command.
        - showCommand (shw): Sets/returns the property sheet's display command.
        - query (q): Query mode flag
    """
@overload #Overload for toolPropertyWindow in ['edit']
def toolPropertyWindow(field: str = ..., helpButton: str = ..., icon: str = ..., location: str = ..., noviceMode: bool = ..., resetButton: str = ..., selectCommand: str = ..., showCommand: str = ..., edit: bool = ...) -> None:
    """toolPropertyWindow is undoable, queryable, and editable.
    
    End users should only call this command as 1. a query (in the custom tool
    property sheet code) or 2. with no arguments to create the default tool
    property sheet. The more complex uses of it are internal.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.toolPropertyWindow()
        pictureObject = cmds.toolPropertyWindow(q=True, icon=True)
    ```

    ---
    - Args:
        - field (fld): Sets/returns the name of the text field used to store the tool name in the property sheet.
        - helpButton (hb): Sets/returns the name of the button used to show help on the tool in the property sheet.
        - icon (icn): Sets/returns the name of the static picture object (used to display the tool icon in the property sheet).
        - location (loc): Sets/returns the location of the current tool property sheet, or an empty string if there is none.
        - noviceMode (nm): Sets/returns the 'novice mode' flag.(unused at the moment)
        - resetButton (rb): Sets/returns the name of the button used to restore the tool settings in the property sheet.
        - selectCommand (sel): Sets/returns the property sheet's select command.
        - showCommand (shw): Sets/returns the property sheet's display command.
        - edit (e): Edit mode flag
    """
@overload #Overload for toolPropertyWindow in ['edit']
def toolPropertyWindow(fld: str = ..., hb: str = ..., icn: str = ..., loc: str = ..., nm: bool = ..., rb: str = ..., sel: str = ..., shw: str = ..., e: bool = ...) -> None:
    """toolPropertyWindow is undoable, queryable, and editable.
    
    End users should only call this command as 1. a query (in the custom tool
    property sheet code) or 2. with no arguments to create the default tool
    property sheet. The more complex uses of it are internal.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.toolPropertyWindow()
        pictureObject = cmds.toolPropertyWindow(q=True, icon=True)
    ```

    ---
    - Args:
        - field (fld): Sets/returns the name of the text field used to store the tool name in the property sheet.
        - helpButton (hb): Sets/returns the name of the button used to show help on the tool in the property sheet.
        - icon (icn): Sets/returns the name of the static picture object (used to display the tool icon in the property sheet).
        - location (loc): Sets/returns the location of the current tool property sheet, or an empty string if there is none.
        - noviceMode (nm): Sets/returns the 'novice mode' flag.(unused at the moment)
        - resetButton (rb): Sets/returns the name of the button used to restore the tool settings in the property sheet.
        - selectCommand (sel): Sets/returns the property sheet's select command.
        - showCommand (shw): Sets/returns the property sheet's display command.
        - edit (e): Edit mode flag
    """
@overload #Overload for toolPropertyWindow in ['edit']
def toolPropertyWindow(field: str = ..., fld: str = ..., helpButton: str = ..., hb: str = ..., icon: str = ..., icn: str = ..., location: str = ..., loc: str = ..., noviceMode: bool = ..., nm: bool = ..., resetButton: str = ..., rb: str = ..., selectCommand: str = ..., sel: str = ..., showCommand: str = ..., shw: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """toolPropertyWindow is undoable, queryable, and editable.
    
    End users should only call this command as 1. a query (in the custom tool
    property sheet code) or 2. with no arguments to create the default tool
    property sheet. The more complex uses of it are internal.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.toolPropertyWindow()
        pictureObject = cmds.toolPropertyWindow(q=True, icon=True)
    ```

    ---
    - Args:
        - field (fld): Sets/returns the name of the text field used to store the tool name in the property sheet.
        - helpButton (hb): Sets/returns the name of the button used to show help on the tool in the property sheet.
        - icon (icn): Sets/returns the name of the static picture object (used to display the tool icon in the property sheet).
        - location (loc): Sets/returns the location of the current tool property sheet, or an empty string if there is none.
        - noviceMode (nm): Sets/returns the 'novice mode' flag.(unused at the moment)
        - resetButton (rb): Sets/returns the name of the button used to restore the tool settings in the property sheet.
        - selectCommand (sel): Sets/returns the property sheet's select command.
        - showCommand (shw): Sets/returns the property sheet's display command.
        - edit (e): Edit mode flag
    """
