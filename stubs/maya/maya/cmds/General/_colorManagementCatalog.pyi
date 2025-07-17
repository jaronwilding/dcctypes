"""Stub files for General category in Maya commands, command: colorManagementCatalog."""

from typing import Any, overload

@overload #Overload for colorManagementCatalog in ['create']
def colorManagementCatalog(addTransform: str = ..., editUserTransformPath: str = ..., listSupportedExtensions: bool = ..., listTransformConnections: bool = ..., path: str = ..., queryUserTransformPath: bool = ..., removeTransform: str = ..., transformConnection: str = ..., type: str = ...) -> None:
    """colorManagementCatalog is NOT undoable, NOT queryable, and NOT editable.
    
    This non-undoable action performs additions and removals of custom color
    transforms from the Autodesk native color transform catalog. Once a custom
    color transform has been added to the catalog, it can be used in the same way
    as the builtin Autodesk native color transforms.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.colorManagementCatalog(addTransform='My Custom Viewing LUT', type='view', path='/path/to/myCustomViewingLUT.lut', transformConnection='ACES')
        cmds.colorManagementCatalog(removeTransform='My Custom Viewing LUT', type='view')
        cmds.colorManagementCatalog(listTransformConnections=True, type='view')
        cmds.colorManagementCatalog(editUserTransformPath='/path/transforms')
    ```

    ---
    - Args:
        - addTransform (adt): Add transform to collection.
        - editUserTransformPath (eut): Edit the user transform directory. By changing the directory, all custom transforms currently added could be changed, and new ones could appear.
        - listSupportedExtensions (lse): List the file extensions that are supported by add transform.  This list is valid for all transform types, and therefore this flag does not require use of the type flag.
        - listTransformConnections (ltc): List the transforms that can be used as source (for "view" and "output" types) or destination (for "input" and "rendering space" types) to connect a custom transform to the rest of the transform collection.
        - path (pth): In addTransform mode, the path to the transform data file.
        - queryUserTransformPath (qut): Query the user transform directory.
        - removeTransform (rmt): Remove transform from collection.
        - transformConnection (tcn): In addTransform mode, an existing transform to which the added transform will be connected. For an input transform or rendering space transform, this will be a destination. For a view or output transform, this will be a source.
        - type (typ): The type of transform added, removed, or whose transform connections are to be listed. Must be one of "view", "rendering space", "input", or "output".
    """
@overload #Overload for colorManagementCatalog in ['create']
def colorManagementCatalog(adt: str = ..., eut: str = ..., lse: bool = ..., ltc: bool = ..., pth: str = ..., qut: bool = ..., rmt: str = ..., tcn: str = ..., typ: str = ...) -> None:
    """colorManagementCatalog is NOT undoable, NOT queryable, and NOT editable.
    
    This non-undoable action performs additions and removals of custom color
    transforms from the Autodesk native color transform catalog. Once a custom
    color transform has been added to the catalog, it can be used in the same way
    as the builtin Autodesk native color transforms.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.colorManagementCatalog(addTransform='My Custom Viewing LUT', type='view', path='/path/to/myCustomViewingLUT.lut', transformConnection='ACES')
        cmds.colorManagementCatalog(removeTransform='My Custom Viewing LUT', type='view')
        cmds.colorManagementCatalog(listTransformConnections=True, type='view')
        cmds.colorManagementCatalog(editUserTransformPath='/path/transforms')
    ```

    ---
    - Args:
        - addTransform (adt): Add transform to collection.
        - editUserTransformPath (eut): Edit the user transform directory. By changing the directory, all custom transforms currently added could be changed, and new ones could appear.
        - listSupportedExtensions (lse): List the file extensions that are supported by add transform.  This list is valid for all transform types, and therefore this flag does not require use of the type flag.
        - listTransformConnections (ltc): List the transforms that can be used as source (for "view" and "output" types) or destination (for "input" and "rendering space" types) to connect a custom transform to the rest of the transform collection.
        - path (pth): In addTransform mode, the path to the transform data file.
        - queryUserTransformPath (qut): Query the user transform directory.
        - removeTransform (rmt): Remove transform from collection.
        - transformConnection (tcn): In addTransform mode, an existing transform to which the added transform will be connected. For an input transform or rendering space transform, this will be a destination. For a view or output transform, this will be a source.
        - type (typ): The type of transform added, removed, or whose transform connections are to be listed. Must be one of "view", "rendering space", "input", or "output".
    """
@overload #Overload for colorManagementCatalog in ['create']
def colorManagementCatalog(addTransform: str = ..., adt: str = ..., editUserTransformPath: str = ..., eut: str = ..., listSupportedExtensions: bool = ..., lse: bool = ..., listTransformConnections: bool = ..., ltc: bool = ..., path: str = ..., pth: str = ..., queryUserTransformPath: bool = ..., qut: bool = ..., removeTransform: str = ..., rmt: str = ..., transformConnection: str = ..., tcn: str = ..., type: str = ..., typ: str = ...) -> None:
    """colorManagementCatalog is NOT undoable, NOT queryable, and NOT editable.
    
    This non-undoable action performs additions and removals of custom color
    transforms from the Autodesk native color transform catalog. Once a custom
    color transform has been added to the catalog, it can be used in the same way
    as the builtin Autodesk native color transforms.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.colorManagementCatalog(addTransform='My Custom Viewing LUT', type='view', path='/path/to/myCustomViewingLUT.lut', transformConnection='ACES')
        cmds.colorManagementCatalog(removeTransform='My Custom Viewing LUT', type='view')
        cmds.colorManagementCatalog(listTransformConnections=True, type='view')
        cmds.colorManagementCatalog(editUserTransformPath='/path/transforms')
    ```

    ---
    - Args:
        - addTransform (adt): Add transform to collection.
        - editUserTransformPath (eut): Edit the user transform directory. By changing the directory, all custom transforms currently added could be changed, and new ones could appear.
        - listSupportedExtensions (lse): List the file extensions that are supported by add transform.  This list is valid for all transform types, and therefore this flag does not require use of the type flag.
        - listTransformConnections (ltc): List the transforms that can be used as source (for "view" and "output" types) or destination (for "input" and "rendering space" types) to connect a custom transform to the rest of the transform collection.
        - path (pth): In addTransform mode, the path to the transform data file.
        - queryUserTransformPath (qut): Query the user transform directory.
        - removeTransform (rmt): Remove transform from collection.
        - transformConnection (tcn): In addTransform mode, an existing transform to which the added transform will be connected. For an input transform or rendering space transform, this will be a destination. For a view or output transform, this will be a source.
        - type (typ): The type of transform added, removed, or whose transform connections are to be listed. Must be one of "view", "rendering space", "input", or "output".
    """
