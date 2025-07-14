"""Stub files for General category in Maya commands, command: sceneLint."""

from typing import Any, overload

@overload #Overload for sceneLint in ['create']
def sceneLint(issueType: str = ..., verbose: bool = ...) -> str | list[str] | list[str]:
    """sceneLint is NOT undoable, queryable, and NOT editable.
    
    { "sceneLint" : { "ISSUE_CODE" : { "description" :
    "DETAILED_DESCRIPTION_OF_ISSUE", "mitigation" : [ // List of mitigations that
    can be applied { "objects" : [
    LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit" :
    DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" :
    DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code" :
    PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }
    
    The sceneLint command is used to analyze the currently loaded scene to find
    potential areas for improvement in performance, memory use, or reduction of
    clutter.
    
    In the query mode it will report back the list of available checks it can do.
    Each check will have an associated short-form which can be passed to the
    command to run specific checks.
    
    In create mode the returned string is a JSON format list of issues and
    mitigations that suggest a way to solve the problem it describes.
    
    Mitigation can be automatically performed by extracting the mitigation code
    and arguments then running the Python code exec(code, {}, {'OBJECTS' :
    objects})

    ---
    - Args:
        - issueType (i): Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking.In query mode, this flag can accept a value.
        - verbose (v): If set then include both name and description when querying the list of available issue types.
    """
@overload #Overload for sceneLint in ['create']
def sceneLint(i: str = ..., v: bool = ...) -> str | list[str] | list[str]:
    """sceneLint is NOT undoable, queryable, and NOT editable.
    
    { "sceneLint" : { "ISSUE_CODE" : { "description" :
    "DETAILED_DESCRIPTION_OF_ISSUE", "mitigation" : [ // List of mitigations that
    can be applied { "objects" : [
    LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit" :
    DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" :
    DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code" :
    PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }
    
    The sceneLint command is used to analyze the currently loaded scene to find
    potential areas for improvement in performance, memory use, or reduction of
    clutter.
    
    In the query mode it will report back the list of available checks it can do.
    Each check will have an associated short-form which can be passed to the
    command to run specific checks.
    
    In create mode the returned string is a JSON format list of issues and
    mitigations that suggest a way to solve the problem it describes.
    
    Mitigation can be automatically performed by extracting the mitigation code
    and arguments then running the Python code exec(code, {}, {'OBJECTS' :
    objects})

    ---
    - Args:
        - issueType (i): Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking.In query mode, this flag can accept a value.
        - verbose (v): If set then include both name and description when querying the list of available issue types.
    """
@overload #Overload for sceneLint in ['create']
def sceneLint(issueType: str = ..., i: str = ..., verbose: bool = ..., v: bool = ...) -> str | list[str] | list[str]:
    """sceneLint is NOT undoable, queryable, and NOT editable.
    
    { "sceneLint" : { "ISSUE_CODE" : { "description" :
    "DETAILED_DESCRIPTION_OF_ISSUE", "mitigation" : [ // List of mitigations that
    can be applied { "objects" : [
    LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit" :
    DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" :
    DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code" :
    PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }
    
    The sceneLint command is used to analyze the currently loaded scene to find
    potential areas for improvement in performance, memory use, or reduction of
    clutter.
    
    In the query mode it will report back the list of available checks it can do.
    Each check will have an associated short-form which can be passed to the
    command to run specific checks.
    
    In create mode the returned string is a JSON format list of issues and
    mitigations that suggest a way to solve the problem it describes.
    
    Mitigation can be automatically performed by extracting the mitigation code
    and arguments then running the Python code exec(code, {}, {'OBJECTS' :
    objects})

    ---
    - Args:
        - issueType (i): Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking.In query mode, this flag can accept a value.
        - verbose (v): If set then include both name and description when querying the list of available issue types.
    """
@overload #Overload for sceneLint in ['query']
def sceneLint(issueType: str = ..., verbose: bool = ..., query: bool = ...) -> str | list[str] | list[str]:
    """sceneLint is NOT undoable, queryable, and NOT editable.
    
    { "sceneLint" : { "ISSUE_CODE" : { "description" :
    "DETAILED_DESCRIPTION_OF_ISSUE", "mitigation" : [ // List of mitigations that
    can be applied { "objects" : [
    LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit" :
    DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" :
    DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code" :
    PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }
    
    The sceneLint command is used to analyze the currently loaded scene to find
    potential areas for improvement in performance, memory use, or reduction of
    clutter.
    
    In the query mode it will report back the list of available checks it can do.
    Each check will have an associated short-form which can be passed to the
    command to run specific checks.
    
    In create mode the returned string is a JSON format list of issues and
    mitigations that suggest a way to solve the problem it describes.
    
    Mitigation can be automatically performed by extracting the mitigation code
    and arguments then running the Python code exec(code, {}, {'OBJECTS' :
    objects})

    ---
    - Args:
        - issueType (i): Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking.In query mode, this flag can accept a value.
        - verbose (v): If set then include both name and description when querying the list of available issue types.
        - query (q): Query mode flag
    """
@overload #Overload for sceneLint in ['query']
def sceneLint(i: str = ..., v: bool = ..., q: bool = ...) -> str | list[str] | list[str]:
    """sceneLint is NOT undoable, queryable, and NOT editable.
    
    { "sceneLint" : { "ISSUE_CODE" : { "description" :
    "DETAILED_DESCRIPTION_OF_ISSUE", "mitigation" : [ // List of mitigations that
    can be applied { "objects" : [
    LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit" :
    DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" :
    DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code" :
    PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }
    
    The sceneLint command is used to analyze the currently loaded scene to find
    potential areas for improvement in performance, memory use, or reduction of
    clutter.
    
    In the query mode it will report back the list of available checks it can do.
    Each check will have an associated short-form which can be passed to the
    command to run specific checks.
    
    In create mode the returned string is a JSON format list of issues and
    mitigations that suggest a way to solve the problem it describes.
    
    Mitigation can be automatically performed by extracting the mitigation code
    and arguments then running the Python code exec(code, {}, {'OBJECTS' :
    objects})

    ---
    - Args:
        - issueType (i): Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking.In query mode, this flag can accept a value.
        - verbose (v): If set then include both name and description when querying the list of available issue types.
        - query (q): Query mode flag
    """
@overload #Overload for sceneLint in ['query']
def sceneLint(issueType: str = ..., i: str = ..., verbose: bool = ..., v: bool = ..., query: bool = ..., q: bool = ...) -> str | list[str] | list[str]:
    """sceneLint is NOT undoable, queryable, and NOT editable.
    
    { "sceneLint" : { "ISSUE_CODE" : { "description" :
    "DETAILED_DESCRIPTION_OF_ISSUE", "mitigation" : [ // List of mitigations that
    can be applied { "objects" : [
    LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit" :
    DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" :
    DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code" :
    PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }
    
    The sceneLint command is used to analyze the currently loaded scene to find
    potential areas for improvement in performance, memory use, or reduction of
    clutter.
    
    In the query mode it will report back the list of available checks it can do.
    Each check will have an associated short-form which can be passed to the
    command to run specific checks.
    
    In create mode the returned string is a JSON format list of issues and
    mitigations that suggest a way to solve the problem it describes.
    
    Mitigation can be automatically performed by extracting the mitigation code
    and arguments then running the Python code exec(code, {}, {'OBJECTS' :
    objects})

    ---
    - Args:
        - issueType (i): Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking.In query mode, this flag can accept a value.
        - verbose (v): If set then include both name and description when querying the list of available issue types.
        - query (q): Query mode flag
    """
@overload #Overload for sceneLint in ['edit']
def sceneLint(issueType: str = ..., verbose: bool = ..., edit: bool = ...) -> str | list[str] | list[str]:
    """sceneLint is NOT undoable, queryable, and NOT editable.
    
    { "sceneLint" : { "ISSUE_CODE" : { "description" :
    "DETAILED_DESCRIPTION_OF_ISSUE", "mitigation" : [ // List of mitigations that
    can be applied { "objects" : [
    LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit" :
    DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" :
    DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code" :
    PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }
    
    The sceneLint command is used to analyze the currently loaded scene to find
    potential areas for improvement in performance, memory use, or reduction of
    clutter.
    
    In the query mode it will report back the list of available checks it can do.
    Each check will have an associated short-form which can be passed to the
    command to run specific checks.
    
    In create mode the returned string is a JSON format list of issues and
    mitigations that suggest a way to solve the problem it describes.
    
    Mitigation can be automatically performed by extracting the mitigation code
    and arguments then running the Python code exec(code, {}, {'OBJECTS' :
    objects})

    ---
    - Args:
        - issueType (i): Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking.In query mode, this flag can accept a value.
        - verbose (v): If set then include both name and description when querying the list of available issue types.
        - edit (e): Edit mode flag
    """
@overload #Overload for sceneLint in ['edit']
def sceneLint(i: str = ..., v: bool = ..., e: bool = ...) -> str | list[str] | list[str]:
    """sceneLint is NOT undoable, queryable, and NOT editable.
    
    { "sceneLint" : { "ISSUE_CODE" : { "description" :
    "DETAILED_DESCRIPTION_OF_ISSUE", "mitigation" : [ // List of mitigations that
    can be applied { "objects" : [
    LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit" :
    DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" :
    DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code" :
    PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }
    
    The sceneLint command is used to analyze the currently loaded scene to find
    potential areas for improvement in performance, memory use, or reduction of
    clutter.
    
    In the query mode it will report back the list of available checks it can do.
    Each check will have an associated short-form which can be passed to the
    command to run specific checks.
    
    In create mode the returned string is a JSON format list of issues and
    mitigations that suggest a way to solve the problem it describes.
    
    Mitigation can be automatically performed by extracting the mitigation code
    and arguments then running the Python code exec(code, {}, {'OBJECTS' :
    objects})

    ---
    - Args:
        - issueType (i): Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking.In query mode, this flag can accept a value.
        - verbose (v): If set then include both name and description when querying the list of available issue types.
        - edit (e): Edit mode flag
    """
@overload #Overload for sceneLint in ['edit']
def sceneLint(issueType: str = ..., i: str = ..., verbose: bool = ..., v: bool = ..., edit: bool = ..., e: bool = ...) -> str | list[str] | list[str]:
    """sceneLint is NOT undoable, queryable, and NOT editable.
    
    { "sceneLint" : { "ISSUE_CODE" : { "description" :
    "DETAILED_DESCRIPTION_OF_ISSUE", "mitigation" : [ // List of mitigations that
    can be applied { "objects" : [
    LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit" :
    DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" :
    DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code" :
    PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }
    
    The sceneLint command is used to analyze the currently loaded scene to find
    potential areas for improvement in performance, memory use, or reduction of
    clutter.
    
    In the query mode it will report back the list of available checks it can do.
    Each check will have an associated short-form which can be passed to the
    command to run specific checks.
    
    In create mode the returned string is a JSON format list of issues and
    mitigations that suggest a way to solve the problem it describes.
    
    Mitigation can be automatically performed by extracting the mitigation code
    and arguments then running the Python code exec(code, {}, {'OBJECTS' :
    objects})

    ---
    - Args:
        - issueType (i): Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking.In query mode, this flag can accept a value.
        - verbose (v): If set then include both name and description when querying the list of available issue types.
        - edit (e): Edit mode flag
    """
