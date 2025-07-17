"""Stub files for Attributes category in Maya commands, command: listAttrPatterns."""

from typing import Any, overload

@overload #Overload for listAttrPatterns in ['create']
def listAttrPatterns(patternType: bool = ..., verbose: bool = ...) -> list[str]:
    """listAttrPatterns is NOT undoable, NOT queryable, and NOT editable.
    
    Attribute patterns are plain text descriptions of an entire Maya attribute
    forest. ("forest" because there could be an arbitrary number of root level
    attributes, it's not restricted to having a single common parent though in
    general that practice is a good idea.) This command lists the various pattern
    types available, usually created via plugin, as well as any specific patterns
    that have already been instantiated. A pattern type is a thing that knows how
    to take some textual description of an attribute tree, e.g. XML or plaintext,
    and convert it into an attribute pattern that can be applied to any node or
    node type in Maya.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.listAttrPatterns()
        // Return: ["approvalAttrs", "sceneAndShotAttrs"] //
        cmds.listAttrPatterns( patternType=True )
        // Return: "xmlPatternFactory" //
        cmds.listAttrPatterns( patternType=True, verbose=True )
        // Return: ["xmlPatternFactory", "xmlPatternFactory/approvalAttrs", "xmlPatternFactory/sceneAndShotAttrs"] //
        cmds.listAttrPatterns( verbose=True )
        Pattern approvalAttrs
        PatternFactory xmlPatternFactory:
        File: "attrPatterns/approvalAttrs.xml"
        Attribute Count: 8
        Attribute Tree:
        fxApproval (compound)
        fxApprover (string)
        fxApprovalDate (int)
        fxApprovalState (enum)
        layoutApproval (compound)
        layoutApprover (string)
        layoutApprovalDate (int)
        layoutApprovalState (enum)
        Pattern sceneAndShotAttrs
        PatternFactory xmlPatternFactory:
        File: "attrPatterns/sceneAndShotAttrs.xml"
        Attribute Count: 4
        Attribute Tree:
        sceneId (int)
        sceneOwner (string)
        shotId (int)
        shotOwner (string)
        // Return: ["approvalAttrs", "sceneAndShotAttrs"] //
    ```

    ---
    - Args:
        - patternType (pt): If turned on then show the list of pattern types rather than actual instantiated patterns.
        - verbose (v): If turned on then show detailed information about the patterns or pattern types. The same list of instance or pattern names is returned as for the non-verbose case.
    """
@overload #Overload for listAttrPatterns in ['create']
def listAttrPatterns(pt: bool = ..., v: bool = ...) -> list[str]:
    """listAttrPatterns is NOT undoable, NOT queryable, and NOT editable.
    
    Attribute patterns are plain text descriptions of an entire Maya attribute
    forest. ("forest" because there could be an arbitrary number of root level
    attributes, it's not restricted to having a single common parent though in
    general that practice is a good idea.) This command lists the various pattern
    types available, usually created via plugin, as well as any specific patterns
    that have already been instantiated. A pattern type is a thing that knows how
    to take some textual description of an attribute tree, e.g. XML or plaintext,
    and convert it into an attribute pattern that can be applied to any node or
    node type in Maya.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.listAttrPatterns()
        // Return: ["approvalAttrs", "sceneAndShotAttrs"] //
        cmds.listAttrPatterns( patternType=True )
        // Return: "xmlPatternFactory" //
        cmds.listAttrPatterns( patternType=True, verbose=True )
        // Return: ["xmlPatternFactory", "xmlPatternFactory/approvalAttrs", "xmlPatternFactory/sceneAndShotAttrs"] //
        cmds.listAttrPatterns( verbose=True )
        Pattern approvalAttrs
        PatternFactory xmlPatternFactory:
        File: "attrPatterns/approvalAttrs.xml"
        Attribute Count: 8
        Attribute Tree:
        fxApproval (compound)
        fxApprover (string)
        fxApprovalDate (int)
        fxApprovalState (enum)
        layoutApproval (compound)
        layoutApprover (string)
        layoutApprovalDate (int)
        layoutApprovalState (enum)
        Pattern sceneAndShotAttrs
        PatternFactory xmlPatternFactory:
        File: "attrPatterns/sceneAndShotAttrs.xml"
        Attribute Count: 4
        Attribute Tree:
        sceneId (int)
        sceneOwner (string)
        shotId (int)
        shotOwner (string)
        // Return: ["approvalAttrs", "sceneAndShotAttrs"] //
    ```

    ---
    - Args:
        - patternType (pt): If turned on then show the list of pattern types rather than actual instantiated patterns.
        - verbose (v): If turned on then show detailed information about the patterns or pattern types. The same list of instance or pattern names is returned as for the non-verbose case.
    """
@overload #Overload for listAttrPatterns in ['create']
def listAttrPatterns(patternType: bool = ..., pt: bool = ..., verbose: bool = ..., v: bool = ...) -> list[str]:
    """listAttrPatterns is NOT undoable, NOT queryable, and NOT editable.
    
    Attribute patterns are plain text descriptions of an entire Maya attribute
    forest. ("forest" because there could be an arbitrary number of root level
    attributes, it's not restricted to having a single common parent though in
    general that practice is a good idea.) This command lists the various pattern
    types available, usually created via plugin, as well as any specific patterns
    that have already been instantiated. A pattern type is a thing that knows how
    to take some textual description of an attribute tree, e.g. XML or plaintext,
    and convert it into an attribute pattern that can be applied to any node or
    node type in Maya.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.listAttrPatterns()
        // Return: ["approvalAttrs", "sceneAndShotAttrs"] //
        cmds.listAttrPatterns( patternType=True )
        // Return: "xmlPatternFactory" //
        cmds.listAttrPatterns( patternType=True, verbose=True )
        // Return: ["xmlPatternFactory", "xmlPatternFactory/approvalAttrs", "xmlPatternFactory/sceneAndShotAttrs"] //
        cmds.listAttrPatterns( verbose=True )
        Pattern approvalAttrs
        PatternFactory xmlPatternFactory:
        File: "attrPatterns/approvalAttrs.xml"
        Attribute Count: 8
        Attribute Tree:
        fxApproval (compound)
        fxApprover (string)
        fxApprovalDate (int)
        fxApprovalState (enum)
        layoutApproval (compound)
        layoutApprover (string)
        layoutApprovalDate (int)
        layoutApprovalState (enum)
        Pattern sceneAndShotAttrs
        PatternFactory xmlPatternFactory:
        File: "attrPatterns/sceneAndShotAttrs.xml"
        Attribute Count: 4
        Attribute Tree:
        sceneId (int)
        sceneOwner (string)
        shotId (int)
        shotOwner (string)
        // Return: ["approvalAttrs", "sceneAndShotAttrs"] //
    ```

    ---
    - Args:
        - patternType (pt): If turned on then show the list of pattern types rather than actual instantiated patterns.
        - verbose (v): If turned on then show detailed information about the patterns or pattern types. The same list of instance or pattern names is returned as for the non-verbose case.
    """
