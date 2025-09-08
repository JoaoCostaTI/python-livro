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
        for e in v:
            pagina.write(f"<ul><li>{e}</li></ul>\n")
    pagina.write("</body></html>")