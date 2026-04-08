class Twitter:

    def __init__(self):
        self.user_following = collections.defaultdict(set) # user : following 
        self.user_posts = collections.defaultdict(list) # user : posts[]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append(tweetId)


    def getNewsFeed(self, userId: int) -> List[int]:
        # immediatley add self to user following 
        self.user_following[userId].add(userId)

        heap = self._initialize_heap(userId)
        news_feed = []
        while heap and len(news_feed) < 10:
            # pop most recent post, then add back next recent post from that user 
            post = heapq.heappop(heap)
            news_feed.append(-post[0])
            index = post[2] - 1
            # adds back if there are still posts left of that user to add
            if index >= 0:
                heapq.heappush(heap, (-self.user_posts[post[1]][index], post[1], index))

        return news_feed
    

    def _initialize_heap(self, userId) -> list:
        # for each user in the following, add their most recent post to a heap. 
        heap = []
        for following in self.user_following[userId]:
            # check if they even have posts first 
            if self.user_posts[following]:
                last_post = len(self.user_posts[following]) - 1
                recent_post = self.user_posts[following][last_post]
                heapq.heappush(heap, (-recent_post, following, last_post))
        return heap
    
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_following[followerId]:
            self.user_following[followerId].remove(followeeId)
