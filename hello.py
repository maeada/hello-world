import os
from dotenv import load_dotenv
import random

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

def demo3():
    """Generate a random number between 1 and 10."""
    num = 5
    for i in range(num):
        x = random.randint(1, 10)
        print(f"Random number[{i}]: {x}")


if __name__ == "__main__":
    # demo1()
    # demo2()
    demo3()