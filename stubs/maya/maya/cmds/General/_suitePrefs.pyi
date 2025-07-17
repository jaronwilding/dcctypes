"""Stub files for General category in Maya commands, command: suitePrefs."""

from typing import Any, overload

@overload #Overload for suitePrefs in ['create']
def suitePrefs(applyToSuite: str = ..., installedAsSuite: bool = ..., isCompleteSuite: bool = ...) -> None:
    """suitePrefs is undoable, NOT queryable, and NOT editable.
    
    This command sets the mouse and keyboard interaction mode for Maya and other
    Suites applications (if Maya is part of a Suites install).

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Check if Maya is part of a Suites install
        isSuiteInstall = cmds.suitePrefs(q=True, installedAsSuite=True)
        if isSuiteInstall:
        #   Check whether Maya mouse and keyboard interaction
        #   has been applied to the Suite.
        applyMayaToSuite = cmds.suitePrefs(q=True, applyToSuite=True)
        if applyMayaToSuite:
        #       Apply Maya mouse and keyboard interaction to
        #       the Suite.
        cmds.suitePrefs(applyToSuite=True)
    ```

    ---
    - Args:
        - applyToSuite (ats): Apply the mouse and keyboard interaction settings for the given application to all applications in the Suite (if Maya is part of a Suites install). Valid values are "Maya", "3dsMax", or "undefined", which signifies that each app is to use
            their own settings.
        - installedAsSuite (ias): Returns true if Maya is part of a Suites install, false otherwise.
        - isCompleteSuite (ics): Returns true if the Suites install contains all Entertainment Creation Suite products, false otherwise.
    """
@overload #Overload for suitePrefs in ['create']
def suitePrefs(ats: str = ..., ias: bool = ..., ics: bool = ...) -> None:
    """suitePrefs is undoable, NOT queryable, and NOT editable.
    
    This command sets the mouse and keyboard interaction mode for Maya and other
    Suites applications (if Maya is part of a Suites install).

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Check if Maya is part of a Suites install
        isSuiteInstall = cmds.suitePrefs(q=True, installedAsSuite=True)
        if isSuiteInstall:
        #   Check whether Maya mouse and keyboard interaction
        #   has been applied to the Suite.
        applyMayaToSuite = cmds.suitePrefs(q=True, applyToSuite=True)
        if applyMayaToSuite:
        #       Apply Maya mouse and keyboard interaction to
        #       the Suite.
        cmds.suitePrefs(applyToSuite=True)
    ```

    ---
    - Args:
        - applyToSuite (ats): Apply the mouse and keyboard interaction settings for the given application to all applications in the Suite (if Maya is part of a Suites install). Valid values are "Maya", "3dsMax", or "undefined", which signifies that each app is to use
            their own settings.
        - installedAsSuite (ias): Returns true if Maya is part of a Suites install, false otherwise.
        - isCompleteSuite (ics): Returns true if the Suites install contains all Entertainment Creation Suite products, false otherwise.
    """
@overload #Overload for suitePrefs in ['create']
def suitePrefs(applyToSuite: str = ..., ats: str = ..., installedAsSuite: bool = ..., ias: bool = ..., isCompleteSuite: bool = ..., ics: bool = ...) -> None:
    """suitePrefs is undoable, NOT queryable, and NOT editable.
    
    This command sets the mouse and keyboard interaction mode for Maya and other
    Suites applications (if Maya is part of a Suites install).

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        # Check if Maya is part of a Suites install
        isSuiteInstall = cmds.suitePrefs(q=True, installedAsSuite=True)
        if isSuiteInstall:
        #   Check whether Maya mouse and keyboard interaction
        #   has been applied to the Suite.
        applyMayaToSuite = cmds.suitePrefs(q=True, applyToSuite=True)
        if applyMayaToSuite:
        #       Apply Maya mouse and keyboard interaction to
        #       the Suite.
        cmds.suitePrefs(applyToSuite=True)
    ```

    ---
    - Args:
        - applyToSuite (ats): Apply the mouse and keyboard interaction settings for the given application to all applications in the Suite (if Maya is part of a Suites install). Valid values are "Maya", "3dsMax", or "undefined", which signifies that each app is to use
            their own settings.
        - installedAsSuite (ias): Returns true if Maya is part of a Suites install, false otherwise.
        - isCompleteSuite (ics): Returns true if the Suites install contains all Entertainment Creation Suite products, false otherwise.
    """
