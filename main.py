import tornado.web
import tornado.ioloop


if __name__ == "__main__":
    app = tornado.web.Aplication([
        (r"/", basicRequestHandler)
    ])
    
    port = 3000
    app.listen(port)
    print(f"App is listening on port: {port} 🔥🔥🔥")