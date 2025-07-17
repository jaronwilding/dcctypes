"""Stub files for General category in Maya commands, command: makePaintable."""

from typing import Any, overload

@overload #Overload for makePaintable in ['create']
def makePaintable([string][string]: [string][string], activate: bool = ..., activateAll: bool = ..., altAttribute: str = ..., attrType: str = ..., clearAll: bool = ..., remove: bool = ..., shapeMode: str = ..., uiName: str = ...) -> None:
    """makePaintable is NOT undoable, queryable, and NOT editable.
    
    Make attributes of nodes paintable to Attribute Paint Tool. This command is
    used to register new attributes to the Attribute Paint tool as paintable. Once
    registered the attributes will be recognized by the Attribute Paint tool and
    the user will be able to paint them.

    Example:
    ```python
        import maya.cmds as cmds
        # Make particle.mass paintable.
        cmds.makePaintable( 'particle', 'mass', attrType='doubleArray' )
        # Make particle.goalPP paintable, with a ui name myGoalPP.
        # Also make the goalPP0 attribute painted simultaneously
        cmds.makePaintable( 'particle', 'goalPP', attrType='doubleArray', ui='myGoalPP', altAttribute='goalPP0' )
        # Make weightGeometryFilter.weights paintable. Define
        # weightGeometryFilter as a deformer node.
        cmds.makePaintable( 'weightGeometryFilter', 'weights', attrType='multiFloat', sm='deformer' )
        # Make all the attributes paintable on the artAttrPaintTest node.
        cmds.makePaintable( 'artAttrPaintTest', 'intArray', attrType='intArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblArray', attrType='doubleArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'vecArray', attrType='vectorArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'intMulti', attrType='multiInteger' )
        cmds.makePaintable( 'artAttrPaintTest', 'fltMulti', attrType='multiFloat' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblMulti', attrType='multiDouble' )
        cmds.makePaintable( 'artAttrPaintTest', 'flt3Multi', attrType='multiVector' )
        cmds.makePaintable( 'artAttrPaintTest', 'dbl3Multi', attrType='multiVector' )
    ```

    ---
    - Args:
        - [string][string]: Input item(s).
        - activate (ac): Activate / deactivate the given paintable attribute. Used to filter out some nodes in the attribute paint tool.
        - activateAll (aca): Activate / deactivate all the registered paintable attributes. Used to filter out some nodes in the attribute paint tool.
        - altAttribute (aa): Define an alternate attribute which will also receive the same values. There can be multiple such flags.
        - attrType (at): Paintable attribute type. Supported types: intArray, doubleArray, vectorArray, multiInteger, multiFloat, multiDouble, multiVector.
        - clearAll (ca): Removes all paintable attribute definitions.
        - remove (rm): Make the attribute not paintable any more.
        - shapeMode (sm): This flag controls how Artisan correlates the paintable node to a corresponding shape node.  It is used for attributes of type multi of multi, where the first multi dimension corresponds to the shape index (i.e. cluster nodes). At present,
            only one value of this flag is supported: "deformer". By default this flag is an empty string, which means that there is a direct indexing (no special mapping required) of the attribute with respect to vertices on the shape.
        - uiName (ui): UI name. Default is the attribute name.
    """
@overload #Overload for makePaintable in ['create']
def makePaintable([string][string]: [string][string], ac: bool = ..., aca: bool = ..., aa: str = ..., at: str = ..., ca: bool = ..., rm: bool = ..., sm: str = ..., ui: str = ...) -> None:
    """makePaintable is NOT undoable, queryable, and NOT editable.
    
    Make attributes of nodes paintable to Attribute Paint Tool. This command is
    used to register new attributes to the Attribute Paint tool as paintable. Once
    registered the attributes will be recognized by the Attribute Paint tool and
    the user will be able to paint them.

    Example:
    ```python
        import maya.cmds as cmds
        # Make particle.mass paintable.
        cmds.makePaintable( 'particle', 'mass', attrType='doubleArray' )
        # Make particle.goalPP paintable, with a ui name myGoalPP.
        # Also make the goalPP0 attribute painted simultaneously
        cmds.makePaintable( 'particle', 'goalPP', attrType='doubleArray', ui='myGoalPP', altAttribute='goalPP0' )
        # Make weightGeometryFilter.weights paintable. Define
        # weightGeometryFilter as a deformer node.
        cmds.makePaintable( 'weightGeometryFilter', 'weights', attrType='multiFloat', sm='deformer' )
        # Make all the attributes paintable on the artAttrPaintTest node.
        cmds.makePaintable( 'artAttrPaintTest', 'intArray', attrType='intArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblArray', attrType='doubleArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'vecArray', attrType='vectorArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'intMulti', attrType='multiInteger' )
        cmds.makePaintable( 'artAttrPaintTest', 'fltMulti', attrType='multiFloat' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblMulti', attrType='multiDouble' )
        cmds.makePaintable( 'artAttrPaintTest', 'flt3Multi', attrType='multiVector' )
        cmds.makePaintable( 'artAttrPaintTest', 'dbl3Multi', attrType='multiVector' )
    ```

    ---
    - Args:
        - [string][string]: Input item(s).
        - activate (ac): Activate / deactivate the given paintable attribute. Used to filter out some nodes in the attribute paint tool.
        - activateAll (aca): Activate / deactivate all the registered paintable attributes. Used to filter out some nodes in the attribute paint tool.
        - altAttribute (aa): Define an alternate attribute which will also receive the same values. There can be multiple such flags.
        - attrType (at): Paintable attribute type. Supported types: intArray, doubleArray, vectorArray, multiInteger, multiFloat, multiDouble, multiVector.
        - clearAll (ca): Removes all paintable attribute definitions.
        - remove (rm): Make the attribute not paintable any more.
        - shapeMode (sm): This flag controls how Artisan correlates the paintable node to a corresponding shape node.  It is used for attributes of type multi of multi, where the first multi dimension corresponds to the shape index (i.e. cluster nodes). At present,
            only one value of this flag is supported: "deformer". By default this flag is an empty string, which means that there is a direct indexing (no special mapping required) of the attribute with respect to vertices on the shape.
        - uiName (ui): UI name. Default is the attribute name.
    """
@overload #Overload for makePaintable in ['create']
def makePaintable([string][string]: [string][string], activate: bool = ..., ac: bool = ..., activateAll: bool = ..., aca: bool = ..., altAttribute: str = ..., aa: str = ..., attrType: str = ..., at: str = ..., clearAll: bool = ..., ca: bool = ..., remove: bool = ..., rm: bool = ..., shapeMode: str = ..., sm: str = ..., uiName: str = ..., ui: str = ...) -> None:
    """makePaintable is NOT undoable, queryable, and NOT editable.
    
    Make attributes of nodes paintable to Attribute Paint Tool. This command is
    used to register new attributes to the Attribute Paint tool as paintable. Once
    registered the attributes will be recognized by the Attribute Paint tool and
    the user will be able to paint them.

    Example:
    ```python
        import maya.cmds as cmds
        # Make particle.mass paintable.
        cmds.makePaintable( 'particle', 'mass', attrType='doubleArray' )
        # Make particle.goalPP paintable, with a ui name myGoalPP.
        # Also make the goalPP0 attribute painted simultaneously
        cmds.makePaintable( 'particle', 'goalPP', attrType='doubleArray', ui='myGoalPP', altAttribute='goalPP0' )
        # Make weightGeometryFilter.weights paintable. Define
        # weightGeometryFilter as a deformer node.
        cmds.makePaintable( 'weightGeometryFilter', 'weights', attrType='multiFloat', sm='deformer' )
        # Make all the attributes paintable on the artAttrPaintTest node.
        cmds.makePaintable( 'artAttrPaintTest', 'intArray', attrType='intArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblArray', attrType='doubleArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'vecArray', attrType='vectorArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'intMulti', attrType='multiInteger' )
        cmds.makePaintable( 'artAttrPaintTest', 'fltMulti', attrType='multiFloat' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblMulti', attrType='multiDouble' )
        cmds.makePaintable( 'artAttrPaintTest', 'flt3Multi', attrType='multiVector' )
        cmds.makePaintable( 'artAttrPaintTest', 'dbl3Multi', attrType='multiVector' )
    ```

    ---
    - Args:
        - [string][string]: Input item(s).
        - activate (ac): Activate / deactivate the given paintable attribute. Used to filter out some nodes in the attribute paint tool.
        - activateAll (aca): Activate / deactivate all the registered paintable attributes. Used to filter out some nodes in the attribute paint tool.
        - altAttribute (aa): Define an alternate attribute which will also receive the same values. There can be multiple such flags.
        - attrType (at): Paintable attribute type. Supported types: intArray, doubleArray, vectorArray, multiInteger, multiFloat, multiDouble, multiVector.
        - clearAll (ca): Removes all paintable attribute definitions.
        - remove (rm): Make the attribute not paintable any more.
        - shapeMode (sm): This flag controls how Artisan correlates the paintable node to a corresponding shape node.  It is used for attributes of type multi of multi, where the first multi dimension corresponds to the shape index (i.e. cluster nodes). At present,
            only one value of this flag is supported: "deformer". By default this flag is an empty string, which means that there is a direct indexing (no special mapping required) of the attribute with respect to vertices on the shape.
        - uiName (ui): UI name. Default is the attribute name.
    """
@overload #Overload for makePaintable in ['query']
def makePaintable([string][string]: [string][string], activate: bool = ..., activateAll: bool = ..., altAttribute: str = ..., attrType: str = ..., clearAll: bool = ..., remove: bool = ..., shapeMode: str = ..., uiName: str = ..., query: bool = ...) -> None:
    """makePaintable is NOT undoable, queryable, and NOT editable.
    
    Make attributes of nodes paintable to Attribute Paint Tool. This command is
    used to register new attributes to the Attribute Paint tool as paintable. Once
    registered the attributes will be recognized by the Attribute Paint tool and
    the user will be able to paint them.

    Example:
    ```python
        import maya.cmds as cmds
        # Make particle.mass paintable.
        cmds.makePaintable( 'particle', 'mass', attrType='doubleArray' )
        # Make particle.goalPP paintable, with a ui name myGoalPP.
        # Also make the goalPP0 attribute painted simultaneously
        cmds.makePaintable( 'particle', 'goalPP', attrType='doubleArray', ui='myGoalPP', altAttribute='goalPP0' )
        # Make weightGeometryFilter.weights paintable. Define
        # weightGeometryFilter as a deformer node.
        cmds.makePaintable( 'weightGeometryFilter', 'weights', attrType='multiFloat', sm='deformer' )
        # Make all the attributes paintable on the artAttrPaintTest node.
        cmds.makePaintable( 'artAttrPaintTest', 'intArray', attrType='intArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblArray', attrType='doubleArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'vecArray', attrType='vectorArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'intMulti', attrType='multiInteger' )
        cmds.makePaintable( 'artAttrPaintTest', 'fltMulti', attrType='multiFloat' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblMulti', attrType='multiDouble' )
        cmds.makePaintable( 'artAttrPaintTest', 'flt3Multi', attrType='multiVector' )
        cmds.makePaintable( 'artAttrPaintTest', 'dbl3Multi', attrType='multiVector' )
    ```

    ---
    - Args:
        - [string][string]: Input item(s).
        - activate (ac): Activate / deactivate the given paintable attribute. Used to filter out some nodes in the attribute paint tool.
        - activateAll (aca): Activate / deactivate all the registered paintable attributes. Used to filter out some nodes in the attribute paint tool.
        - altAttribute (aa): Define an alternate attribute which will also receive the same values. There can be multiple such flags.
        - attrType (at): Paintable attribute type. Supported types: intArray, doubleArray, vectorArray, multiInteger, multiFloat, multiDouble, multiVector.
        - clearAll (ca): Removes all paintable attribute definitions.
        - remove (rm): Make the attribute not paintable any more.
        - shapeMode (sm): This flag controls how Artisan correlates the paintable node to a corresponding shape node.  It is used for attributes of type multi of multi, where the first multi dimension corresponds to the shape index (i.e. cluster nodes). At present,
            only one value of this flag is supported: "deformer". By default this flag is an empty string, which means that there is a direct indexing (no special mapping required) of the attribute with respect to vertices on the shape.
        - uiName (ui): UI name. Default is the attribute name.
        - query (q): Query mode flag
    """
@overload #Overload for makePaintable in ['query']
def makePaintable([string][string]: [string][string], ac: bool = ..., aca: bool = ..., aa: str = ..., at: str = ..., ca: bool = ..., rm: bool = ..., sm: str = ..., ui: str = ..., q: bool = ...) -> None:
    """makePaintable is NOT undoable, queryable, and NOT editable.
    
    Make attributes of nodes paintable to Attribute Paint Tool. This command is
    used to register new attributes to the Attribute Paint tool as paintable. Once
    registered the attributes will be recognized by the Attribute Paint tool and
    the user will be able to paint them.

    Example:
    ```python
        import maya.cmds as cmds
        # Make particle.mass paintable.
        cmds.makePaintable( 'particle', 'mass', attrType='doubleArray' )
        # Make particle.goalPP paintable, with a ui name myGoalPP.
        # Also make the goalPP0 attribute painted simultaneously
        cmds.makePaintable( 'particle', 'goalPP', attrType='doubleArray', ui='myGoalPP', altAttribute='goalPP0' )
        # Make weightGeometryFilter.weights paintable. Define
        # weightGeometryFilter as a deformer node.
        cmds.makePaintable( 'weightGeometryFilter', 'weights', attrType='multiFloat', sm='deformer' )
        # Make all the attributes paintable on the artAttrPaintTest node.
        cmds.makePaintable( 'artAttrPaintTest', 'intArray', attrType='intArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblArray', attrType='doubleArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'vecArray', attrType='vectorArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'intMulti', attrType='multiInteger' )
        cmds.makePaintable( 'artAttrPaintTest', 'fltMulti', attrType='multiFloat' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblMulti', attrType='multiDouble' )
        cmds.makePaintable( 'artAttrPaintTest', 'flt3Multi', attrType='multiVector' )
        cmds.makePaintable( 'artAttrPaintTest', 'dbl3Multi', attrType='multiVector' )
    ```

    ---
    - Args:
        - [string][string]: Input item(s).
        - activate (ac): Activate / deactivate the given paintable attribute. Used to filter out some nodes in the attribute paint tool.
        - activateAll (aca): Activate / deactivate all the registered paintable attributes. Used to filter out some nodes in the attribute paint tool.
        - altAttribute (aa): Define an alternate attribute which will also receive the same values. There can be multiple such flags.
        - attrType (at): Paintable attribute type. Supported types: intArray, doubleArray, vectorArray, multiInteger, multiFloat, multiDouble, multiVector.
        - clearAll (ca): Removes all paintable attribute definitions.
        - remove (rm): Make the attribute not paintable any more.
        - shapeMode (sm): This flag controls how Artisan correlates the paintable node to a corresponding shape node.  It is used for attributes of type multi of multi, where the first multi dimension corresponds to the shape index (i.e. cluster nodes). At present,
            only one value of this flag is supported: "deformer". By default this flag is an empty string, which means that there is a direct indexing (no special mapping required) of the attribute with respect to vertices on the shape.
        - uiName (ui): UI name. Default is the attribute name.
        - query (q): Query mode flag
    """
@overload #Overload for makePaintable in ['query']
def makePaintable([string][string]: [string][string], activate: bool = ..., ac: bool = ..., activateAll: bool = ..., aca: bool = ..., altAttribute: str = ..., aa: str = ..., attrType: str = ..., at: str = ..., clearAll: bool = ..., ca: bool = ..., remove: bool = ..., rm: bool = ..., shapeMode: str = ..., sm: str = ..., uiName: str = ..., ui: str = ..., query: bool = ..., q: bool = ...) -> None:
    """makePaintable is NOT undoable, queryable, and NOT editable.
    
    Make attributes of nodes paintable to Attribute Paint Tool. This command is
    used to register new attributes to the Attribute Paint tool as paintable. Once
    registered the attributes will be recognized by the Attribute Paint tool and
    the user will be able to paint them.

    Example:
    ```python
        import maya.cmds as cmds
        # Make particle.mass paintable.
        cmds.makePaintable( 'particle', 'mass', attrType='doubleArray' )
        # Make particle.goalPP paintable, with a ui name myGoalPP.
        # Also make the goalPP0 attribute painted simultaneously
        cmds.makePaintable( 'particle', 'goalPP', attrType='doubleArray', ui='myGoalPP', altAttribute='goalPP0' )
        # Make weightGeometryFilter.weights paintable. Define
        # weightGeometryFilter as a deformer node.
        cmds.makePaintable( 'weightGeometryFilter', 'weights', attrType='multiFloat', sm='deformer' )
        # Make all the attributes paintable on the artAttrPaintTest node.
        cmds.makePaintable( 'artAttrPaintTest', 'intArray', attrType='intArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblArray', attrType='doubleArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'vecArray', attrType='vectorArray' )
        cmds.makePaintable( 'artAttrPaintTest', 'intMulti', attrType='multiInteger' )
        cmds.makePaintable( 'artAttrPaintTest', 'fltMulti', attrType='multiFloat' )
        cmds.makePaintable( 'artAttrPaintTest', 'dblMulti', attrType='multiDouble' )
        cmds.makePaintable( 'artAttrPaintTest', 'flt3Multi', attrType='multiVector' )
        cmds.makePaintable( 'artAttrPaintTest', 'dbl3Multi', attrType='multiVector' )
    ```

    ---
    - Args:
        - [string][string]: Input item(s).
        - activate (ac): Activate / deactivate the given paintable attribute. Used to filter out some nodes in the attribute paint tool.
        - activateAll (aca): Activate / deactivate all the registered paintable attributes. Used to filter out some nodes in the attribute paint tool.
        - altAttribute (aa): Define an alternate attribute which will also receive the same values. There can be multiple such flags.
        - attrType (at): Paintable attribute type. Supported types: intArray, doubleArray, vectorArray, multiInteger, multiFloat, multiDouble, multiVector.
        - clearAll (ca): Removes all paintable attribute definitions.
        - remove (rm): Make the attribute not paintable any more.
        - shapeMode (sm): This flag controls how Artisan correlates the paintable node to a corresponding shape node.  It is used for attributes of type multi of multi, where the first multi dimension corresponds to the shape index (i.e. cluster nodes). At present,
            only one value of this flag is supported: "deformer". By default this flag is an empty string, which means that there is a direct indexing (no special mapping required) of the attribute with respect to vertices on the shape.
        - uiName (ui): UI name. Default is the attribute name.
        - query (q): Query mode flag
    """
