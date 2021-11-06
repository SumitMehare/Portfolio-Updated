from django.db import models

class Blog (models.Model):
    title = models.CharField(max_length=200)
    pub_dt = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_dt_pretty(self):
        return self.pub_dt.strftime('%b %e %Y')