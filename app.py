from models.post import Post

__author__ = "jrbattles"

post01 = Post("Post01 title", "Post01 content", "Post01 author")
post02 = Post("my title", "Post02 content", "Post02 author")

print(post01.content)
print(post02.content)
