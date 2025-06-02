from bot import send_message

def run_notifier():
    send_message('Reminder from service')
    
    
if __name__ == "__main__":
    run_notifier()
    print("Service has been executed.")