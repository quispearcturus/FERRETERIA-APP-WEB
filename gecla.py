import ast

# Leemos el contenido del archivo 'my_Script.py'
with open('apps\sales\models\\sale.py', 'r') as file:
    script_content = file.read()

# Parseamos el código fuente a un árbol de sintaxis abstracta
tree = ast.parse(script_content)

# Buscamos las clases en el árbol de sintaxis
for node in tree.body:
    if isinstance(node, ast.ClassDef):  # Verificamos si es una clase
        print(f"Clase encontrada: {node.name}")
        
        # Iteramos sobre las declaraciones dentro de la clase (atributos, métodos, etc.)
        class_attributes = []
        for class_node in node.body:
            if isinstance(class_node, ast.Assign):  # Si es una asignación, es un atributo
                for target in class_node.targets:
                    if isinstance(target, ast.Name):
                        class_attributes.append(target.id)

        # Imprimimos los atributos de la clase
        print(f"Atributos de la clase {node.name}: {class_attributes}")
        print('---')

# # Llamamos a la función y mostramos los nombres de las clases
# nombres_de_clases = obtener_clases('apps\sales\models\\voucher.py')
# text = f"from apps.sales.models.voucher import {', '.join(nombres_de_clases)}"
# for i in nombres_de_clases:
#     print(f"admin.site.register({i})")
# # print(text)
