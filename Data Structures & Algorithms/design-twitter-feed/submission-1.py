class Twitter:

    def __init__(self):
        self.follows = {}
        self.feed = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        idx = len(self.feed) - 1
        res = []
        youFollow = self.follows[userId] if userId in self.follows else []
        while len(res) < 10 and idx >= 0:
            if self.feed[idx][0] == userId or self.feed[idx][0] in youFollow:
                res.append(self.feed[idx][1])
            idx -= 1
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        self.follows[followerId].discard(followeeId)
