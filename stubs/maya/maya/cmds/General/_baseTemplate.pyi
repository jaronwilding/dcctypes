"""Stub files for General category in Maya commands, command: baseTemplate."""

from typing import Any, overload

@overload #Overload for baseTemplate in ['create']
def baseTemplate([string]: [string], fileName: str = ..., force: bool = ..., silent: bool = ..., unload: bool = ..., viewList: str = ...) -> None:
    """baseTemplate is NOT undoable, queryable, and editable.
    
    This is the class for the commands that edit and/or query templates.

    Example:
    ```python
        import maya.cmds as cmds
        #    Determine if template exists
        #
        cmds.baseTemplate ('foo.xml', exists=True)
        #
    ```

    ---
    - Args:
        - [string]: Input item(s).
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - force (f): This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file.  When used in create mode, it will allow an
            existing template to be recreated (for example when using fromContainer argument to regenerate a template).
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - unload (u): Unload the specified template.  This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
    """
@overload #Overload for baseTemplate in ['create']
def baseTemplate([string]: [string], fn: str = ..., f: bool = ..., si: bool = ..., u: bool = ..., vl: str = ...) -> None:
    """baseTemplate is NOT undoable, queryable, and editable.
    
    This is the class for the commands that edit and/or query templates.

    Example:
    ```python
        import maya.cmds as cmds
        #    Determine if template exists
        #
        cmds.baseTemplate ('foo.xml', exists=True)
        #
    ```

    ---
    - Args:
        - [string]: Input item(s).
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - force (f): This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file.  When used in create mode, it will allow an
            existing template to be recreated (for example when using fromContainer argument to regenerate a template).
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - unload (u): Unload the specified template.  This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
    """
@overload #Overload for baseTemplate in ['create']
def baseTemplate([string]: [string], fileName: str = ..., fn: str = ..., force: bool = ..., f: bool = ..., silent: bool = ..., si: bool = ..., unload: bool = ..., u: bool = ..., viewList: str = ..., vl: str = ...) -> None:
    """baseTemplate is NOT undoable, queryable, and editable.
    
    This is the class for the commands that edit and/or query templates.

    Example:
    ```python
        import maya.cmds as cmds
        #    Determine if template exists
        #
        cmds.baseTemplate ('foo.xml', exists=True)
        #
    ```

    ---
    - Args:
        - [string]: Input item(s).
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - force (f): This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file.  When used in create mode, it will allow an
            existing template to be recreated (for example when using fromContainer argument to regenerate a template).
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - unload (u): Unload the specified template.  This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
    """
@overload #Overload for baseTemplate in ['query']
def baseTemplate([string]: [string], exists: bool = ..., fileName: str = ..., matchFile: str = ..., silent: bool = ..., viewList: str = ..., query: bool = ...) -> None:
    """baseTemplate is NOT undoable, queryable, and editable.
    
    This is the class for the commands that edit and/or query templates.

    Example:
    ```python
        import maya.cmds as cmds
        #    Determine if template exists
        #
        cmds.baseTemplate ('foo.xml', exists=True)
        #
    ```

    ---
    - Args:
        - [string]: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - matchFile (mf): Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation.In query mode, this flag needs a value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
        - query (q): Query mode flag
    """
@overload #Overload for baseTemplate in ['query']
def baseTemplate([string]: [string], ex: bool = ..., fn: str = ..., mf: str = ..., si: bool = ..., vl: str = ..., q: bool = ...) -> None:
    """baseTemplate is NOT undoable, queryable, and editable.
    
    This is the class for the commands that edit and/or query templates.

    Example:
    ```python
        import maya.cmds as cmds
        #    Determine if template exists
        #
        cmds.baseTemplate ('foo.xml', exists=True)
        #
    ```

    ---
    - Args:
        - [string]: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - matchFile (mf): Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation.In query mode, this flag needs a value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
        - query (q): Query mode flag
    """
@overload #Overload for baseTemplate in ['query']
def baseTemplate([string]: [string], exists: bool = ..., ex: bool = ..., fileName: str = ..., fn: str = ..., matchFile: str = ..., mf: str = ..., silent: bool = ..., si: bool = ..., viewList: str = ..., vl: str = ..., query: bool = ..., q: bool = ...) -> None:
    """baseTemplate is NOT undoable, queryable, and editable.
    
    This is the class for the commands that edit and/or query templates.

    Example:
    ```python
        import maya.cmds as cmds
        #    Determine if template exists
        #
        cmds.baseTemplate ('foo.xml', exists=True)
        #
    ```

    ---
    - Args:
        - [string]: Input item(s).
        - exists (ex): Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.
        - fileName (fn): Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is
            recommended but not required that the filename and template name correspond.
        - matchFile (mf): Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation.In query mode, this flag needs a value.
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - viewList (vl): Used in query mode, returns a list of all views defined on the template.
        - query (q): Query mode flag
    """
@overload #Overload for baseTemplate in ['edit']
def baseTemplate([string]: [string], silent: bool = ..., edit: bool = ...) -> None:
    """baseTemplate is NOT undoable, queryable, and editable.
    
    This is the class for the commands that edit and/or query templates.

    Example:
    ```python
        import maya.cmds as cmds
        #    Determine if template exists
        #
        cmds.baseTemplate ('foo.xml', exists=True)
        #
    ```

    ---
    - Args:
        - [string]: Input item(s).
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - edit (e): Edit mode flag
    """
@overload #Overload for baseTemplate in ['edit']
def baseTemplate([string]: [string], si: bool = ..., e: bool = ...) -> None:
    """baseTemplate is NOT undoable, queryable, and editable.
    
    This is the class for the commands that edit and/or query templates.

    Example:
    ```python
        import maya.cmds as cmds
        #    Determine if template exists
        #
        cmds.baseTemplate ('foo.xml', exists=True)
        #
    ```

    ---
    - Args:
        - [string]: Input item(s).
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - edit (e): Edit mode flag
    """
@overload #Overload for baseTemplate in ['edit']
def baseTemplate([string]: [string], silent: bool = ..., si: bool = ..., edit: bool = ..., e: bool = ...) -> None:
    """baseTemplate is NOT undoable, queryable, and editable.
    
    This is the class for the commands that edit and/or query templates.

    Example:
    ```python
        import maya.cmds as cmds
        #    Determine if template exists
        #
        cmds.baseTemplate ('foo.xml', exists=True)
        #
    ```

    ---
    - Args:
        - [string]: Input item(s).
        - silent (si): Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        - edit (e): Edit mode flag
    """
