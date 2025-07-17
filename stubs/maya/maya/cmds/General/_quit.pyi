"""Stub files for General category in Maya commands, command: quit."""

from typing import Any, overload

@overload #Overload for quit in ['create']
def quit(abort: bool = ..., exitCode: int = ..., force: bool = ...) -> None:
    """quit is undoable, NOT queryable, and NOT editable.
    
    This command is used to exit the application.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.quit()
        cmds.quit(force=True)
    ```

    ---
    - Args:
        - abort (a): Will quit without saving like -force, but will also prevent preferences/hotkeys/colors from being saved.  Use at your own risk.
        - exitCode (ec): Specifies the exit code to be returned once the application exits.  The default exit code is 0.
        - force (f): If specified, this flag will force a quit without saving or prompting for saving changes. Use at your own risk.
    """
@overload #Overload for quit in ['create']
def quit(a: bool = ..., ec: int = ..., f: bool = ...) -> None:
    """quit is undoable, NOT queryable, and NOT editable.
    
    This command is used to exit the application.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.quit()
        cmds.quit(force=True)
    ```

    ---
    - Args:
        - abort (a): Will quit without saving like -force, but will also prevent preferences/hotkeys/colors from being saved.  Use at your own risk.
        - exitCode (ec): Specifies the exit code to be returned once the application exits.  The default exit code is 0.
        - force (f): If specified, this flag will force a quit without saving or prompting for saving changes. Use at your own risk.
    """
@overload #Overload for quit in ['create']
def quit(abort: bool = ..., a: bool = ..., exitCode: int = ..., ec: int = ..., force: bool = ..., f: bool = ...) -> None:
    """quit is undoable, NOT queryable, and NOT editable.
    
    This command is used to exit the application.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.quit()
        cmds.quit(force=True)
    ```

    ---
    - Args:
        - abort (a): Will quit without saving like -force, but will also prevent preferences/hotkeys/colors from being saved.  Use at your own risk.
        - exitCode (ec): Specifies the exit code to be returned once the application exits.  The default exit code is 0.
        - force (f): If specified, this flag will force a quit without saving or prompting for saving changes. Use at your own risk.
    """
