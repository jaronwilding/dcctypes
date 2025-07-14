"""Stub files for General category in Maya commands, command: commandLogging."""

from typing import Any, overload

@overload #Overload for commandLogging in ['create']
def commandLogging(historySize: int = ..., logCommands: bool = ..., logFile: str = ..., recordCommands: bool = ..., resetLogFile: bool = ...) -> None:
    """commandLogging is undoable, queryable, and NOT editable.
    
    This command controls logging of Maya commands, in memory and on disk.
    
    Note that if commands are logged in memory, they will be available to the
    crash reporter and appear in crash logs.

    ---
    - Args:
        - historySize (hs): Sets the number of entries in the in-memory command history.
        - logCommands (lc): Enables or disables the on-disk logging of commands.
        - logFile (lf): Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.
        - recordCommands (rc): Enables or disables the in-memory logging of commands.
        - resetLogFile (rl): Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).
    """
@overload #Overload for commandLogging in ['create']
def commandLogging(hs: int = ..., lc: bool = ..., lf: str = ..., rc: bool = ..., rl: bool = ...) -> None:
    """commandLogging is undoable, queryable, and NOT editable.
    
    This command controls logging of Maya commands, in memory and on disk.
    
    Note that if commands are logged in memory, they will be available to the
    crash reporter and appear in crash logs.

    ---
    - Args:
        - historySize (hs): Sets the number of entries in the in-memory command history.
        - logCommands (lc): Enables or disables the on-disk logging of commands.
        - logFile (lf): Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.
        - recordCommands (rc): Enables or disables the in-memory logging of commands.
        - resetLogFile (rl): Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).
    """
@overload #Overload for commandLogging in ['create']
def commandLogging(historySize: int = ..., hs: int = ..., logCommands: bool = ..., lc: bool = ..., logFile: str = ..., lf: str = ..., recordCommands: bool = ..., rc: bool = ..., resetLogFile: bool = ..., rl: bool = ...) -> None:
    """commandLogging is undoable, queryable, and NOT editable.
    
    This command controls logging of Maya commands, in memory and on disk.
    
    Note that if commands are logged in memory, they will be available to the
    crash reporter and appear in crash logs.

    ---
    - Args:
        - historySize (hs): Sets the number of entries in the in-memory command history.
        - logCommands (lc): Enables or disables the on-disk logging of commands.
        - logFile (lf): Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.
        - recordCommands (rc): Enables or disables the in-memory logging of commands.
        - resetLogFile (rl): Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).
    """
@overload #Overload for commandLogging in ['query']
def commandLogging(historySize: int = ..., logCommands: bool = ..., logFile: str = ..., recordCommands: bool = ..., resetLogFile: bool = ..., query: bool = ...) -> None:
    """commandLogging is undoable, queryable, and NOT editable.
    
    This command controls logging of Maya commands, in memory and on disk.
    
    Note that if commands are logged in memory, they will be available to the
    crash reporter and appear in crash logs.

    ---
    - Args:
        - historySize (hs): Sets the number of entries in the in-memory command history.
        - logCommands (lc): Enables or disables the on-disk logging of commands.
        - logFile (lf): Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.
        - recordCommands (rc): Enables or disables the in-memory logging of commands.
        - resetLogFile (rl): Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).
        - query (q): Query mode flag
    """
@overload #Overload for commandLogging in ['query']
def commandLogging(hs: int = ..., lc: bool = ..., lf: str = ..., rc: bool = ..., rl: bool = ..., q: bool = ...) -> None:
    """commandLogging is undoable, queryable, and NOT editable.
    
    This command controls logging of Maya commands, in memory and on disk.
    
    Note that if commands are logged in memory, they will be available to the
    crash reporter and appear in crash logs.

    ---
    - Args:
        - historySize (hs): Sets the number of entries in the in-memory command history.
        - logCommands (lc): Enables or disables the on-disk logging of commands.
        - logFile (lf): Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.
        - recordCommands (rc): Enables or disables the in-memory logging of commands.
        - resetLogFile (rl): Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).
        - query (q): Query mode flag
    """
@overload #Overload for commandLogging in ['query']
def commandLogging(historySize: int = ..., hs: int = ..., logCommands: bool = ..., lc: bool = ..., logFile: str = ..., lf: str = ..., recordCommands: bool = ..., rc: bool = ..., resetLogFile: bool = ..., rl: bool = ..., query: bool = ..., q: bool = ...) -> None:
    """commandLogging is undoable, queryable, and NOT editable.
    
    This command controls logging of Maya commands, in memory and on disk.
    
    Note that if commands are logged in memory, they will be available to the
    crash reporter and appear in crash logs.

    ---
    - Args:
        - historySize (hs): Sets the number of entries in the in-memory command history.
        - logCommands (lc): Enables or disables the on-disk logging of commands.
        - logFile (lf): Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.
        - recordCommands (rc): Enables or disables the in-memory logging of commands.
        - resetLogFile (rl): Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).
        - query (q): Query mode flag
    """
@overload #Overload for commandLogging in ['edit']
def commandLogging(historySize: int = ..., logCommands: bool = ..., logFile: str = ..., recordCommands: bool = ..., resetLogFile: bool = ..., edit: bool = ...) -> None:
    """commandLogging is undoable, queryable, and NOT editable.
    
    This command controls logging of Maya commands, in memory and on disk.
    
    Note that if commands are logged in memory, they will be available to the
    crash reporter and appear in crash logs.

    ---
    - Args:
        - historySize (hs): Sets the number of entries in the in-memory command history.
        - logCommands (lc): Enables or disables the on-disk logging of commands.
        - logFile (lf): Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.
        - recordCommands (rc): Enables or disables the in-memory logging of commands.
        - resetLogFile (rl): Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).
        - edit (e): Edit mode flag
    """
@overload #Overload for commandLogging in ['edit']
def commandLogging(hs: int = ..., lc: bool = ..., lf: str = ..., rc: bool = ..., rl: bool = ..., e: bool = ...) -> None:
    """commandLogging is undoable, queryable, and NOT editable.
    
    This command controls logging of Maya commands, in memory and on disk.
    
    Note that if commands are logged in memory, they will be available to the
    crash reporter and appear in crash logs.

    ---
    - Args:
        - historySize (hs): Sets the number of entries in the in-memory command history.
        - logCommands (lc): Enables or disables the on-disk logging of commands.
        - logFile (lf): Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.
        - recordCommands (rc): Enables or disables the in-memory logging of commands.
        - resetLogFile (rl): Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).
        - edit (e): Edit mode flag
    """
@overload #Overload for commandLogging in ['edit']
def commandLogging(historySize: int = ..., hs: int = ..., logCommands: bool = ..., lc: bool = ..., logFile: str = ..., lf: str = ..., recordCommands: bool = ..., rc: bool = ..., resetLogFile: bool = ..., rl: bool = ..., edit: bool = ..., e: bool = ...) -> None:
    """commandLogging is undoable, queryable, and NOT editable.
    
    This command controls logging of Maya commands, in memory and on disk.
    
    Note that if commands are logged in memory, they will be available to the
    crash reporter and appear in crash logs.

    ---
    - Args:
        - historySize (hs): Sets the number of entries in the in-memory command history.
        - logCommands (lc): Enables or disables the on-disk logging of commands.
        - logFile (lf): Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.
        - recordCommands (rc): Enables or disables the in-memory logging of commands.
        - resetLogFile (rl): Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).
        - edit (e): Edit mode flag
    """
