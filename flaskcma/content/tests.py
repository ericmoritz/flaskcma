from datetime import datetime
from mongoengine import connect
from flaskcma.content.documents import Content
from flaskcma.app import app
connect("test")
import unittest
from flaskext.hipmongoengine.backends.auth import User


class TestContentView(unittest.TestCase):
    def setUp(self):
        Content.objects().delete()
        User.objects().delete()

        u = User(username="test-user", password="")
        u.save()
        
        c = Content(path="/test-path/",
                    title="Test Content item",
                    author=u,
                    publish_date=datetime.now(),
                    is_published=True)
        c.save()

    def test_get(self):
        client = app.test_client()
        import pdb; pdb.set_trace()

        rv = client.get("/test-path/")
        
        
                    
if __name__ == '__main__':
    unittest.main()
