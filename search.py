# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    """
    Depth first search can be implemented by using the stack data structure.The pacman position in maze,direction
    and cost list is initialised.
    The initial state is pushed into the stack and the stack elements are looped
    until the stack is empty.If the next position of the visited node is goal state then
    the path is returned otherwise it is pushed into the stack and is marked visited
    """
    dfsstack = util.Stack()
    initialnode = (problem.getStartState(), [], [])
    dfsstack.push( initialnode )
    visited = []

    while not dfsstack.isEmpty():
        currentnode, currentaction , currentcost = dfsstack.pop()

        if(not currentnode in visited):
            visited.append(currentnode)

            if problem.isGoalState(currentnode):
                return currentaction

            for nextnode, nextaction, nextcost in problem.getSuccessors(currentnode):
                nextstate = (nextnode, currentaction +[nextaction], currentcost + [nextcost])
                dfsstack.push(nextstate)

    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    """
    Breadth first search is implemented by using the queue data structure
    hence, queue can be used to finding the path.Based on the util.py,push and pop
    is implemented for queue.The starting position, action to be performed is pushed into the queue.
    The state depicts the coordinate of the pacman in the
    maze, its direction and cost lists.Actions have cost associated with it.
    The visited positions is marked visited on the list,
    The queue starting state is popped out and then the neighbours
    are checked. If the position is the goal state then path is returned otherwise state is
    pushed into the queue and the position is marked visited in the list.
    """
    bfsqueue = util.Queue()
    initialnode = (problem.getStartState(), [], [])
    bfsqueue.push( initialnode )
    visited = []

    while not bfsqueue.isEmpty():
        currentnode, currentaction , currentcost = bfsqueue.pop()

        if(not currentnode in visited):
            visited.append(currentnode)

            if problem.isGoalState(currentnode):
                return currentaction

            for nextnode, nextaction, nextcost in problem.getSuccessors(currentnode):
                nextstate = (nextnode, currentaction +[nextaction], currentcost + [nextcost])
                bfsqueue.push(nextstate)

    return []
  

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """
    Uniform Cost Search can be implemented using the priority queue where the initial position
    of pacman in maze,its direction list and initialcost of zero is its begin state.
    The begin state is pushed in the priority queue along with priority which is the cost.
    visited list is used to keep track of visited positions.
    While the queue is not empty, the position of pacman is popped based on the lowest priority(cost)
    and its neighbouring nodes are checked.If it is goal state then path is returned otherwise
    nodes looped and pushed into the priority queue. The actions are added and pushed and costs are also
    added and pushed
    """
    ucqueue = util.PriorityQueue()
    initialcost=0
    begin=(problem.getStartState(),[],initialcost)
    ucqueue.push(begin, initialcost )
    visited = []

    while not ucqueue.isEmpty():
        node, action, currentcost = ucqueue.pop()

        if(not node in visited):
            visited.append(node)

            if problem.isGoalState(node):
                return action

            for nextnode, nextdirection, nextcost in problem.getSuccessors(node):
                nextstate=(nextnode, action+[nextdirection], currentcost + nextcost)
                cost=currentcost + nextcost
                ucqueue.push(nextstate,cost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """
    A* search can be implemented using the Priority queue in which the start state of pacman
    position, action list and initial cost is pushed. The heuristic function is called and
    it is stored in hcost.The initialcost is zero hence,hcost is the
    priority which is pushed in the priority queue. A visited list is
    used for keeping track of the visited positions in the maze.The states are popped out based on lowest
    heuristic and neighbouring nodes are looped and tracked to check if it is the goal.The unvisited nodes are added to the
    priority queue along with summing the actions and costs.The priority is calculated by adding all the costs
    and heuristic costs.The next state is pushed along with priority into the priorityqueue. 
    """
        
    aqueue = util.PriorityQueue()
    initialcost = 0
    start = (problem.getStartState(), [], initialcost)
    hcost = initialcost + heuristic(problem.getStartState(), problem)
    aqueue.push(start,hcost)
    visited = []
    while not aqueue.isEmpty():
        node, action, cost = aqueue.pop()
        if(not node in visited):
            visited.append(node)
            if problem.isGoalState(node):
                return action
            for nextnode, nextdirection, nextcost in problem.getSuccessors(node):
                HeuristicCost=heuristic(nextnode, problem)
                totalcost = cost + nextcost + HeuristicCost
                nextstate = (nextnode, action + [nextdirection], cost + nextcost)
                aqueue.push(nextstate, totalcost)
        
    return []           
    util.raiseNotDefined()   
       


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
