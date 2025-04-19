import os
from dotenv import load_dotenv

def demo1():
    print("hello world")

def demo2():
    """Load environment variables from .env file and print them."""
    # Load .env file to environment
    load_dotenv()

    API = os.getenv('API')
    print(f"API: {API}")

    user_name = os.getenv("USERNAME")
    print(f"USERNAME: {user_name}")

if __name__ == "__main__":
    print(demo1())
    print(demo2())