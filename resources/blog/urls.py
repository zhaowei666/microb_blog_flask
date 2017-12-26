from views import homepage

from flask import Blueprint, url_for

blog_bp = Blueprint('blog', __name__,
                    url_prefix='',
                    subdomain='blog')


blog_bp.add_url_rule('/', view_func=homepage, methods=['GET'])
blog_bp.add_url_rule('/index', view_func=homepage, methods=['GET'])
