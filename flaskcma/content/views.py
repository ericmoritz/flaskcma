from flask import (Module, request, abort, render_template, current_app)
from flaskcma.content.documents import Content
from flaskcma import utils


mod = Module(__name__, name="content",
             url_prefix="")


@mod.route("/<path>/edit/<content_type>/")
def edit_content(path, content_type="Content"):
    path = "/%s/"

    # Get the content type otherwise 404
    try:
        Document = utils.content_type(current_app, content_type)
    except KeyError:
        abort(404)
    
    content = Document.objects(path=path).first()

    if content is None:
        content = Document()

    Form = content.admin_form()

    if Form is None:
        abort(404) # We can't edit this content item
    
    form = Form(request.forms, instance=content)

    if request.method == "post" and form.validate():
        doc = form.save()
        redirect(doc.path)

    return render_template("content.html",
                           content=content,
                           admin_form=form)
                           
@mod.route("/<path>/")
def content_detail(path):
    path = "/%s/" % (path, )
    content = Content.objects(path=path).first()

    if content is None:
        abort(404)

    return render_template("content.html",
                           content=content)

    
# Register these documents with flaskcma
mod.flaskcma = {
    'content_list': [Content],
}
