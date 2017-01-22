from bloghandler import BlogHandler
from models.model_posts_comments import Post


# Render posts with latest first
class HomePage(BlogHandler):
    def get(self):
        posts = Post.all().order('-created')
        user = self.user
        self.render('HomePage.html', posts=posts, user=user)
