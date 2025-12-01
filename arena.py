import webbrowser

url = "https://www.youtube.com/watch?v=LoT9H_OgyrI"

download = url[:12] + 'ss' + url[12:]

webbrowser.open(download)