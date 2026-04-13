import sys

DEBUG = True

def __epsilon(n, states, transitions):
    set_states = set(states)

    ret = set([])
    visited = [False] * n
    while set_states:
        curr = set_states.pop()
        visited[curr - 1] = True
        ret.add(curr)
        
        for t in transitions:
            if (int(t[0]) == curr and t[1] == 'E') and not visited[int(t[2]) - 1]:
                set_states.add(int(t[2]))
    return ret



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
        
    if(not input_string):
        input_string = input("Enter input string: ")

    if DEBUG:
        print(f'Using input \"{input_string}\"...')
    
    states = set([start])                  # start simulation at the start state
    states = (__epsilon(n, states, transitions))
    i = 0                           # counter for grabbing correct character
    while(i < len(input_string)):
        char = input_string[i]      # char: current character being checked
        next_states = set()
        # Check all possible routes for transitioning to this character
        for curr in states:         # curr: curr state being checked
            for t in transitions:
                if(int(t[0]) == curr) and t[1] == char:
                    next_states.add(int(t[2]))
        next_states = (__epsilon(n, next_states, transitions))
        states = next_states
        if(len(states) == 0):
            print("False")
            return 0
        i += 1
    for accept_state in accept:
        if accept_state in states:
            print("True")
            return 1
    print("False")
    return 0


    
if __name__=="__main__":
    main()