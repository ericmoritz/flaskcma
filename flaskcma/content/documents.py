from mongoengine import *
from flaskext.hipmongoengine.backends.auth import User
from wtforms.ext.mongoengine.orm import model_form


class Content(Document):
    # Every piece of content must have an author
    author = ReferenceField(User, required=True)

    # Canonical path to this piece of content
    path = StringField(required=True,
                       unique_with="publish_date")


    # Publishing information
    publish_date = DateTimeField(required=True)
    is_published = BooleanField(required=True)


    # All content has a title, summary and body
    title = StringField()
    summary = StringField()
    body = StringField()


    ####
    ## Related Content
    ####

    # Tags that this content pertains to
    tags = ListField(StringField())

    # A list of links.  This could be a list of on-site paths that can be
    # used to look up related Content objects, or it could be fully qualified
    # URLs to external sources.
    links = ListField(StringFields()) 


    def admin_form(self):
        """Return the WTForm for editting this content object"""
        return model_form(self.__class__)

    def linked_content(self, content_types=None):
        spec = {'links': {'$in': self.links}}

        # If content types is defined, restrict the query by content types
        if content_types:
            spec['_types'] = {'$in': content_types}

        return self.objects.find(spec)

    def related_content(self, content_types=None):
        spec = {'tags': {'$in': self.tags}}

        # If content types is defined, restrict the query by content types
        if content_types:
            spec['_types'] = {'$in': content_types}

        return self.objects.find(spec)
        
