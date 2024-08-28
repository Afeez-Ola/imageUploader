import tornado.web
import tornado.ioloop
import sys
import tornado.autoreload


class uploadRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        
    def post(self):
        files = self.request.files["imgFile"]
        
        for file in files:
            fh = open(f"img/{file.filename}", "wb")
            fh.write(file.body)
            fh.close()
        self.write(f"http://localhost:{port}/img/{file.filename}")   
        
        

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", uploadRequestHandler),
        (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "img"})
    ])
    port = int(sys.argv[1]) if sys.argv == 1 else 7000
    app.port = port
    app.listen(app.port)
    print(f"App listening on port: {app.port}")
    tornado.autoreload.start()
    tornado.ioloop.IOLoop.instance().start()

    