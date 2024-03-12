from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Software Companies</title>
  <style>
    table {
      width: 80%;
      border-collapse: collapse;
      margin: 20px;
    }
    th, td {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }
    th {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>

  <h2>Top Software Companies with revenue table</h2>

  <table>
<caption>Top Five Revenue Generating Software Companies</caption>
    <thead>
      <tr>
        <th>Rank</th>
        <th>Company</th>
        <th>Revenue (in billions USD)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>Amazon</td>
        <td>385.23</td>
      </tr>
      <tr>
        <td>2</td>
        <td>Apple</td>
        <td>365.78</td>
      </tr>
      <tr>
        <td>3</td>
        <td>Alphabet (Google)</td>
        <td>183.03</td>
      </tr>
      <tr>
        <td>4</td>
        <td>Microsoft</td>
        <td>168.09</td>
      </tr>
      <tr>
        <td>5</td>
        <td>Facebook</td>
        <td>85.97</td>
      </tr>
    </tbody>
  </table>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()