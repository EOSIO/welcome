import sys
import json

source = 'readmeiosample_in.txt'
target = 'markdown_out.txt'

block_header = '[block:api-header]'
block_code = '[block:code]'
block_callout = '[block:callout]'
block_parameters = '[block:parameters]'
block_parameters_data = '[block:parameters:data]'
block_image = '[block:image]'
block_embed = '[block:embed]'
block_end = '[/block]'
state_text = 'text'

def translate_type(type):
    if type == 'warning':
        return 'caution'
    else:
        return type

def translate_language(language):
    if language == 'cplusplus':
        return 'cpp'
    else:
        return language

def get_value_from(line):
    value = line.strip()
    first_double_quote_idx = line.find('"')
    last_double_quote_idx = line.rfind('"')
    return value[first_double_quote_idx: last_double_quote_idx-1]

if len(sys.argv) > 2:
    source = sys.argv[1]
    target = sys.argv[2]

print('reading from [' + source + '] and writting to [' + target + ']')

markdown_content = ''
state = state_text
with open(source) as fp:
    code, name, language, type, body, title, cols, rows, data_json  = '', '', '', '', '', '', '', '', ''
    data_rows = []
    for line in fp:
        # block:header
        if state == state_text and line.startswith(block_header):
            state = block_header
            continue
        elif state == block_header and line.startswith(block_end):
            data_json = json.loads(data_json)
            title = data_json["title"] if "title" in data_json.keys() else ''
            markdown_content = markdown_content + '## ' + title + '\n'
            state = state_text
            continue
        elif state == block_header:
            data_json = data_json + line
            continue

        # block:code
        if state == state_text and line.startswith(block_code):
            state = block_code
            continue
        elif state == block_code and line.startswith(block_end):
            data_json = json.loads(data_json)
            data_json = data_json["codes"][0]
            name = data_json["name"] if "name" in data_json.keys() else ''
            language = data_json["language"] if "language" in data_json.keys() else ''
            code = data_json["code"] if "code" in data_json.keys() else ''
            markdown_content = markdown_content + name + '\n' + '```' + translate_language(language) + '\n' + code + '\n' + '```' + '\n'
            state = state_text
            continue
        elif state == block_code:
            data_json = data_json + line
            continue

        # block:callout
        if state == state_text and line.startswith(block_callout):
            state = block_callout
            continue
        elif state == block_callout and line.startswith(block_end):
            data_json = json.loads(data_json)
            type = data_json["type"] if "type" in data_json.keys() else ''
            title = data_json["title"] if "title" in data_json.keys() else ''
            body = data_json["body"] if "body" in data_json.keys() else ''
            markdown_content = markdown_content + '[[' + type + ']]' + '\n' + '|' + title + '\n' + body + '\n'
            state = state_text
            continue
        elif state == block_callout:
            data_json = data_json + line
            continue

        # block:parameters
        if state == state_text and line.startswith(block_parameters):
            state = block_parameters
            continue
        elif state == block_parameters and line.startswith(block_end):
            data_json = json.loads(data_json)

            cols_count = data_json["cols"]
            rows_count = data_json["rows"]

            columns = [''] * cols_count
            rows_matrix = [[''] * cols_count for i in range(rows_count)]

            for key in data_json["data"]:
                value = data_json["data"][key]
                if 'h-' in key:
                    idx = key.replace('h-', '')
                    columns[int(idx)] = value
                else:
                    row_idx, col_idx = key.split('-')
                    row_idx, col_idx = int(row_idx), int(col_idx)
                    rows_matrix[row_idx][col_idx] = value

            # write the column names
            markdown_content = markdown_content + '|'
            for col_idx in range(cols_count):
                markdown_content = markdown_content + columns[col_idx] + '|'
            markdown_content = markdown_content + '\n'
            
            # write the underlying column names
            markdown_content = markdown_content + '|'
            for col_idx in range(cols_count):
                markdown_content = markdown_content + '---|'
            markdown_content = markdown_content + '\n'

            # write the underlying column names
            for row_idx in range(rows_count):
                markdown_content = markdown_content + '|'
                for col_idx in range(cols_count):
                    markdown_content = markdown_content + rows_matrix[row_idx][col_idx] + '|'
                markdown_content = markdown_content + '\n'

            state = state_text
            continue
        elif state == block_parameters:
            data_json = data_json + line
            continue

        # block:image
        # block:embed
        elif state == state_text:
            code, name, language, type, body, title, cols, rows, data_json  = '', '', '', '', '', '', '', '', ''
            markdown_content = markdown_content + line

print('parse completed, write to [' + target + '] file.')

file = open(target, 'w') 
file.write(markdown_content)  
file.close() 

