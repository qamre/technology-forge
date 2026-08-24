import os
import http.server

CONFIG_DIR = "/etc/app/config"
SECRET_DIR = "/etc/app/secrets"

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        lines = ["INVENTORY SERVICE", "=================="]
        lines.append(f"APP_ENV env var: {os.environ.get('APP_ENV', '<not set>')}")
        lines.append(f"DB_USERNAME env var: {os.environ.get('DB_USERNAME', '<not set>')}")

        if os.path.isdir(CONFIG_DIR):
            for f in sorted(os.listdir(CONFIG_DIR)):
                path = os.path.join(CONFIG_DIR, f)
                if os.path.isfile(path):
                    with open(path) as fh:
                        lines.append(f"config file {f}: {fh.read().strip()}")

        if os.path.isdir(SECRET_DIR):
            for f in sorted(os.listdir(SECRET_DIR)):
                path = os.path.join(SECRET_DIR, f)
                if os.path.isfile(path):
                    with open(path) as fh:
                        lines.append(f"secret file {f}: {fh.read().strip()}")

        body = "\n".join(lines).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body)

http.server.HTTPServer(("0.0.0.0", 5678), Handler).serve_forever()
