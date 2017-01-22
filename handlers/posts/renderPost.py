from google.appengine.ext import db


from handlers.bloghandler import BlogHandler
from models.model_posts_comments import blog_key


class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return
        user = self.user
        self.render("permalink.html", post=post)



