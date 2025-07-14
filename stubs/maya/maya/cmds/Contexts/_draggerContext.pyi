"""Stub files for Contexts category in Maya commands, command: draggerContext."""

from typing import Any, overload

@overload #Overload for draggerContext in ['create']
def draggerContext([name]: [name], cursor: str = ..., dragCommand: script = ..., drawString: str = ..., exists: bool = ..., finalize: script = ..., history: bool = ..., holdCommand: script = ..., image1: str = ..., image2: str = ..., image3: str = ..., initialize: script = ..., name: str = ..., plane: [float, float, float] = ..., prePressCommand: script = ..., pressCommand: script = ..., projection: str = ..., releaseCommand: script = ..., snapping: bool = ..., space: str = ..., stepsCount: int = ..., undoMode: str = ...) -> str:
    """draggerContext is undoable, queryable, and editable.
    
    The draggerContext allows the user to program the behavior of the mouse or an
    equivalent dragging device in MEL.

    ---
    - Args:
        - [name]: Input item(s).
        - cursor (cur): Cursor displayed while context is active.  Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".
        - dragCommand (dc): Command called when mouse dragger is dragged.
        - drawString (ds): A string to be drawn at the current position of the pointer.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - finalize (fnz): Command called when the tool is exited.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - holdCommand (hc): Command called when mouse dragger is held.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - initialize (inz): Command called when the tool is entered.
        - name (n): If this is a tool command, name the tool appropriately.
        - plane (pl): Provide normal of projection plane (see -projection flag for details).
        - prePressCommand (ppc): Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.
        - pressCommand (pc): Command called when mouse dragger is pressed.
        - projection (pr): Sets current projection of drag point. Valid types are:viewPlaneproject to view planeobjectViewPlaneproject to object plane (parallel to view plane)objectPlaneproject to specified plane defined by object location and normal (default)
            0,1,0planeproject to specified plane defined by origin and normal (default) 0,1,0sketchPlaneproject to sketch planexAxisproject to closest point on X axisyAxisproject to closest point on Y axiszAxisproject to closest point on Z
            axisboundingSphereproject to closest point on object sphere boundsboundingBoxproject to closest point on object bounding box
        - releaseCommand (rc): Command called when mouse dragger is released.
        - snapping (snp): Enable/disable snapping for dragger context.
        - space (sp): Sets current space that coordinates are reported in. Types are:worldworld space (global)objectobject space (local)screenscreen space
        - stepsCount (sc): Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.
        - undoMode (um): Undo queue mode for the context actions. Acceptable values are:"all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk."step" - all the actions that happen between each
            press and release are combined into one undo chunk."sequence" - all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger
            context.
    """
@overload #Overload for draggerContext in ['create']
def draggerContext([name]: [name], cur: str = ..., dc: script = ..., ds: str = ..., ex: bool = ..., fnz: script = ..., ch: bool = ..., hc: script = ..., i1: str = ..., i2: str = ..., i3: str = ..., inz: script = ..., n: str = ..., pl: [float, float, float] = ..., ppc: script = ..., pc: script = ..., pr: str = ..., rc: script = ..., snp: bool = ..., sp: str = ..., sc: int = ..., um: str = ...) -> str:
    """draggerContext is undoable, queryable, and editable.
    
    The draggerContext allows the user to program the behavior of the mouse or an
    equivalent dragging device in MEL.

    ---
    - Args:
        - [name]: Input item(s).
        - cursor (cur): Cursor displayed while context is active.  Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".
        - dragCommand (dc): Command called when mouse dragger is dragged.
        - drawString (ds): A string to be drawn at the current position of the pointer.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - finalize (fnz): Command called when the tool is exited.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - holdCommand (hc): Command called when mouse dragger is held.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - initialize (inz): Command called when the tool is entered.
        - name (n): If this is a tool command, name the tool appropriately.
        - plane (pl): Provide normal of projection plane (see -projection flag for details).
        - prePressCommand (ppc): Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.
        - pressCommand (pc): Command called when mouse dragger is pressed.
        - projection (pr): Sets current projection of drag point. Valid types are:viewPlaneproject to view planeobjectViewPlaneproject to object plane (parallel to view plane)objectPlaneproject to specified plane defined by object location and normal (default)
            0,1,0planeproject to specified plane defined by origin and normal (default) 0,1,0sketchPlaneproject to sketch planexAxisproject to closest point on X axisyAxisproject to closest point on Y axiszAxisproject to closest point on Z
            axisboundingSphereproject to closest point on object sphere boundsboundingBoxproject to closest point on object bounding box
        - releaseCommand (rc): Command called when mouse dragger is released.
        - snapping (snp): Enable/disable snapping for dragger context.
        - space (sp): Sets current space that coordinates are reported in. Types are:worldworld space (global)objectobject space (local)screenscreen space
        - stepsCount (sc): Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.
        - undoMode (um): Undo queue mode for the context actions. Acceptable values are:"all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk."step" - all the actions that happen between each
            press and release are combined into one undo chunk."sequence" - all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger
            context.
    """
@overload #Overload for draggerContext in ['create']
def draggerContext([name]: [name], cursor: str = ..., cur: str = ..., dragCommand: script = ..., dc: script = ..., drawString: str = ..., ds: str = ..., exists: bool = ..., ex: bool = ..., finalize: script = ..., fnz: script = ..., history: bool = ..., ch: bool = ..., holdCommand: script = ..., hc: script = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., initialize: script = ..., inz: script = ..., name: str = ..., n: str = ..., plane: [float, float, float] = ..., pl: [float, float, float] = ..., prePressCommand: script = ..., ppc: script = ..., pressCommand: script = ..., pc: script = ..., projection: str = ..., pr: str = ..., releaseCommand: script = ..., rc: script = ..., snapping: bool = ..., snp: bool = ..., space: str = ..., sp: str = ..., stepsCount: int = ..., sc: int = ..., undoMode: str = ..., um: str = ...) -> str:
    """draggerContext is undoable, queryable, and editable.
    
    The draggerContext allows the user to program the behavior of the mouse or an
    equivalent dragging device in MEL.

    ---
    - Args:
        - [name]: Input item(s).
        - cursor (cur): Cursor displayed while context is active.  Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".
        - dragCommand (dc): Command called when mouse dragger is dragged.
        - drawString (ds): A string to be drawn at the current position of the pointer.
        - exists (ex): Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        - finalize (fnz): Command called when the tool is exited.
        - history (ch): If this is a tool command, turn the construction history on for the tool in question.
        - holdCommand (hc): Command called when mouse dragger is held.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - initialize (inz): Command called when the tool is entered.
        - name (n): If this is a tool command, name the tool appropriately.
        - plane (pl): Provide normal of projection plane (see -projection flag for details).
        - prePressCommand (ppc): Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.
        - pressCommand (pc): Command called when mouse dragger is pressed.
        - projection (pr): Sets current projection of drag point. Valid types are:viewPlaneproject to view planeobjectViewPlaneproject to object plane (parallel to view plane)objectPlaneproject to specified plane defined by object location and normal (default)
            0,1,0planeproject to specified plane defined by origin and normal (default) 0,1,0sketchPlaneproject to sketch planexAxisproject to closest point on X axisyAxisproject to closest point on Y axiszAxisproject to closest point on Z
            axisboundingSphereproject to closest point on object sphere boundsboundingBoxproject to closest point on object bounding box
        - releaseCommand (rc): Command called when mouse dragger is released.
        - snapping (snp): Enable/disable snapping for dragger context.
        - space (sp): Sets current space that coordinates are reported in. Types are:worldworld space (global)objectobject space (local)screenscreen space
        - stepsCount (sc): Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.
        - undoMode (um): Undo queue mode for the context actions. Acceptable values are:"all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk."step" - all the actions that happen between each
            press and release are combined into one undo chunk."sequence" - all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger
            context.
    """
@overload #Overload for draggerContext in ['query']
def draggerContext([name]: [name], anchorPoint: [float, float, float] = ..., button: int = ..., currentStep: int = ..., cursor: str = ..., dragCommand: script = ..., dragPoint: [float, float, float] = ..., drawString: str = ..., finalize: script = ..., helpString: str = ..., holdCommand: script = ..., image1: str = ..., image2: str = ..., image3: str = ..., initialize: script = ..., modifier: str = ..., plane: [float, float, float] = ..., prePressCommand: script = ..., pressCommand: script = ..., projection: str = ..., releaseCommand: script = ..., snapping: bool = ..., space: str = ..., stepsCount: int = ..., undoMode: str = ..., query: bool = ...) -> str:
    """draggerContext is undoable, queryable, and editable.
    
    The draggerContext allows the user to program the behavior of the mouse or an
    equivalent dragging device in MEL.

    ---
    - Args:
        - [name]: Input item(s).
        - anchorPoint (ap): Anchor point (double array) where dragger was initially pressed.
        - button (bu): Returns the current mouse button (1,2,3).
        - currentStep (cs): Current step (press-drag-release sequence) for dragger context. When queried before first press event happened, returns 0.
        - cursor (cur): Cursor displayed while context is active.  Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".
        - dragCommand (dc): Command called when mouse dragger is dragged.
        - dragPoint (dp): Drag point (double array) current position of dragger during drag.
        - drawString (ds): A string to be drawn at the current position of the pointer.
        - finalize (fnz): Command called when the tool is exited.
        - helpString (hs): Help string for context
        - holdCommand (hc): Command called when mouse dragger is held.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - initialize (inz): Command called when the tool is entered.
        - modifier (mo): Returns the current modifier type:  ctrl, alt or none.
        - plane (pl): Provide normal of projection plane (see -projection flag for details).
        - prePressCommand (ppc): Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.
        - pressCommand (pc): Command called when mouse dragger is pressed.
        - projection (pr): Sets current projection of drag point. Valid types are:viewPlaneproject to view planeobjectViewPlaneproject to object plane (parallel to view plane)objectPlaneproject to specified plane defined by object location and normal (default)
            0,1,0planeproject to specified plane defined by origin and normal (default) 0,1,0sketchPlaneproject to sketch planexAxisproject to closest point on X axisyAxisproject to closest point on Y axiszAxisproject to closest point on Z
            axisboundingSphereproject to closest point on object sphere boundsboundingBoxproject to closest point on object bounding box
        - releaseCommand (rc): Command called when mouse dragger is released.
        - snapping (snp): Enable/disable snapping for dragger context.
        - space (sp): Sets current space that coordinates are reported in. Types are:worldworld space (global)objectobject space (local)screenscreen space
        - stepsCount (sc): Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.
        - undoMode (um): Undo queue mode for the context actions. Acceptable values are:"all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk."step" - all the actions that happen between each
            press and release are combined into one undo chunk."sequence" - all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger
            context.
        - query (q): Query mode flag
    """
@overload #Overload for draggerContext in ['query']
def draggerContext([name]: [name], ap: [float, float, float] = ..., bu: int = ..., cs: int = ..., cur: str = ..., dc: script = ..., dp: [float, float, float] = ..., ds: str = ..., fnz: script = ..., hs: str = ..., hc: script = ..., i1: str = ..., i2: str = ..., i3: str = ..., inz: script = ..., mo: str = ..., pl: [float, float, float] = ..., ppc: script = ..., pc: script = ..., pr: str = ..., rc: script = ..., snp: bool = ..., sp: str = ..., sc: int = ..., um: str = ..., q: bool = ...) -> str:
    """draggerContext is undoable, queryable, and editable.
    
    The draggerContext allows the user to program the behavior of the mouse or an
    equivalent dragging device in MEL.

    ---
    - Args:
        - [name]: Input item(s).
        - anchorPoint (ap): Anchor point (double array) where dragger was initially pressed.
        - button (bu): Returns the current mouse button (1,2,3).
        - currentStep (cs): Current step (press-drag-release sequence) for dragger context. When queried before first press event happened, returns 0.
        - cursor (cur): Cursor displayed while context is active.  Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".
        - dragCommand (dc): Command called when mouse dragger is dragged.
        - dragPoint (dp): Drag point (double array) current position of dragger during drag.
        - drawString (ds): A string to be drawn at the current position of the pointer.
        - finalize (fnz): Command called when the tool is exited.
        - helpString (hs): Help string for context
        - holdCommand (hc): Command called when mouse dragger is held.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - initialize (inz): Command called when the tool is entered.
        - modifier (mo): Returns the current modifier type:  ctrl, alt or none.
        - plane (pl): Provide normal of projection plane (see -projection flag for details).
        - prePressCommand (ppc): Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.
        - pressCommand (pc): Command called when mouse dragger is pressed.
        - projection (pr): Sets current projection of drag point. Valid types are:viewPlaneproject to view planeobjectViewPlaneproject to object plane (parallel to view plane)objectPlaneproject to specified plane defined by object location and normal (default)
            0,1,0planeproject to specified plane defined by origin and normal (default) 0,1,0sketchPlaneproject to sketch planexAxisproject to closest point on X axisyAxisproject to closest point on Y axiszAxisproject to closest point on Z
            axisboundingSphereproject to closest point on object sphere boundsboundingBoxproject to closest point on object bounding box
        - releaseCommand (rc): Command called when mouse dragger is released.
        - snapping (snp): Enable/disable snapping for dragger context.
        - space (sp): Sets current space that coordinates are reported in. Types are:worldworld space (global)objectobject space (local)screenscreen space
        - stepsCount (sc): Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.
        - undoMode (um): Undo queue mode for the context actions. Acceptable values are:"all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk."step" - all the actions that happen between each
            press and release are combined into one undo chunk."sequence" - all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger
            context.
        - query (q): Query mode flag
    """
@overload #Overload for draggerContext in ['query']
def draggerContext([name]: [name], anchorPoint: [float, float, float] = ..., ap: [float, float, float] = ..., button: int = ..., bu: int = ..., currentStep: int = ..., cs: int = ..., cursor: str = ..., cur: str = ..., dragCommand: script = ..., dc: script = ..., dragPoint: [float, float, float] = ..., dp: [float, float, float] = ..., drawString: str = ..., ds: str = ..., finalize: script = ..., fnz: script = ..., helpString: str = ..., hs: str = ..., holdCommand: script = ..., hc: script = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., initialize: script = ..., inz: script = ..., modifier: str = ..., mo: str = ..., plane: [float, float, float] = ..., pl: [float, float, float] = ..., prePressCommand: script = ..., ppc: script = ..., pressCommand: script = ..., pc: script = ..., projection: str = ..., pr: str = ..., releaseCommand: script = ..., rc: script = ..., snapping: bool = ..., snp: bool = ..., space: str = ..., sp: str = ..., stepsCount: int = ..., sc: int = ..., undoMode: str = ..., um: str = ..., query: bool = ..., q: bool = ...) -> str:
    """draggerContext is undoable, queryable, and editable.
    
    The draggerContext allows the user to program the behavior of the mouse or an
    equivalent dragging device in MEL.

    ---
    - Args:
        - [name]: Input item(s).
        - anchorPoint (ap): Anchor point (double array) where dragger was initially pressed.
        - button (bu): Returns the current mouse button (1,2,3).
        - currentStep (cs): Current step (press-drag-release sequence) for dragger context. When queried before first press event happened, returns 0.
        - cursor (cur): Cursor displayed while context is active.  Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".
        - dragCommand (dc): Command called when mouse dragger is dragged.
        - dragPoint (dp): Drag point (double array) current position of dragger during drag.
        - drawString (ds): A string to be drawn at the current position of the pointer.
        - finalize (fnz): Command called when the tool is exited.
        - helpString (hs): Help string for context
        - holdCommand (hc): Command called when mouse dragger is held.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - initialize (inz): Command called when the tool is entered.
        - modifier (mo): Returns the current modifier type:  ctrl, alt or none.
        - plane (pl): Provide normal of projection plane (see -projection flag for details).
        - prePressCommand (ppc): Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.
        - pressCommand (pc): Command called when mouse dragger is pressed.
        - projection (pr): Sets current projection of drag point. Valid types are:viewPlaneproject to view planeobjectViewPlaneproject to object plane (parallel to view plane)objectPlaneproject to specified plane defined by object location and normal (default)
            0,1,0planeproject to specified plane defined by origin and normal (default) 0,1,0sketchPlaneproject to sketch planexAxisproject to closest point on X axisyAxisproject to closest point on Y axiszAxisproject to closest point on Z
            axisboundingSphereproject to closest point on object sphere boundsboundingBoxproject to closest point on object bounding box
        - releaseCommand (rc): Command called when mouse dragger is released.
        - snapping (snp): Enable/disable snapping for dragger context.
        - space (sp): Sets current space that coordinates are reported in. Types are:worldworld space (global)objectobject space (local)screenscreen space
        - stepsCount (sc): Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.
        - undoMode (um): Undo queue mode for the context actions. Acceptable values are:"all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk."step" - all the actions that happen between each
            press and release are combined into one undo chunk."sequence" - all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger
            context.
        - query (q): Query mode flag
    """
@overload #Overload for draggerContext in ['edit']
def draggerContext([name]: [name], cursor: str = ..., dragCommand: script = ..., drawString: str = ..., finalize: script = ..., holdCommand: script = ..., image1: str = ..., image2: str = ..., image3: str = ..., initialize: script = ..., plane: [float, float, float] = ..., prePressCommand: script = ..., pressCommand: script = ..., projection: str = ..., releaseCommand: script = ..., snapping: bool = ..., space: str = ..., stepsCount: int = ..., undoMode: str = ..., edit: bool = ...) -> str:
    """draggerContext is undoable, queryable, and editable.
    
    The draggerContext allows the user to program the behavior of the mouse or an
    equivalent dragging device in MEL.

    ---
    - Args:
        - [name]: Input item(s).
        - cursor (cur): Cursor displayed while context is active.  Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".
        - dragCommand (dc): Command called when mouse dragger is dragged.
        - drawString (ds): A string to be drawn at the current position of the pointer.
        - finalize (fnz): Command called when the tool is exited.
        - holdCommand (hc): Command called when mouse dragger is held.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - initialize (inz): Command called when the tool is entered.
        - plane (pl): Provide normal of projection plane (see -projection flag for details).
        - prePressCommand (ppc): Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.
        - pressCommand (pc): Command called when mouse dragger is pressed.
        - projection (pr): Sets current projection of drag point. Valid types are:viewPlaneproject to view planeobjectViewPlaneproject to object plane (parallel to view plane)objectPlaneproject to specified plane defined by object location and normal (default)
            0,1,0planeproject to specified plane defined by origin and normal (default) 0,1,0sketchPlaneproject to sketch planexAxisproject to closest point on X axisyAxisproject to closest point on Y axiszAxisproject to closest point on Z
            axisboundingSphereproject to closest point on object sphere boundsboundingBoxproject to closest point on object bounding box
        - releaseCommand (rc): Command called when mouse dragger is released.
        - snapping (snp): Enable/disable snapping for dragger context.
        - space (sp): Sets current space that coordinates are reported in. Types are:worldworld space (global)objectobject space (local)screenscreen space
        - stepsCount (sc): Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.
        - undoMode (um): Undo queue mode for the context actions. Acceptable values are:"all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk."step" - all the actions that happen between each
            press and release are combined into one undo chunk."sequence" - all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger
            context.
        - edit (e): Edit mode flag
    """
@overload #Overload for draggerContext in ['edit']
def draggerContext([name]: [name], cur: str = ..., dc: script = ..., ds: str = ..., fnz: script = ..., hc: script = ..., i1: str = ..., i2: str = ..., i3: str = ..., inz: script = ..., pl: [float, float, float] = ..., ppc: script = ..., pc: script = ..., pr: str = ..., rc: script = ..., snp: bool = ..., sp: str = ..., sc: int = ..., um: str = ..., e: bool = ...) -> str:
    """draggerContext is undoable, queryable, and editable.
    
    The draggerContext allows the user to program the behavior of the mouse or an
    equivalent dragging device in MEL.

    ---
    - Args:
        - [name]: Input item(s).
        - cursor (cur): Cursor displayed while context is active.  Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".
        - dragCommand (dc): Command called when mouse dragger is dragged.
        - drawString (ds): A string to be drawn at the current position of the pointer.
        - finalize (fnz): Command called when the tool is exited.
        - holdCommand (hc): Command called when mouse dragger is held.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - initialize (inz): Command called when the tool is entered.
        - plane (pl): Provide normal of projection plane (see -projection flag for details).
        - prePressCommand (ppc): Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.
        - pressCommand (pc): Command called when mouse dragger is pressed.
        - projection (pr): Sets current projection of drag point. Valid types are:viewPlaneproject to view planeobjectViewPlaneproject to object plane (parallel to view plane)objectPlaneproject to specified plane defined by object location and normal (default)
            0,1,0planeproject to specified plane defined by origin and normal (default) 0,1,0sketchPlaneproject to sketch planexAxisproject to closest point on X axisyAxisproject to closest point on Y axiszAxisproject to closest point on Z
            axisboundingSphereproject to closest point on object sphere boundsboundingBoxproject to closest point on object bounding box
        - releaseCommand (rc): Command called when mouse dragger is released.
        - snapping (snp): Enable/disable snapping for dragger context.
        - space (sp): Sets current space that coordinates are reported in. Types are:worldworld space (global)objectobject space (local)screenscreen space
        - stepsCount (sc): Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.
        - undoMode (um): Undo queue mode for the context actions. Acceptable values are:"all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk."step" - all the actions that happen between each
            press and release are combined into one undo chunk."sequence" - all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger
            context.
        - edit (e): Edit mode flag
    """
@overload #Overload for draggerContext in ['edit']
def draggerContext([name]: [name], cursor: str = ..., cur: str = ..., dragCommand: script = ..., dc: script = ..., drawString: str = ..., ds: str = ..., finalize: script = ..., fnz: script = ..., holdCommand: script = ..., hc: script = ..., image1: str = ..., i1: str = ..., image2: str = ..., i2: str = ..., image3: str = ..., i3: str = ..., initialize: script = ..., inz: script = ..., plane: [float, float, float] = ..., pl: [float, float, float] = ..., prePressCommand: script = ..., ppc: script = ..., pressCommand: script = ..., pc: script = ..., projection: str = ..., pr: str = ..., releaseCommand: script = ..., rc: script = ..., snapping: bool = ..., snp: bool = ..., space: str = ..., sp: str = ..., stepsCount: int = ..., sc: int = ..., undoMode: str = ..., um: str = ..., edit: bool = ..., e: bool = ...) -> str:
    """draggerContext is undoable, queryable, and editable.
    
    The draggerContext allows the user to program the behavior of the mouse or an
    equivalent dragging device in MEL.

    ---
    - Args:
        - [name]: Input item(s).
        - cursor (cur): Cursor displayed while context is active.  Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".
        - dragCommand (dc): Command called when mouse dragger is dragged.
        - drawString (ds): A string to be drawn at the current position of the pointer.
        - finalize (fnz): Command called when the tool is exited.
        - holdCommand (hc): Command called when mouse dragger is held.
        - image1 (i1): First of three possible icons representing the tool associated with the context.
        - image2 (i2): Second of three possible icons representing the tool associated with the context.
        - image3 (i3): Third of three possible icons representing the tool associated with the context.
        - initialize (inz): Command called when the tool is entered.
        - plane (pl): Provide normal of projection plane (see -projection flag for details).
        - prePressCommand (ppc): Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.
        - pressCommand (pc): Command called when mouse dragger is pressed.
        - projection (pr): Sets current projection of drag point. Valid types are:viewPlaneproject to view planeobjectViewPlaneproject to object plane (parallel to view plane)objectPlaneproject to specified plane defined by object location and normal (default)
            0,1,0planeproject to specified plane defined by origin and normal (default) 0,1,0sketchPlaneproject to sketch planexAxisproject to closest point on X axisyAxisproject to closest point on Y axiszAxisproject to closest point on Z
            axisboundingSphereproject to closest point on object sphere boundsboundingBoxproject to closest point on object bounding box
        - releaseCommand (rc): Command called when mouse dragger is released.
        - snapping (snp): Enable/disable snapping for dragger context.
        - space (sp): Sets current space that coordinates are reported in. Types are:worldworld space (global)objectobject space (local)screenscreen space
        - stepsCount (sc): Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.
        - undoMode (um): Undo queue mode for the context actions. Acceptable values are:"all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk."step" - all the actions that happen between each
            press and release are combined into one undo chunk."sequence" - all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger
            context.
        - edit (e): Edit mode flag
    """
