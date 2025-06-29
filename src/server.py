from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Здесь можно обрабатывать GET-запросы
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('contacts.html', 'r', encoding='utf-8') as file:
            self.wfile.write(file.read().encode('utf-8'))


def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', 8000)  # Сервер будет работать на порту 8000
    httpd = server_class(server_address, handler_class)
    print('Запуск сервера на порту 8000...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()