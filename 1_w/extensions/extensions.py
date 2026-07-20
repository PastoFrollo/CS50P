def main():
    name = input("File name: ").lower().lstrip()
    type = media_type(name)
    print(type)

def media_type(extension):
    if ".gif" in extension:
        return "image/gif"
    elif ".jpg" in extension:
        return "image/jpg"
    elif ".jpeg" in extension:
        return "image/jpeg"
    elif ".png" in extension:
        return "image/png"
    elif ".pdf" in extension:
        return "application/pdf"
    elif ".txt" in extension:
        return "text/txt"
    elif ".zip" in extension:
        return "application/zip"
    else:
        return "application/octet-stream"
    
main()