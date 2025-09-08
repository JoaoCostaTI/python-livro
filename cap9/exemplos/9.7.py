with open('pagina.html', 'w', encoding='utf-8') as pagina:
    pagina.write("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Titulo da Página</title>
</head>
<body>
    Olá!
"""         
)
    for l in range(22):
        pagina.write(f"<p>{l}</p>\n")
    pagina.write("</body>")
    pagina.write("</html>")
