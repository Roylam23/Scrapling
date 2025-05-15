from scrapling import Fetcher
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

fetcher = Fetcher(auto_match=False)

@app.route('/scrap', methods=['POST'])
def scrap():
    try:
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({'error': '請提供要抓取的 URL'}), 400

        url = data['url']

        # 使用 stealthy_headers 來避免被偵測為爬蟲
        page = fetcher.get(url, stealthy_headers=True)

        # 取得所有文字內容, 忽略 script 和 style 標籤
        text_content = page.get_all_text(ignore_tags=('script', 'style'))
        # 過濾所有特殊字符(\n, \t, \r)等
        text_content = text_content.replace('\n', '').replace('\t', '').replace('\r', '')

        return jsonify({
            'status': page.status,
            'content': text_content
        })

    except Exception as e:
        return jsonify({'error': f'抓取失敗: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 