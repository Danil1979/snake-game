import random
import enum

class Player():
  name = "testing player"
  group = "Children of Odin"
  members = [
    ["Thor", "12834823"],
    ["Loki", "98854678"],
    ["Hela", "87654654"]
  ]
  informed = False

  def __init__(self, setup):
    # setup = {
    #   maze_size: [int, int],
    #   static_snake_length: bool
    # }
    self.setup = setup

  def run(self, problem):
    # problem = {
    #   snake_locations: [[int,int],[int,int],...],
    #   current_direction: str,
    #   food_locations: [[int,int],[int,int],...],
    # }
    solution = []
    directions = "nswe"
    # the following algorithm is NOT a valid algorithm
    # it randomly generates solution that is invalid
    # its purpose is to show you how this class will work
    # not a guide to how to write your algorithm
    solution = bfs(problem, self.setup)
    # solution = [random.choice(directions) for step in range(random.randint(1,10))]
    # the following search tree is a static search tree 
    # to show you the format of the variable 
    # to generate a search tree that can be displayed in the frontend.
    # you are required to generate the search tree based on your search algorithm
    search_tree = [
      {
        "id": 1,
        "state": "0,0",
        "expansionsequence": 1,
        "children": [2,3,4],
        "actions": ["n","w","e"],
        "removed": False,
        "parent": None
      },
      {
        "id": 2,
        "state": "5,0",
        "expansionsequence": 2,
        "children": [5,6,7],
        "actions": ["n","s","w"],
        "removed": False,
        "parent": 1
      },
      {
        "id": 3,
        "state": "0,3",
        "expansionsequence": -1,
        "children": [],
        "actions": [],
        "removed": False,
        "parent": 1
      },
      {
        "id": 4,
        "state": "0,4",
        "expansionsequence": -1,
        "children": [],
        "actions": [],
        "removed": False,
        "parent": 1
      },
      {
        "id": 5,
        "state": "5,0",
        "expansionsequence": -1,
        "children": [],
        "actions": [],
        "removed": True,
        "parent": 2
      },
      {
        "id": 6,
        "state": "5,3",
        "expansionsequence": -1,
        "children": [],
        "actions": [],
        "removed": False,
        "parent": 2
      },
      {
        "id": 7,
        "state": "1,0",
        "expansionsequence": -1,
        "children": [],
        "actions": [],
        "removed": False,
        "parent": 2
      }
    ]
    # this function should return the solution and the search_tree
    return solution, search_tree

class Directions(enum.Enum): 
    North = 'n'
    East = 'e'
    South = 's'
    West = 'w'

class Node:
    def __init__(self, state=None, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.action = action
    def addChildren(self, children):
        self.children.extend(children)
    
def bfs(problem, setup):
     print(Directions('n'))
     print("this is breadth-first search.")
     frontier = []
     explored = []
     found_goal = False
     goalie = Node()
     solution = []
     frontier.append(Node(problem["snake_locations"][0], None))
     while not found_goal:
        # expand the first in the frontier
        children = expandAndReturnChildren(setup["maze_size"], frontier[0])
        # add children list to the expanded node
        frontier[0].addChildren(children)
        # add to the explored list
        explored.append(frontier[0])
        for x in problem["snake_locations"]:     
            explored.append(Node(x, None))
        # remove the expanded frontier
        del frontier[0]
        # add children to the frontier
        for child in children:
            # check if a node was expanded or generated previously
            if not (child.state in [e.state for e in explored]) and not (child.state in [f.state for f in frontier]):
                # goal test
                if child.state == problem["food_locations"][0]:
                    found_goal = True
                    goalie = child
                frontier.append(child)
        print("Explored:", [e.state for e in explored])
        print("Frontier:", [f.state for f in frontier])
        print("Children:", [c.state for c in children])
        print("")
        
        solution = [goalie.action]
        path = [goalie.state]
        while goalie.parent is not None:
            
            solution.insert(0, goalie.parent.action)
            path.insert(0,goalie.parent.state)
            for e in explored:
                if e.state == goalie.parent.state:
                    goalie = e
                    break
     print("path: ",path)
     del solution[0]
     return solution
        
def expandAndReturnChildren(maze, node):
    children = []
    expand = [-1,1]
    for x in expand:
        if node.state[0]+x <= maze[0] and node.state[0]+x >= 0 and node.state[1] <= maze[1] and node.state[1] >= 0:
            if x == -1:
                direction = 'w'
            elif x == 1:
                direction = 'e'
            children.append(Node([node.state[0]+x,node.state[1]],node, direction))
    for y in expand:
        if node.state[0] <= maze[0] and node.state[0] >= 0 and node.state[1]+y <= maze[1] and node.state[1]+y >= 0:
            if y == -1:
                direction = 'n'
            elif y == 1:
                direction = 's'
            children.append(Node([node.state[0],node.state[1]+y],node, direction))
    print("return child")

    return children
if __name__ == "__main__":
  p1 = Player({ "maze_size": [10,10], "static_snake_length": True })
  sol, st = p1.run({'snake_locations': [[5, 2]], 'current_direction': 'e', 'food_locations': [[0, 7]]})
  print("Solution is:", sol)
  print("Search tree is:")
  print(st)