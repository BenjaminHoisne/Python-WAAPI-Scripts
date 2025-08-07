# WAAPI

Collection of python scripts using WAAPI to automate common tasks in Wwise project.
These tools help speed up workflows such as event creation, volume adjustment, and project auditing.

## Scripts

### CreateEventFromCSV  
- **Description**: Create Wwise events from a CSV file.
- **CSV Format**: Two columns - `name`, `path` (e.g., `Event_Play_Footstep`, `\Events\Footsteps\`)
- **Usage**: Runs the script, loads the CSV file, and creates events at the specified locations. It also creates the hierarchy in Wwise if necessary.

### SetVolumeOnSelectedObjects
- **Description**: Changes the volume of selected objects in Wwise.
- **Usage**: Select objects in Wwise, launches the script, requests the desired volume value (in dB) and applies it to the selection.

### CreateCSVFromSoundAndKeyword
- **Description**: Generates a CSV file listing objects containing a given keyword, with name, ID, path, and volume.
- **Usage**: Launches the script, enter a path for the CSV file, enter the keyword to sort among the objects.

### SetVolumeOnKeyword
- **Description**: Searches for objects containing a keyword and adjusts their volume.
- **Usage**: Runs the script, enter the keyword and the desired volume level.

### Audit Tool
- **Description**: Searches the project for objects of a given type and creates an audit CSV containing ID, name, path, type, number of children, parent, and duration.
- **Usage**: Runs the script, enters the object type (e.g., Sound, Event), and generates the CSV.
