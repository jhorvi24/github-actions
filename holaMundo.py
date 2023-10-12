import os 

def main():
    nombre = os.getenv("USERNAME")
    print(f"!Hi, {nombre} World desde GitHub")


if __name__=='__main__':
    main()