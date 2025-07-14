"""Stub files for General category in Maya commands, command: threadCount."""

from typing import Any, overload

@overload #Overload for threadCount in ['create']
def threadCount(numberOfThreads: int = ...) -> None:
    """threadCount is undoable, queryable, and NOT editable.
    
    This command sets the number of threads to be used by Maya in regions of code
    that are multithreaded. By default the number of threads is equal to the
    number of logical CPUs, not the number of physical CPUs. Logical CPUs are
    different from physical CPUs in the following ways:
    
    A physical CPU with hyperthreading counts as two logical CPUs
    A dual-core CPU counts as two logical CPUs
    
    With some workloads, using one thread per logical CPU may not perform well.
    This is sometimes the case with hyperthreading. It is worth experimenting with
    different numbers of threads to see which gives the best performance. Note
    that having more threads can mean Maya uses more memory.
    
    Setting a value of zero means the number of threads used will equal the number
    of logical processors in the system.

    ---
    - Args:
        - numberOfThreads (n): Sets the number of threads to use
    """
@overload #Overload for threadCount in ['create']
def threadCount(n: int = ...) -> None:
    """threadCount is undoable, queryable, and NOT editable.
    
    This command sets the number of threads to be used by Maya in regions of code
    that are multithreaded. By default the number of threads is equal to the
    number of logical CPUs, not the number of physical CPUs. Logical CPUs are
    different from physical CPUs in the following ways:
    
    A physical CPU with hyperthreading counts as two logical CPUs
    A dual-core CPU counts as two logical CPUs
    
    With some workloads, using one thread per logical CPU may not perform well.
    This is sometimes the case with hyperthreading. It is worth experimenting with
    different numbers of threads to see which gives the best performance. Note
    that having more threads can mean Maya uses more memory.
    
    Setting a value of zero means the number of threads used will equal the number
    of logical processors in the system.

    ---
    - Args:
        - numberOfThreads (n): Sets the number of threads to use
    """
@overload #Overload for threadCount in ['create']
def threadCount(numberOfThreads: int = ..., n: int = ...) -> None:
    """threadCount is undoable, queryable, and NOT editable.
    
    This command sets the number of threads to be used by Maya in regions of code
    that are multithreaded. By default the number of threads is equal to the
    number of logical CPUs, not the number of physical CPUs. Logical CPUs are
    different from physical CPUs in the following ways:
    
    A physical CPU with hyperthreading counts as two logical CPUs
    A dual-core CPU counts as two logical CPUs
    
    With some workloads, using one thread per logical CPU may not perform well.
    This is sometimes the case with hyperthreading. It is worth experimenting with
    different numbers of threads to see which gives the best performance. Note
    that having more threads can mean Maya uses more memory.
    
    Setting a value of zero means the number of threads used will equal the number
    of logical processors in the system.

    ---
    - Args:
        - numberOfThreads (n): Sets the number of threads to use
    """
@overload #Overload for threadCount in ['query']
def threadCount(numberOfThreads: int = ..., query: bool = ...) -> None:
    """threadCount is undoable, queryable, and NOT editable.
    
    This command sets the number of threads to be used by Maya in regions of code
    that are multithreaded. By default the number of threads is equal to the
    number of logical CPUs, not the number of physical CPUs. Logical CPUs are
    different from physical CPUs in the following ways:
    
    A physical CPU with hyperthreading counts as two logical CPUs
    A dual-core CPU counts as two logical CPUs
    
    With some workloads, using one thread per logical CPU may not perform well.
    This is sometimes the case with hyperthreading. It is worth experimenting with
    different numbers of threads to see which gives the best performance. Note
    that having more threads can mean Maya uses more memory.
    
    Setting a value of zero means the number of threads used will equal the number
    of logical processors in the system.

    ---
    - Args:
        - numberOfThreads (n): Sets the number of threads to use
        - query (q): Query mode flag
    """
@overload #Overload for threadCount in ['query']
def threadCount(n: int = ..., q: bool = ...) -> None:
    """threadCount is undoable, queryable, and NOT editable.
    
    This command sets the number of threads to be used by Maya in regions of code
    that are multithreaded. By default the number of threads is equal to the
    number of logical CPUs, not the number of physical CPUs. Logical CPUs are
    different from physical CPUs in the following ways:
    
    A physical CPU with hyperthreading counts as two logical CPUs
    A dual-core CPU counts as two logical CPUs
    
    With some workloads, using one thread per logical CPU may not perform well.
    This is sometimes the case with hyperthreading. It is worth experimenting with
    different numbers of threads to see which gives the best performance. Note
    that having more threads can mean Maya uses more memory.
    
    Setting a value of zero means the number of threads used will equal the number
    of logical processors in the system.

    ---
    - Args:
        - numberOfThreads (n): Sets the number of threads to use
        - query (q): Query mode flag
    """
@overload #Overload for threadCount in ['query']
def threadCount(numberOfThreads: int = ..., n: int = ..., query: bool = ..., q: bool = ...) -> None:
    """threadCount is undoable, queryable, and NOT editable.
    
    This command sets the number of threads to be used by Maya in regions of code
    that are multithreaded. By default the number of threads is equal to the
    number of logical CPUs, not the number of physical CPUs. Logical CPUs are
    different from physical CPUs in the following ways:
    
    A physical CPU with hyperthreading counts as two logical CPUs
    A dual-core CPU counts as two logical CPUs
    
    With some workloads, using one thread per logical CPU may not perform well.
    This is sometimes the case with hyperthreading. It is worth experimenting with
    different numbers of threads to see which gives the best performance. Note
    that having more threads can mean Maya uses more memory.
    
    Setting a value of zero means the number of threads used will equal the number
    of logical processors in the system.

    ---
    - Args:
        - numberOfThreads (n): Sets the number of threads to use
        - query (q): Query mode flag
    """
@overload #Overload for threadCount in ['edit']
def threadCount(numberOfThreads: int = ..., edit: bool = ...) -> None:
    """threadCount is undoable, queryable, and NOT editable.
    
    This command sets the number of threads to be used by Maya in regions of code
    that are multithreaded. By default the number of threads is equal to the
    number of logical CPUs, not the number of physical CPUs. Logical CPUs are
    different from physical CPUs in the following ways:
    
    A physical CPU with hyperthreading counts as two logical CPUs
    A dual-core CPU counts as two logical CPUs
    
    With some workloads, using one thread per logical CPU may not perform well.
    This is sometimes the case with hyperthreading. It is worth experimenting with
    different numbers of threads to see which gives the best performance. Note
    that having more threads can mean Maya uses more memory.
    
    Setting a value of zero means the number of threads used will equal the number
    of logical processors in the system.

    ---
    - Args:
        - numberOfThreads (n): Sets the number of threads to use
        - edit (e): Edit mode flag
    """
@overload #Overload for threadCount in ['edit']
def threadCount(n: int = ..., e: bool = ...) -> None:
    """threadCount is undoable, queryable, and NOT editable.
    
    This command sets the number of threads to be used by Maya in regions of code
    that are multithreaded. By default the number of threads is equal to the
    number of logical CPUs, not the number of physical CPUs. Logical CPUs are
    different from physical CPUs in the following ways:
    
    A physical CPU with hyperthreading counts as two logical CPUs
    A dual-core CPU counts as two logical CPUs
    
    With some workloads, using one thread per logical CPU may not perform well.
    This is sometimes the case with hyperthreading. It is worth experimenting with
    different numbers of threads to see which gives the best performance. Note
    that having more threads can mean Maya uses more memory.
    
    Setting a value of zero means the number of threads used will equal the number
    of logical processors in the system.

    ---
    - Args:
        - numberOfThreads (n): Sets the number of threads to use
        - edit (e): Edit mode flag
    """
@overload #Overload for threadCount in ['edit']
def threadCount(numberOfThreads: int = ..., n: int = ..., edit: bool = ..., e: bool = ...) -> None:
    """threadCount is undoable, queryable, and NOT editable.
    
    This command sets the number of threads to be used by Maya in regions of code
    that are multithreaded. By default the number of threads is equal to the
    number of logical CPUs, not the number of physical CPUs. Logical CPUs are
    different from physical CPUs in the following ways:
    
    A physical CPU with hyperthreading counts as two logical CPUs
    A dual-core CPU counts as two logical CPUs
    
    With some workloads, using one thread per logical CPU may not perform well.
    This is sometimes the case with hyperthreading. It is worth experimenting with
    different numbers of threads to see which gives the best performance. Note
    that having more threads can mean Maya uses more memory.
    
    Setting a value of zero means the number of threads used will equal the number
    of logical processors in the system.

    ---
    - Args:
        - numberOfThreads (n): Sets the number of threads to use
        - edit (e): Edit mode flag
    """
