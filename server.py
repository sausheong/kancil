import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from flask import Flask, render_template, jsonify, request

index = None
# set up the index, either load it from disk to create it on the fly
def initialise_index():
    global index
    if os.path.exists(os.environ["INDEX_FILE"]):
        index = GPTSimpleVectorIndex.load_from_disk(os.environ["INDEX_FILE"])
    else:
        documents = SimpleDirectoryReader(os.environ["LOAD_DIR"]).load_data()
        index = GPTSimpleVectorIndex.from_documents(documents)

# get path for GUI  
gui_dir = os.path.join(os.path.dirname(__file__), 'gui')  
if not os.path.exists(gui_dir): 
    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gui')

# start server
server = Flask(__name__, static_folder=gui_dir, template_folder=gui_dir)

# initialise index
initialise_index()

@server.route('/')
def landing():
    return render_template('index.html')

@server.route('/query', methods=['POST'])
def query():
    global index
    data = request.json
    response = index.query(data["input"])
    return jsonify({'query': data["input"], 
                    'response': str(response), 
                    'source': response.get_formatted_sources()})