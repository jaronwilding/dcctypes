"""Stub files for General category in Maya commands, command: editDisplayLayerGlobals."""

from typing import Any, overload

@overload #Overload for editDisplayLayerGlobals in ['create']
def editDisplayLayerGlobals(baseId: int = ..., currentDisplayLayer: name = ..., mergeType: int = ..., useCurrent: bool = ...) -> bool | str | int | int:
    """editDisplayLayerGlobals is undoable, queryable, and NOT editable.
    
    Edit the parameter values common to all display layers. Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and some, eg.
    currentDisplayLayer, are stored in the file.

    ---
    - Args:
        - baseId (bi): Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        - currentDisplayLayer (cdl): Set current display layer; ie. the one that all new objects are added to.
        - mergeType (mt): Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        - useCurrent (uc): Set whether or not to enable usage of the current display layer as the destination for all new nodes.
    """
@overload #Overload for editDisplayLayerGlobals in ['create']
def editDisplayLayerGlobals(bi: int = ..., cdl: name = ..., mt: int = ..., uc: bool = ...) -> bool | str | int | int:
    """editDisplayLayerGlobals is undoable, queryable, and NOT editable.
    
    Edit the parameter values common to all display layers. Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and some, eg.
    currentDisplayLayer, are stored in the file.

    ---
    - Args:
        - baseId (bi): Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        - currentDisplayLayer (cdl): Set current display layer; ie. the one that all new objects are added to.
        - mergeType (mt): Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        - useCurrent (uc): Set whether or not to enable usage of the current display layer as the destination for all new nodes.
    """
@overload #Overload for editDisplayLayerGlobals in ['create']
def editDisplayLayerGlobals(baseId: int = ..., bi: int = ..., currentDisplayLayer: name = ..., cdl: name = ..., mergeType: int = ..., mt: int = ..., useCurrent: bool = ..., uc: bool = ...) -> bool | str | int | int:
    """editDisplayLayerGlobals is undoable, queryable, and NOT editable.
    
    Edit the parameter values common to all display layers. Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and some, eg.
    currentDisplayLayer, are stored in the file.

    ---
    - Args:
        - baseId (bi): Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        - currentDisplayLayer (cdl): Set current display layer; ie. the one that all new objects are added to.
        - mergeType (mt): Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        - useCurrent (uc): Set whether or not to enable usage of the current display layer as the destination for all new nodes.
    """
@overload #Overload for editDisplayLayerGlobals in ['query']
def editDisplayLayerGlobals(baseId: int = ..., currentDisplayLayer: name = ..., mergeType: int = ..., useCurrent: bool = ..., query: bool = ...) -> bool | str | int | int:
    """editDisplayLayerGlobals is undoable, queryable, and NOT editable.
    
    Edit the parameter values common to all display layers. Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and some, eg.
    currentDisplayLayer, are stored in the file.

    ---
    - Args:
        - baseId (bi): Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        - currentDisplayLayer (cdl): Set current display layer; ie. the one that all new objects are added to.
        - mergeType (mt): Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        - useCurrent (uc): Set whether or not to enable usage of the current display layer as the destination for all new nodes.
        - query (q): Query mode flag
    """
@overload #Overload for editDisplayLayerGlobals in ['query']
def editDisplayLayerGlobals(bi: int = ..., cdl: name = ..., mt: int = ..., uc: bool = ..., q: bool = ...) -> bool | str | int | int:
    """editDisplayLayerGlobals is undoable, queryable, and NOT editable.
    
    Edit the parameter values common to all display layers. Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and some, eg.
    currentDisplayLayer, are stored in the file.

    ---
    - Args:
        - baseId (bi): Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        - currentDisplayLayer (cdl): Set current display layer; ie. the one that all new objects are added to.
        - mergeType (mt): Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        - useCurrent (uc): Set whether or not to enable usage of the current display layer as the destination for all new nodes.
        - query (q): Query mode flag
    """
@overload #Overload for editDisplayLayerGlobals in ['query']
def editDisplayLayerGlobals(baseId: int = ..., bi: int = ..., currentDisplayLayer: name = ..., cdl: name = ..., mergeType: int = ..., mt: int = ..., useCurrent: bool = ..., uc: bool = ..., query: bool = ..., q: bool = ...) -> bool | str | int | int:
    """editDisplayLayerGlobals is undoable, queryable, and NOT editable.
    
    Edit the parameter values common to all display layers. Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and some, eg.
    currentDisplayLayer, are stored in the file.

    ---
    - Args:
        - baseId (bi): Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        - currentDisplayLayer (cdl): Set current display layer; ie. the one that all new objects are added to.
        - mergeType (mt): Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        - useCurrent (uc): Set whether or not to enable usage of the current display layer as the destination for all new nodes.
        - query (q): Query mode flag
    """
@overload #Overload for editDisplayLayerGlobals in ['edit']
def editDisplayLayerGlobals(baseId: int = ..., currentDisplayLayer: name = ..., mergeType: int = ..., useCurrent: bool = ..., edit: bool = ...) -> bool | str | int | int:
    """editDisplayLayerGlobals is undoable, queryable, and NOT editable.
    
    Edit the parameter values common to all display layers. Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and some, eg.
    currentDisplayLayer, are stored in the file.

    ---
    - Args:
        - baseId (bi): Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        - currentDisplayLayer (cdl): Set current display layer; ie. the one that all new objects are added to.
        - mergeType (mt): Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        - useCurrent (uc): Set whether or not to enable usage of the current display layer as the destination for all new nodes.
        - edit (e): Edit mode flag
    """
@overload #Overload for editDisplayLayerGlobals in ['edit']
def editDisplayLayerGlobals(bi: int = ..., cdl: name = ..., mt: int = ..., uc: bool = ..., e: bool = ...) -> bool | str | int | int:
    """editDisplayLayerGlobals is undoable, queryable, and NOT editable.
    
    Edit the parameter values common to all display layers. Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and some, eg.
    currentDisplayLayer, are stored in the file.

    ---
    - Args:
        - baseId (bi): Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        - currentDisplayLayer (cdl): Set current display layer; ie. the one that all new objects are added to.
        - mergeType (mt): Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        - useCurrent (uc): Set whether or not to enable usage of the current display layer as the destination for all new nodes.
        - edit (e): Edit mode flag
    """
@overload #Overload for editDisplayLayerGlobals in ['edit']
def editDisplayLayerGlobals(baseId: int = ..., bi: int = ..., currentDisplayLayer: name = ..., cdl: name = ..., mergeType: int = ..., mt: int = ..., useCurrent: bool = ..., uc: bool = ..., edit: bool = ..., e: bool = ...) -> bool | str | int | int:
    """editDisplayLayerGlobals is undoable, queryable, and NOT editable.
    
    Edit the parameter values common to all display layers. Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and some, eg.
    currentDisplayLayer, are stored in the file.

    ---
    - Args:
        - baseId (bi): Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        - currentDisplayLayer (cdl): Set current display layer; ie. the one that all new objects are added to.
        - mergeType (mt): Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        - useCurrent (uc): Set whether or not to enable usage of the current display layer as the destination for all new nodes.
        - edit (e): Edit mode flag
    """
