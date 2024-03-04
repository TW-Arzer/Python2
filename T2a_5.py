import os, sys

if __name__ == "__main__":
    with os.scandir(".") as files:
        for i, file in enumerate(sorted([f for f in files if f.is_file() and f.name.startswith("test") and f.name[-4:].lower() == ".txt"], key=lambda x: x.name)):
            print(i, file.name)
            nouveau_nom = str(i + 1) + ".txt"

            print("On renomme \"" + file.name + "\" en \"" + nouveau_nom + "\"", file=sys.stderr)
            os.rename(file, nouveau_nom)

