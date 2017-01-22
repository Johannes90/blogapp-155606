import time
from google.appengine.ext import db

from handlers.bloghandler import BlogHandler
from models.model_posts_comments import blog_key


# Implement like functionality when pressing like button
class Like(BlogHandler):
    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user and post and self.user.name not in post.likers:
            post.likes += 1
            post.likers.append(self.user.name)
            post.put()
            time.sleep(0.1)
            self.redirect('/%s' % str(post.key().id()))
        else:
            self.render("permalink.html", post=post)


# Implement Like Functionality when pressing unlike button
class UnLike(BlogHandler):
    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user and post and self.user.name in post.likers:
            post.likes -= 1
            post.likers.remove(self.user.name)
            post.put()
            time.sleep(0.1)
            self.redirect('/%s' % str(post.key().id()))
        else:
            self.redirect('/%s' % str(post.key().id()))