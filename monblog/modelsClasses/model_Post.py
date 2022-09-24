from monblog.models import *

class PostClass (object):
    @staticmethod
    def listPosts():
        try :
            return Post.objects.all()
        except Exception as e:
            print(e)
            return None

    