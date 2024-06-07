from serialListen import listen, control


if __name__ == "__main__":
    while True:
        try:
            data = listen()
            if data:
                control(data)
        except KeyboardInterrupt:
            print("KEYBOARD INTERRUPTED")
