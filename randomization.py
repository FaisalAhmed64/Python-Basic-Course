from pathlib import Path

# absulate path
# c:\programme Files\Microsoft
# /user/local/bin
# relative path


path = Path()
for file in path.glob("*.py"):
    print(file)
print(path.glob("*.py"))
path = Path("ecommerce")
path = Path("emails")
print(path.exists())
print(path.exists())
