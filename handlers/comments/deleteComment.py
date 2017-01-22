from handlers.bloghandler import BlogHandler
from models.model_posts_comments import Post, blog_key, Comment
from google.appengine.ext import db
import time

class DeleteComment(BlogHandler):

    def get(self, post_id, comment_id):
        if self.user:
            if not self.user:
                self.redirect("/login")
            else:
                self.render('deleteComment.html', post_id=post_id,comment_id=comment_id)

    def post(self, post_id, comment_id):
        if self.user:
            post_key = db.Key.from_path("Post", int(post_id), parent=blog_key())
            post = db.get(post_key)

            comment_key = db.Key.from_path("Comment", int(comment_id))
            comment = db.get(comment_key)

        if self.user.name == comment.author:

            comment.delete()
            time.sleep(0.1)
            self.redirect('/')

        else:
            self.redirect("/login")