from flask import Flask, request, jsonify

app=Flask(__name__)

menus = {
    1 : {"id":1, "name":"Espresso", "price":3800},
    2 : {"id":2, "name":"Americano", "price":4100},
    3 : {"id":3, "name":"CafeLatte", "price":4600},
}

@app.route('/')
def hello_flask():
    return 'Hello World!'

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus | 자료를 자원에 추가한다.
""" ---- 미션으로 인해 line 80에 수정한 버전이 있습니다 ----
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()
    new_menu={
        "id" : request_data["id"],
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus[request_data["id"]]=new_menu
    return jsonify(new_menu)

if __name__=='__main__':
    app.run()
"""


"""
필수 과제 : 메뉴 관리 CRUD 구현하기
HTTP 메서드 PUT 를 이용해 Update, DELETE 를 이용해 Delete 기능을 구현해주세요.

PUT /menu/<int:id> : 해당하는 id에 해당하는 데이터를 갱신합니다. (HTTPRequest의 Body에 갱신할 내용이 json으로 전달됩니다.)

DELETE /menu/<int:id> : 해당하는 id에 해당하는 데이터를 삭제합니다.

@app.route() 의 인자로 들어가는 경로에는 다음과 같이 사용해줄 수도 있습니다.
@app.route('/<name>') # URL에 <>를 붙임으로서 이를 함수의 인자로 대입할 수 있습니다.
def my_view_func(name):
    return name

"""

@app.route('/menus/<i>', methods=['PUT'])
def Update(i):
    i=int(i)
    request_data=request.get_json()
    request_data["id"]=i
    menus[i]=request_data
    return jsonify(menus)
    
@app.route('/menus/<i>', methods=['DELETE'])
def Delete(i):
    i=int(i)
    del menus[i]
    return jsonify(menus)
# Postman Agent를 통해 Update와 Delete가 정상적으로 작동함을 확인하였다.

"""
보너스 과제 I: ID야 움직여라 얍!


새로운 menu를 추가하는 POST 영역에서 id가 4로 고정되어있는 문제가 발생합니다.

POST 요청이 들어올 때마다 id가 하나씩 증가하여 menu 리스트에 추가될 수 있도록 코드를 수정해주세요.

이 과제는 필수 과제 이후에 진행되어야 합니다.
"""

@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()
    #---- id값이 이미 menus에 있으면 keys값 중 최댓값+1 로 id 변경, 중복된 id값이 들어와도 최초값으로 변경해 menus에 삽입
    exst=list(menus.keys())
    if request_data["id"] in exst:
        request_data["id"]=max(exst)+1
    #----
    new_menu={
        "id" : request_data["id"],
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus[request_data["id"]]=new_menu
    return jsonify(new_menu)

if __name__=='__main__':
    app.run()