from instapy import InstaPy 

session = InstaPy(username = "memetty_suy_tetty", password = "porcoddio1")
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

#################################################################
# TENERE COMMENTATO UN DEI DUE BLOCCHI DI ISTRUZIONI

session.set_do_follow(True, percentage=100)
session.like_by_tags(["meme", "lmao", "lol", "funnymeme", "likeforlike", "memes", "memeita", "cancer", "gay"], amount = 4)
session.set_dont_like(["blm"])

#session.unfollow_users(amount= ??? , allFollowing=True, splee_dealy=12)

#################################################################

session.end()

