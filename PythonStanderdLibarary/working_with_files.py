from pathlib import Path
from time import ctime
import shutil

path = Path("Modules/ecommerce/__init__.py")
print(path.exists())
# rename
# path.rename("init.txt")

# delete the file
# path.unlink()

# path information
print(ctime(path.stat().st_ctime))

# reading content
print(path.read_text())


# copying and pasting files using path which is not ideal for ding this stupff using python
source = Path("Modules/ecommerce/__init__.py")
target = Path() / "__init__.py"

# target.write_text(source.read_text())
shutil.copy(source, target)
