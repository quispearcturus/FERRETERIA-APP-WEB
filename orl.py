import webbrowser

# Ruta del archivo de texto con las URLs
archivo_urls = 'linker.txt'

# Leer las URLs del archivo
with open(archivo_urls, 'r') as file:
    urls = file.readlines()

# Abrir cada URL en una nueva pestaña
for url in urls:
    webbrowser.open_new_tab(url.strip())
