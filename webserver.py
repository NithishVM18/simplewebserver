from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
   <head>
  <title> sample web page</title>
</head>

<body>
 <center><h3>NITHISH-26018775</h3>
 <table border="2" cellspacing="2" cellpadding="10" width="800" >
    <caption> Device Information</caption>
    <tr>
         <td>S.No</td>
         <td>Device Type</td>
         <td>Device Name</td>
    </tr>
     <tr>
          <td>1.</td>
          <td>Device Name</td>
          <td>TL15-53M-G2</td>
     </tr>
     <tr>
          <td>2.</td>
          <td>Processor</td>
          <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
     
          
     </tr>
     <tr>
          <td>3.</td>
          <td>installed ram</td>
          <td>16.0 GB (15.7 GB usable)</td>
      

      </tr> 
      <tr>  
          <td>4.</td>
          <td>Grapics card</td>
          <td>Intel(R) Graphics (128 MB)</td>
       </tr>
       <tr>
           <td>5.</td>
           <td>Storage</td>
           <td>138 GB of 477 GB used</td>

       </tr>
       <tr>
            <td>6.</td>
            <td>Device ID</td>
            <td>78AF937A-E6C0-4F88-A684-0447E8493082</td>
       </tr>
       <tr>
              <td>7.</td>
              <td>Product ID</td>
              <td>00342-42945-55016-AAOEM</td>
    </tr>
    <tr>
               <td>8.</td>
               <td>System Type</td>
               <td>64-bit operating system, x64-based processor</td>
    </tr>
    <tr>
                <td>9.</td>
                <td>Pen and Touch</td>
                <td>No pen or touch input is available for this display</td>
          </tr>
          </table>

              
          </center>      
<body/>     
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()