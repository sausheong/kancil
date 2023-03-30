import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from dotenv import load_dotenv
load_dotenv()

print("Loading files in the load directory...")
# Load and save the index to disk
documents = SimpleDirectoryReader(
    input_dir=os.environ["LOAD_DIR"]).load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

# Save the index to disk
index.save_to_disk(os.environ["INDEX_FILE"])
print("Done.")