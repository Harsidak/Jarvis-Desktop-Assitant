import os
import shutil
import comtypes
import sys

def clear_comtypes_cache():
    try:
        # Get the cache directory
        gen_dir = comtypes.client._gen_dir
        print(f"Comtypes cache directory: {gen_dir}")
        
        if os.path.exists(gen_dir):
            print("Removing cache directory contents...")
            # We want to keep the __init__.py if possible, or just nuke the folder and let comtypes recreation it.
            # Comtypes usually recreates it.
            for item in os.listdir(gen_dir):
                if item == "__init__.py":
                    continue
                path = os.path.join(gen_dir, item)
                try:
                    if os.path.isdir(path):
                        shutil.rmtree(path)
                    else:
                        os.remove(path)
                    print(f"Deleted: {item}")
                except Exception as e:
                    print(f"Failed to delete {item}: {e}")
            print("Cache cleared.")
        else:
            print("Cache directory not found.")
            
    except Exception as e:
        print(f"Error clearing cache: {e}")

if __name__ == "__main__":
    clear_comtypes_cache()
