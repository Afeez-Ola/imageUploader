import tornado.web
import tornado.ioloop


class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("We are live baby!")
    

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", uploadHandler),
        (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "img"})
    ])
    
    port = 3000
    app.listen(port)
    print(f"App is listening on port: {port} 🔥🔥🔥")
    tornado.ioloop.IOLoop.instance().start()