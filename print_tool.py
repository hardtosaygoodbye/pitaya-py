import json

def print_js_var(js_var, value):
    fh = open('visiable/'+ js_var +'.js', 'w')
    fh.write('var '+ js_var + ' =' + json.dumps(value) + ';')
    fh.close()

def print_k_line(res):
    result = []
    for data in res:
        one_line = [str(data['t']), str(data['o']), str(data['c']), 0, 0, str(data['l']), str(data['h']), 0, 0, 0]
        result.append(one_line)
    print_js_var('rawData', result)

def print_trade_arr(trade_arr):
    result = []
    for data in trade_arr:
        if data['status'] == 'open':
            tmp = {
                'name': 'xxx',
                'coord': [str(data['t']), str(data['price'])],
                'value': str(data['price']) + '\n买入 ',
                'itemStyle': {
                    'color': 'rgb(200,60,85)'
                }
            }
        else:
            tmp = {
                'name': 'xxx',
                'coord': [str(data['t']), str(data['price'])],
                'value': str(data['price']) + '\n买入 ',
                'itemStyle': {
                    'color': 'rgb(200,60,85)'
                }
            }
        result.append(tmp)
    print(result)
    print_js_var('tradeData', result)