from pathlib import Path

path = Path("Modules/ecommerce")

print("Exists:", path.exists())
# path.mkdir()
# path.rmdir()
# path.rename("modules")

print(path.iterdir())
for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir() if p.is_dir()]
# get all file recursilvery
py_files = [p for p in path.rglob("**/*.py")]
print(py_files)
