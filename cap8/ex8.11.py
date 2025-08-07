def validaString(msg, min, max):
    if len(msg) < min or len(msg) > max:
        return False
    else:
        return True
print(validaString('algum nome aq', 4, 8))