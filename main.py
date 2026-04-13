import sys

DEBUG = True

def main():
    file = None
    input_string = None
    text = None

    if len(sys.argv) > 1:
        file = sys.argv[1]
    if len(sys.argv) > 2:
        input_string = sys.argv[2]

    while(not text):
        if(not file):
            file = input("Enter file name: ")
        try:
            text = open(file)
        except OSError:
            print(f"Failed to open file {file}, try again")
            file = None

    # PARSING #
    n = int(text.readline().strip())            # No. of states
    start = int(text.readline().strip())        # Start state

    k = int(text.readline().strip())            # number of accept states
    accept = []
    for i in range(k):
        accept.append(int(text.readline().strip())) # accept states

    alphabet = list(text.readline().strip())    # alphabet; guaranteed no repeats

    t = int(text.readline().strip())            # number of transitions
    transitions = []
    for i in range(t):
        transitions.append(text.readline().strip().split(','))
    text.close()

    # SIMULATING #
    if DEBUG:
        print(f'===NFA @ {file}===\n'
            f'number of states: {n}\n'
            f'start state: {start}\n'
            f'symbols: {alphabet}\n'
            f'accept states: {accept}\n'
            f'transitions: {transitions}\n======')
    
if __name__=="__main__":
    main()