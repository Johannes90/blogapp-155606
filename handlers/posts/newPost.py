from handlers.bloghandler import BlogHandler
from models.model_posts_comments import blog_key
from models.model_posts_comments import Post
from models.model_users import User


class NewPost(BlogHandler):
    def get(self):
        if self.user:
            self.render("newPost.html")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            self.redirect('/')

        title = self.request.get('title')
        content = self.request.get('content')
        user_id = self.user.key().id()
        author = User.by_id(user_id).name

        if title and content:
            post = Post(parent=blog_key(), title=title, content=content, user_id=user_id, author=author)
            post.put()
            self.redirect('/%s' % str(post.key().id()))
        else:
            error = "Please enter some content for your post!"
            self.render("newPost.html", title=title, content=content, error=error)