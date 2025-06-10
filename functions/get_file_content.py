import os

def get_file_content(working_directory, directory=None):
    # normalize
    root = os.path.abspath(working_directory)

    # if directory == None or ".", treat it as root
    target_rel = directory or "."

    # join & normalize
    candidate = os.path.abspath(os.path.join(root, target_rel))

    # make sure directory is still under root 
    if not candidate.startswith(root + os.sep):
        return f'Error: Cannot list "{directory}" as it is outside permitted working directory'

    # check if this is a file, read & return metadata if so
    if os.path.isfile(candidate):
        try:
            size = os.path.getsize(candidate)
            is_dir = os.path.isdir(candidate)

            MAX_CHARS = 10000
            with open(candidate, "r") as f:
                chunk = f.read(MAX_CHARS + 1)
            if len(chunk) > MAX_CHARS:
                content = chunk[:MAX_CHARS]
                truncated = True
            else:
                content = chunk
                truncated = False
        except Exception as e:
            return f"Error: {e}"
        
        #metadata formatting
        name = os.path.basename(candidate)
        metadata = f" - {name}: file_size{size} bytes, is_dir={is_dir}"

        if truncated:
            content += f'\n[...File "{candidate}" truncated at {MAX_CHARS} characters]'
        
        return metadata + "\n" + content
