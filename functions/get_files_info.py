import os

def get_files_info(working_directory, directory=None):
    # normalize
    root = os.path.abspath(working_directory)

    # if directory == None or ".", treat it as root
    target_rel = directory or "."

    # join & normalize
    candidate = os.path.abspath(os.path.join(root, target_rel))

    # make sure directory is still under root 
    if not (candidate == root or candidate.startswith(root + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside permitted working directory'

    # assure directory exists and is directory
    if not os.path.isdir(candidate):
        return f'Error: "{directory}" is not a directory'
    
    entries = []
    try:
        for name in os.listdir(candidate):
            full = os.path.join(candidate, name)
            size = os.path.getsize(full)
            is_dir = os.path.isdir(full)
            entries.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
    except Exception as e:
        return f"Error: {e}"
    
    return "\n".join(entries)
