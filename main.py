from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import TBED_LMstudio

#settings
server_port = 9111
platform = "LMstudio" #Use "LMstudio" or "Ollama"
port = 1234 #use the port for LM Studio or for Ollama
url = 'http://localhost:1234/v1/chat/completions'
model = "llama3"



class RequestHandler(BaseHTTPRequestHandler):
    
    def _send_response(self, status_code, response_data):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_bytes = json.dumps(response_data).encode('utf-8')
        self.wfile.write(response_bytes)

    def do_POST(self):
        try:
            # Get the content length from headers
            content_length = int(self.headers['Content-Length'])
            
            # Read the request body
            post_data = self.rfile.read(content_length)
            
            # Parse JSON data
            json_data = json.loads(post_data.decode('utf-8'))
            
            # Process the received data (example processing)
            # print("Received data:", json_data)
            if 'platform_override' in json_data:
                l_platform = json_data['platform_override']
            else:
                l_platform = platform

            if 'port_override' in json_data:
                port_override = True
                port = json_data['port_override']
            else:
                port_override = False


            if 'message' in json_data:
                json_message = json_data['message']
                if True: #l_platform == "LMstudio":
                    if port_override:
                        result = TBED_LMstudio.detect(json_message,model,port)
                    else:
                        result = TBED_LMstudio.detect(json_message,model)
                elif False: #l_platform == "Ollama":
                    result = {"response":"error"}

                if result['result'] == "success":
                    data = result['response']
                else:
                    print("Response status code:", result)
                    data = "E"
            else:
                data = "Please use the json format {model:'',message:''} and optionally you can use {platform_override:'',port_override:'',url_override:'', model_override:''}"

            
            
            
            # Prepare response
            response_data = {
                "status": "success",
                "message": "Data received successfully",
                "emergency": data
            }
            
            # Send success response
            self._send_response(200, response_data)
            
        except json.JSONDecodeError:
            # Handle invalid JSON
            error_response = {
                "status": "error",
                "message": "Invalid JSON format"
            }
            self._send_response(400, error_response)
            
        except Exception as e:
            # Handle other errors
            error_response = {
                "status": "error",
                "message": str(e)
            }
            self._send_response(500, error_response)

def run_server(port=server_port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()