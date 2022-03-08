import os

def main():
    name = os.environ.get("Name")
    print(name)
    
if __name__ == "__main__":
    main()