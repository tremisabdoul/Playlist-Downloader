from os import popen, startfile
from platform import system


def remove_until(path: str, delimiter: str):
    l = len(delimiter)
    while len(path) >= l:
        if delimiter == path[:l]:
            return path[l:len(path)]
        path = path[1:len(path)]
    return None


def remove_from(path: str, delimiter: str):
    l = len(delimiter)
    buffer = ""
    while len(path) >= l:
        if delimiter == path[len(path)-l:len(path)]:
            return path
        path = path[:len(path)-1]
    return None


def main():
    OS = system()
    print("\nInstalling youtube-search-python...")
    print(popen("pip install youtube-search-python").read())
    print("\nInstalling pytube...")
    print(popen("pip install pytube").read())
    
    path = popen("pip -V").read()

    path = remove_until(path, " from ")
    if OS == "Windows":
        path = remove_from(path, "\\Lib\\site-packages\\")
    else:
        path = remove_from(path, "/Lib/site-packages/")
    path += "pytube"
    
    startfile(path)
    print("\nREADME ! - README ! - README ! - README ! - README ! - README ! - README ! - README ! - README !")
    print("README ! - README ! - README ! - README ! - README ! - README ! - README ! - README ! - README !")
    print("README ! - README ! - README ! - README ! - README ! - README ! - README ! - README ! - README !\n")
    print("You have to fix the library that I just open for you.")
    print("Currnt fix: Change the function_patterns array in cipher.py at line 264 to include this:")
    print("function_patterns = [")
    print("\t# https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377")
    print("\t# https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8")
    print("\t# var Bpa = [iha];")
    print("\t# ...")
    print("\t# a.C && (b = a.get(\"n\")) && (b = Bpa[0](b), a.set(\"n\", b),")
    print("\t# Bpa.length || iha("")) }};")
    print("\t# In the above case, `iha` is the relevant function name")
    print("\tr'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\(\"n\"\)\)\s*&&.*?\|\|\s*([a-z]+)',")
    print("\tr'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',")
    print("\tr'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',")
    print("]")
    print("\nIf it does not fix your issue search this:")
    print("\tpytube RegexMatchError: get_throttling_function_name: could not find match for multiple")
    print("\nREADME ! - README ! - README ! - README ! - README ! - README ! - README ! - README ! - README !")
    print("README ! - README ! - README ! - README ! - README ! - README ! - README ! - README ! - README !")
    print("README ! - README ! - README ! - README ! - README ! - README ! - README ! - README ! - README !\n\n")

    x = ""
    while x != "i did read this":
        x = input('Write "i did read this" then enter to exit')
    
    return None


main()
