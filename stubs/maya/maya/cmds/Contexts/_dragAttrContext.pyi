"""Stub files for Contexts category in Maya commands, command: dragAttrContext."""

from typing import Any, overload

@overload #Overload for dragAttrContext in ['create']
def dragAttrContext([name]: [name], connectTo: name = ..., exists: bool = ..., history: bool = ..., image1: str = ..., image2: str = ..., image3: str = ..., name: str = ..., reset: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polyPlane( w=10, h=10, sx=3, sy=3, ax=(0, 1, 0), tx=1, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext' )
        # Example 1: Move along X direction and rotate around X at the same time.
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('pPlane1.translateX', 'pPlane1.rotateX') )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 2: Extrude a face and then modify the distance that it is extruded by.
        cmds.polyExtrudeFacet( 'pPlane1.f[0]', ch=1, kft=0, pvx=-1.633333373, pvy=-1.111623654, pvz=3.142515589, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1, ran=0, divisions=1, twist=0, taper=1, off=0, ltz=0, ws=0, ltx=0, lty=0, lrx=0, lry=0, lrz=0, lsx=1, lsy=1, lsz=1, ldx=1, ldy=0, ldz=0, w=0, gx=0, gy=-1, gz=0, att=0, mx=0, my=0, mz=0, sma=30 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo='polyExtrudeFace1.localTranslateZ' )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 3: Do a wedge face and modify both the number of divisions and the
        # angle at the same time.
        cmds.polyWedgeFace( 'pPlane1.f[0]', 'pPlane1.e[30]', ws=1, wedgeAngle=90, divisions=4, ed=30, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('polyWedgeFace1.wedgeAngle', 'polyWedgeFace1.divisions') )
        cmds.setToolTo( 'myDragAttrContext' )
    ```

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - reset (r): Resets the list of attributes to which the context is connected.
    """
@overload #Overload for dragAttrContext in ['create']
def dragAttrContext([name]: [name], ct: name = ..., ex: bool = ..., ch: bool = ..., i1: str = ..., i2: str = ..., i3: str = ..., n: str = ..., r: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polyPlane( w=10, h=10, sx=3, sy=3, ax=(0, 1, 0), tx=1, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext' )
        # Example 1: Move along X direction and rotate around X at the same time.
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('pPlane1.translateX', 'pPlane1.rotateX') )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 2: Extrude a face and then modify the distance that it is extruded by.
        cmds.polyExtrudeFacet( 'pPlane1.f[0]', ch=1, kft=0, pvx=-1.633333373, pvy=-1.111623654, pvz=3.142515589, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1, ran=0, divisions=1, twist=0, taper=1, off=0, ltz=0, ws=0, ltx=0, lty=0, lrx=0, lry=0, lrz=0, lsx=1, lsy=1, lsz=1, ldx=1, ldy=0, ldz=0, w=0, gx=0, gy=-1, gz=0, att=0, mx=0, my=0, mz=0, sma=30 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo='polyExtrudeFace1.localTranslateZ' )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 3: Do a wedge face and modify both the number of divisions and the
        # angle at the same time.
        cmds.polyWedgeFace( 'pPlane1.f[0]', 'pPlane1.e[30]', ws=1, wedgeAngle=90, divisions=4, ed=30, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('polyWedgeFace1.wedgeAngle', 'polyWedgeFace1.divisions') )
        cmds.setToolTo( 'myDragAttrContext' )
    ```

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - reset (r): Resets the list of attributes to which the context is connected.
    """
@overload #Overload for dragAttrContext in ['create']
def dragAttrContext([name]: [name], connectTo: name = ..., ct: name = ..., exists: bool = ..., ex: bool = ..., history: bool = ..., ch: bool = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., name: str = ..., n: str = ..., reset: bool = ..., r: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polyPlane( w=10, h=10, sx=3, sy=3, ax=(0, 1, 0), tx=1, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext' )
        # Example 1: Move along X direction and rotate around X at the same time.
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('pPlane1.translateX', 'pPlane1.rotateX') )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 2: Extrude a face and then modify the distance that it is extruded by.
        cmds.polyExtrudeFacet( 'pPlane1.f[0]', ch=1, kft=0, pvx=-1.633333373, pvy=-1.111623654, pvz=3.142515589, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1, ran=0, divisions=1, twist=0, taper=1, off=0, ltz=0, ws=0, ltx=0, lty=0, lrx=0, lry=0, lrz=0, lsx=1, lsy=1, lsz=1, ldx=1, ldy=0, ldz=0, w=0, gx=0, gy=-1, gz=0, att=0, mx=0, my=0, mz=0, sma=30 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo='polyExtrudeFace1.localTranslateZ' )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 3: Do a wedge face and modify both the number of divisions and the
        # angle at the same time.
        cmds.polyWedgeFace( 'pPlane1.f[0]', 'pPlane1.e[30]', ws=1, wedgeAngle=90, divisions=4, ed=30, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('polyWedgeFace1.wedgeAngle', 'polyWedgeFace1.divisions') )
        cmds.setToolTo( 'myDragAttrContext' )
    ```

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - name (n): If this is a tool command, name the tool appropriately.
        - reset (r): Resets the list of attributes to which the context is connected.
    """
@overload #Overload for dragAttrContext in ['query']
def dragAttrContext([name]: [name], connectTo: name = ..., image1: str = ..., image2: str = ..., image3: str = ..., query: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polyPlane( w=10, h=10, sx=3, sy=3, ax=(0, 1, 0), tx=1, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext' )
        # Example 1: Move along X direction and rotate around X at the same time.
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('pPlane1.translateX', 'pPlane1.rotateX') )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 2: Extrude a face and then modify the distance that it is extruded by.
        cmds.polyExtrudeFacet( 'pPlane1.f[0]', ch=1, kft=0, pvx=-1.633333373, pvy=-1.111623654, pvz=3.142515589, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1, ran=0, divisions=1, twist=0, taper=1, off=0, ltz=0, ws=0, ltx=0, lty=0, lrx=0, lry=0, lrz=0, lsx=1, lsy=1, lsz=1, ldx=1, ldy=0, ldz=0, w=0, gx=0, gy=-1, gz=0, att=0, mx=0, my=0, mz=0, sma=30 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo='polyExtrudeFace1.localTranslateZ' )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 3: Do a wedge face and modify both the number of divisions and the
        # angle at the same time.
        cmds.polyWedgeFace( 'pPlane1.f[0]', 'pPlane1.e[30]', ws=1, wedgeAngle=90, divisions=4, ed=30, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('polyWedgeFace1.wedgeAngle', 'polyWedgeFace1.divisions') )
        cmds.setToolTo( 'myDragAttrContext' )
    ```

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for dragAttrContext in ['query']
def dragAttrContext([name]: [name], ct: name = ..., i1: str = ..., i2: str = ..., i3: str = ..., q: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polyPlane( w=10, h=10, sx=3, sy=3, ax=(0, 1, 0), tx=1, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext' )
        # Example 1: Move along X direction and rotate around X at the same time.
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('pPlane1.translateX', 'pPlane1.rotateX') )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 2: Extrude a face and then modify the distance that it is extruded by.
        cmds.polyExtrudeFacet( 'pPlane1.f[0]', ch=1, kft=0, pvx=-1.633333373, pvy=-1.111623654, pvz=3.142515589, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1, ran=0, divisions=1, twist=0, taper=1, off=0, ltz=0, ws=0, ltx=0, lty=0, lrx=0, lry=0, lrz=0, lsx=1, lsy=1, lsz=1, ldx=1, ldy=0, ldz=0, w=0, gx=0, gy=-1, gz=0, att=0, mx=0, my=0, mz=0, sma=30 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo='polyExtrudeFace1.localTranslateZ' )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 3: Do a wedge face and modify both the number of divisions and the
        # angle at the same time.
        cmds.polyWedgeFace( 'pPlane1.f[0]', 'pPlane1.e[30]', ws=1, wedgeAngle=90, divisions=4, ed=30, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('polyWedgeFace1.wedgeAngle', 'polyWedgeFace1.divisions') )
        cmds.setToolTo( 'myDragAttrContext' )
    ```

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for dragAttrContext in ['query']
def dragAttrContext([name]: [name], connectTo: name = ..., ct: name = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., query: bool = ..., q: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polyPlane( w=10, h=10, sx=3, sy=3, ax=(0, 1, 0), tx=1, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext' )
        # Example 1: Move along X direction and rotate around X at the same time.
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('pPlane1.translateX', 'pPlane1.rotateX') )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 2: Extrude a face and then modify the distance that it is extruded by.
        cmds.polyExtrudeFacet( 'pPlane1.f[0]', ch=1, kft=0, pvx=-1.633333373, pvy=-1.111623654, pvz=3.142515589, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1, ran=0, divisions=1, twist=0, taper=1, off=0, ltz=0, ws=0, ltx=0, lty=0, lrx=0, lry=0, lrz=0, lsx=1, lsy=1, lsz=1, ldx=1, ldy=0, ldz=0, w=0, gx=0, gy=-1, gz=0, att=0, mx=0, my=0, mz=0, sma=30 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo='polyExtrudeFace1.localTranslateZ' )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 3: Do a wedge face and modify both the number of divisions and the
        # angle at the same time.
        cmds.polyWedgeFace( 'pPlane1.f[0]', 'pPlane1.e[30]', ws=1, wedgeAngle=90, divisions=4, ed=30, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('polyWedgeFace1.wedgeAngle', 'polyWedgeFace1.divisions') )
        cmds.setToolTo( 'myDragAttrContext' )
    ```

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - query (q): Query mode flag
    """
@overload #Overload for dragAttrContext in ['edit']
def dragAttrContext([name]: [name], connectTo: name = ..., image1: str = ..., image2: str = ..., image3: str = ..., reset: bool = ..., edit: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polyPlane( w=10, h=10, sx=3, sy=3, ax=(0, 1, 0), tx=1, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext' )
        # Example 1: Move along X direction and rotate around X at the same time.
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('pPlane1.translateX', 'pPlane1.rotateX') )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 2: Extrude a face and then modify the distance that it is extruded by.
        cmds.polyExtrudeFacet( 'pPlane1.f[0]', ch=1, kft=0, pvx=-1.633333373, pvy=-1.111623654, pvz=3.142515589, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1, ran=0, divisions=1, twist=0, taper=1, off=0, ltz=0, ws=0, ltx=0, lty=0, lrx=0, lry=0, lrz=0, lsx=1, lsy=1, lsz=1, ldx=1, ldy=0, ldz=0, w=0, gx=0, gy=-1, gz=0, att=0, mx=0, my=0, mz=0, sma=30 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo='polyExtrudeFace1.localTranslateZ' )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 3: Do a wedge face and modify both the number of divisions and the
        # angle at the same time.
        cmds.polyWedgeFace( 'pPlane1.f[0]', 'pPlane1.e[30]', ws=1, wedgeAngle=90, divisions=4, ed=30, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('polyWedgeFace1.wedgeAngle', 'polyWedgeFace1.divisions') )
        cmds.setToolTo( 'myDragAttrContext' )
    ```

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (r): Resets the list of attributes to which the context is connected.
        - edit (e): Edit mode flag
    """
@overload #Overload for dragAttrContext in ['edit']
def dragAttrContext([name]: [name], ct: name = ..., i1: str = ..., i2: str = ..., i3: str = ..., r: bool = ..., e: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polyPlane( w=10, h=10, sx=3, sy=3, ax=(0, 1, 0), tx=1, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext' )
        # Example 1: Move along X direction and rotate around X at the same time.
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('pPlane1.translateX', 'pPlane1.rotateX') )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 2: Extrude a face and then modify the distance that it is extruded by.
        cmds.polyExtrudeFacet( 'pPlane1.f[0]', ch=1, kft=0, pvx=-1.633333373, pvy=-1.111623654, pvz=3.142515589, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1, ran=0, divisions=1, twist=0, taper=1, off=0, ltz=0, ws=0, ltx=0, lty=0, lrx=0, lry=0, lrz=0, lsx=1, lsy=1, lsz=1, ldx=1, ldy=0, ldz=0, w=0, gx=0, gy=-1, gz=0, att=0, mx=0, my=0, mz=0, sma=30 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo='polyExtrudeFace1.localTranslateZ' )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 3: Do a wedge face and modify both the number of divisions and the
        # angle at the same time.
        cmds.polyWedgeFace( 'pPlane1.f[0]', 'pPlane1.e[30]', ws=1, wedgeAngle=90, divisions=4, ed=30, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('polyWedgeFace1.wedgeAngle', 'polyWedgeFace1.divisions') )
        cmds.setToolTo( 'myDragAttrContext' )
    ```

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (r): Resets the list of attributes to which the context is connected.
        - edit (e): Edit mode flag
    """
@overload #Overload for dragAttrContext in ['edit']
def dragAttrContext([name]: [name], connectTo: name = ..., ct: name = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., reset: bool = ..., r: bool = ..., edit: bool = ..., e: bool = ...) -> str:
    """dragAttrContext is undoable, queryable, and editable.
    
    The dragAttrContext allows a user to manipulate the attributes of an object by
    using a virtual slider within the viewport. The virtual slider is used by
    dragging in a viewport with the middle mouse button. The speed at which the
    attributes are changed can be controlled by holding down the Ctrl key to slow
    it down and the Shift key to speed it up.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.polyPlane( w=10, h=10, sx=3, sy=3, ax=(0, 1, 0), tx=1, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext' )
        # Example 1: Move along X direction and rotate around X at the same time.
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('pPlane1.translateX', 'pPlane1.rotateX') )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 2: Extrude a face and then modify the distance that it is extruded by.
        cmds.polyExtrudeFacet( 'pPlane1.f[0]', ch=1, kft=0, pvx=-1.633333373, pvy=-1.111623654, pvz=3.142515589, tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1, ran=0, divisions=1, twist=0, taper=1, off=0, ltz=0, ws=0, ltx=0, lty=0, lrx=0, lry=0, lrz=0, lsx=1, lsy=1, lsz=1, ldx=1, ldy=0, ldz=0, w=0, gx=0, gy=-1, gz=0, att=0, mx=0, my=0, mz=0, sma=30 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo='polyExtrudeFace1.localTranslateZ' )
        cmds.setToolTo( 'myDragAttrContext' )
        # Example 3: Do a wedge face and modify both the number of divisions and the
        # angle at the same time.
        cmds.polyWedgeFace( 'pPlane1.f[0]', 'pPlane1.e[30]', ws=1, wedgeAngle=90, divisions=4, ed=30, ch=1 )
        cmds.dragAttrContext( 'myDragAttrContext', edit=True, connectTo=('polyWedgeFace1.wedgeAngle', 'polyWedgeFace1.divisions') )
        cmds.setToolTo( 'myDragAttrContext' )
    ```

    ---
    - Args:
        - [name]: Input item(s).
        - connectTo (ct): Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - reset (r): Resets the list of attributes to which the context is connected.
        - edit (e): Edit mode flag
    """
