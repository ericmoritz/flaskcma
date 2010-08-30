from flask import (Module)
from flaskcma.stories.documents import Story

mod = Module(__name__, name="stories")

mod.flaskcma = {
    'content_list': [Story]
}
