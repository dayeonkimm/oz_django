from tabom.models import Like

class DuplicationError(Exception):
    pass

def do_like(user_id: int, article_id: int) -> Like:
    if Like.objects.filter(user_id=user_id, article_id=article_id).exists():
        raise DuplicationError("뭐라뭐라")
    return Like.objects.create(user_id=user_id, article_id=article_id)