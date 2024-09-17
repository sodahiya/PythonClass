path = "/../"

if path.endswith("/"):
    path = path[:-1]
if "//" in path:
    path = path.replace("//", "/")
if "///" in path:
    path = path.replace("///", "/")
lst = []

while ".." in path:
    lst = list(path.split("/"))
    lst.pop((lst.index("..") - 1))
    lst.pop(lst.index(".."))
    path = "/"
    path += "/".join(lst)

print(path)