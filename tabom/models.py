from django.db import models


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)  # audit column
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


# Create your models here.


class User(BaseModel):
    name = models.CharField(max_length=50)


class Article(BaseModel):
    title = models.CharField(max_length=255)


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user","article"], name="unique_user_article"),
        ]


# 장고 view -> 다른 진영에서 controller (특히 spring)

# view/controller -> service(장고에는 없음) -> model/entity -> database

# 객체 지향 -> 책임과 역할..? : loose coupling(결합이 느슨해야 좋음)
# 하나의 책임 역할 -> single responsible principle
