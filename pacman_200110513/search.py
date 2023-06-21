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

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    # 存储已经查询过的位置
    closed = []
    # 找到起点
    cur = problem.getStartState()
    # 用栈来进行深度优先搜索，栈中元素为（当前位置，从起点到当前位置的actions集合）
    fringe = util.Stack()
    fringe.push((cur, []))

    while not fringe.isEmpty():
        cur, actions = fringe.pop()
        # 如果是终点，则返回actions集
        if problem.isGoalState(cur):
            return actions
        # 否则继续搜索
        if cur not in closed:
            closed.append(cur)
            successors = problem.getSuccessors(cur)
            for successor in successors:
                if successor[0] not in closed:
                    fringe.push((successor[0], actions + [successor[1]]))
    # 未找到路径
    return False


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    # 存储已经查询过的位置
    closed = []
    # 找到起点
    cur = problem.getStartState()
    # 用队列来进行广度优先搜索，队列中元素为（当前位置，从起点到当前位置的actions集合）
    fringe = util.Queue()
    fringe.push((cur, []))

    while not fringe.isEmpty():
        cur, actions = fringe.pop()
        # 如果是终点，则返回actions集
        if problem.isGoalState(cur):
            return actions
        # 否则继续搜索
        if cur not in closed:
            closed.append(cur)
            successors = problem.getSuccessors(cur)
            for successor in successors:
                if successor[0] not in closed:
                    fringe.push((successor[0], actions + [successor[1]]))
    # 未找到路径
    return False

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    # 存储已经查询过的位置
    closed = []
    # 找到起点
    cur = problem.getStartState()
    # 用优先队列PriorityQueue来进行代价一致算法的搜索，队列中元素为（当前位置，从起点到当前位置的actions集合）
    fringe = util.PriorityQueue()
    fringe.push((cur, []), 0)

    while not fringe.isEmpty():
        cur, actions = fringe.pop()
        # 如果是终点，则返回actions集
        if problem.isGoalState(cur):
            return actions
        # 否则继续搜索
        if cur not in closed:
            closed.append(cur)
            successors = problem.getSuccessors(cur)
            for successor in successors:
                if successor[0] not in closed:
                    new_actions = actions + [successor[1]]
                    fringe.push((successor[0], new_actions), problem.getCostOfActions(new_actions))
    # 未找到路径
    return False

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

    # 存储已经查询过的位置
    closed = []
    # 找到起点
    cur = problem.getStartState()
    # 用优先队列PriorityQueue来进行代价一致算法的搜索，队列中元素为（当前位置，从起点到当前位置的actions集合）
    fringe = util.PriorityQueue()
    fringe.push((cur, []), heuristic(cur, problem))

    while not fringe.isEmpty():
        cur, actions = fringe.pop()
        # 如果是终点，则返回actions集
        if problem.isGoalState(cur):
            return actions
        # 否则继续搜索
        if cur not in closed:
            closed.append(cur)
            successors = problem.getSuccessors(cur)
            for successor in successors:
                if successor[0] not in closed:
                    new_actions = actions + [successor[1]]
                    cost = problem.getCostOfActions(new_actions) + heuristic(successor[0], problem)
                    fringe.push((successor[0], new_actions), cost)
    # 未找到路径
    return False

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
