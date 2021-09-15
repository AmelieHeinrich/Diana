class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger:
    def info(message):
        print(bcolors.OKGREEN, '')
        print(message)
        print(bcolors.ENDC, '')

    def error(message):
        print(bcolors.FAIL, '')
        print(message)
        print(bcolors.ENDC, '')

    def warn(message):
        print(bcolors.WARNING, '')
        print(message)
        print(bcolors.ENDC, '')

    def fatal(message):
        print(bcolors.FAIL, '')
        print(message)
        print(bcolors.ENDC, '')
        
        raise Exception(f"Fatal point hit! {message}")