from google.appengine.ext import db

from handlers.bloghandler import BlogHandler
from models.model_posts_comments import blog_key
from models.model_users import User


class EditPost(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return self.render("404.html")

        if self.user.name == post.author:
            self.render("editPost.html", post=post, title=post.title, content=post.content)

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        title = self.request.get('title')
        content = self.request.get('content')

        if self.user and self.user.name == post.author:
            if title and content:
                post.title = title
                post.content = content
                post.put()
                self.redirect('/%s' % str(post.key().id()))
            else:
                error = "Please enter some content for your post!"
                self.render("editPost.html", post=post, title=title, content=content, error=error)
        else:
            error = "You need to be logged in to edit your post!"
            return self.render('login.html', error=error)