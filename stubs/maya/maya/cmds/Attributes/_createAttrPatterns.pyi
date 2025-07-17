"""Stub files for Attributes category in Maya commands, command: createAttrPatterns."""

from typing import Any, overload

@overload #Overload for createAttrPatterns in ['create']
def createAttrPatterns(patternDefinition: str = ..., patternFile: str = ..., patternType: str = ...) -> str:
    """createAttrPatterns is undoable, NOT queryable, and NOT editable.
    
    Create a new instance of an attribute pattern given a pattern type (e.g. XML)
    and a string or data file containing the description of the attribute tree in
    the pattern's format.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.createAttrPatterns( patternType="xmlPattern", patternFile="patterns/patternFile.xml" )
        // Result: [myXMLPattern] //
    ```

    ---
    - Args:
        - patternDefinition (pd): Hardcoded string containing the pattern definition, for simpler formats that don't really need a separate file for definition.
        - patternFile (pf): File where the pattern information can be found
        - patternType (pt): Name of the pattern definition type to use in creating this instance of the pattern.
    """
@overload #Overload for createAttrPatterns in ['create']
def createAttrPatterns(pd: str = ..., pf: str = ..., pt: str = ...) -> str:
    """createAttrPatterns is undoable, NOT queryable, and NOT editable.
    
    Create a new instance of an attribute pattern given a pattern type (e.g. XML)
    and a string or data file containing the description of the attribute tree in
    the pattern's format.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.createAttrPatterns( patternType="xmlPattern", patternFile="patterns/patternFile.xml" )
        // Result: [myXMLPattern] //
    ```

    ---
    - Args:
        - patternDefinition (pd): Hardcoded string containing the pattern definition, for simpler formats that don't really need a separate file for definition.
        - patternFile (pf): File where the pattern information can be found
        - patternType (pt): Name of the pattern definition type to use in creating this instance of the pattern.
    """
@overload #Overload for createAttrPatterns in ['create']
def createAttrPatterns(patternDefinition: str = ..., pd: str = ..., patternFile: str = ..., pf: str = ..., patternType: str = ..., pt: str = ...) -> str:
    """createAttrPatterns is undoable, NOT queryable, and NOT editable.
    
    Create a new instance of an attribute pattern given a pattern type (e.g. XML)
    and a string or data file containing the description of the attribute tree in
    the pattern's format.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.createAttrPatterns( patternType="xmlPattern", patternFile="patterns/patternFile.xml" )
        // Result: [myXMLPattern] //
    ```

    ---
    - Args:
        - patternDefinition (pd): Hardcoded string containing the pattern definition, for simpler formats that don't really need a separate file for definition.
        - patternFile (pf): File where the pattern information can be found
        - patternType (pt): Name of the pattern definition type to use in creating this instance of the pattern.
    """
