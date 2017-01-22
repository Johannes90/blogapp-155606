#!/usr/bin/env python

# Imports

import webapp2

from handlers.auth.login import Login
from handlers.auth.logout import Logout
from handlers.auth.signup import Register
from handlers.comments.deleteComment import DeleteComment
from handlers.comments.editComment import EditComment
from handlers.comments.newComment import NewComment
from handlers.homepage import HomePage
from handlers.likes.like import Like
from handlers.likes.like import UnLike
from handlers.posts.deletePost import DeletePost
from handlers.posts.editPost import EditPost
from handlers.posts.newPost import NewPost
from handlers.posts.renderPost import PostPage


# Routes

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/signup', Register),
    ('/login', Login),
    ('/logout', Logout),
    ('/new-post', NewPost),
    ('/([0-9]+)', PostPage),
    ('/edit/([0-9]+)', EditPost),
    ('/delete/([0-9]+)', DeletePost),
    ('/like/([0-9]+)', Like),
    ('/unlike/([0-9]+)', UnLike),
    ('/newComment/([0-9]+)', NewComment),
    ('/deleteComment/([0-9]+)/([0-9]+)', DeleteComment),
    ('/editComment/([0-9]+)/([0-9]+)', EditComment)
], debug=True)
