import time
from copy import deepcopy
import numpy as np


# takes the input of current states and evaluvates the best path to goal state
def bestsolution(state):
    bestsol = np.array([], int).reshape(-1, 16)
    count = len(state) - 1
    while count != -1:
        bestsol = np.insert(bestsol, 0, state[count]['puzzle'], 0)
        count = (state[count]['parent'])
    'print(bestsol.reshape(-1, 4, 4))'
    return bestsol.reshape(-1, 4, 4)


# this function checks for the uniqueness of the iteration(it) state, weather it has been previously traversed or not.
def all(checkarray):
    set = []
    for it in set:
        for checkarray in it:
            return 1
        else:
            return 0

# this function calculates the manhattan distance
def heuristic(puzzle, goal):
    a = abs(puzzle // 4 - goal // 4)
    b = abs(puzzle % 4 - goal % 4)
    mhcost = a + b
    'print(sum(mhcost[1:]))'
    return sum(mhcost[1:])


# will indentify the coordinates of each of goal or initial state values
def coordinates(puzzle):
    pos = np.array(range(16))
    for p, q in enumerate(puzzle):
        pos[q] = p
    'print(pos)'
    return pos


def evaluate(puzzle, goal):
    steps = np.array([('up', [0, 1, 2, 3], -4), ('down', [12, 13, 14, 15], 4), ('left', [0, 4, 8, 12], -1), ('right', [3, 7, 11, 15], 1)],
                     dtype=[('move', str, 1), ('position', list), ('head', int)])

    'print(steps)'
    dtstate = [('puzzle', list), ('parent', int), ('gn', int), ('hn', int)] #datatype

    'print("check 1")'
    costg = coordinates(goal)
    parent = -1
    gn = 0

    'print("check 2")'
    hn = heuristic(coordinates(puzzle), costg)

    'print("check 3")'
    state = np.array([(puzzle, parent, gn, hn)], dtstate)

    # We make use of priority queues with position as keys and fn as value.
    dtpriority = [('position', int), ('fn', int)]
    priority = np.array([(0, hn)], dtpriority)

    while 1:
        priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])
        position, fn = priority[0]
        priority = np.delete(priority, 0, 0)
        # sort priority queue using merge sort,the first element is picked for exploring remove from queue what we are exploring
        puzzle, parent, gn, hn = state[position]
        puzzle = np.array(puzzle)
        # Identify the blank(0) square in input
        blank0 = int(np.where(puzzle == 0)[0])
        # Identify the blank(1) square in input
        blank1 = int(np.where(puzzle == 1)[0])
        '''print("blank0: ", blank0)
        print("blank1: ", blank1)'''
        gn = gn + 1  #path cost
        c = 1  # purpose of c?
        start_time = time.time()
        for s in steps:
            c = c + 1  #why?
            if blank0 not in s['position']:
                # generate new state as copy of current
                openstates = deepcopy(puzzle)
                #swap
                openstates[blank0], openstates[blank0 + s['head']] = openstates[blank0 + s['head']], openstates[blank0]
                # The all function is called, if the node has been previously explored or not
                if ~(np.all(list(state['puzzle']) == openstates, 1)).any():
                    end_time = time.time()
                    if ((end_time - start_time) > 2):
                        print(" The 8 puzzle is unsolvable ! \n")
                        exit

                    hn = heuristic(coordinates(openstates), costg) # manhattan distance
                    # generate and add new state in the list
                    q = np.array([(openstates, position, gn, hn)], dtstate)
                    state = np.append(state, q, 0)
                    # f(n) is the sum of cost to reach node and the cost to rech fromt he node to the goal state
                    fn = gn + hn  # path cost + heuristic

                    'print("check 4")'
                    q = np.array([(len(state) - 1, fn)], dtpriority)
                    priority = np.append(priority, q, 0)
                    # Checking if the node in openstates are matching the goal state.
                    if np.array_equal(openstates, goal):
                        return state, len(priority)

            if blank1 not in s['position']:
                # generate new state as copy of current
                openstates = deepcopy(puzzle)
                #swap
                openstates[blank1], openstates[blank1 + s['head']] = openstates[blank1 + s['head']], openstates[blank1]
                # The all function is called, if the node has been previously explored or not
                if ~(np.all(list(state['puzzle']) == openstates, 1)).any():
                    end_time = time.time()
                    if ((end_time - start_time) > 2):
                        print(" The 8 puzzle is unsolvable ! \n")
                        exit

                    hn = heuristic(coordinates(openstates), costg)  #manhattan distance
                    # generate and add new state in the list
                    q = np.array([(openstates, position, gn, hn)], dtstate)
                    state = np.append(state, q, 0)
                    # f(n) is the sum of cost to reach node and the cost to rech fromt he node to the goal state
                    fn = gn + hn  # path cost + heuristic

                    'print("check 5")'
                    q = np.array([(len(state) - 1, fn)], dtpriority)
                    'print(q)'
                    priority = np.append(priority, q, 0)
                    # Checking if the node in openstates are matching the goal state.
                    if np.array_equal(openstates, goal):
                        return state, len(priority)

    return state, len(priority)


def solve(puzzle, goal):
    state, visited = evaluate(puzzle, goal)
    bestpath = bestsolution(state)
    totalmoves = len(bestpath) - 1
    visit = len(state) - visited
    return totalmoves, visit, len(state)



