import time

from handlers.bloghandler import BlogHandler
from google.appengine.ext import db
from models.model_posts_comments import blog_key

# Directing the user to confirmation.
class DeletePost(BlogHandler):
    def get(self, post_id):
        if self.user:
            if not self.user:
                self.redirect("/login")
            else:
                self.render('deletePost.html', post_id=id)

    def post(self, post_id):
        if self.user:
            key = db.Key.from_path("Post", int(post_id), parent=blog_key())
            post = db.get(key)
        if self.user.name == post.author:
            post.delete()
            time.sleep(0.1)
            self.redirect('/')
        else:
            return self.redirect('/login')