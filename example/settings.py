import site
from mongoengine import connect
site.addsitedir("../")
connect("scratch")
