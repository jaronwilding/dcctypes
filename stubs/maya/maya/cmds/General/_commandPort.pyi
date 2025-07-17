"""Stub files for General category in Maya commands, command: commandPort."""

from typing import Any, overload

@overload #Overload for commandPort in ['create']
def commandPort(bufferSize: int = ..., close: bool = ..., echoOutput: bool = ..., listPorts: bool = ..., name: str = ..., noreturn: bool = ..., pickleOutput: bool = ..., prefix: str = ..., returnNumCommands: bool = ..., securityWarning: bool = ..., sourceType: str = ...) -> bool:
    """commandPort is undoable, queryable, and NOT editable.
    
    Opens or closes the Maya command port. The command port comprises a socket to
    which a client program may connect. An example command port client "mcp" is
    included in the Motion Capture developers kit.
    
    It supports multi-byte commands and uses utf-8 as its transform format. It
    will receive utf8 command string and decode it to Maya native coding. The
    result will also be encoded to utf-8 before sending back.
    
    Care should be taken regarding INET domain sockets as no user identification,
    or authorization is required to connect to a given socket, and all commands
    (including "system(...)") are allowed and executed with the user id and
    permissions of the Maya user. The prefix flag can be used to reduce this
    security risk, as only the prefix command is executed.
    
    The query flag can be used to determine if a given command port exists. See
    examples below.

    Example:
    ```python
        import maya.cmds as cmds
        # Open a command port with the default name "mayaCommand".
        cmds.commandPort()
        # Close the command port with the default name. Open client connections
        # are not broken.
        cmds.commandPort( cl=True )
        # Query to see if the command command port "mayaCommand" exists.
        cmds.commandPort( 'mayaCommand', q=True )
    ```

    ---
    - Args:
        - bufferSize (bs): Commands and results are each subject to size limits. This option allows the user to specify the size of the buffer used to communicate with Maya. If unspecified the default buffer size is 4096 characters. Commands longer than bufferSize
            characters will cause the client connection to close. Results longer that bufferSize characters are replaced with an error message.
        - close (cl): Closes the commandPort, deletes the pipes
        - echoOutput (eo): Sends a copy of all command output to the command port. Typically only the result is transmitted. This option provides a copy of all output.
        - listPorts (lp): Returns the available ports
        - name (n): Specifies the name of the command port which this command creates. CommandPort names of the formnamecreate a UNIX domain socket on the localhost corresponding toname. Ifnamedoes not begin with "/", then /tmp/nameis used. Ifnamebegins with
            "/",namedenotes the full path to the socket. Names of the form :port numbercreate an INET domain on the local host at the given port.
        - noreturn (nr): Do not write the results from executed commands back to the command port socket. Instead, the results from executed commands are written to the script editor window. As no information passes back to the command port client regarding the
            execution of the submitted commands, care must be taken not to overflow the command buffer, which would cause the connection to close.
        - pickleOutput (po): Python output will be pickled.
        - prefix (pre): The string argument is the name of a Maya command taking one string argument. This command is called each time data is sent to the command port. The data written to the command port is passed as the argument to the prefix command. The data
            from the command port is encoded as with enocodeString and enclosed in quotes. If newline characters are embedded in the command port data, the input is split into individual lines. These lines are treated as if they were separate writes to
            the command port. Only the result to the last prefix command is returned.
        - returnNumCommands (rnc): Ignore the result of the command, but return the number of commands that have been read and executed in this call. This is a simple way to track buffer overflow. This flag is ignored when thenoreturnflag is specified.
        - securityWarning (sw): Enables security warning on command port input.
        - sourceType (stp): The string argument is used to indicate which source type would be passed to the commandPort, like "mel", "python". The default source type is "mel".
    """
@overload #Overload for commandPort in ['create']
def commandPort(bs: int = ..., cl: bool = ..., eo: bool = ..., lp: bool = ..., n: str = ..., nr: bool = ..., po: bool = ..., pre: str = ..., rnc: bool = ..., sw: bool = ..., stp: str = ...) -> bool:
    """commandPort is undoable, queryable, and NOT editable.
    
    Opens or closes the Maya command port. The command port comprises a socket to
    which a client program may connect. An example command port client "mcp" is
    included in the Motion Capture developers kit.
    
    It supports multi-byte commands and uses utf-8 as its transform format. It
    will receive utf8 command string and decode it to Maya native coding. The
    result will also be encoded to utf-8 before sending back.
    
    Care should be taken regarding INET domain sockets as no user identification,
    or authorization is required to connect to a given socket, and all commands
    (including "system(...)") are allowed and executed with the user id and
    permissions of the Maya user. The prefix flag can be used to reduce this
    security risk, as only the prefix command is executed.
    
    The query flag can be used to determine if a given command port exists. See
    examples below.

    Example:
    ```python
        import maya.cmds as cmds
        # Open a command port with the default name "mayaCommand".
        cmds.commandPort()
        # Close the command port with the default name. Open client connections
        # are not broken.
        cmds.commandPort( cl=True )
        # Query to see if the command command port "mayaCommand" exists.
        cmds.commandPort( 'mayaCommand', q=True )
    ```

    ---
    - Args:
        - bufferSize (bs): Commands and results are each subject to size limits. This option allows the user to specify the size of the buffer used to communicate with Maya. If unspecified the default buffer size is 4096 characters. Commands longer than bufferSize
            characters will cause the client connection to close. Results longer that bufferSize characters are replaced with an error message.
        - close (cl): Closes the commandPort, deletes the pipes
        - echoOutput (eo): Sends a copy of all command output to the command port. Typically only the result is transmitted. This option provides a copy of all output.
        - listPorts (lp): Returns the available ports
        - name (n): Specifies the name of the command port which this command creates. CommandPort names of the formnamecreate a UNIX domain socket on the localhost corresponding toname. Ifnamedoes not begin with "/", then /tmp/nameis used. Ifnamebegins with
            "/",namedenotes the full path to the socket. Names of the form :port numbercreate an INET domain on the local host at the given port.
        - noreturn (nr): Do not write the results from executed commands back to the command port socket. Instead, the results from executed commands are written to the script editor window. As no information passes back to the command port client regarding the
            execution of the submitted commands, care must be taken not to overflow the command buffer, which would cause the connection to close.
        - pickleOutput (po): Python output will be pickled.
        - prefix (pre): The string argument is the name of a Maya command taking one string argument. This command is called each time data is sent to the command port. The data written to the command port is passed as the argument to the prefix command. The data
            from the command port is encoded as with enocodeString and enclosed in quotes. If newline characters are embedded in the command port data, the input is split into individual lines. These lines are treated as if they were separate writes to
            the command port. Only the result to the last prefix command is returned.
        - returnNumCommands (rnc): Ignore the result of the command, but return the number of commands that have been read and executed in this call. This is a simple way to track buffer overflow. This flag is ignored when thenoreturnflag is specified.
        - securityWarning (sw): Enables security warning on command port input.
        - sourceType (stp): The string argument is used to indicate which source type would be passed to the commandPort, like "mel", "python". The default source type is "mel".
    """
@overload #Overload for commandPort in ['create']
def commandPort(bufferSize: int = ..., bs: int = ..., close: bool = ..., cl: bool = ..., echoOutput: bool = ..., eo: bool = ..., listPorts: bool = ..., lp: bool = ..., name: str = ..., n: str = ..., noreturn: bool = ..., nr: bool = ..., pickleOutput: bool = ..., po: bool = ..., prefix: str = ..., pre: str = ..., returnNumCommands: bool = ..., rnc: bool = ..., securityWarning: bool = ..., sw: bool = ..., sourceType: str = ..., stp: str = ...) -> bool:
    """commandPort is undoable, queryable, and NOT editable.
    
    Opens or closes the Maya command port. The command port comprises a socket to
    which a client program may connect. An example command port client "mcp" is
    included in the Motion Capture developers kit.
    
    It supports multi-byte commands and uses utf-8 as its transform format. It
    will receive utf8 command string and decode it to Maya native coding. The
    result will also be encoded to utf-8 before sending back.
    
    Care should be taken regarding INET domain sockets as no user identification,
    or authorization is required to connect to a given socket, and all commands
    (including "system(...)") are allowed and executed with the user id and
    permissions of the Maya user. The prefix flag can be used to reduce this
    security risk, as only the prefix command is executed.
    
    The query flag can be used to determine if a given command port exists. See
    examples below.

    Example:
    ```python
        import maya.cmds as cmds
        # Open a command port with the default name "mayaCommand".
        cmds.commandPort()
        # Close the command port with the default name. Open client connections
        # are not broken.
        cmds.commandPort( cl=True )
        # Query to see if the command command port "mayaCommand" exists.
        cmds.commandPort( 'mayaCommand', q=True )
    ```

    ---
    - Args:
        - bufferSize (bs): Commands and results are each subject to size limits. This option allows the user to specify the size of the buffer used to communicate with Maya. If unspecified the default buffer size is 4096 characters. Commands longer than bufferSize
            characters will cause the client connection to close. Results longer that bufferSize characters are replaced with an error message.
        - close (cl): Closes the commandPort, deletes the pipes
        - echoOutput (eo): Sends a copy of all command output to the command port. Typically only the result is transmitted. This option provides a copy of all output.
        - listPorts (lp): Returns the available ports
        - name (n): Specifies the name of the command port which this command creates. CommandPort names of the formnamecreate a UNIX domain socket on the localhost corresponding toname. Ifnamedoes not begin with "/", then /tmp/nameis used. Ifnamebegins with
            "/",namedenotes the full path to the socket. Names of the form :port numbercreate an INET domain on the local host at the given port.
        - noreturn (nr): Do not write the results from executed commands back to the command port socket. Instead, the results from executed commands are written to the script editor window. As no information passes back to the command port client regarding the
            execution of the submitted commands, care must be taken not to overflow the command buffer, which would cause the connection to close.
        - pickleOutput (po): Python output will be pickled.
        - prefix (pre): The string argument is the name of a Maya command taking one string argument. This command is called each time data is sent to the command port. The data written to the command port is passed as the argument to the prefix command. The data
            from the command port is encoded as with enocodeString and enclosed in quotes. If newline characters are embedded in the command port data, the input is split into individual lines. These lines are treated as if they were separate writes to
            the command port. Only the result to the last prefix command is returned.
        - returnNumCommands (rnc): Ignore the result of the command, but return the number of commands that have been read and executed in this call. This is a simple way to track buffer overflow. This flag is ignored when thenoreturnflag is specified.
        - securityWarning (sw): Enables security warning on command port input.
        - sourceType (stp): The string argument is used to indicate which source type would be passed to the commandPort, like "mel", "python". The default source type is "mel".
    """
