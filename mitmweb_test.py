"""
mitmweb -p 8890 -s mitmweb_test.py
"""
import re
from mitmproxy import ctx

file = open(f'{__file__}.log', 'a+', encoding='utf-8', buffering=1)


def request(flow):
    pass


def response(flow):
    request = flow.request
    response = flow.response

    # 1.替换
    if 'https://www.aqistudy.cn/?mobile=false' in request.url:
        response.text = response.text.replace(r'debugflag = true;', 'debugflag = false;')
        response.text = response.text.replace(r'return false;', 'return true;')

    # 2.替换
    elif 'https://www.aqistudy.cn/html/city_realtime.php?v=2.3' in request.url:
        evals = re.findall(r'eval.*?;', response.text)
        evals_0 = evals[0]
        evals_0_note = f'//{evals_0}'
        response.text = response.text.replace(evals_0, evals_0_note)
