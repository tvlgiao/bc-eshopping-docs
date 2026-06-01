"""Tiny HTTP server: serves a one-page bridge that turns an uploaded file
into an automatic browser download. Run on :9001."""
import http.server, socketserver

PAGE = b"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>capture</title>
<style>body{font:14px/1.4 system-ui;padding:1rem;background:#fafaf9}
.ok{color:#059669}pre{background:#fff;padding:.5rem;border:1px solid #ddd;border-radius:4px}</style>
</head><body>
<h3>capture-bridge</h3>
<input type="file" id="up" accept="image/*">
<pre id="log">waiting...</pre>
<script>
document.getElementById('up').addEventListener('change',function(e){
  var f=e.target.files[0]; if(!f){return;}
  var a=document.createElement('a');
  a.href=URL.createObjectURL(f);
  a.download=f.name||'capture.png';
  document.body.appendChild(a); a.click();
  setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},1500);
  var l=document.getElementById('log');
  l.textContent='DOWNLOAD: '+a.download+' ('+f.size+' bytes)';
  l.className='ok';
});
</script></body></html>"""

class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.send_header("Content-Type","text/html"); self.end_headers()
        self.wfile.write(PAGE)
    def log_message(self,*a,**k): pass

with socketserver.TCPServer(("127.0.0.1", 9001), H) as s:
    print("capture-bridge http://127.0.0.1:9001")
    s.serve_forever()
