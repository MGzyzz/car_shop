from controllers.base import BaseController
import requests
import utils
from controllers.base import BaseController
from db.database import Database
from template_engine.jinja import env


class PagesController(BaseController):

    def get_list(self):
        tmp = env.get_template('pages/home.html')
        body = tmp.render(information=Database.all())
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)


    def new(self):
        tmp = env.get_template('pages/create_page.html')
        body = tmp.render()
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def create(self):
        id = {'id': next(utils.id_gen)}
        self.request.body.update(id)
        Database.add(self.request.body)
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_status(301)
        self.response.add_header('Location', '/')
        self.response.set_body('<a href="/">Back to posts list</a>')

    def get_image(self):
        id_image = int(self.request.query['id'][0])
        if id_image is not None:
            post = Database.find_by_id(id_image)
            if post is not None:
                tmp = env.get_template('pages/find_post.html')
                body = tmp.render(information=post)

                self.response.add_header('Content-Type', 'text/html')
                self.response.set_body(body)
            else:
                self.response.set_status(404)
                self.response.set_body('Post not found')
        else:
            self.response.set_status(400)
            self.response.set_body('Bad Request: missing post id')

    def search_post(self):
        tmp = env.get_template('pages/search.html')
        body = tmp.render()
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)


