# menu.py
class MenuItem:
    def __init__(self, name, url, children=None):
        self.name = name
        self.url = url
        self.children = children if children else []

    def __str__(self):
        return f"{self.name} ({self.url})"

# Definir el menú
menu = [
    MenuItem("Inicio", "/"),
    MenuItem("Productos", "/productos", [
        MenuItem("Categoría 1", "/productos/categoria-1"),
        MenuItem("Categoría 2", "/productos/categoria-2")
    ]),
    MenuItem("Contacto", "/contacto")
]

for item in menu:     
    print(item.name)  
    if item.children:
        for child in item.children:
            print(child.name)