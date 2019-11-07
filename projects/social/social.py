from random import randint

class Queue:
    def __init__(self):
        self.store = []

    def size(self):
        return len(self.store)

    def enqueue(self, value):
        self.store.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.store.pop(0)
        return None

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i}")

        # create friendships

        # loop through user_id of friends
        for user_id in self.users:
            #  loop through a random range btw 1 and avgFriendship
            for i in range(randint(1, avgFriendships - 1)):
                # get a random user_id
                rand_user_id = randint(1, self.lastID)
                if(rand_user_id != user_id):
                    self.addFriendship(user_id, rand_user_id)


    def getAllSocialDepth(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # The best traversal method is breath-first traversal, since we'd be recording the shortest path
        # create an empty queue and enqueue the starting vertex ID
        depth = 1
        q = Queue()
        q.enqueue(self.friendships[userID])
        # while the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            level = q.dequeue()
            # create a list to hold all next friends
            new_friends = set()
            for val in level:
                # if that vertex has not been visited and also not the userID
                if val not in visited and val != userID:
                    # then mark it as visited, set the shortest path as the value
                    visited[val] = depth
                    # then add all of it's neighbours to the new_friend set
                    new_friends = new_friends.union(self.friendships[val])
            # Don't enqueue and empty set
            if (new_friends):
                q.enqueue(new_friends)
            # reset new_friends
            new_friends = set()
            # increment depth
            depth += 1
        return visited

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # The best traversal method is breath-first traversal, since we'd be recording the shortest path
        # create an empty queue and enqueue the starting vertex ID
        depth = 1
        q = Queue()
        q.enqueue(self.friendships[userID])
        # while the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            level = q.dequeue()
            # create a list to hold all next friends
            new_friends = set()
            for val in level:
                # if that vertex has not been visited and also not the userID
                if val not in visited and val != userID:
                    # then mark it as visited, set the shortest path as the value
                    visited[val] = depth
                    # then add all of it's neighbours to the new_friend set
                    new_friends = new_friends.union(self.friendships[val])
            # Don't enqueue and empty set
            if (new_friends):
                q.enqueue(new_friends)
            # reset new_friends
            new_friends = set()
            # increment depth
            depth += 1
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

# Example Result

# {1: {4, 6, 7}, 2: {4}, 3: {9, 10}, 4: {1, 2}, 5: {10}, 6: {1}, 7: {1}, 8: set(), 9: {3}, 10: {3, 5}}

# {4: 1, 6: 1, 7: 1, 2: 2}

"""
   7   6
    \ /
     1
      \
       4
        \
         2
    This is correct when compared with the friendships dict
"""

# More Connected Example

# friendships: {1: {2, 5}, 2: {1}, 3: {9}, 4: {10}, 5: {8, 1, 9}, 6: {8, 7}, 7: {6}, 8: {9, 5, 6}, 9: {8, 10, 3, 5}, 10: {9, 4}}

# social path: {2: 1, 5: 1, 8: 2, 9: 2, 3: 3, 6: 3, 10: 3, 4: 4, 7: 4}

"""
       2
        \
         1
          \
       6   5    10
      / \ /  \ /  \
     7   8 -- 9    4
               \
                3
    This is correct when compared with the friendships dict
"""
