from models.post import Post
from database import Database

Database.initialize()

post = Post.from_mongo('70f2ccb7431e48ed9fa3cb020ed0afd9')
print(post)

posts = Post.from_blog('456')

for post in posts:
    print(post)
