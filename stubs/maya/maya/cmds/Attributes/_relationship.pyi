"""Stub files for Attributes category in Maya commands, command: relationship."""

from typing import Any, overload

@overload #Overload for relationship in ['create']
def relationship(b: bool = ..., relationshipData: str = ...) -> None:
    """relationship is undoable, queryable, and editable.
    
    This is primarily for use with file IO. Rather than write out the specific
    attributes/connections required to maintain a relationship, a description of
    the related nodes/plugs is written instead. The relationship must have an
    owner node, and have a specific type. During file read, maya will make the
    connections and/or set the data necessary to represent the realtionship in the
    dependency graph.

    ---
    - Args:
        - b: Break the specified relationship instead of creating it
        - relationshipData (rd): Provide relationship data to be used when creating the relationship.
    """
@overload #Overload for relationship in ['create']
def relationship(rd: str = ...) -> None:
    """relationship is undoable, queryable, and editable.
    
    This is primarily for use with file IO. Rather than write out the specific
    attributes/connections required to maintain a relationship, a description of
    the related nodes/plugs is written instead. The relationship must have an
    owner node, and have a specific type. During file read, maya will make the
    connections and/or set the data necessary to represent the realtionship in the
    dependency graph.

    ---
    - Args:
        - b: Break the specified relationship instead of creating it
        - relationshipData (rd): Provide relationship data to be used when creating the relationship.
    """
@overload #Overload for relationship in ['create']
def relationship(b: bool = ..., relationshipData: str = ..., rd: str = ...) -> None:
    """relationship is undoable, queryable, and editable.
    
    This is primarily for use with file IO. Rather than write out the specific
    attributes/connections required to maintain a relationship, a description of
    the related nodes/plugs is written instead. The relationship must have an
    owner node, and have a specific type. During file read, maya will make the
    connections and/or set the data necessary to represent the realtionship in the
    dependency graph.

    ---
    - Args:
        - b: Break the specified relationship instead of creating it
        - relationshipData (rd): Provide relationship data to be used when creating the relationship.
    """
@overload #Overload for relationship in ['query']
def relationship(b: bool = ..., relationshipData: str = ..., query: bool = ...) -> None:
    """relationship is undoable, queryable, and editable.
    
    This is primarily for use with file IO. Rather than write out the specific
    attributes/connections required to maintain a relationship, a description of
    the related nodes/plugs is written instead. The relationship must have an
    owner node, and have a specific type. During file read, maya will make the
    connections and/or set the data necessary to represent the realtionship in the
    dependency graph.

    ---
    - Args:
        - b: Break the specified relationship instead of creating it
        - relationshipData (rd): Provide relationship data to be used when creating the relationship.
        - query (q): Query mode flag
    """
@overload #Overload for relationship in ['query']
def relationship(rd: str = ..., q: bool = ...) -> None:
    """relationship is undoable, queryable, and editable.
    
    This is primarily for use with file IO. Rather than write out the specific
    attributes/connections required to maintain a relationship, a description of
    the related nodes/plugs is written instead. The relationship must have an
    owner node, and have a specific type. During file read, maya will make the
    connections and/or set the data necessary to represent the realtionship in the
    dependency graph.

    ---
    - Args:
        - b: Break the specified relationship instead of creating it
        - relationshipData (rd): Provide relationship data to be used when creating the relationship.
        - query (q): Query mode flag
    """
@overload #Overload for relationship in ['query']
def relationship(b: bool = ..., relationshipData: str = ..., rd: str = ..., query: bool = ..., q: bool = ...) -> None:
    """relationship is undoable, queryable, and editable.
    
    This is primarily for use with file IO. Rather than write out the specific
    attributes/connections required to maintain a relationship, a description of
    the related nodes/plugs is written instead. The relationship must have an
    owner node, and have a specific type. During file read, maya will make the
    connections and/or set the data necessary to represent the realtionship in the
    dependency graph.

    ---
    - Args:
        - b: Break the specified relationship instead of creating it
        - relationshipData (rd): Provide relationship data to be used when creating the relationship.
        - query (q): Query mode flag
    """
@overload #Overload for relationship in ['edit']
def relationship(b: bool = ..., relationshipData: str = ..., edit: bool = ...) -> None:
    """relationship is undoable, queryable, and editable.
    
    This is primarily for use with file IO. Rather than write out the specific
    attributes/connections required to maintain a relationship, a description of
    the related nodes/plugs is written instead. The relationship must have an
    owner node, and have a specific type. During file read, maya will make the
    connections and/or set the data necessary to represent the realtionship in the
    dependency graph.

    ---
    - Args:
        - b: Break the specified relationship instead of creating it
        - relationshipData (rd): Provide relationship data to be used when creating the relationship.
        - edit (e): Edit mode flag
    """
@overload #Overload for relationship in ['edit']
def relationship(rd: str = ..., e: bool = ...) -> None:
    """relationship is undoable, queryable, and editable.
    
    This is primarily for use with file IO. Rather than write out the specific
    attributes/connections required to maintain a relationship, a description of
    the related nodes/plugs is written instead. The relationship must have an
    owner node, and have a specific type. During file read, maya will make the
    connections and/or set the data necessary to represent the realtionship in the
    dependency graph.

    ---
    - Args:
        - b: Break the specified relationship instead of creating it
        - relationshipData (rd): Provide relationship data to be used when creating the relationship.
        - edit (e): Edit mode flag
    """
@overload #Overload for relationship in ['edit']
def relationship(b: bool = ..., relationshipData: str = ..., rd: str = ..., edit: bool = ..., e: bool = ...) -> None:
    """relationship is undoable, queryable, and editable.
    
    This is primarily for use with file IO. Rather than write out the specific
    attributes/connections required to maintain a relationship, a description of
    the related nodes/plugs is written instead. The relationship must have an
    owner node, and have a specific type. During file read, maya will make the
    connections and/or set the data necessary to represent the realtionship in the
    dependency graph.

    ---
    - Args:
        - b: Break the specified relationship instead of creating it
        - relationshipData (rd): Provide relationship data to be used when creating the relationship.
        - edit (e): Edit mode flag
    """
