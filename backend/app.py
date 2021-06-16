import datetime
import json

from flask import Flask, request, render_template, make_response
import pymysql
from flask_cors import CORS
import os

#大志修改2021.6.4
app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
CORS(app, supports_credentials=True)
db = pymysql.connect(host='121.196.111.9',
                     port=3306,
                     user='root',
                     passwd='zxc110',
                     db='ALAL'
                     )
db.autocommit(True)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()

#大志修改2021.6.4
labels = {'1': "科技", '2': "新闻", '3': "美食", '4': "校园", '5': "更多"}
user_info = {
    'id': '',
    'name': '',
    'head_portrait': '',
    'password': '',
    'email': '',
    'role': '',
    'emotional_state': '',
    'couple': '',
    'sex': '',
    'birth': '',
    'job': '',
    'city': '',
    'ideal_type': '',
    'question': ''
}

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     if app.debug:
#         return requests.get('http://localhost:8603/{}'.format(path)).text
#     return render_template("index.html")

#大志修改2021.6.4
def updateUserInfo():
    sql = 'SELECT name,password,head_portrait,email,role,emotional_state,couple,sex,birth,job,city,ideal_type,question FROM user WHERE user_id="%s"' % user_info[
        'id']
    cursor.execute(sql)
    row = cursor.fetchone()
    if row != None:
        user_info['name'] = row[0]
        user_info['password'] = row[1]
        user_info['head_portrait'] = row[2]
        user_info['email'] = row[3]
        user_info['role'] = row[4]
        user_info['emotional_state'] = row[5]
        user_info['couple'] = row[6]
        user_info['sex'] = row[7]
        user_info['birth'] = row[8]
        user_info['job'] = row[9]
        user_info['city'] = row[10]
        user_info['ideal_type'] = row[11]
        user_info['question'] = row[12]
        # file_object = open("user_info.txt", "w")
        # json.dump(user_info, file_object)
        # file_object.close()


# 1.index


@app.route('/index/getNewBlog', methods=['GET'])  # 指定接口访问的路径，支持什么请求方式get，post
def getNewBlog():
    currentPage = int(request.values.get("currentPage"))
    pageSize = int(request.values.get("pageSize"))
    data = {}
    sql = "SELECT COUNT(*) FROM moment"
    cursor.execute(sql)
    total = cursor.fetchone()
    data['total'] = total
    data['currentPage'] = currentPage + 1
    records = []
    sql = "SELECT moment_id,user_id,publish_time,content,like_num FROM moment ORDER BY publish_time DESC"

    cursor.execute(sql)
    row = cursor.fetchone()
    start = (currentPage - 1) * pageSize
    end = currentPage * pageSize
    i = 0
    size = 0
    while row:
        if i >= start:
            size += 1
            record = {}
            record['moment_id'] = row[0]
            record['id'] = row[1]
            record['publish_time'] = row[2].strftime("%Y-%m-%d %H:%M:%S")
            record['content'] = row[3]
            record['like_num'] = row[4]
         #   record['name'] = row[5]
            records.append(record)
            i += 1
            if i >= end:
                break
        row = cursor.fetchone()

    data['size'] = size
    data['code'] = 'success'
    data['records'] = records
    return data

# 2.TagCloud;
@app.route('/index/getHotTag', methods=['GET'])
def getHotTag():
    data = {}
    data['records'] = [{'uid': '1', 'name': '科技'},
                       {'uid': '2', 'name': '新闻'},
                       {'uid': '3', 'name': '美食'},
                       {'uid': '4', 'name': '校园'},
                       {'uid': '5', 'name': '更多'}]
    data['code'] = 'success'
    return data



#大志_更改完成

@app.route('/api/getBlogByUid/moment_id=<blog_id>', methods=['GET'])
def getBlogByUid(blog_id):
    print("blog_id:"+blog_id)
    sql = 'SELECT moment_id,moment.user_id,publish_time,content,picture,read_limit,like_num FROM moment where moment_id ="%s"' \
          %str(blog_id)
    cursor.execute(sql)
    blog = cursor.fetchone()
    sql = 'SELECT name FROM user where user_id="%s"' %blog[1]
    cursor.execute(sql)
    user_name = cursor.fetchone()
    result = {}
    result['author'] = user_name[0]
    result['time'] = blog[2].strftime("%Y-%m-%d %H:%M:%S")
    result['content'] = blog[3]
    result['picture'] = blog[4]
    result['read_limit'] = blog[5]
    result['likeCount'] = blog[6]

    result['code'] = 'success'
    return result


@app.route('/index/getWebConfig', methods=['GET'])
def getWebConfig():
    data = {}
    data['createTime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data['openAdmiration'] = '1'
    data['openComment'] = '1'
    data['code'] = 'success'
    return data


@app.route('/web/comment/payCreditByUid', methods=['GET'])
def payCreditByUid():
    blog_id = int(request.values.get("blog_id"))
    user_id=int(request.values.get("id"))
    data = {}
    credit = 0
    sql = 'CALL readBlog(%d,"%s",%s)' % (
        blog_id, user_info['user_id'], '@credit')
    cursor.execute(sql)
    sql1 = " select @credit"
    cursor.execute(sql1)
    recredit = cursor.fetchone()[0]
    if user_info['reputation'] == 1:
        data['code'] = 'error'
        data['message'] = '你个烂人信誉积分只有1，你不配'
        return data
    if recredit > 0:
        data['code'] = 'success'
    elif recredit < 0:
        data['code'] = 'error'
        data['message'] = '您积分不足，差%d' % recredit

    updateUserInfo()
    return data

#大志_添加评论   已更改
@app.route('/web/comment/add', methods=['POST'])
def addComment():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    user_id=int(data_json.get("id"))
    blogUid = int(data_json.get("blogUid"))
    content = data_json.get("content")

    # sql = 'SELECT MAX(comment_id) FROM Comment'
    # cursor.execute(sql)
    #
    # row = cursor.fetchone()
    # comment_id = 0
    # if row[0] == None:
    #     comment_id = 1
    # else:
    #     comment_id = int(row[0]) + 1
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = 'INSERT INTO comment(moment_id,user_id,time,content) VALUES (%d,%d,"%s","%s")' % (
         blogUid, user_id, time, content)
    cursor.execute(sql)

    data = {}
    data['code'] = 'success'
    return data


# 6.home
# 大志_更改数据库名称
@app.route('/oauth/getFeedbackList', methods=['GET'])
def getFeedbackList():
    user_id = int(request.values.get("id"))
    data = {}
    sql = 'SELECT content FROM message WHERE self_user_id="%s"' % user_id
    cursor.execute(sql)
    row = cursor.fetchone()
    records = []
    while row != None:
        records.append(row[0])
        row = cursor.fetchone()
    print(records)
    data['records'] = records
    data['code'] = '200'
    return data


@app.route('/getUserinfo', methods=['GET'])
def getUserInfo():
    user_id = int(request.values.get("id"))
    data = {}
    data['user_info'] = user_info
    data['code'] = '200'
    return data


@app.route('/logout/logout', methods=['GET'])
def logout():
    data={}
    data['code'] = 'success'
    data['message'] = '退出成功'
    return data

# 大志_ 更改成 查询好友列表
@app.route('/web/comment/getFollowListByUser',methods=['GET'])
def getFollowListByUser():
    user_id = int(request.values.get("id"))
    data = {}
    records = []
    sql = 'SELECT user_id2,name FROM friend,user WHERE user_id2=user.user_id AND user_id1="%s" ORDER BY time DESC' % \
          user_id
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        record = {}
        record['follower_id'] = row[0]
        idd = row[0]
        sql1 = " SELECT name from user WHERE user_id = %s" % idd
        cursor.execute(sql1)
        nname = cursor.fetchone()[0]
        record['createTime'] = row[1]
        record['nickName'] = nname
        records.append(record)
        row = cursor.fetchone()

    data['records'] = records
    data['code'] = '200'
    return data

# 大志_ 我觉得莫得收藏
@app.route('/web/comment/getCollectListByUser')
def getCollectListByUser():
    data = {}
    records = []
    sql = 'SELECT blog_id,time,name FROM Favorites WHERE user_id="%s" ORDER BY time DESC' % user_info[
        'user_id']
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        record = {}
        record['blog_id'] = row[0]
        record['createTime'] = row[1]
        record['name'] = row[2]
        records.append(record)
        row = cursor.fetchone()

    data['records'] = records
    data['code'] = 'success'
    return data

# 大志_ 我觉得没历史
@app.route('/web/comment/getHistoryListByUser', methods=['POST'])
def getHistoryListByUser():
    data = {}
    records = []
    sql = 'SELECT History.blog_id,time,title ' \
          'FROM History,Blog ' \
          'WHERE History.blog_id=Blog.blog_id AND History.user_id="%s" AND state=0 ' \
          'ORDER BY time DESC' % user_info['user_id']
    cursor.execute(sql)
    row = cursor.fetchone()
    i = 0
    while row:
        i += 1
        record = {}
        record['blog_id'] = row[0]
        record['createTime'] = row[1]
        record['title'] = row[2]
        records.append(record)
        row = cursor.fetchone()

    data['records'] = records
    if i == 0:
        data['code'] = 'error'
        data['message'] = '暂无历史浏览记录'
    else:
        data['code'] = 'success'
    return data

# 大志_juede 没搜索
@app.route('/search/sqlSearchBlog', methods=['GET'])
def search():
    # currentPage = int(request.values.get("currentPage"))
    # pageSize = int(request.values.get("pageSize"))
    str = request.values.get("keywords")
    data = {}
    sql = 'SELECT COUNT(*) FROM Blog WHERE state=0 AND title LIKE %s '
    request = ['%' + str + '%']
    print(sql)
    cursor.execute(sql, request)
    total = cursor.fetchone()[0]
    print(total)
    data['total'] = total
    # data['currentPage'] = currentPage + 1
    # print(data['currentPage'])
    records = []
    sql = 'SELECT * FROM Blog WHERE state=0 AND title LIKE %s  ORDER BY publish_time DESC'
    cursor.execute(sql, request)
    row = cursor.fetchone()
    # start = (currentPage - 1) * pageSize
    # end = currentPage * pageSize
    size = 0
    while row:
        size += 1
        record = {}
        record['user_id'] = row[1]
        record['blogUid'] = row[0]
        blog_labels = row[9].split(",")
        blog_label_name = []
        for blog_label in blog_labels:
            blog_label_name.append(labels[blog_label])

        record['labels'] = blog_label_name
        record['summary'] = row[4][0:100]
        record['clickCount'] = row[7]
        record['likeCount'] = row[6]
        record['time'] = row[2].strftime("%Y-%m-%d %H:%M:%S")
        record['title'] = row[3]
        print(record)
        records.append(record)

        row = cursor.fetchone()

    data['size'] = size
    data['code'] = 'success'
    data['records'] = records
    return data


# 个人页查找所有moment 的 list
@app.route('/web/comment/getListByUser', methods=['POST'])
def getCommentListByUser():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    data = {}
    commentList = []
    replyList = []
    user_id = user_info['user_id']
    sql = 'select name from user where user_id="%d"' % user_id
    cursor.execute(sql)
    name = cursor.fetchone()[0]
    # 前面的name是我评论的文章的作者的姓名，后面的name是评论我的文章的用户姓名
    sql = "SELECT comment.user_id,comment.moment_id,comment.time,comment.content,moment.user_id,user.name from comment,moment,user where comment.moment_id=moment.moment_id and user.user_id=moment.user_id and comment.user_id='%d'" % user_id
    cursor.execute(sql)
    row = cursor.fetchone()
    end = 10
    comment = 0
    reply = 0
    size = 0
    while row:
        if comment <= 10:
            comment += 1
            record = {}
            record['uid'] = row[0]
            record['createTime'] = row[3]
            record['blogUid'] = row[2]
            user = {}
            user['nickName'] = row[6]
            user['source'] = 'BLOG_INFO'
            user['sourceName'] = '博客详情'
            user['content'] = row[4]
            record['user'] = user
            commentList.append(record)
        else:
            break
        row = cursor.fetchone()

    sql = "SELECT comment.user_id,comment.moment_id,comment.time,comment.content,moment.user_id,user.name from comment,moment,user where comment.moment_id=moment.moment_id and user.user_id=comment.user_id and moment.user_id=" + user_id
    cursor.execute(sql)
    row = cursor.fetchone()
    end = 10
    comment = 0
    reply = 0
    size = 0
    while row:
        if reply <= 10:
            reply += 1
            record = {}
            record['uid'] = row[0]
            record['createTime'] = row[3]
            record['blogUid'] = row[2]
            user = {}
            # 评论我的博客的用户名称
            user['nickName'] = row[6]
            user['source'] = 'BLOG_INFO'
            user['sourceName'] = '博客详情'
            user['content'] = row[4]
            record['user'] = user
            replyList.append(record)
        else:
            break
        row = cursor.fetchone()

    data['code'] = 'success'
    data['commentList'] = commentList
    data['replyList'] = replyList
    return data

# 大志_点赞
@app.route('/api/praiseBlogByUid', methods=['GET'])
def praiseBlogByUid():
    print("I am in praiseBlogByUid")
    id = int(request.values.get('uid'))
    user_id = int(request.values.get('id'))
    # SQL语句点赞数+1
    sql1 = "UPDATE moment SET like_num = like_num +1 WHERE moment_id='%d'" % id
    # SQL语句查询点赞数
    sql2 = "SELECT like_num FROM moment WHERE moment_id='%d'" % id
    sql3 = "INSERT INTO `moment`.`like` (`user_id`, `moment_id`, `time`) VALUES ('%d', '%d', current_time);" % (
        user_id, id)

    # 执行SQL语句
    flag = False
    try:
        cursor.execute(sql2)
        number = cursor.fetchall()
        cursor.execute(sql3)
        cursor.execute(sql1)
        flag = True
    except:
        flag = False
    if flag == True:
        return {"code": 'success', "number": number[0][0] + 1}

    return {"code": 'error', "number": number[0][0], "message": "您已经点过赞了！"}

# 大志_获取点赞数

def getPraise(id):
    sql = "SELECT like_num FROM moment WHERE moment_id='%d'" % id
    try:
        # 执行SQL语句
        cursor.execute(sql)
        number = cursor.fetchall()
    except:
        print('error')
        db.rollback()
    return number

# 大志_ 不需要改
@app.route('/api/getBlogPraiseCountByUid', methods=['GET'])
def getBlogPraiseCountByUid():
    print("I am in getBlogPraiseCountByUid")
    id = int(request.values.get('uid'))
    return getPraise(id)


#  大志_这没啥用
@app.route('/api/addCollectBlog', methods=['GET'])
def addCollectBlog():
    print("I am in addCollectBlog")
    id = int(request.values.get('uid'))
    collectName = str(request.values.get('collectName'))
    data = {}
    print(user_info)
    if user_info['user_id'] == '':
        data["code"] = 'error'
        data['message'] = '您尚未登录！'
        return data
    sql = "INSERT INTO `blogs`.`Favorites` (`user_id`, `blog_id`, `time`, `name`) VALUES ('%s', '%d', current_time, '%s');" % (
        user_info['user_id'], id, collectName)
    try:
        cursor.execute(sql)
        data['code'] = 'success'
    except:
        db.rollback()
        data['code'] = 'error'
        data['message'] = '您已经收藏过了'
        print('error啦！！！！')
    return data


#  这没啥用_大志
@app.route('/web/comment/getPraiseListByUser', methods=['POST'])
def getPraiseList():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    currentPage = data_json.get("currentPage")
    user_id = data_json.get("id")
    pageSize = data_json.get("pageSize")
    data = {}
    records = []
    data["records"] = records
    sql = "select Approval.user_id,Approval.blog_id,Approval.time,Blog.title from Approval,Blog where Approval.blog_id=Blog.blog_id and Approval.user_id='" + user_id + "'"
    cursor.execute(sql)
    row = cursor.fetchone()
    start = (currentPage - 1) * pageSize
    end = currentPage * pageSize
    i = 0
    size = 0
    while row:
        if i >= start:
            size += 1
            record = {}
            record['uid'] = row[0]
            record['createTime'] = row[2]
            user = {}
            user['uid'] = row[1]
            user['title'] = row[3]
            record['blog'] = user
            records.append(record)
            i += 1
            if i >= end:
                break
        row = cursor.fetchone()

    data['code'] = 'success'
    data['records'] = records
    return data

# 大志_用户登录验证
@app.route('/oauth/verify/<token>')
def authVerify(token):

    data={}
    data['code'] = 'success'
    data['message'] = '登录成功'
    try:
        db.ping()
    except:
        db.connect()
        print("disconect")
    sql = "SELECT * FROM user WHERE user_id = '%s'" % token
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        user_info['id'] = row[0]
        user_info['name'] = row[1]
        user_info['head_portrait'] = row[2]
        user_info['password'] = row[3]
        user_info['email'] = row[4]
        user_info['role'] = row[5]
        user_info['emotional_state'] = row[6]
        user_info['couple'] = row[7]
        user_info['sex'] = row[8]
        user_info['birth'] = row[9].strftime("%Y-%m-%d")
        user_info['job'] = row[10]
        user_info['city'] = row[11]
        user_info['ideal_type'] = row[12]
        user_info['question'] = row[13]
    data['id'] = user_info.get('id')
    print("loginnn")
    print(user_info)
    data['records'] = user_info
    file_object = open("user_info.txt", "w")
    json.dump(user_info, file_object)
    file_object.close()
    return data


# 7.blog
# @app.route('/tag/getTagList', methods=['GET'])
# def getBlogTagList():
#     data = {}
#     records = [{"uid": 1, "content": "科技"}, {"uid": 2, "content": "新闻"}, {"uid": 3, "content": "美食"},
#                {"uid": 4, "content": "校园"}, {"uid": 5, "content": "更多"}]
#     data['records'] = records
#     data['code'] = 'success'
#     return data

# 66改成返回动态查看状态选择
@app.route('/blogSort/getList', methods=['GET'])
def getBlogSortList():
    data = {}
    records = []
    activity = {}
    activity['uid'] = 0
    activity['name'] = "所有人均可见"
    records.append(activity)
    activity['uid'] = 1
    activity['name'] = "仅好友可见"
    records.append(activity)
    activity['uid'] = 2
    activity['name'] = "仅自己可见"
    records.append(activity)

    data['records'] = records
    data['code'] = 'success'
    return data

# 大志_添加博客
@app.route('/blog/add', methods=['POST'])
def addBlog():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    form = data_json
    print(form)
    sql = "SELECT MAX(moment_id) FROM moment"
    cursor.execute(sql)
    max_id = cursor.fetchone()
    if max_id == None:
        blog_id = 1
    else:
        blog_id = max_id[0] + 1
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    label_num = form.get("tagUid")
    activityid = str(form.get("blogSortUid"))
    nnum = 0
    sql1 = "INSERT INTO `ALAL`.`moment` (`moment_id`, `user_id`, `publish_time`, `content`, `picture`, `read_limit`, `like_num`) VALUES ('%d', '%d', '%s', '%s', '%s', '%d', '%d');" % (
    blog_id, form.get("id"), time, form.get("content"), form.get("picture"), form.get("read_limit"), nnum)
    cursor.execute(sql1)
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    updateUserInfo()
    data = {}
    data['code'] = '200'
    data['message'] = '发布博客成功'
    data['moment_id']=blog_id
    return data


# 8.大志_获取关注者列表，没啥用了
@app.route('/api/getFollowedByUid', methods=['GET'])
def getFollowedByUid():
    uid = request.values.get("uid")
    print("getfollowedbyuid")
    print(user_info)
    print(uid)
    sql = "SELECT * FROM Follow WHERE user_id=\"" + \
          user_info['user_id'] + "\" AND follower_id='" + uid + "'"
    cursor.execute(sql)
    row = cursor.fetchone()
    data = {}
    if row == None:
        data['liked'] = 0
    else:
        data['liked'] = 1
    data['code'] = 'success'
    print(data.get('liked'))
    return data

# 大志_关注_应该没啥用
@app.route('/api/FollowByUid', methods=['GET'])
def followByUid():
    uid = request.values.get("uid")
    if uid == user_info['user_id']:
        data = {}
        data['code'] = 'error'
        data['message'] = '自己不能关注自己'
        return data

    sql = "SELECT * FROM Follow WHERE user_id= '" + \
          user_info['user_id'] + "' AND follower_id= '" + uid + "'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if row == None:
        print(user_info['user_id'])
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "INSERT INTO Follow VALUES ('" + \
              user_info['user_id'] + "','" + uid + "','" + time + "')"
        cursor.execute(sql)
    else:
        sql = "DELETE FROM Follow WHERE user_id= '" + \
              user_info['user_id'] + "' AND follower_id='" + uid + "'"
        cursor.execute(sql)
    data = {}
    data['code'] = 'success'
    return data


# 9.sort
# 大志_查看活动的博客_应该没啥用
@app.route('/sort/getSortList', methods=['GET'])
def getSortList():
    data = {}
    records = []
    sql = "SELECT activity_id,name,description FROM Activity"
    cursor.execute(sql)
    row = cursor.fetchone()
    i = 0
    while row:
        print(row)
        i += 1
        activity = {}
        activity['id'] = int(row[0])
        activity['content'] = row[1]
        activity['description'] = row[2]
        records.append(activity)
        row = cursor.fetchone()

    data['records'] = records
    if i == 0:
        data['code'] = 'error'
        data['message'] = '暂无活动'
    else:
        data['code'] = 'success'
    return data

# 查看活动下的博客
@app.route('/sort/getArticleBySort', methods=['GET'])
def getArticleBySort():
    id = int(request.values.get("id"))
    data = {}
    records = []
    sql = "SELECT Blog.user_id,publish_time,title,label,activity,name ,blog_id" \
          " FROM Blog,Activity " \
          " WHERE Blog.activity=Activity.activity_id AND activity=" + \
          str(id) + " ORDER BY publish_time DESC"
    cursor.execute(sql)
    row = cursor.fetchone()
    i = 0
    while row:
        i += 1
        blog = {}
        blog['title'] = row[2]
        blog['author'] = row[0]
        blog['uid'] = row[6]
        label_nums = row[3].split(",")
        blog_labels = []
        for label_num in label_nums:
            label = {}
            label['uid'] = label_num
            label['content'] = labels[label_num]
            blog_labels.append(label)
        blog['labels'] = blog_labels
        blogSort = {}
        blogSort['uid'] = row[4]
        blogSort['sortName'] = row[5]
        blog['blogSort'] = blogSort
        blog['time'] = row[1].strftime('%Y-%m-%d %H:%M:%S')
        records.append(blog)
        row = cursor.fetchone()

    data['records'] = records
    if i == 0:
        data['code'] = 'error'
        data['message'] = '此活动下暂无博客'
    else:
        data['code'] = 'success'

    return data


# 10.tag
# 大志_获取tag列表_应该没啥用
@app.route('/tag/getTagList', methods=['GET'])
def getTagList():
    data = {'records': [
        {'id': '1', 'name': '科技'},
        {'id': '2', 'name': '新闻'},
        {'id': '3', 'name': '美食'},
        {'id': '4', 'name': '校园'},
        {'id': '5', 'name': '更多'},
    ], 'code': 'success'}
    return data

# 大志_通过标签查博客_应该没啥用
@app.route('/tag/getArticleByTagUid', methods=['GET'])
def getArticleByTagUid():
    tagUid = request.values.get("tagUid")
    sql = "SELECT title,Blog.user_id,label,activity,publish_time,name " \
          "FROM Blog,Activity " \
          "WHERE Blog.activity=Activity.activity_id " \
          "AND label LIKE \"%" + tagUid + "%\" " + \
          "ORDER BY publish_time DESC"
    cursor.execute(sql)
    row = cursor.fetchone()
    records = []
    i = 0
    while row:
        i += 1
        blog = {}
        blog['title'] = row[0]
        blog['author'] = row[1]
        blog_labels = []
        label_nums = row[2].split(",")
        for label_num in label_nums:
            label = {}
            label['uid'] = label_num
            label['content'] = labels[label_num]
            blog_labels.append(label)
        blog['labels'] = blog_labels
        blogSort = {}
        blogSort['uid'] = row[3]
        blogSort['sortName'] = row[5]
        blog['blogSort'] = blogSort
        blog['time'] = row[4].strftime('%Y-%m-%d %H:%M:%S')
        records.append(blog)
        row = cursor.fetchone()
    data = {}
    data['records'] = records
    if i == 0:
        data['code'] = 'error'
        data['message'] = '此标签下暂无博客'
    else:
        data['code'] = 'success'
    return data

# 没啥用_管理员处理举报
# 11.admin
@app.route('/admin/workReport', methods=['POST'])
def workReport():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    uid = data_json.get("uid")
    blog_id = data_json.get("blog_id")
    status = data_json.get("status")
    if status == 1:
        sql = 'UPDATE Report SET state=1 WHERE user_id="%s" AND blog_id=%d' % (
            uid, blog_id)
        cursor.execute(sql)
        sql = 'UPDATE Report SET state=1 WHERE blog_id=%d' % blog_id
        cursor.execute(sql)
    else:
        sql = 'UPDATE Report SET state=2 WHERE user_id="%s" AND blog_id=%d' % (
            uid, blog_id)
        cursor.execute(sql)
    data = {}
    data['code'] = 'success'
    updateUserInfo()
    return data

# dazhi_管理员获取举报列表_没啥用
@app.route('/admin/getReportList')
def getReportList():
    data = {}
    records = []
    data["records"] = records
    user_id = user_info['user_id']
    sql = "select Report.user_id,Report.blog_id,Report.time,Report.reason,Report.state,Blog.title from Report,Blog where Report.state=0 AND Report.blog_id=Blog.blog_id"
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        record = {}
        record['uid'] = row[0]
        record['blog_id'] = row[1]
        record['time'] = row[2]
        record['reason'] = row[3]
        record['status'] = row[4]
        record['title'] = row[5]
        records.append(record)
        row = cursor.fetchone()

    data['code'] = 'success'
    data['message'] = '操作成功'
    return data

# 举报_按时间排序
@app.route('/admin/getSortList')
def getActivityList():
    data = {}
    records = []
    data["records"] = records
    sql = "select * from Activity"
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        record = {}
        record['uid'] = row[0]
        record['sortName'] = row[2]
        record['startTime'] = row[3]
        record['endTime'] = row[4]
        record['credit'] = row[5]
        records.append(record)
        row = cursor.fetchone()

    data['code'] = 'success'
    return data

# 大志认为这没啥用_举报博客
@app.route('/admin/blogSort/add', methods=['POST'])
def addBlogSort():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    activityName = data_json.get("sortName")
    description = data_json.get("description")
    startTime = data_json.get("startTime")
    endTime = data_json.get("endTime")
    credit = int(data_json.get("credit"))
    data = {}
    records = []
    data["records"] = records
    user_id = user_info['user_id']
    sql = "select count(*) from Activity"
    cursor.execute(sql)
    num = cursor.fetchone()[0] + 1
    sql = 'INSERT INTO Activity (activity_id,user_id,name,start_time,end_time,credit,description) VALUES (%d,"%s","%s","%s","%s",%d,"%s")' % (
        num, user_info['user_id'], activityName, startTime, endTime, credit, description)
    print(sql)
    cursor.execute(sql)
    row = cursor.fetchone()
    data['message'] = '添加活动成功'
    data['code'] = 'success'
    return data


# 大志_注册
@app.route('/login/register', methods=['POST'])
def localRegister():
    print("I am in registerAndregister")
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    username = data_json.get("userName")
    password = data_json.get("passWord")
    email = data_json.get("email")
    nickname = data_json.get("nickName")


    sql = "SELECT * FROM user WHERE user_id = '%s'" % username
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 向数据库提交
        results = cursor.fetchall()

    except:
        # 发生错误时回滚
        print('error')
        db.rollback()
    data = {}
    if len(results) == 0:
        data['code'] = 'success'
        data['message'] = '注册成功'
        sql = "INSERT INTO `user` (`user_id`, `name`, `head_portrait`，`password`, `email`, `role`, `emotional_state`, `couple`,`sex`,`birth`,`job`,`city`,`ideal_type`,`question`) VALUES ('%s','%s', '%s', '%s', '%s', '1', '%d', '%d', '%s','%s','%s','%s','%s','%s');" % (
            username,data_json.get("head_portrait") ,nickname, password, email,data_json.get("emotional_state"),data_json.get("couple"),data_json.get("sex"),data_json.get("birth"),data_json.get("job"),data_json.get("city"),data_json.get("ideal_type"),data_json.get("question"))
        cursor.execute(sql)
        sql = "SELECT * FROM user WHERE user_id = '%s'" % username
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            user_info['user_id'] = row[0]
            user_info['name'] = row[1]
            user_info['head_portrait'] = row[2]
            user_info['password'] = row[3]
            user_info['email'] = row[4]
            user_info['role'] = row[5]
            user_info['emotional_state'] = row[6]
            user_info['couple'] = row[7]
            user_info['sex'] = row[8]
            user_info['birth'] = row[9]
            user_info['job'] = row[10]
            user_info['city'] = row[11]
            user_info['ideal_type'] = row[12]
            user_info['question'] = row[13]
    else:
        data['code'] = 'error'
        data['message'] = '注册失败,该账号已被注册'

    sql = "SELECT * FROM user "
    cursor.execute(sql)
    return data


# 4.大志觉得没啥用_举报
@app.route('/api/reportBlog', methods=['GET'])
def ReportBlog():
    print("I AM IN ReportBlog!")
    id = int(request.values.get('uid'))
    content = str(request.values.get("reason"))
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO `blogs`.`Report` (`user_id`, `blog_id`, `time`, `reason`, `state`) VALUES ('%s', '%d', '%s', '%s', 0);" % (
        user_info['user_id'], id, time, content)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        comment = cursor.fetchall()
    except:
        print('error')
        db.rollback()
    data = {}
    data['code'] = 'success'
    data['message'] = '举报成功'
    return data


# 12 大志_读取评论
@app.route('/web/comment/getList', methods=['POST'])
def GetCommentList():
    print("I AM IN GetCommentList!")
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    id = int(data_json.get('blogUid'))
    data = {}
    data['code'] = 'success'
    records = []
    sql = "SELECT * FROM comment WHERE moment_id='%d'" % id
    #   try:
    # 执行SQL语句
    try:
        # 执行SQL语句
        cursor.execute(sql)
        comment = cursor.fetchall()
    except:
        print('error')
        data['code'] = 'error'
        db.rollback()
    if len(comment)== 0 :
        data['code'] = 'success'
        data['records']= []
    for i in range(0, min(9, len(comment))):
        record = {}
        record['uid'] = int(i)
        record['createTime'] = comment[i][3].strftime("%Y-%m-%d %H:%M:%S")
        sql = "SELECT name FROM user WHERE user_id = '%s'" % comment[i][1]
        cursor.execute(sql)
        nname = cursor.fetchall()
        name = nname[0][0]
        user = {}
        user['id'] = comment[i][1]
        user['nickName'] = name
        record['user'] = user
        record['content'] = comment[i][4]
        records.append(record)

    data['records'] = records
    return data


#大志_这里没改哦，应该加一个momentID
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        base_path = os.path.abspath(os.path.dirname(__file__))
        print(base_path)
        dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        upload_path = os.path.join(base_path, 'static\\uploads\\') + "%s.jpg" % dt
        print(upload_path)
        f.save(upload_path)
        data={}
        data['code']='success'
        data['uid']="%s.jpg" % dt
        return data

@app.route('/uploadMomentPhotos', methods=['POST'])
def uploadMomentPhoto():
    print("uploadmoment")
    print(request.data)
    datastr = str(request.data, 'utf-8')
    print(datastr)
    data_json = json.loads(datastr)
    moment_id = data_json.get("moment_id")
    pics = []
    print(data_json)
    print(data_json.get("picList"))
    pics = data_json.get("picList")
    uurl = ""
    for pic in pics:
        uurl = uurl + "," + pic
    data = {}
    sql = "Update moment SET picture ='%s' WHERE (moment_id=%d);" %(uurl,moment_id)
    print(sql)
    data ['code'] = 'success'
    try:
        # 执行SQL语句
        cursor.execute(sql)
    except:
        # 发生错误时回滚
        print('error')
        db.rollback()
        data['code'] = 'error'
    return data

# show photo
@app.route('/display/img/<string:filename>', methods=['GET'])
def display_img(filename):
    base_path = os.path.abspath(os.path.dirname(__file__))
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(
                base_path + '/static/uploads/' + filename, "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/jpg'
            return response
    else:
        pass


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/')
def welcome():
    return render_template("index.html")


# @app.route('/')
# def welcome():
#     return render_template("Welcome.html")



@app.route('/api/getBlogPicByUid/moment_id=<moment_id>', methods=['GET'])
def getBlogPicByUid(moment_id):
    # moment_id= request.args.get("moment_id")
    print("picblog:"+moment_id)
    data = {}
    data['code'] = 'success'
    sql = 'SELECT picture FROM moment WHERE moment_id="%s"' % moment_id
    cursor.execute(sql)
    row=cursor.fetchone()
    data['urls']=[]
    if row != None:
        picture=row[0]
        data['urls']=picture.split(str=",")
    return data

@app.route('/index/getAvatarsByUserID', methods=['GET'])
def getAvatarsByUserID():
    id=request.values.get("id")
    print(id)
    data = {}
    data['code'] = 'success'
    data['urls']=[]

    sql='SELECT sex FROM user WHERE user_id="%s"'%id
    print(sql)
    cursor.execute(sql)
    row = cursor.fetchone()
    sex=row[0]
    print(sex)
    if sex=='f':
        sql = 'SELECT head_portrait FROM user WHERE sex="m" and emotional_state=0'
    else:
        sql = 'SELECT head_portrait FROM user WHERE sex="f" and emotional_state=0'
    try :
       cursor.execute(sql)
       row=cursor.fetchone()
    except :
        print("error")
        db.rollback()
    i=0
    while row:
        data['urls'].append(row[0])
        i+=1
        if i == 9:
            break
        try :
            row = cursor.fetchone()
        except :
            print("error")
            db.rollback()

    return data

@app.route('/question/editQuestion', methods=['POST'])
def editQuestion():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    user_id=data_json.get("id")
    questions=str(data_json.get("questionData"),'utf-8') 
    user_id=request['id']
    sql = 'UPDATE user SET question="%s" WHERE user_id="%s"' % (questions,user_id)
    try :
        cursor.execute(sql)
    except :
        print("error")
        db.rollback()
    data = {}
    data['code'] = 'success'
    return data

# 大志_登录函数

@app.route('/login/login', methods=['POST'])
def LocalLogin():
    print("I am in loginAndLogin")
    
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    username = data_json.get("userName")
    password = data_json.get("passWord")
    print(username)
    print(password)
    sql = "SELECT * FROM user WHERE user_id = '%s' AND password = '%s' " % (
        username, password)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 向数据库提交
        results = cursor.fetchall()

    except:
        # 发生错误时回滚
        print('error')
        db.rollback()
    data = {}
    user_info={}
    if len(results) == 0:
        data['code'] = 'error'
        data['message'] = '密码不正确'
    else:
        data['code'] = 'success'
        data['message'] = '登录成功'
        sql = "SELECT * FROM user WHERE user_id = '%s'" % username
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            user_info['id'] = row[0]
            user_info['name'] = row[1]
            user_info['avatar'] = row[2]
            user_info['password'] = row[3]
            user_info['email'] = row[4]
            user_info['role'] = row[5]
            user_info['emotional_state'] = row[6]
            user_info['couple'] = row[7]
            user_info['sex'] = row[8]
            user_info['birth'] = row[9].strftime("%Y-%m-%d")
            user_info['job'] = row[10]
            user_info['city'] = row[11]
            user_info['idealType'] = row[12]
            user_info['question'] = row[13]
        data['id'] = user_info.get('id')
    print("loginnn")
    print(user_info)
    data['records'] = user_info
    file_object = open("user_info.txt", "w")
    json.dump(user_info, file_object)
    file_object.close()

    return data

@app.route('/user/editResume', methods=['POST'])
def editInformation():
    global user_info
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    newUesrInfo = data_json.get("userInfo")
    data = {}
    data['code'] = 'success'
    user_info = newUesrInfo
    sql ="UPDATE `ALAL`.`user` SET `user_id` = '%d', `name` = '%s', `head_portrait` = '%s', `password` = '%s', `email` = '%s', `role` = '%d', `emotional_state` = %d', `couple` = '%d', `sex` = '%s', `birth` = '%s', `job` = '%s', `city` = '%s', `ideal_type` = '%s', `question` = '%s' WHERE (`user_id` = '%d');"\
         %(user_info['user_id'],user_info['name'],user_info['head_portrait'],user_info['password'],user_info['email'],user_info['role'],user_info['emotional_state'],user_info['couple'],user_info['sex'],user_info['birth'],user_info['job'],user_info['city'],user_info['ideal_type'],user_info['question'])
    try:
        # 执行SQL语句
        cursor.execute(sql)
    except:
        # 发生错误时回滚
        print('error')
        db.rollback()
        data['code'] = 'error'
    return data

@app.route('/user/getFriendsRequestList', methods=['GET'])
def getFriendRequest():
    # datastr = str(request.data, 'utf-8')
    # data_json = json.loads(datastr)
    # id = data_json.get("id")
    id =request.args.get("id")
    print("friendrequest "+id)
    data = {}
    data['code'] = 'success'
    sql = "SELECT * FROM friend_apply WHERE (state=0 and respondent_id='%s')" %(id)
    results=None
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 向数据库提交
        results = cursor.fetchall()
    except Exception as e:
        # 发生错误时回滚
        print('error'+str(e))
        db.rollback()
    if len(results) == 0:
        data['code'] = 'error'
        data['message'] = 'no application'
    else :
        applications = []
        for i in range(0,len(results)):
            application = {}
            application['id'] = results[i][1]
            application['createdTime'] = results[i][3].strftime("%Y-%m-%d %H:%M:%S")
            sql1 = "SELECT 'user'.'name' from 'user' WHERE ('user_id'= '%s')" % (application['id'])
            try:
                # 执行SQL语句
                cursor.execute(sql1)
                # 向数据库提交
                uuser = cursor.fetchone()
            except:
                # 发生错误时回滚
                print('error')
                db.rollback()
            nname = uuser[0]
            application['applicant']=nname
            applications.append(application)
        data['list'] = applications
    return data

@app.route('/user/editPassword', methods=['POST'])
def editPassword():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    id = data_json.get("id")
    pwd = data_json.get("password")
    data = {}
    data['code'] = 'success'
    sql = "UPDATE 'user' SET 'password'='%s' WHERE ('user_id'='%d');" % (pwd,id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
    except:
        # 发生错误时回滚
        print('error')
        db.rollback()
        data['code']='error'

    return data

@app.route('/submitResult', methods=['POST'])
def submitResult():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    id = data_json.get("id")
    accept = data_json.get("accept")
    sql = "SELECT * from 'friend_apply' WHERE ('application_id'='%d');"%(id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 向数据库提交
        apply = cursor.fetchone()
    except:
        # 发生错误时回滚
        print('error')
        db.rollback()
    if accept == true:
        sql = "INSERT INTO `ALAL`.`friend`(`user_id1`, `user_id2`, `time`) VALUES('%d', '%d', '%s');"%(apply[1],apply[2],apply[3])
        try:
            # 执行SQL语句
            cursor.execute(sql1)
        except:
            # 发生错误时回滚
            print('error')
            db.rollback()
        sql1 = "UPDATE 'friend_apply' SET 'state'='1' WHERE ('application_id'='%d');" % (id)
        try:
            # 执行SQL语句
            cursor.execute(sql1)
        except:
            # 发生错误时回滚
            print('error')
            db.rollback()
    else :
        sql1 = "UPDATE 'friend_apply' SET 'state'='2' WHERE ('application_id'='%d');" % (id)
        try:
            # 执行SQL语句
            cursor.execute(sql1)
        except:
            # 发生错误时回滚
            print('error')
            db.rollback()
    data = {}
    data['code'] = 'success'
    return data

@app.route('/getBlogListByID', methods=['GET'])
def getBlogListByID():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    id = data_json.get("id")
    page = data_json.get("currentPage")
    size = data_json.get("size")

    sql = "SELECT * from 'moment' WHERE 'user_id'='%d'"%(id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 向数据库提交
        results = cursor.fetchall()
    except:
        # 发生错误时回滚
        print('error')
        db.rollback()
    data = {}
    data['code']='success'
    if len(results) == 0:
        data['code'] = 'success'
        data['total'] = 0
        data['size'] = size
        data['currentPage'] = page
        records = []
        data['records'] = records
    else :
        data['code'] = 'success'
        data['total'] = len(results)
        data['size'] = size
        data['currentPage'] = page
        records = results
        data['records'] = records
    return data

@app.route('/getQuestion', methods=['GET'])
def getQuestion():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    id = data_json.get("id")
    sql = "SELECT 'question' from user WHERE 'user_id'=%d;"%(id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 向数据库提交
        result = cursor.fetchone()
    except:
        # 发生错误时回滚
        print('error')
        db.rollback()
    qs=result[0].split("/")
    data = {}
    qd=[]
    qusetion={}
    for i in (1,5):
        qusetion['id']=i
        qusetion['title']='填空题：请填写你的问题'
        qusetion['type']='textarea'
        qusetion['data']=qs[i-1]
        qd.append(qusetion)
    data['qusetionData'] = qd
    return data

@app.route('/submitQuestion', methods=['POST'])
def submitQuestions():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    id = data_json.get("id")
    ans = data_json.get("questionData")
    qans = ans[0]+"/"+ans[1] + "/" + ans[2] + "/" + ans[3] + "/" + ans[4]
    data = {}
    data ['code'] = 'success'
    sql = "UPDATE 'friend_apply' SET 'question_answer'='%s' WHERE 'application_id'='%d';"%(qans,id)
    try:
        # 执行SQL语句
        cursor.execute(sql)
    except:
        # 发生错误时回滚
        print('error')
        db.rollback()
        data['code']='error'
    return data

@app.route('/getQuestions', methods=['GET'])
def getQuestions():
    datastr = str(request.data, 'utf-8')
    data_json = json.loads(datastr)
    id = data_json.get("id")
    sql = "SELECT * from friend_apply WHERE 'application_id'=%d;" % (id)
    data = {}
    data['code'] = 'success'
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 向数据库提交
        result = cursor.fetchone()
    except:
        # 发生错误时回滚
        print('error')
        db.rollback()
        data['code'] = 'error'

    qs = result[0].split("/")
    qd = []
    qusetion = {}
    for i in (1, 5):
        qusetion['id'] = i
        qusetion['title'] = '填空题：请填写你的问题'
        qusetion['type'] = 'textarea'
        qusetion['data'] = qs[i - 1]
        qd.append(qusetion)
    data['qusetionData'] = qd
    return data

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")