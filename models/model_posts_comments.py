from google.appengine.ext import db
from handlers.bloghandler import render_template


class Post(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    user_id = db.IntegerProperty(required=True)
    author = db.StringProperty(required=True)
    likes = db.IntegerProperty(default=0)
    likers = db.StringListProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    @classmethod
    def by_id(cls, post_id):
        return Post.get_by_id(int(post_id))

    def render(self, user):
        comments = Comment.all().filter('post_id =', self).order('-created')
        self._render_text = self.content.replace('\n', '<br>')
        return render_template("post.html", post=self, user=user, comments=comments)


def blog_key(name='default'):
    return db.Key.from_path('blogs', name)


class Comment(db.Model):
    comment = db.TextProperty(required=True)
    author = db.StringProperty(required=True)
    post_id = db.ReferenceProperty(Post)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    @classmethod
    def render(cls, self):
        self._render_text = self.comment.replace('\n', '<br>')
        return render_template("comment.html", comments=self)
