from http.server import BaseHTTPRequestHandler, HTTPServer



hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):

        with open('index.html', 'r', encoding="utf-8") as f:
            html_content = f.read()
            self.send_response(200)  # Отправка кода ответа
            self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
            self.end_headers()  # Завершение формирования заголовков ответа
            self.wfile.write(bytes(html_content, 'utf-8'))  # Тело ответа



if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")