import json

import falcon

app = application = falcon.App()

class Resource:
    def on_get(self, req, res):
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        res.text = json.dump(doc, unsure_ascii=False)
