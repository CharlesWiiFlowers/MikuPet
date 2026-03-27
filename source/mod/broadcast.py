class AppBroadcast():
    def __init__(self, settings):
        super().__init__()
        self.running = True
        threading.Thread(target=self.listen_to_console, daemon=True).start()
        self.settings = settings
        
        # Create the main window
        
        
    def listen_to_console(self):
        self.global_broadcast(f"Loaded SETTINGS: \n{self.settings}")
        while self.running:
            # This thread can be used to listen to console input or other events
            try:
                command = input()
                if command.lower() == 'miku bye' or command.lower() == 'bye':
                    self.running = False
                    self.broadcast("Goodbye~!! 💕👋.")
                    self.stop()
                elif command.lower() == 'miku hello' or command.lower() == 'hello':
                    self.broadcast("Hello~!! 💕")
                elif command.lower() == 'how are you' or command.lower() == 'how are you?' or command.lower() == 'miku how are you':
                    self.broadcast("I am fine, thank you~!! 💕")
                else:
                    self.broadcast("I do not understand you~ 🥺")
            except EOFError as e:
                warnings.warn(f"Error: {e}")
                break
    
    def broadcast(self, text:str):
        print(f"Miku: {text}")

    def global_broadcast(self, text:str):
        print(f"[SYSTEM]: {text}")

    def run(self):
        # This thread can be used for broadcasting messages or handling background tasks
        pass