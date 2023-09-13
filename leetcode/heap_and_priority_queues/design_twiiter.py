"""
Leetcode 355: Design Twitter
https://leetcode.com/problems/design-twitter/

Analysis:
1. postTweet
    - Time complexity: O(1)
    - Space complexity: O(1)
2. getNewsFeed
    - Time complexity: O(n(log(n))
        - n is the number of tweets in the user's feed
        - n(log(n)) is the time complexity of the merge sort
        - Alternatively, we can use a heap to store the tweets
            and retrieve the top 10 tweets in O(log(k)) time
            where k is the number of tweets in the heap, which
            depends on the number of followees a user has.
    - Space complexity: O(n)
3. follow
    - Time complexity: O(1)
    - Space complexity: O(1)
4. unfollow
    - Time complexity: O(1)
    - Space complexity: O(1)
5. get_user
    - Time complexity: O(1)
    - Space complexity: O(1)
"""
from collections import deque
from heapq import merge
from typing import List


class User:
    def __init__(self, id: int):
        """ Instantiate a User object """
        self.id = id
        self.tweets = deque()
        self.followees = set()


class Twitter:
    """
    Twitter class that allows users to post tweets, follow other users,
    and retrieve the 10 most recent tweets in the user's feed.
    """
    MAX_FEED = 10  # max number of tweets in a feed

    def __init__(self):
        """ Instantiate a Twitter object """
        self.users = {}
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """ Add the tweet to the user's tweets list """
        user = self.get_user(userId)
        self.tweet_count += 1
        user.tweets.appendleft((self.tweet_count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Generates a feed of the top 10 tweets from the user
        and their followees
        """

        user = self.get_user(userId)
        feed = user.tweets
        for followee_id in user.followees:
            followee = self.get_user(followee_id)
            feed = merge(feed, followee.tweets, reverse=True)
        top_tweets = [tweet[1] for tweet in feed]
        return top_tweets[:self.MAX_FEED]

    def follow(self, followerId: int, followeeId: int) -> None:
        """ Follow a user """
        follower = self.get_user(followerId)
        follower.followees.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """ Unfollow a user """
        user = self.get_user(followerId)
        user.followees.discard(followeeId)

    def get_user(self, id: int) -> User:
        """ Get a user from the user's dictionary """
        if id not in self.users:
            self.users[id] = User(id)
        return self.users[id]
