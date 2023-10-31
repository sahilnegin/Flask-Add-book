from flask  import Flask ,jsonify,request 
app = Flask(__name__)
books=[]
@app.route("/addname",methods=['POST'])
def add_book():
    data = request.get_json()
    if 'name' in data and  'year' in data and 'author' in data:
        for book in books:
            if book['name'] == data['name']:
                return jsonify({"message":"book already exist there "})
        book={
            'name':data['name'],
            'year':data['year'],
            'author':data['author']
        } 
        books.append(book)
        return jsonify({"message":"book was added "})
    else:
        return jsonify({"message":"Enter valiad details "})

@app.route("/show", methods=['GET'])
def showbook():
    return jsonify({"books":books})  


@app.route('/delete_book/<string:name>', methods=['DELETE'])
def delete_book(name):
    global books
    # Filter out the book with the specified name
    books = [book for book in books if book['name'] != name]
    return jsonify({'message': 'Book deleted successfully'})




if __name__ == '__main__':
    app.run(debug=True)