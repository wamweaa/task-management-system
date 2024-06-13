import ipdb

def start_debug():
    ipdb.set_trace()  # This will start the debugger at this point in the code

def debug_example():
    x = 10
    y = 20
    result = x + y
    print(f"The result is {result}")
    start_debug()  # Trigger the debugger here
    print("Continuing after debug")

if __name__ == "__main__":
    debug_example()
