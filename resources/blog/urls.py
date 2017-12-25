from views import homepage

from flask import Blueprint

blog_bp = Blueprint('blog', __name__,
                    url_prefix='')
blog_bp.add_url_rule('/index', view_func=homepage, methods=['GET'])