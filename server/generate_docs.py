import json
import os
from huggingface_api import generate_description

# Templates
FUNCTION_TEMPLATE = "Function {name} takes {params} and {desc}.\nReturns: {ret}."
FILE_TEMPLATE = "# File: {filename}\nPurpose: {desc}\nContains:\n{functions}\n"

def process_function(func, api_token):
    name = func["name"]
    params = ", ".join(func["parameters"]) if func["parameters"] else "no parameters"
    comment = func["comment"]
    body = func["body"]
    
    desc = comment if comment else generate_description(body, api_token)
    ret = "a computed result"
    return FUNCTION_TEMPLATE.format(name=name, params=params, desc=desc, ret=ret)

def process_file(file_data, api_token):
    filename = file_data["file"]
    functions = file_data["functions"]
    func_descriptions = [process_function(f, api_token) for f in functions]
    func_list = "\n".join([f"- {f['name']}" for f in functions])
    desc = generate_description("\n".join([f["body"] for f in functions]), api_token)
    
    markdown = FILE_TEMPLATE.format(filename=filename, desc=desc, functions="\n".join(func_descriptions))
    return filename, markdown

def generate_documentation(json_file, output_dir, api_token):
    with open(json_file, "r") as f:
        data = json.load(f)
    
    os.makedirs(output_dir, exist_ok=True)
    
    for file_data in data:
        filename, markdown = process_file(file_data, api_token)
        with open(os.path.join(output_dir, f"{filename}.md"), "w") as f:
            f.write(markdown)

if __name__ == "__main__":
    token = os.environ.get("HF_API_TOKEN")
    generate_documentation("codebase.json", "docs", token)
