from handlers.bloghandler import BlogHandler
from models.model_posts_comments import Post, blog_key, Comment
import time


class EditComment(BlogHandler):

    def get(self, post_id, comment_id):
        if self.user:
            post = Post.get_by_id(int(post_id), parent=blog_key())
            comment = Comment.get_by_id(int(comment_id))
            if comment and comment.author == self.user.name:
                self.render("editComment.html", comment=comment)
            else:
                self.redirect("/error")
        else:
            self.redirect("/login")

    def post(self, post_id, comment_id):
        post = Post.get_by_id(int(post_id), parent=blog_key())
        if self.user:
            comment = Comment.get_by_id(int(comment_id))
            if self.request.get("comment") and comment.author == self.user.name:
                comment.comment = self.request.get("comment")
                comment.put()
                time.sleep(0.1)
                self.redirect('/%s' % str(post.key().id()))
            else:
                error = "Please fill in comment."
                self.render(
                    "editComment.html",
                    comment=comment)
        else:
            self.redirect("/login")