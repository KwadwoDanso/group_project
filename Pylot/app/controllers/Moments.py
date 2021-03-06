from system.core.controller import *

class Moments(Controller):
    def __init__(self, action):
        super(Moments, self).__init__(action)
        self.load_model('Moment')

    def index(self):
        cats = self.models['Moment'].get_cats()
        return self.load_view('index.html', cats = cats)

    def add(self):
        data = {
            'category':     request.form['category'],
            'beginning':    request.form['beg'],
            'ending':       request.form['end'],
            'url':          request.form['url']
        }
        self.models['Moment'].create(data)
        return jsonify(test=test)

    def category(self):
        data = {'category': request.form['category']}
        self.models['Moment'].cat(data)
        return jsonify(category = data)

    # def get_cat(self):
    #     cats = self.models['Momemt'].get_cats()
    #     return jsonify(cats=cats)