from flask import Flask
from flask import request, jsonify
import bookrecommend as br

app = Flask(__name__)

@app.route('/api/search', methods=['GET', 'POST'])
def search():
    print request.json
    searchText = request.json['searchText']
    recommendList = br.popularityRecommend()
    print recommendList
    # return jsonify([{
    #     'title': searchText,
    #     'content': 'Blala from backend'
    # }])
    return recommendList
