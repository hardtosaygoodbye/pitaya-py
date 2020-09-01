import json

def print_js_var(js_var, value):
    fh = open('visiable/'+ js_var +'.js', 'w')
    fh.write('var '+ js_var + ' =' + json.dumps(value) + ';')
    fh.close()

def print_k_line(res):
    result = []
    for data in res:
        one_line = [data['t'], float(data['o']), float(data['c']), 0, 0, float(data['l']), float(data['h']), 0, 0, 0]
        result.append(one_line)
    print_js_var('rawData', result)