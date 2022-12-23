from dotenv import load_dotenv
from collector import StreamManager

if __name__ == "__main__":
    load_dotenv()
    manager = StreamManager()
    manager.test()
