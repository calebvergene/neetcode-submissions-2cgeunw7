class Twitter:
    # basically go through following. compare last added element (stack), and save the most recent one. do this 10 times

    def __init__(self):
        self.following = collections.defaultdict(list) # user: [users]
        self.user_posts = collections.defaultdict(list) # user: posts
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # need to follow urself when you init user
        if userId not in self.following:
            self.following[userId].append(userId)
        self.user_posts[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        # need to reverse this list before adding back. stack of taken tweets
        
        # find the most recent posts
        for i in range(10):
            most_recent = (-1, -1) # tweetId, userId. store userId to add it back to their feed. 
            for user in self.following[userId]:
                if self.user_posts[user]:
                    recent_post = self.user_posts[user][-1]   
                    most_recent = max(most_recent, (recent_post, user))
            # no more posts
            if most_recent == (-1,-1):
                break
            self.user_posts[most_recent[1]].pop()
            news.append(most_recent)
    
        # add posts back
        add_back = reversed(news)
        for post in add_back:
            self.user_posts[post[1]].append(post[0])
        
        return [n[0] for n in news]

    def follow(self, followerId: int, followeeId: int) -> None:
        # add followerId to users so that you can also add itself as one of the followers
        if followerId not in self.following:
            self.following[followerId].append(followerId)
        # cant follow twice
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            return
        if followerId == followeeId:
            return
        self.following[followerId].remove(followeeId)
