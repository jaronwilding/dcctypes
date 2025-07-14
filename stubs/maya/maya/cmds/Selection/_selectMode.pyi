"""Stub files for Selection category in Maya commands, command: selectMode."""

from typing import Any, overload

@overload #Overload for selectMode in ['create']
def selectMode(component: bool = ..., hierarchical: bool = ..., leaf: bool = ..., object: bool = ..., preset: bool = ..., root: bool = ..., template: bool = ...) -> bool:
    """selectMode is undoable, queryable, and NOT editable.
    
    The selectMode command is used to change the selection mode. Object,
    component, root, leaf and template modes are mutually exclusive.

    ---
    - Args:
        - component (co): Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are
            selectable.
        - hierarchical (h): Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template.  Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root,
            leaf, or template was last on.
        - leaf (l): Set leaf selection mode on.  This mode allows the leaf level objects to be selected.  It is similar to object selection mode but ignores the object selection mask.
        - object (o): Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable.  The masks
            are controlled by the "selectType" command.  Object selection mode selects the leaf level objects.
        - preset (p): Allow selection of anything with the mask set, independent of it being an object or a component.
        - root (r): Set root selection mode on.  This mode allows the root of a hierarchy to be selected by selecting any of its descendents.  It ignores the object selection mask.
        - template (t): Set template selection mode on.  This mode allows selection of templated objects.  It selects the templated object closest to the root of the hierarchy.
    """
@overload #Overload for selectMode in ['create']
def selectMode(co: bool = ..., h: bool = ..., l: bool = ..., o: bool = ..., p: bool = ..., r: bool = ..., t: bool = ...) -> bool:
    """selectMode is undoable, queryable, and NOT editable.
    
    The selectMode command is used to change the selection mode. Object,
    component, root, leaf and template modes are mutually exclusive.

    ---
    - Args:
        - component (co): Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are
            selectable.
        - hierarchical (h): Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template.  Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root,
            leaf, or template was last on.
        - leaf (l): Set leaf selection mode on.  This mode allows the leaf level objects to be selected.  It is similar to object selection mode but ignores the object selection mask.
        - object (o): Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable.  The masks
            are controlled by the "selectType" command.  Object selection mode selects the leaf level objects.
        - preset (p): Allow selection of anything with the mask set, independent of it being an object or a component.
        - root (r): Set root selection mode on.  This mode allows the root of a hierarchy to be selected by selecting any of its descendents.  It ignores the object selection mask.
        - template (t): Set template selection mode on.  This mode allows selection of templated objects.  It selects the templated object closest to the root of the hierarchy.
    """
@overload #Overload for selectMode in ['create']
def selectMode(component: bool = ..., co: bool = ..., hierarchical: bool = ..., h: bool = ..., leaf: bool = ..., l: bool = ..., object: bool = ..., o: bool = ..., preset: bool = ..., p: bool = ..., root: bool = ..., r: bool = ..., template: bool = ..., t: bool = ...) -> bool:
    """selectMode is undoable, queryable, and NOT editable.
    
    The selectMode command is used to change the selection mode. Object,
    component, root, leaf and template modes are mutually exclusive.

    ---
    - Args:
        - component (co): Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are
            selectable.
        - hierarchical (h): Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template.  Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root,
            leaf, or template was last on.
        - leaf (l): Set leaf selection mode on.  This mode allows the leaf level objects to be selected.  It is similar to object selection mode but ignores the object selection mask.
        - object (o): Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable.  The masks
            are controlled by the "selectType" command.  Object selection mode selects the leaf level objects.
        - preset (p): Allow selection of anything with the mask set, independent of it being an object or a component.
        - root (r): Set root selection mode on.  This mode allows the root of a hierarchy to be selected by selecting any of its descendents.  It ignores the object selection mask.
        - template (t): Set template selection mode on.  This mode allows selection of templated objects.  It selects the templated object closest to the root of the hierarchy.
    """
@overload #Overload for selectMode in ['query']
def selectMode(component: bool = ..., hierarchical: bool = ..., leaf: bool = ..., object: bool = ..., preset: bool = ..., root: bool = ..., template: bool = ..., query: bool = ...) -> bool:
    """selectMode is undoable, queryable, and NOT editable.
    
    The selectMode command is used to change the selection mode. Object,
    component, root, leaf and template modes are mutually exclusive.

    ---
    - Args:
        - component (co): Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are
            selectable.
        - hierarchical (h): Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template.  Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root,
            leaf, or template was last on.
        - leaf (l): Set leaf selection mode on.  This mode allows the leaf level objects to be selected.  It is similar to object selection mode but ignores the object selection mask.
        - object (o): Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable.  The masks
            are controlled by the "selectType" command.  Object selection mode selects the leaf level objects.
        - preset (p): Allow selection of anything with the mask set, independent of it being an object or a component.
        - root (r): Set root selection mode on.  This mode allows the root of a hierarchy to be selected by selecting any of its descendents.  It ignores the object selection mask.
        - template (t): Set template selection mode on.  This mode allows selection of templated objects.  It selects the templated object closest to the root of the hierarchy.
        - query (q): Query mode flag
    """
@overload #Overload for selectMode in ['query']
def selectMode(co: bool = ..., h: bool = ..., l: bool = ..., o: bool = ..., p: bool = ..., r: bool = ..., t: bool = ..., q: bool = ...) -> bool:
    """selectMode is undoable, queryable, and NOT editable.
    
    The selectMode command is used to change the selection mode. Object,
    component, root, leaf and template modes are mutually exclusive.

    ---
    - Args:
        - component (co): Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are
            selectable.
        - hierarchical (h): Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template.  Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root,
            leaf, or template was last on.
        - leaf (l): Set leaf selection mode on.  This mode allows the leaf level objects to be selected.  It is similar to object selection mode but ignores the object selection mask.
        - object (o): Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable.  The masks
            are controlled by the "selectType" command.  Object selection mode selects the leaf level objects.
        - preset (p): Allow selection of anything with the mask set, independent of it being an object or a component.
        - root (r): Set root selection mode on.  This mode allows the root of a hierarchy to be selected by selecting any of its descendents.  It ignores the object selection mask.
        - template (t): Set template selection mode on.  This mode allows selection of templated objects.  It selects the templated object closest to the root of the hierarchy.
        - query (q): Query mode flag
    """
@overload #Overload for selectMode in ['query']
def selectMode(component: bool = ..., co: bool = ..., hierarchical: bool = ..., h: bool = ..., leaf: bool = ..., l: bool = ..., object: bool = ..., o: bool = ..., preset: bool = ..., p: bool = ..., root: bool = ..., r: bool = ..., template: bool = ..., t: bool = ..., query: bool = ..., q: bool = ...) -> bool:
    """selectMode is undoable, queryable, and NOT editable.
    
    The selectMode command is used to change the selection mode. Object,
    component, root, leaf and template modes are mutually exclusive.

    ---
    - Args:
        - component (co): Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are
            selectable.
        - hierarchical (h): Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template.  Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root,
            leaf, or template was last on.
        - leaf (l): Set leaf selection mode on.  This mode allows the leaf level objects to be selected.  It is similar to object selection mode but ignores the object selection mask.
        - object (o): Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable.  The masks
            are controlled by the "selectType" command.  Object selection mode selects the leaf level objects.
        - preset (p): Allow selection of anything with the mask set, independent of it being an object or a component.
        - root (r): Set root selection mode on.  This mode allows the root of a hierarchy to be selected by selecting any of its descendents.  It ignores the object selection mask.
        - template (t): Set template selection mode on.  This mode allows selection of templated objects.  It selects the templated object closest to the root of the hierarchy.
        - query (q): Query mode flag
    """
@overload #Overload for selectMode in ['edit']
def selectMode(component: bool = ..., hierarchical: bool = ..., leaf: bool = ..., object: bool = ..., preset: bool = ..., root: bool = ..., template: bool = ..., edit: bool = ...) -> bool:
    """selectMode is undoable, queryable, and NOT editable.
    
    The selectMode command is used to change the selection mode. Object,
    component, root, leaf and template modes are mutually exclusive.

    ---
    - Args:
        - component (co): Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are
            selectable.
        - hierarchical (h): Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template.  Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root,
            leaf, or template was last on.
        - leaf (l): Set leaf selection mode on.  This mode allows the leaf level objects to be selected.  It is similar to object selection mode but ignores the object selection mask.
        - object (o): Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable.  The masks
            are controlled by the "selectType" command.  Object selection mode selects the leaf level objects.
        - preset (p): Allow selection of anything with the mask set, independent of it being an object or a component.
        - root (r): Set root selection mode on.  This mode allows the root of a hierarchy to be selected by selecting any of its descendents.  It ignores the object selection mask.
        - template (t): Set template selection mode on.  This mode allows selection of templated objects.  It selects the templated object closest to the root of the hierarchy.
        - edit (e): Edit mode flag
    """
@overload #Overload for selectMode in ['edit']
def selectMode(co: bool = ..., h: bool = ..., l: bool = ..., o: bool = ..., p: bool = ..., r: bool = ..., t: bool = ..., e: bool = ...) -> bool:
    """selectMode is undoable, queryable, and NOT editable.
    
    The selectMode command is used to change the selection mode. Object,
    component, root, leaf and template modes are mutually exclusive.

    ---
    - Args:
        - component (co): Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are
            selectable.
        - hierarchical (h): Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template.  Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root,
            leaf, or template was last on.
        - leaf (l): Set leaf selection mode on.  This mode allows the leaf level objects to be selected.  It is similar to object selection mode but ignores the object selection mask.
        - object (o): Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable.  The masks
            are controlled by the "selectType" command.  Object selection mode selects the leaf level objects.
        - preset (p): Allow selection of anything with the mask set, independent of it being an object or a component.
        - root (r): Set root selection mode on.  This mode allows the root of a hierarchy to be selected by selecting any of its descendents.  It ignores the object selection mask.
        - template (t): Set template selection mode on.  This mode allows selection of templated objects.  It selects the templated object closest to the root of the hierarchy.
        - edit (e): Edit mode flag
    """
@overload #Overload for selectMode in ['edit']
def selectMode(component: bool = ..., co: bool = ..., hierarchical: bool = ..., h: bool = ..., leaf: bool = ..., l: bool = ..., object: bool = ..., o: bool = ..., preset: bool = ..., p: bool = ..., root: bool = ..., r: bool = ..., template: bool = ..., t: bool = ..., edit: bool = ..., e: bool = ...) -> bool:
    """selectMode is undoable, queryable, and NOT editable.
    
    The selectMode command is used to change the selection mode. Object,
    component, root, leaf and template modes are mutually exclusive.

    ---
    - Args:
        - component (co): Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are
            selectable.
        - hierarchical (h): Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template.  Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root,
            leaf, or template was last on.
        - leaf (l): Set leaf selection mode on.  This mode allows the leaf level objects to be selected.  It is similar to object selection mode but ignores the object selection mask.
        - object (o): Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable.  The masks
            are controlled by the "selectType" command.  Object selection mode selects the leaf level objects.
        - preset (p): Allow selection of anything with the mask set, independent of it being an object or a component.
        - root (r): Set root selection mode on.  This mode allows the root of a hierarchy to be selected by selecting any of its descendents.  It ignores the object selection mask.
        - template (t): Set template selection mode on.  This mode allows selection of templated objects.  It selects the templated object closest to the root of the hierarchy.
        - edit (e): Edit mode flag
    """
