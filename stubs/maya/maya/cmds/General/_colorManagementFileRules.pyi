"""Stub files for General category in Maya commands, command: colorManagementFileRules."""

from typing import Any, overload

@overload #Overload for colorManagementFileRules in ['create']
def colorManagementFileRules(addRule: str = ..., colorSpace: str = ..., down: str = ..., evaluate: str = ..., extension: str = ..., listRules: bool = ..., load: bool = ..., moveUp: str = ..., pattern: str = ..., remove: str = ..., restoreDefaults: bool = ..., save: bool = ...) -> None:
    """colorManagementFileRules is NOT undoable, queryable, and editable.
    
    This non-undoable action manages the list of rules that Maya uses to assign an
    initial input color space to dependency graph nodes that read in color
    information from a file. Rules are structured in a chain of responsibility,
    from highest priority rule to lowest priority rule, each rule matching a file
    path pattern and extension. If a rule matches a given file path, its color
    space is returned as the result of rules evaluation, and no further rule is
    considered. The lowest priority rule will always return a match. Rules can be
    added, removed, and changed in priority in the list. Each rule can have its
    file path pattern, extension, and color space changed. The rule list can be
    saved to user preferences, and loaded from user preferences.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.colorManagementFileRules(add='ruleName', pattern='filePattern', extension='extension', colorSpace='colorSpace')
        cmds.colorManagementFileRules(remove='ruleName')
        cmds.colorManagementFileRules(up='ruleName')
        cmds.colorManagementFileRules(down='ruleName')
        cmds.colorManagementFileRules('ruleName', edit=True, pattern='filePattern')
        cmds.colorManagementFileRules('ruleName', edit=True, extension='extension')
        cmds.colorManagementFileRules('ruleName', edit=True, colorSpace='colorSpace')
        cmds.colorManagementFileRules('ruleName', query=True, pattern=True)
        cmds.colorManagementFileRules('ruleName', query=True, extension=True)
        cmds.colorManagementFileRules('ruleName', query=True, colorSpace=True)
        cmds.colorManagementFileRules(save=True)
        cmds.colorManagementFileRules(load=True)
        # Return array of rule name strings.
        cmds.colorManagementFileRules(listRules=True)
        # Return input space corresponding to file path.
        cmds.colorManagementFileRules(evaluate=filePath)
    ```

    ---
    - Args:
        - addRule (add): Add a rule with the argument name to the list of rules, as the highest-priority rule.  If this flag is used, the pattern, extension, and colorSpace flags must be used as well, to specify the file rule pattern, extension, and color space,
            respectively.
        - colorSpace (cs): The input color space for the rule.  If the rule matches a file path, this is the color space that is returned.  This color space must match an existing color space in the input color space list.
        - down (dwn): Move the rule with the argument name down one position towards lower priority.
        - evaluate (ev): Evaluates the list of rules and returns the input color space name that corresponds to the argument file path.
        - extension (ext): The file extension for the rule is case insensitive
        - listRules (lsr): Returns an array of rule name strings, in order, from lowest-priority (rule 0) to highest-priority (last rule in array).
        - load (ld): Read the rules from Maya preferences.  Any existing rules are cleared.
        - moveUp (up): Move the rule with the argument name up one position towards higher priority.
        - pattern (pat): The file path pattern for the rule.  This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see
            http://en.wikipedia.org/wiki/Glob_%28programming%29.
        - remove (rm): Remove the rule with the argument name from the list of rules.
        - restoreDefaults (rde): Restore the list of rules to the default ones only.
        - save (sav): Save the rules to Maya preferences.
    """
@overload #Overload for colorManagementFileRules in ['create']
def colorManagementFileRules(add: str = ..., cs: str = ..., dwn: str = ..., ev: str = ..., ext: str = ..., lsr: bool = ..., ld: bool = ..., up: str = ..., pat: str = ..., rm: str = ..., rde: bool = ..., sav: bool = ...) -> None:
    """colorManagementFileRules is NOT undoable, queryable, and editable.
    
    This non-undoable action manages the list of rules that Maya uses to assign an
    initial input color space to dependency graph nodes that read in color
    information from a file. Rules are structured in a chain of responsibility,
    from highest priority rule to lowest priority rule, each rule matching a file
    path pattern and extension. If a rule matches a given file path, its color
    space is returned as the result of rules evaluation, and no further rule is
    considered. The lowest priority rule will always return a match. Rules can be
    added, removed, and changed in priority in the list. Each rule can have its
    file path pattern, extension, and color space changed. The rule list can be
    saved to user preferences, and loaded from user preferences.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.colorManagementFileRules(add='ruleName', pattern='filePattern', extension='extension', colorSpace='colorSpace')
        cmds.colorManagementFileRules(remove='ruleName')
        cmds.colorManagementFileRules(up='ruleName')
        cmds.colorManagementFileRules(down='ruleName')
        cmds.colorManagementFileRules('ruleName', edit=True, pattern='filePattern')
        cmds.colorManagementFileRules('ruleName', edit=True, extension='extension')
        cmds.colorManagementFileRules('ruleName', edit=True, colorSpace='colorSpace')
        cmds.colorManagementFileRules('ruleName', query=True, pattern=True)
        cmds.colorManagementFileRules('ruleName', query=True, extension=True)
        cmds.colorManagementFileRules('ruleName', query=True, colorSpace=True)
        cmds.colorManagementFileRules(save=True)
        cmds.colorManagementFileRules(load=True)
        # Return array of rule name strings.
        cmds.colorManagementFileRules(listRules=True)
        # Return input space corresponding to file path.
        cmds.colorManagementFileRules(evaluate=filePath)
    ```

    ---
    - Args:
        - addRule (add): Add a rule with the argument name to the list of rules, as the highest-priority rule.  If this flag is used, the pattern, extension, and colorSpace flags must be used as well, to specify the file rule pattern, extension, and color space,
            respectively.
        - colorSpace (cs): The input color space for the rule.  If the rule matches a file path, this is the color space that is returned.  This color space must match an existing color space in the input color space list.
        - down (dwn): Move the rule with the argument name down one position towards lower priority.
        - evaluate (ev): Evaluates the list of rules and returns the input color space name that corresponds to the argument file path.
        - extension (ext): The file extension for the rule is case insensitive
        - listRules (lsr): Returns an array of rule name strings, in order, from lowest-priority (rule 0) to highest-priority (last rule in array).
        - load (ld): Read the rules from Maya preferences.  Any existing rules are cleared.
        - moveUp (up): Move the rule with the argument name up one position towards higher priority.
        - pattern (pat): The file path pattern for the rule.  This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see
            http://en.wikipedia.org/wiki/Glob_%28programming%29.
        - remove (rm): Remove the rule with the argument name from the list of rules.
        - restoreDefaults (rde): Restore the list of rules to the default ones only.
        - save (sav): Save the rules to Maya preferences.
    """
@overload #Overload for colorManagementFileRules in ['create']
def colorManagementFileRules(addRule: str = ..., add: str = ..., colorSpace: str = ..., cs: str = ..., down: str = ..., dwn: str = ..., evaluate: str = ..., ev: str = ..., extension: str = ..., ext: str = ..., listRules: bool = ..., lsr: bool = ..., load: bool = ..., ld: bool = ..., moveUp: str = ..., up: str = ..., pattern: str = ..., pat: str = ..., remove: str = ..., rm: str = ..., restoreDefaults: bool = ..., rde: bool = ..., save: bool = ..., sav: bool = ...) -> None:
    """colorManagementFileRules is NOT undoable, queryable, and editable.
    
    This non-undoable action manages the list of rules that Maya uses to assign an
    initial input color space to dependency graph nodes that read in color
    information from a file. Rules are structured in a chain of responsibility,
    from highest priority rule to lowest priority rule, each rule matching a file
    path pattern and extension. If a rule matches a given file path, its color
    space is returned as the result of rules evaluation, and no further rule is
    considered. The lowest priority rule will always return a match. Rules can be
    added, removed, and changed in priority in the list. Each rule can have its
    file path pattern, extension, and color space changed. The rule list can be
    saved to user preferences, and loaded from user preferences.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.colorManagementFileRules(add='ruleName', pattern='filePattern', extension='extension', colorSpace='colorSpace')
        cmds.colorManagementFileRules(remove='ruleName')
        cmds.colorManagementFileRules(up='ruleName')
        cmds.colorManagementFileRules(down='ruleName')
        cmds.colorManagementFileRules('ruleName', edit=True, pattern='filePattern')
        cmds.colorManagementFileRules('ruleName', edit=True, extension='extension')
        cmds.colorManagementFileRules('ruleName', edit=True, colorSpace='colorSpace')
        cmds.colorManagementFileRules('ruleName', query=True, pattern=True)
        cmds.colorManagementFileRules('ruleName', query=True, extension=True)
        cmds.colorManagementFileRules('ruleName', query=True, colorSpace=True)
        cmds.colorManagementFileRules(save=True)
        cmds.colorManagementFileRules(load=True)
        # Return array of rule name strings.
        cmds.colorManagementFileRules(listRules=True)
        # Return input space corresponding to file path.
        cmds.colorManagementFileRules(evaluate=filePath)
    ```

    ---
    - Args:
        - addRule (add): Add a rule with the argument name to the list of rules, as the highest-priority rule.  If this flag is used, the pattern, extension, and colorSpace flags must be used as well, to specify the file rule pattern, extension, and color space,
            respectively.
        - colorSpace (cs): The input color space for the rule.  If the rule matches a file path, this is the color space that is returned.  This color space must match an existing color space in the input color space list.
        - down (dwn): Move the rule with the argument name down one position towards lower priority.
        - evaluate (ev): Evaluates the list of rules and returns the input color space name that corresponds to the argument file path.
        - extension (ext): The file extension for the rule is case insensitive
        - listRules (lsr): Returns an array of rule name strings, in order, from lowest-priority (rule 0) to highest-priority (last rule in array).
        - load (ld): Read the rules from Maya preferences.  Any existing rules are cleared.
        - moveUp (up): Move the rule with the argument name up one position towards higher priority.
        - pattern (pat): The file path pattern for the rule.  This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see
            http://en.wikipedia.org/wiki/Glob_%28programming%29.
        - remove (rm): Remove the rule with the argument name from the list of rules.
        - restoreDefaults (rde): Restore the list of rules to the default ones only.
        - save (sav): Save the rules to Maya preferences.
    """
@overload #Overload for colorManagementFileRules in ['query']
def colorManagementFileRules(colorSpace: str = ..., colorSpaceDescription: str = ..., colorSpaceFamilies: str = ..., colorSpaceNames: bool = ..., enabled: bool = ..., extension: str = ..., pattern: str = ..., query: bool = ...) -> None:
    """colorManagementFileRules is NOT undoable, queryable, and editable.
    
    This non-undoable action manages the list of rules that Maya uses to assign an
    initial input color space to dependency graph nodes that read in color
    information from a file. Rules are structured in a chain of responsibility,
    from highest priority rule to lowest priority rule, each rule matching a file
    path pattern and extension. If a rule matches a given file path, its color
    space is returned as the result of rules evaluation, and no further rule is
    considered. The lowest priority rule will always return a match. Rules can be
    added, removed, and changed in priority in the list. Each rule can have its
    file path pattern, extension, and color space changed. The rule list can be
    saved to user preferences, and loaded from user preferences.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.colorManagementFileRules(add='ruleName', pattern='filePattern', extension='extension', colorSpace='colorSpace')
        cmds.colorManagementFileRules(remove='ruleName')
        cmds.colorManagementFileRules(up='ruleName')
        cmds.colorManagementFileRules(down='ruleName')
        cmds.colorManagementFileRules('ruleName', edit=True, pattern='filePattern')
        cmds.colorManagementFileRules('ruleName', edit=True, extension='extension')
        cmds.colorManagementFileRules('ruleName', edit=True, colorSpace='colorSpace')
        cmds.colorManagementFileRules('ruleName', query=True, pattern=True)
        cmds.colorManagementFileRules('ruleName', query=True, extension=True)
        cmds.colorManagementFileRules('ruleName', query=True, colorSpace=True)
        cmds.colorManagementFileRules(save=True)
        cmds.colorManagementFileRules(load=True)
        # Return array of rule name strings.
        cmds.colorManagementFileRules(listRules=True)
        # Return input space corresponding to file path.
        cmds.colorManagementFileRules(evaluate=filePath)
    ```

    ---
    - Args:
        - colorSpace (cs): The input color space for the rule.  If the rule matches a file path, this is the color space that is returned.  This color space must match an existing color space in the input color space list.
        - colorSpaceDescription (csd): Returns the description for a specific color space.In query mode, this flag needs a value.
        - colorSpaceFamilies (csf): Returns the list of families for a specific color space. Used to add submenus when populating the color spaces UI popup of a rule.In query mode, this flag needs a value.
        - colorSpaceNames (csn): Returns the list of available color spaces. Used to populate the color spaces UI popup of a rule.
        - enabled (ena): Are the file rules enabled?
        - extension (ext): The file extension for the rule is case insensitive
        - pattern (pat): The file path pattern for the rule.  This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see
            http://en.wikipedia.org/wiki/Glob_%28programming%29.
        - query (q): Query mode flag
    """
@overload #Overload for colorManagementFileRules in ['query']
def colorManagementFileRules(cs: str = ..., csd: str = ..., csf: str = ..., csn: bool = ..., ena: bool = ..., ext: str = ..., pat: str = ..., q: bool = ...) -> None:
    """colorManagementFileRules is NOT undoable, queryable, and editable.
    
    This non-undoable action manages the list of rules that Maya uses to assign an
    initial input color space to dependency graph nodes that read in color
    information from a file. Rules are structured in a chain of responsibility,
    from highest priority rule to lowest priority rule, each rule matching a file
    path pattern and extension. If a rule matches a given file path, its color
    space is returned as the result of rules evaluation, and no further rule is
    considered. The lowest priority rule will always return a match. Rules can be
    added, removed, and changed in priority in the list. Each rule can have its
    file path pattern, extension, and color space changed. The rule list can be
    saved to user preferences, and loaded from user preferences.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.colorManagementFileRules(add='ruleName', pattern='filePattern', extension='extension', colorSpace='colorSpace')
        cmds.colorManagementFileRules(remove='ruleName')
        cmds.colorManagementFileRules(up='ruleName')
        cmds.colorManagementFileRules(down='ruleName')
        cmds.colorManagementFileRules('ruleName', edit=True, pattern='filePattern')
        cmds.colorManagementFileRules('ruleName', edit=True, extension='extension')
        cmds.colorManagementFileRules('ruleName', edit=True, colorSpace='colorSpace')
        cmds.colorManagementFileRules('ruleName', query=True, pattern=True)
        cmds.colorManagementFileRules('ruleName', query=True, extension=True)
        cmds.colorManagementFileRules('ruleName', query=True, colorSpace=True)
        cmds.colorManagementFileRules(save=True)
        cmds.colorManagementFileRules(load=True)
        # Return array of rule name strings.
        cmds.colorManagementFileRules(listRules=True)
        # Return input space corresponding to file path.
        cmds.colorManagementFileRules(evaluate=filePath)
    ```

    ---
    - Args:
        - colorSpace (cs): The input color space for the rule.  If the rule matches a file path, this is the color space that is returned.  This color space must match an existing color space in the input color space list.
        - colorSpaceDescription (csd): Returns the description for a specific color space.In query mode, this flag needs a value.
        - colorSpaceFamilies (csf): Returns the list of families for a specific color space. Used to add submenus when populating the color spaces UI popup of a rule.In query mode, this flag needs a value.
        - colorSpaceNames (csn): Returns the list of available color spaces. Used to populate the color spaces UI popup of a rule.
        - enabled (ena): Are the file rules enabled?
        - extension (ext): The file extension for the rule is case insensitive
        - pattern (pat): The file path pattern for the rule.  This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see
            http://en.wikipedia.org/wiki/Glob_%28programming%29.
        - query (q): Query mode flag
    """
@overload #Overload for colorManagementFileRules in ['query']
def colorManagementFileRules(colorSpace: str = ..., cs: str = ..., colorSpaceDescription: str = ..., csd: str = ..., colorSpaceFamilies: str = ..., csf: str = ..., colorSpaceNames: bool = ..., csn: bool = ..., enabled: bool = ..., ena: bool = ..., extension: str = ..., ext: str = ..., pattern: str = ..., pat: str = ..., query: bool = ..., q: bool = ...) -> None:
    """colorManagementFileRules is NOT undoable, queryable, and editable.
    
    This non-undoable action manages the list of rules that Maya uses to assign an
    initial input color space to dependency graph nodes that read in color
    information from a file. Rules are structured in a chain of responsibility,
    from highest priority rule to lowest priority rule, each rule matching a file
    path pattern and extension. If a rule matches a given file path, its color
    space is returned as the result of rules evaluation, and no further rule is
    considered. The lowest priority rule will always return a match. Rules can be
    added, removed, and changed in priority in the list. Each rule can have its
    file path pattern, extension, and color space changed. The rule list can be
    saved to user preferences, and loaded from user preferences.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.colorManagementFileRules(add='ruleName', pattern='filePattern', extension='extension', colorSpace='colorSpace')
        cmds.colorManagementFileRules(remove='ruleName')
        cmds.colorManagementFileRules(up='ruleName')
        cmds.colorManagementFileRules(down='ruleName')
        cmds.colorManagementFileRules('ruleName', edit=True, pattern='filePattern')
        cmds.colorManagementFileRules('ruleName', edit=True, extension='extension')
        cmds.colorManagementFileRules('ruleName', edit=True, colorSpace='colorSpace')
        cmds.colorManagementFileRules('ruleName', query=True, pattern=True)
        cmds.colorManagementFileRules('ruleName', query=True, extension=True)
        cmds.colorManagementFileRules('ruleName', query=True, colorSpace=True)
        cmds.colorManagementFileRules(save=True)
        cmds.colorManagementFileRules(load=True)
        # Return array of rule name strings.
        cmds.colorManagementFileRules(listRules=True)
        # Return input space corresponding to file path.
        cmds.colorManagementFileRules(evaluate=filePath)
    ```

    ---
    - Args:
        - colorSpace (cs): The input color space for the rule.  If the rule matches a file path, this is the color space that is returned.  This color space must match an existing color space in the input color space list.
        - colorSpaceDescription (csd): Returns the description for a specific color space.In query mode, this flag needs a value.
        - colorSpaceFamilies (csf): Returns the list of families for a specific color space. Used to add submenus when populating the color spaces UI popup of a rule.In query mode, this flag needs a value.
        - colorSpaceNames (csn): Returns the list of available color spaces. Used to populate the color spaces UI popup of a rule.
        - enabled (ena): Are the file rules enabled?
        - extension (ext): The file extension for the rule is case insensitive
        - pattern (pat): The file path pattern for the rule.  This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see
            http://en.wikipedia.org/wiki/Glob_%28programming%29.
        - query (q): Query mode flag
    """
@overload #Overload for colorManagementFileRules in ['edit']
def colorManagementFileRules(colorSpace: str = ..., extension: str = ..., pattern: str = ..., edit: bool = ...) -> None:
    """colorManagementFileRules is NOT undoable, queryable, and editable.
    
    This non-undoable action manages the list of rules that Maya uses to assign an
    initial input color space to dependency graph nodes that read in color
    information from a file. Rules are structured in a chain of responsibility,
    from highest priority rule to lowest priority rule, each rule matching a file
    path pattern and extension. If a rule matches a given file path, its color
    space is returned as the result of rules evaluation, and no further rule is
    considered. The lowest priority rule will always return a match. Rules can be
    added, removed, and changed in priority in the list. Each rule can have its
    file path pattern, extension, and color space changed. The rule list can be
    saved to user preferences, and loaded from user preferences.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.colorManagementFileRules(add='ruleName', pattern='filePattern', extension='extension', colorSpace='colorSpace')
        cmds.colorManagementFileRules(remove='ruleName')
        cmds.colorManagementFileRules(up='ruleName')
        cmds.colorManagementFileRules(down='ruleName')
        cmds.colorManagementFileRules('ruleName', edit=True, pattern='filePattern')
        cmds.colorManagementFileRules('ruleName', edit=True, extension='extension')
        cmds.colorManagementFileRules('ruleName', edit=True, colorSpace='colorSpace')
        cmds.colorManagementFileRules('ruleName', query=True, pattern=True)
        cmds.colorManagementFileRules('ruleName', query=True, extension=True)
        cmds.colorManagementFileRules('ruleName', query=True, colorSpace=True)
        cmds.colorManagementFileRules(save=True)
        cmds.colorManagementFileRules(load=True)
        # Return array of rule name strings.
        cmds.colorManagementFileRules(listRules=True)
        # Return input space corresponding to file path.
        cmds.colorManagementFileRules(evaluate=filePath)
    ```

    ---
    - Args:
        - colorSpace (cs): The input color space for the rule.  If the rule matches a file path, this is the color space that is returned.  This color space must match an existing color space in the input color space list.
        - extension (ext): The file extension for the rule is case insensitive
        - pattern (pat): The file path pattern for the rule.  This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see
            http://en.wikipedia.org/wiki/Glob_%28programming%29.
        - edit (e): Edit mode flag
    """
@overload #Overload for colorManagementFileRules in ['edit']
def colorManagementFileRules(cs: str = ..., ext: str = ..., pat: str = ..., e: bool = ...) -> None:
    """colorManagementFileRules is NOT undoable, queryable, and editable.
    
    This non-undoable action manages the list of rules that Maya uses to assign an
    initial input color space to dependency graph nodes that read in color
    information from a file. Rules are structured in a chain of responsibility,
    from highest priority rule to lowest priority rule, each rule matching a file
    path pattern and extension. If a rule matches a given file path, its color
    space is returned as the result of rules evaluation, and no further rule is
    considered. The lowest priority rule will always return a match. Rules can be
    added, removed, and changed in priority in the list. Each rule can have its
    file path pattern, extension, and color space changed. The rule list can be
    saved to user preferences, and loaded from user preferences.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.colorManagementFileRules(add='ruleName', pattern='filePattern', extension='extension', colorSpace='colorSpace')
        cmds.colorManagementFileRules(remove='ruleName')
        cmds.colorManagementFileRules(up='ruleName')
        cmds.colorManagementFileRules(down='ruleName')
        cmds.colorManagementFileRules('ruleName', edit=True, pattern='filePattern')
        cmds.colorManagementFileRules('ruleName', edit=True, extension='extension')
        cmds.colorManagementFileRules('ruleName', edit=True, colorSpace='colorSpace')
        cmds.colorManagementFileRules('ruleName', query=True, pattern=True)
        cmds.colorManagementFileRules('ruleName', query=True, extension=True)
        cmds.colorManagementFileRules('ruleName', query=True, colorSpace=True)
        cmds.colorManagementFileRules(save=True)
        cmds.colorManagementFileRules(load=True)
        # Return array of rule name strings.
        cmds.colorManagementFileRules(listRules=True)
        # Return input space corresponding to file path.
        cmds.colorManagementFileRules(evaluate=filePath)
    ```

    ---
    - Args:
        - colorSpace (cs): The input color space for the rule.  If the rule matches a file path, this is the color space that is returned.  This color space must match an existing color space in the input color space list.
        - extension (ext): The file extension for the rule is case insensitive
        - pattern (pat): The file path pattern for the rule.  This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see
            http://en.wikipedia.org/wiki/Glob_%28programming%29.
        - edit (e): Edit mode flag
    """
@overload #Overload for colorManagementFileRules in ['edit']
def colorManagementFileRules(colorSpace: str = ..., cs: str = ..., extension: str = ..., ext: str = ..., pattern: str = ..., pat: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """colorManagementFileRules is NOT undoable, queryable, and editable.
    
    This non-undoable action manages the list of rules that Maya uses to assign an
    initial input color space to dependency graph nodes that read in color
    information from a file. Rules are structured in a chain of responsibility,
    from highest priority rule to lowest priority rule, each rule matching a file
    path pattern and extension. If a rule matches a given file path, its color
    space is returned as the result of rules evaluation, and no further rule is
    considered. The lowest priority rule will always return a match. Rules can be
    added, removed, and changed in priority in the list. Each rule can have its
    file path pattern, extension, and color space changed. The rule list can be
    saved to user preferences, and loaded from user preferences.

    Example:
    ```python
        import maya.cmds as cmds
        import maya.cmds as cmds
        cmds.colorManagementFileRules(add='ruleName', pattern='filePattern', extension='extension', colorSpace='colorSpace')
        cmds.colorManagementFileRules(remove='ruleName')
        cmds.colorManagementFileRules(up='ruleName')
        cmds.colorManagementFileRules(down='ruleName')
        cmds.colorManagementFileRules('ruleName', edit=True, pattern='filePattern')
        cmds.colorManagementFileRules('ruleName', edit=True, extension='extension')
        cmds.colorManagementFileRules('ruleName', edit=True, colorSpace='colorSpace')
        cmds.colorManagementFileRules('ruleName', query=True, pattern=True)
        cmds.colorManagementFileRules('ruleName', query=True, extension=True)
        cmds.colorManagementFileRules('ruleName', query=True, colorSpace=True)
        cmds.colorManagementFileRules(save=True)
        cmds.colorManagementFileRules(load=True)
        # Return array of rule name strings.
        cmds.colorManagementFileRules(listRules=True)
        # Return input space corresponding to file path.
        cmds.colorManagementFileRules(evaluate=filePath)
    ```

    ---
    - Args:
        - colorSpace (cs): The input color space for the rule.  If the rule matches a file path, this is the color space that is returned.  This color space must match an existing color space in the input color space list.
        - extension (ext): The file extension for the rule is case insensitive
        - pattern (pat): The file path pattern for the rule.  This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see
            http://en.wikipedia.org/wiki/Glob_%28programming%29.
        - edit (e): Edit mode flag
    """
