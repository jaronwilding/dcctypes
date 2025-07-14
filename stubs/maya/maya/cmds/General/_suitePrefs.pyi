"""Stub files for General category in Maya commands, command: suitePrefs."""

from typing import Any, overload

@overload #Overload for suitePrefs in ['create']
def suitePrefs(applyToSuite: str = ..., installedAsSuite: bool = ..., isCompleteSuite: bool = ...) -> None:
    """suitePrefs is undoable, NOT queryable, and NOT editable.
    
    This command sets the mouse and keyboard interaction mode for Maya and other
    Suites applications (if Maya is part of a Suites install).

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

    ---
    - Args:
        - applyToSuite (ats): Apply the mouse and keyboard interaction settings for the given application to all applications in the Suite (if Maya is part of a Suites install). Valid values are "Maya", "3dsMax", or "undefined", which signifies that each app is to use
            their own settings.
        - installedAsSuite (ias): Returns true if Maya is part of a Suites install, false otherwise.
        - isCompleteSuite (ics): Returns true if the Suites install contains all Entertainment Creation Suite products, false otherwise.
    """
