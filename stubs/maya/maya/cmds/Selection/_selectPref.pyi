"""Stub files for Selection category in Maya commands, command: selectPref."""

from typing import Any, overload

@overload #Overload for selectPref in ['create']
def selectPref(affectsActive: bool = ..., allowHiliteSelection: bool = ..., clickBoxSize: int = ..., clickDrag: bool = ..., disableComponentPopups: bool = ..., expandPopupList: bool = ..., ignoreSelectionPriority: bool = ..., manipClickBoxSize: int = ..., popupMenuSelection: bool = ..., selectionChildHighlightMode: int = ..., singleBoxSelection: bool = ..., xformNoSelect: bool = ...) -> bool:
    """selectPref is undoable, queryable, and NOT editable.
    
    This command controls state variables used to selection UI behavior.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPref(popupMenuSelection=True,disableComponentPopups=True)
    ```

    ---
    - Args:
        - affectsActive (aa): Set affects-active toggle which when on causes the active list to be affected when changing between object and component selection mode.
        - allowHiliteSelection (ahs): When in component selection mode, allow selection of objects for editing.  If an object is selected for editing, it appears in the hilite color and its selectable components are automatically displayed.
        - clickBoxSize (cbs): When click selecting, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position.
            The size must be positive.
        - clickDrag (cld): Set click/drag selection interaction on/off
        - disableComponentPopups (dcp): A separate preference to allow users to disable popup menus when selecting components.  This pref is only meaningful if the popupMenuSelection pref is enabled.
        - expandPopupList (epl): When in popup selection mode, if this is set then all selection items that contain multiple objects or components will be be expanded such that each object or component will be a single new selection item.
        - ignoreSelectionPriority (isp): If this is set, selection priority will be ignored when performing selection.
        - manipClickBoxSize (mcb): When selecting a manipulator, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor
            position. The size must be positive.
        - popupMenuSelection (pms): If this is set, a popup menu will be displayed and used to determine the object to select. The menu lists the current user box (marquee) of selected candidate objects.
        - selectionChildHighlightMode (sch): Controls the highlighting of the children of a selected object. Valid modes are:  0: Always highlight children 1: Never highlight children 2: Use per-object "Selection Child Highlight" setting.  Default mode is (0): Always highlight
            children.  For (2), each DAG object has an individual "Selection Child Highlight" boolean flag. By default, this flag will be TRUE. When mode (2) is enabled, the control is deferred to the selected object's "Selection Child Highlight" flag.
        - singleBoxSelection (sbs): Set single box selection on/off. This flag indicates whether just single object will be selected when the user box (marquee) selects several objects if flag set to true.  Otherwise, all those objects inside the box will be selected.
        - xformNoSelect (xns): Disable selection in xform tools
    """
@overload #Overload for selectPref in ['create']
def selectPref(aa: bool = ..., ahs: bool = ..., cbs: int = ..., cld: bool = ..., dcp: bool = ..., epl: bool = ..., isp: bool = ..., mcb: int = ..., pms: bool = ..., sch: int = ..., sbs: bool = ..., xns: bool = ...) -> bool:
    """selectPref is undoable, queryable, and NOT editable.
    
    This command controls state variables used to selection UI behavior.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPref(popupMenuSelection=True,disableComponentPopups=True)
    ```

    ---
    - Args:
        - affectsActive (aa): Set affects-active toggle which when on causes the active list to be affected when changing between object and component selection mode.
        - allowHiliteSelection (ahs): When in component selection mode, allow selection of objects for editing.  If an object is selected for editing, it appears in the hilite color and its selectable components are automatically displayed.
        - clickBoxSize (cbs): When click selecting, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position.
            The size must be positive.
        - clickDrag (cld): Set click/drag selection interaction on/off
        - disableComponentPopups (dcp): A separate preference to allow users to disable popup menus when selecting components.  This pref is only meaningful if the popupMenuSelection pref is enabled.
        - expandPopupList (epl): When in popup selection mode, if this is set then all selection items that contain multiple objects or components will be be expanded such that each object or component will be a single new selection item.
        - ignoreSelectionPriority (isp): If this is set, selection priority will be ignored when performing selection.
        - manipClickBoxSize (mcb): When selecting a manipulator, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor
            position. The size must be positive.
        - popupMenuSelection (pms): If this is set, a popup menu will be displayed and used to determine the object to select. The menu lists the current user box (marquee) of selected candidate objects.
        - selectionChildHighlightMode (sch): Controls the highlighting of the children of a selected object. Valid modes are:  0: Always highlight children 1: Never highlight children 2: Use per-object "Selection Child Highlight" setting.  Default mode is (0): Always highlight
            children.  For (2), each DAG object has an individual "Selection Child Highlight" boolean flag. By default, this flag will be TRUE. When mode (2) is enabled, the control is deferred to the selected object's "Selection Child Highlight" flag.
        - singleBoxSelection (sbs): Set single box selection on/off. This flag indicates whether just single object will be selected when the user box (marquee) selects several objects if flag set to true.  Otherwise, all those objects inside the box will be selected.
        - xformNoSelect (xns): Disable selection in xform tools
    """
@overload #Overload for selectPref in ['create']
def selectPref(affectsActive: bool = ..., aa: bool = ..., allowHiliteSelection: bool = ..., ahs: bool = ..., clickBoxSize: int = ..., cbs: int = ..., clickDrag: bool = ..., cld: bool = ..., disableComponentPopups: bool = ..., dcp: bool = ..., expandPopupList: bool = ..., epl: bool = ..., ignoreSelectionPriority: bool = ..., isp: bool = ..., manipClickBoxSize: int = ..., mcb: int = ..., popupMenuSelection: bool = ..., pms: bool = ..., selectionChildHighlightMode: int = ..., sch: int = ..., singleBoxSelection: bool = ..., sbs: bool = ..., xformNoSelect: bool = ..., xns: bool = ...) -> bool:
    """selectPref is undoable, queryable, and NOT editable.
    
    This command controls state variables used to selection UI behavior.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPref(popupMenuSelection=True,disableComponentPopups=True)
    ```

    ---
    - Args:
        - affectsActive (aa): Set affects-active toggle which when on causes the active list to be affected when changing between object and component selection mode.
        - allowHiliteSelection (ahs): When in component selection mode, allow selection of objects for editing.  If an object is selected for editing, it appears in the hilite color and its selectable components are automatically displayed.
        - clickBoxSize (cbs): When click selecting, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position.
            The size must be positive.
        - clickDrag (cld): Set click/drag selection interaction on/off
        - disableComponentPopups (dcp): A separate preference to allow users to disable popup menus when selecting components.  This pref is only meaningful if the popupMenuSelection pref is enabled.
        - expandPopupList (epl): When in popup selection mode, if this is set then all selection items that contain multiple objects or components will be be expanded such that each object or component will be a single new selection item.
        - ignoreSelectionPriority (isp): If this is set, selection priority will be ignored when performing selection.
        - manipClickBoxSize (mcb): When selecting a manipulator, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor
            position. The size must be positive.
        - popupMenuSelection (pms): If this is set, a popup menu will be displayed and used to determine the object to select. The menu lists the current user box (marquee) of selected candidate objects.
        - selectionChildHighlightMode (sch): Controls the highlighting of the children of a selected object. Valid modes are:  0: Always highlight children 1: Never highlight children 2: Use per-object "Selection Child Highlight" setting.  Default mode is (0): Always highlight
            children.  For (2), each DAG object has an individual "Selection Child Highlight" boolean flag. By default, this flag will be TRUE. When mode (2) is enabled, the control is deferred to the selected object's "Selection Child Highlight" flag.
        - singleBoxSelection (sbs): Set single box selection on/off. This flag indicates whether just single object will be selected when the user box (marquee) selects several objects if flag set to true.  Otherwise, all those objects inside the box will be selected.
        - xformNoSelect (xns): Disable selection in xform tools
    """
@overload #Overload for selectPref in ['query']
def selectPref(affectsActive: bool = ..., allowHiliteSelection: bool = ..., autoSelectContainer: bool = ..., autoSelectOutlinerSetMembers: bool = ..., autoUseDepth: bool = ..., clickBoxSize: int = ..., clickDrag: bool = ..., containerCentricSelection: bool = ..., disableComponentPopups: bool = ..., expandPopupList: bool = ..., ignoreSelectionPriority: bool = ..., manipClickBoxSize: int = ..., paintSelect: bool = ..., paintSelectWithDepth: bool = ..., popupMenuSelection: bool = ..., preSelectBackfacing: bool = ..., preSelectClosest: bool = ..., preSelectDeadSpace: int = ..., preSelectHilite: bool = ..., preSelectHiliteSize: float = ..., preSelectTweakDeadSpace: int = ..., selectTypeChangeAffectsActive: bool = ..., selectionChildHighlightMode: int = ..., singleBoxSelection: bool = ..., straightLineDistance: bool = ..., trackSelectionOrder: bool = ..., useDepth: bool = ..., xformNoSelect: bool = ..., query: bool = ...) -> bool:
    """selectPref is undoable, queryable, and NOT editable.
    
    This command controls state variables used to selection UI behavior.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPref(popupMenuSelection=True,disableComponentPopups=True)
    ```

    ---
    - Args:
        - affectsActive (aa): Set affects-active toggle which when on causes the active list to be affected when changing between object and component selection mode.
        - allowHiliteSelection (ahs): When in component selection mode, allow selection of objects for editing.  If an object is selected for editing, it appears in the hilite color and its selectable components are automatically displayed.
        - autoSelectContainer (asc): When enabled, with container centric selection also on, whenever the root transform is selected in the viewport, the container node will automatically be selected as well.
        - autoSelectOutlinerSetMembers (asm): When enabled selecting a set in the Outliner will automatically select the set members instead.
        - autoUseDepth (aud): When enabled, useDepth and paintSelectWithDepth will be automatically enabled in shaded display mode and disabled in wireframe display mode.
        - clickBoxSize (cbs): When click selecting, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position.
            The size must be positive.
        - clickDrag (cld): Set click/drag selection interaction on/off
        - containerCentricSelection (ccs): When enabled, selecting any DAG node in a container in the viewport will select the container's root transform if there is one.  If there is no root transform then the highest DAG node in the container will be selected.  There is no effect
            when selecting nodes which are not in a container.
        - disableComponentPopups (dcp): A separate preference to allow users to disable popup menus when selecting components.  This pref is only meaningful if the popupMenuSelection pref is enabled.
        - expandPopupList (epl): When in popup selection mode, if this is set then all selection items that contain multiple objects or components will be be expanded such that each object or component will be a single new selection item.
        - ignoreSelectionPriority (isp): If this is set, selection priority will be ignored when performing selection.
        - manipClickBoxSize (mcb): When selecting a manipulator, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor
            position. The size must be positive.
        - paintSelect (ps): When enabled, the select tool will use drag selection instead of marquee selection.
        - paintSelectWithDepth (psd): When enabled, paint selection will not select components that are behind the surface in the current camera view.
        - popupMenuSelection (pms): If this is set, a popup menu will be displayed and used to determine the object to select. The menu lists the current user box (marquee) of selected candidate objects.
        - preSelectBackfacing (psb): When enabled preselection will highlight backfacing components whose normals face away from the camera.
        - preSelectClosest (psc): When enabled and the cursor is over a surface, preselection highlighting will try to preselect the closest component to the cursor regardless of distance.
        - preSelectDeadSpace (pds): This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface.
        - preSelectHilite (psh): When enabled, the closest component under the cursor will be highlighted to indicate that clicking will select that component.
        - preSelectHiliteSize (phs): This value defines the size of the region around the cursor used for preselection highlighting. Within this region the closest component to the cursor will be highlighted.
        - preSelectTweakDeadSpace (pdt): This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface in tweak mode.
        - selectTypeChangeAffectsActive (stc): If true then the active list will be updated according to the new selection preferences.
        - selectionChildHighlightMode (sch): Controls the highlighting of the children of a selected object. Valid modes are:  0: Always highlight children 1: Never highlight children 2: Use per-object "Selection Child Highlight" setting.  Default mode is (0): Always highlight
            children.  For (2), each DAG object has an individual "Selection Child Highlight" boolean flag. By default, this flag will be TRUE. When mode (2) is enabled, the control is deferred to the selected object's "Selection Child Highlight" flag.
        - singleBoxSelection (sbs): Set single box selection on/off. This flag indicates whether just single object will be selected when the user box (marquee) selects several objects if flag set to true.  Otherwise, all those objects inside the box will be selected.
        - straightLineDistance (sld): If true then use straight line distances for selection proximity.
        - trackSelectionOrder (tso): When enabled, the order of selected objects and components will be tracked.  The 'ls' command will be able to return the active list in the order of selection which will allow scripts to be written that depend on the order.
        - useDepth (ud): When enabled, marquee selection will not select components that are behind the surface in the current camera view.
        - xformNoSelect (xns): Disable selection in xform tools
        - query (q): Query mode flag
    """
@overload #Overload for selectPref in ['query']
def selectPref(aa: bool = ..., ahs: bool = ..., asc: bool = ..., asm: bool = ..., aud: bool = ..., cbs: int = ..., cld: bool = ..., ccs: bool = ..., dcp: bool = ..., epl: bool = ..., isp: bool = ..., mcb: int = ..., ps: bool = ..., psd: bool = ..., pms: bool = ..., psb: bool = ..., psc: bool = ..., pds: int = ..., psh: bool = ..., phs: float = ..., pdt: int = ..., stc: bool = ..., sch: int = ..., sbs: bool = ..., sld: bool = ..., tso: bool = ..., ud: bool = ..., xns: bool = ..., q: bool = ...) -> bool:
    """selectPref is undoable, queryable, and NOT editable.
    
    This command controls state variables used to selection UI behavior.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPref(popupMenuSelection=True,disableComponentPopups=True)
    ```

    ---
    - Args:
        - affectsActive (aa): Set affects-active toggle which when on causes the active list to be affected when changing between object and component selection mode.
        - allowHiliteSelection (ahs): When in component selection mode, allow selection of objects for editing.  If an object is selected for editing, it appears in the hilite color and its selectable components are automatically displayed.
        - autoSelectContainer (asc): When enabled, with container centric selection also on, whenever the root transform is selected in the viewport, the container node will automatically be selected as well.
        - autoSelectOutlinerSetMembers (asm): When enabled selecting a set in the Outliner will automatically select the set members instead.
        - autoUseDepth (aud): When enabled, useDepth and paintSelectWithDepth will be automatically enabled in shaded display mode and disabled in wireframe display mode.
        - clickBoxSize (cbs): When click selecting, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position.
            The size must be positive.
        - clickDrag (cld): Set click/drag selection interaction on/off
        - containerCentricSelection (ccs): When enabled, selecting any DAG node in a container in the viewport will select the container's root transform if there is one.  If there is no root transform then the highest DAG node in the container will be selected.  There is no effect
            when selecting nodes which are not in a container.
        - disableComponentPopups (dcp): A separate preference to allow users to disable popup menus when selecting components.  This pref is only meaningful if the popupMenuSelection pref is enabled.
        - expandPopupList (epl): When in popup selection mode, if this is set then all selection items that contain multiple objects or components will be be expanded such that each object or component will be a single new selection item.
        - ignoreSelectionPriority (isp): If this is set, selection priority will be ignored when performing selection.
        - manipClickBoxSize (mcb): When selecting a manipulator, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor
            position. The size must be positive.
        - paintSelect (ps): When enabled, the select tool will use drag selection instead of marquee selection.
        - paintSelectWithDepth (psd): When enabled, paint selection will not select components that are behind the surface in the current camera view.
        - popupMenuSelection (pms): If this is set, a popup menu will be displayed and used to determine the object to select. The menu lists the current user box (marquee) of selected candidate objects.
        - preSelectBackfacing (psb): When enabled preselection will highlight backfacing components whose normals face away from the camera.
        - preSelectClosest (psc): When enabled and the cursor is over a surface, preselection highlighting will try to preselect the closest component to the cursor regardless of distance.
        - preSelectDeadSpace (pds): This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface.
        - preSelectHilite (psh): When enabled, the closest component under the cursor will be highlighted to indicate that clicking will select that component.
        - preSelectHiliteSize (phs): This value defines the size of the region around the cursor used for preselection highlighting. Within this region the closest component to the cursor will be highlighted.
        - preSelectTweakDeadSpace (pdt): This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface in tweak mode.
        - selectTypeChangeAffectsActive (stc): If true then the active list will be updated according to the new selection preferences.
        - selectionChildHighlightMode (sch): Controls the highlighting of the children of a selected object. Valid modes are:  0: Always highlight children 1: Never highlight children 2: Use per-object "Selection Child Highlight" setting.  Default mode is (0): Always highlight
            children.  For (2), each DAG object has an individual "Selection Child Highlight" boolean flag. By default, this flag will be TRUE. When mode (2) is enabled, the control is deferred to the selected object's "Selection Child Highlight" flag.
        - singleBoxSelection (sbs): Set single box selection on/off. This flag indicates whether just single object will be selected when the user box (marquee) selects several objects if flag set to true.  Otherwise, all those objects inside the box will be selected.
        - straightLineDistance (sld): If true then use straight line distances for selection proximity.
        - trackSelectionOrder (tso): When enabled, the order of selected objects and components will be tracked.  The 'ls' command will be able to return the active list in the order of selection which will allow scripts to be written that depend on the order.
        - useDepth (ud): When enabled, marquee selection will not select components that are behind the surface in the current camera view.
        - xformNoSelect (xns): Disable selection in xform tools
        - query (q): Query mode flag
    """
@overload #Overload for selectPref in ['query']
def selectPref(affectsActive: bool = ..., aa: bool = ..., allowHiliteSelection: bool = ..., ahs: bool = ..., autoSelectContainer: bool = ..., asc: bool = ..., autoSelectOutlinerSetMembers: bool = ..., asm: bool = ..., autoUseDepth: bool = ..., aud: bool = ..., clickBoxSize: int = ..., cbs: int = ..., clickDrag: bool = ..., cld: bool = ..., containerCentricSelection: bool = ..., ccs: bool = ..., disableComponentPopups: bool = ..., dcp: bool = ..., expandPopupList: bool = ..., epl: bool = ..., ignoreSelectionPriority: bool = ..., isp: bool = ..., manipClickBoxSize: int = ..., mcb: int = ..., paintSelect: bool = ..., ps: bool = ..., paintSelectWithDepth: bool = ..., psd: bool = ..., popupMenuSelection: bool = ..., pms: bool = ..., preSelectBackfacing: bool = ..., psb: bool = ..., preSelectClosest: bool = ..., psc: bool = ..., preSelectDeadSpace: int = ..., pds: int = ..., preSelectHilite: bool = ..., psh: bool = ..., preSelectHiliteSize: float = ..., phs: float = ..., preSelectTweakDeadSpace: int = ..., pdt: int = ..., selectTypeChangeAffectsActive: bool = ..., stc: bool = ..., selectionChildHighlightMode: int = ..., sch: int = ..., singleBoxSelection: bool = ..., sbs: bool = ..., straightLineDistance: bool = ..., sld: bool = ..., trackSelectionOrder: bool = ..., tso: bool = ..., useDepth: bool = ..., ud: bool = ..., xformNoSelect: bool = ..., xns: bool = ..., query: bool = ..., q: bool = ...) -> bool:
    """selectPref is undoable, queryable, and NOT editable.
    
    This command controls state variables used to selection UI behavior.

    Example:
    ```python
        import maya.cmds as cmds
        cmds.selectPref(popupMenuSelection=True,disableComponentPopups=True)
    ```

    ---
    - Args:
        - affectsActive (aa): Set affects-active toggle which when on causes the active list to be affected when changing between object and component selection mode.
        - allowHiliteSelection (ahs): When in component selection mode, allow selection of objects for editing.  If an object is selected for editing, it appears in the hilite color and its selectable components are automatically displayed.
        - autoSelectContainer (asc): When enabled, with container centric selection also on, whenever the root transform is selected in the viewport, the container node will automatically be selected as well.
        - autoSelectOutlinerSetMembers (asm): When enabled selecting a set in the Outliner will automatically select the set members instead.
        - autoUseDepth (aud): When enabled, useDepth and paintSelectWithDepth will be automatically enabled in shaded display mode and disabled in wireframe display mode.
        - clickBoxSize (cbs): When click selecting, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position.
            The size must be positive.
        - clickDrag (cld): Set click/drag selection interaction on/off
        - containerCentricSelection (ccs): When enabled, selecting any DAG node in a container in the viewport will select the container's root transform if there is one.  If there is no root transform then the highest DAG node in the container will be selected.  There is no effect
            when selecting nodes which are not in a container.
        - disableComponentPopups (dcp): A separate preference to allow users to disable popup menus when selecting components.  This pref is only meaningful if the popupMenuSelection pref is enabled.
        - expandPopupList (epl): When in popup selection mode, if this is set then all selection items that contain multiple objects or components will be be expanded such that each object or component will be a single new selection item.
        - ignoreSelectionPriority (isp): If this is set, selection priority will be ignored when performing selection.
        - manipClickBoxSize (mcb): When selecting a manipulator, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor
            position. The size must be positive.
        - paintSelect (ps): When enabled, the select tool will use drag selection instead of marquee selection.
        - paintSelectWithDepth (psd): When enabled, paint selection will not select components that are behind the surface in the current camera view.
        - popupMenuSelection (pms): If this is set, a popup menu will be displayed and used to determine the object to select. The menu lists the current user box (marquee) of selected candidate objects.
        - preSelectBackfacing (psb): When enabled preselection will highlight backfacing components whose normals face away from the camera.
        - preSelectClosest (psc): When enabled and the cursor is over a surface, preselection highlighting will try to preselect the closest component to the cursor regardless of distance.
        - preSelectDeadSpace (pds): This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface.
        - preSelectHilite (psh): When enabled, the closest component under the cursor will be highlighted to indicate that clicking will select that component.
        - preSelectHiliteSize (phs): This value defines the size of the region around the cursor used for preselection highlighting. Within this region the closest component to the cursor will be highlighted.
        - preSelectTweakDeadSpace (pdt): This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface in tweak mode.
        - selectTypeChangeAffectsActive (stc): If true then the active list will be updated according to the new selection preferences.
        - selectionChildHighlightMode (sch): Controls the highlighting of the children of a selected object. Valid modes are:  0: Always highlight children 1: Never highlight children 2: Use per-object "Selection Child Highlight" setting.  Default mode is (0): Always highlight
            children.  For (2), each DAG object has an individual "Selection Child Highlight" boolean flag. By default, this flag will be TRUE. When mode (2) is enabled, the control is deferred to the selected object's "Selection Child Highlight" flag.
        - singleBoxSelection (sbs): Set single box selection on/off. This flag indicates whether just single object will be selected when the user box (marquee) selects several objects if flag set to true.  Otherwise, all those objects inside the box will be selected.
        - straightLineDistance (sld): If true then use straight line distances for selection proximity.
        - trackSelectionOrder (tso): When enabled, the order of selected objects and components will be tracked.  The 'ls' command will be able to return the active list in the order of selection which will allow scripts to be written that depend on the order.
        - useDepth (ud): When enabled, marquee selection will not select components that are behind the surface in the current camera view.
        - xformNoSelect (xns): Disable selection in xform tools
        - query (q): Query mode flag
    """
