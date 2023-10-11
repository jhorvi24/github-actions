import os 

def main():
    nombre = os.getenv("USERNAME")
    lenguaje = os.getenv("LANGUAGE")
    print(f"!Hi, {nombre} World desde GitHub usando {lenguaje}")


if __name__=='__main__':
    main()