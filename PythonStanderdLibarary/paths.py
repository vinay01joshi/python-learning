from pathlib import Path

# row string in windows
print("Path", Path(r"C:\Program Files\Microsoft"))

#Mac or Liunx
print(Path("/user/local/bin"))

# Current direcotry Path
print(Path())

# Relavitve Path
print(Path("../Modules/ecommerce/__init.py"))

# combining the Path
print(Path() / "ecommerce")

# Home direcotry of the user
print(Path().home())


path = Path("Modules/ecommerce/__init__.py")
print("Path Is Exists", path.exists())
print("Path is File", path.is_file())
print("Path is Dir", path.is_dir())
print("File Name in the Path", path.name)
print("Path stem", path.stem)
print("File extenstion", path.suffix)
print(path.parent)
path = path.with_name("file.txt")
print(path)
print(path.absolute())
