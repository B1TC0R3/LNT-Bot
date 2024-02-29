from datetime import date, datetime

def info(message):
    print(f"[{datetime.now()}] \x1b[1m\x1b[32mINFO\x1b[0m {message}")

def warn(message):
    print(f"[{datetime.now()}] \x1b[1m\x1b[33mWARNING\x1b[0m {message}")

def error(message):
    print(f"[{datetime.now()}] \x1b[1m\x1b[31mERROR\x1b[0m {message}")
