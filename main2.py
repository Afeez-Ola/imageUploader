import tornado.web
import tornado.ioloop
import sys

class uploadHandler(tornado.web.RequestHandler):
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
    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    app = tornado.web.Application([
        (r"/", uploadHandler),
        (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "img/"})
    ])
    
    app.port = port
    
    app.listen(app.port)
    print(f"App listening on port: {app.port} 🔥🔥🔥")
    tornado.ioloop.IOLoop.instance().start()