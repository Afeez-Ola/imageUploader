import tornado.web
import tornado.ioloop


class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        
        files = self.request.files["imgFile"]
        
        for file in files:
            fh = open(f"img/{file.filename}", "wb")
            fh.write(f"{file.body}")
            
            fh.close()
        self.write(f"http://localhost:3000/img/{file.filename}")
    

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", uploadHandler),
        (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "img"})
    ])
    
    port = 3000
    app.listen(port)
    print(f"App is listening on port: {port} 🔥🔥🔥")
    tornado.ioloop.IOLoop.instance().start()