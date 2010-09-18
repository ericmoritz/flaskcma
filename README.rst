Flask CMA, the "let's not focus on if this is a good idea or not edition"
===========================================================================


Flask CMA is the merging of a wiki and a content management system.  Any content
object can be created at any URL simply be hitting the edit button.

This is an experiment in correcting flaws present in existing content systems with
the following goals:

  * Any piece of content can be directly related to another piece of content
  * Any piece of content can be losely related by topic (tags) to another piece of
    content
  * Once published, URLs to piece of content can not change.  These URLs are 
    permalinks to a piece of content.  Content can only be redirected perminately
    or deleted.
  * Admin sites are for losers.  Allow direct manipulation of content on the
    URL it lives on by authorized users.
  * Any related content, either directly related or losely related can be 
    fetch on the fly in the template.  Caching should be transparent to the 
    template designers.



**Note**: This was an experiment.  It's probably not a good idea to look at this.