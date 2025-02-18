# EX01 Developing a Simple Webserver
## Date:28-02-2024

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
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
```

## OUTPUT:
![alt text](2024-03-12-1.png)
![alt text](<2024-03-12 (2).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
