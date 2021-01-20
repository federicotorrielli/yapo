from models import *

repo = Repository()

for item in repo.get_items():
    print(item)

# for item in repo.get_items(item_id="1"):
#     print(item)

for item in repo.get_vocabularies():
    print(item)

# for item in repo.get_property("https://evilscript.altervista.org/productCatalog.owl#EAN"):
#     print(item)