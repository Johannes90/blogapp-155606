from google.appengine.ext import db
import time
from handlers.bloghandler import BlogHandler
from models.model_posts_comments import Post, blog_key, Comment


class NewComment(BlogHandler):

    def get(self):

        if not self.user:
            return self.redirect("/login")
        post_id = self.request.get("post")
        post = Post.get_by_id(int(post_id), parent=blog_key())
        title = post.title
        content = post.content
        self.render(
            "newComment.html",
            title=title,
            content=content,
            post_id=post.key())

    def post(self,post_id):
        key = db.Key.from_path("Post", int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return
        if not self.user:
            return self.redirect("/login")
        comment = self.request.get("comment")
        author = self.user.name

        if comment:
            comment = Comment(
                comment=comment,
                post_id=post,
                author=author)
            comment.put()
            time.sleep(0.1)
            self.redirect('/')

        else:
            error = "please comment"
            self.render(
                "permalink.html",
                post=post,
                comment=comment,
                error=error)
