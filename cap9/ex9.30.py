filmes = {
    "drama":["Poderoso Chefão", 'Algum outro Drama'],
    "Comédia": ["American Pie", 'Alguma outra comédia'],
    "guerra": ['Rambo', 'Caixão tiro']
}
with open('filmes.html', 'w', encoding='utf-8') as pagina:
    pagina.write(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
            <title>Filmes</title>
        </head>
        <body>
        """
    )
    for c, v in filmes.items():
        pagina.write(f"<h1>{c}</h1>\n")
        pagina.write("<ul>")
        for e in v:
            pagina.write(f"<li>{e}</li>\n")
        pagina.write("</ul>")
    pagina.write("</body></html>")