from django.db import models


class Video(models.Model):       # A 1      B   2     C  3
    urls = models.URLField()
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
# url_a, ..... 1
# url_b, ..... 2
# url_c, ..... 3


class Comment(models.Model):   # 1 - 5шт    2 - 3 шт
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comment")

# text_a,..,id, comment_video_id = 1
# text_b,..,id, comment_video_id = 1
# text_c,..,id, comment_video_id = 1
# text_a,..,id, comment_video_id = 2
# text_b,..,id, comment_video_id = 2
# text_c,..,id, comment_video_id = 3

