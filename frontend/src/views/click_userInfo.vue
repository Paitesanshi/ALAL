<template>
  <article>
    <div class="top">
      <el-button><a href="index.vue>">返回</a></el-button>
    </div>
    <div class="userInfo">
      <div align="center">
        <td style="width: 25%" aligin="center">
          <el-image
            style="width: 128px; height: 128px; border-radius: 50%;"
			:src="this.UserList.avatar">
          </el-image>
        </td>
        <div class="myInfo" style="font-weight: bold">
          <td>姓名：</td>
          <td>{{this.UserList.name}}</td>
          <tr>
          <td>情感状况：</td>
          <td>{{this.UserList.emotional_state}}</td>
          </tr>
          <tr>
            <td>理想型：</td>
            <td>{{this.UserList.idealType}}</td>
          </tr>
          <br>
          <button @click="goToAnswer">添加好友</button>
        </div>
      </div>
    </div>
    <div>
      <br>
      <div class="left" style="width: 250px;float: left">
        <tr>
          <td>性别：</td>
          <td>{{this.UserList.sex}}</td>
        </tr>
        <tr>
          <td>邮箱：</td>
          <td>{{this.UserList.email}}</td>
        </tr>
        <tr>
          <td>城市：</td>
          <td>{{this.UserList.city}}</td>
        </tr>
        <tr>
          <td>职业：</td>
          <td>{{this.UserList.job}}</td>
        </tr>
        <!--          <tr>-->
        <!--            <td>学校：</td>-->
        <!--            <td>{{this.$store.state.user.userInfo.school}}</td>-->
        <!--          </tr>-->
        <tr>
          <td>理想型：</td>
          <td>{{this.UserList.ideal_type}}</td>
        </tr>
      </div>
    <div style="float: right">
      <div
        v-for="item in newBlogData"
        :key="item.moment_id"
        class="blogs"
         @click="goToInfo(item)"
        data-scroll-reveal="enter bottom over 1s"
        style="width:600px"
      >

        <p class="blogtext">{{ item.content }}</p>
        <div class="bloginfo">
          <ul>
            <li class="author">
              <span class="iconfont">&#xe60f;</span>
              <a href="javascript:void(0);" @click="goToAuthor(item.id)">{{
                  item.name
                }}</a>
            </li>
           
         
            <li class="like">
              <span class="iconfont">&#xe663;</span>
              {{ item.like_num }}
            </li>
            <li class="createTime">
              <span class="iconfont">&#xe606;</span>
              {{ item.publish_time }}
            </li>
          </ul>
        </div>
      </div>

      <div class="isEnd">
        <!-- <span v-if="!isEnd">正在加载中~</span> -->

        <div class="lds-css ng-scope" v-if="!isEnd && loading">
          <div style="width:100%;height:100%" class="lds-facebook">
            <div></div>
            <div></div>
            <div></div>
          </div>
        </div>
      </div>
    </div>
    </div>
  </article>
</template>

<script>
import FirstRecommend from '../components/FirstRecommend'
import VideoPlayer from '../components/VideoPlayer'
import ThirdRecommend from '../components/ThirdRecommend'
import FourthRecommend from '../components/FourthRecommend'
import TagCloud from '../components/TagCloud'
import HotBlog from '../components/HotBlog'
import FollowUs from '../components/FollowUs'
import Link from '../components/Link'
import {getBlogListByID } from '../api/blog'
import {getUserInfoByID } from '../api/user'
import { Loading } from 'element-ui'
import CameraCapture from '../components/CameraCapture'
import Camera from '../components/Camera'
import PhotoWall from '../components/PhotoWall'
import { getNewBlog,getBlogsByUid } from '@/api/index'
export default {
  props: ['list', 'imageUrl'],
  components: {
    // 注册组件
    FirstRecommend,
    FourthRecommend,
    ThirdRecommend,
    TagCloud,
    HotBlog,
    FollowUs,
    Link,
    VideoPlayer,
    CameraCapture,
    Camera,
    PhotoWall,
  },
  data () {
    return {
      loadingInstance: null, // loading对象
      VUE_MOGU_WEB: process.env.VUE_MOGU_WEB,
      firstData: [], // ；一级推荐数据
      secondData: [], // ；二级级推荐数据
      newBlogData: [], // 最新文章
      hotBlogData: [], // 最热文章
      hotTagData: [], // 最新标签
      keyword: '',
      currentPage: 1,
      pageSize: 15,
      total: 0, // 总数量
      isEnd: false, // 是否到底底部了
      loading: false, // 是否正在加载
      // 用户信息展示
      UserList: {
	  id: '',
		    avatar: '',
        name: '',
        sex: '',
        city: '',
        emotional_state: '',
        email: '',
        birthDate: '',
        idealType: '',
        job: ''
      }
    }
  },
  mounted () {
    // 注册scroll事件并监听
    this.loading = false
  },
  created () {
    // 获取最新博客
    this.getBlogList()
	this.getClickUserInfo()
  },
  methods: {
    // 跳转到文章详情【或推广链接】
    goToInfo (blog) {
      if (
        this.$store.state.user.isLogin &&
        this.$store.state.user.userInfo.reputation == 1
      ) {
        this.$notify.error({
          title: '警告',
          message: '宁信誉积分太低，宁不配',
          offset: 100
        })
      } else {
        let routeData = this.$router.resolve({
          path: '/info',
          query: { blogUid: blog.blog_id }
        })
        console.log(blog.id)
        window.open(routeData.href, '_blank')
      }
    },
    // 跳转到搜索详情页
    goToList (uid) {
      this.$router.push({
        path: '/list',
        query: { sortUid: uid }
      })
    },

    // 跳转到搜索详情页
    goToAuthor (author) {
      this.$router.push({
        path: '/list',
        query: { author: author }
      })
    },

    // 最新博客列表
    getBlogList () {
      var that = this
      that.loadingInstance = Loading.service({
        lock: true,
        text: '正在努力加载中……',
        background: 'rgba(0, 0, 0, 0.7)'
      })

      var params = new URLSearchParams()
	  params.append('id', this.$route.query.id)
      params.append('currentPage', this.currentPage)
      params.append('pageSize', this.pageSize)
      getBlogsByUid(params)
        .then(response => {
          if (response.data.code === this.$ECode.SUCCESS) {
            that.newBlogData = response.data.records
            that.total = response.data.total
            that.pageSize = response.data.size
            that.currentPage = response.data.currentPage
          }
          that.loadingInstance.close()
        })
        .catch(error => {
          // for (let i = 0; i < 5; ++i) {
          //   this.newBlogData.push({
          //     title: 'test',
          //     author: 'ptss',
          //     labels: ['技术', '数据库'],
          //     summary: '略略略',
          //     clickCount: 100,
          //     likeCount: 200,
          //     time: '2020-12-2'
          //   })
          // }
          this.newBlogData.push(
            {
              moment_id: '7',
              name: '桑随远',
              content: '今天又重温了一遍《傲慢与偏见》，再次被伊丽莎白与达西的爱情感动了，希望自己早点可以找到心仪的另一半啊！',
              id: '7',
              like_num: '5',
              publish_time: '2021-6-16 19:26:43'
            },
            {
              moment_id: '8',
              name: '桑随远',
              content: '今晚的夕阳格外美丽~~',
              id: '7',
              like_num: '4',
              publish_time: '2021-6-16 20:24:55'
            },
            {
              moment_id: '9',
              name: '桑随远',
              content: '马上就要周末啦！太开心了！！',
              id: '7',
              like_num: '12',
              publish_time: '2021-6-16 23:22:23'
            })
          that.loadingInstance.close()
        })
    },
      goToInfo (moment) {
      if (
        this.$store.state.user.isLogin &&
        this.$store.state.user.userInfo.reputation == 1
      ) {
        this.$notify.error({
          title: '警告',
          message: '宁信誉积分太低，宁不配',
          offset: 100
        })
      } else {
        // let routeData = this.$router.resolve({
        //   path: '/info',
        //   query: { blogUid: moment.moment_id }
        // })
        // console.log(moment.moment_id)
        // window.open(routeData.href, '_blank')
        this.$router.push({
          path: '/info',
          query: {blogUid: moment.moment_id}
        })
      }
      },
	getClickUserInfo () {
      var that = this
      var params = new URLSearchParams()
	  params.append('id', this.$route.query.id)
      getUserInfoByID(params)
        .then(response => {
          if (response.data.code === this.$ECode.SUCCESS) {
            that.UserList=response.data.records
          }
        })
        .catch(error => {
          that.UserList= {
		avatar:'http://images.zastatic.com/app/seo/randomuser/2_11.jpg',
        city: '北京',
        name: '桑随远',
        sex: '女',
        emotion: '单身',
        career: '教师',
        email: '18301111@bjtu.edu.cn',
        birthDate: '1985-09-02',
        ideal_type: '性格好，热爱运动'
      }
        })
    },
    loadContent: function () {
      var that = this
      that.loading = false
      that.currentPage = that.currentPage + 1
      var params = new URLSearchParams()
      params.append('currentPage', that.currentPage)
      params.append('pageSize', that.pageSize)
      getNewBlog(params).then(response => {
        if (
          response.data.code === this.$ECode.SUCCESS &&
          response.data.records.length > 0
        ) {
          that.isEnd = false
          var newData = that.newBlogData.concat(response.data.records)
          that.newBlogData = newData
          that.total = response.data.total
          that.pageSize = response.data.size
          that.currentPage = response.data.current
          // 全部加载完毕
          if (newData.length < that.pageSize) {
            that.isEnd = true
          }
        } else {
          that.isEnd = true
        }
        that.loading = false
      })
    },
    goToAnswer () {
      this.$router.push({path: '/answer_questions',query:{id:this.$route.query.id}})
    }
  }
}
</script>

<style>
.el-loading-mask {
  z-index: 2002;
}
button{
  background: #7fb4d7;
  padding: 10px;
  color: #fff;
  text-decoration: none;
  cursor: pointer;
  border-radius:15px;
}
.myInfo{
  color: #000000;
  /* 表格边框颜色 */
  border: 0.5px;
}
.left{
  font-weight: bold;
  padding: 20px 200px 40px 50px;
  background-color: white;
  float:left
}
.blogsbox{
  float: right;
}
.isEnd {
  float: left;
  width: 100%;
  height: 80px;
  text-align: center;
}

.ng-scope {
  margin: 0 auto;
  width: 18%;
  height: 10%;
}

.loadContent {
  width: 120px;
  height: 30px;
  line-height: 30px;
  font-size: 16px;
  margin: 0 auto;
  color: aliceblue;
  cursor: pointer;
  background: rgba(0, 0, 0, 0.8);
}

@keyframes lds-facebook_1 {
  0% {
    top: 0px;
    height: 200px;
  }
  50% {
    top: 80px;
    height: 40px;
  }
  100% {
    top: 80px;
    height: 40px;
  }
}

@-webkit-keyframes lds-facebook_1 {
  0% {
    top: 0px;
    height: 200px;
  }
  50% {
    top: 80px;
    height: 40px;
  }
  100% {
    top: 80px;
    height: 40px;
  }
}

@keyframes lds-facebook_2 {
  0% {
    top: 20px;
    height: 160px;
  }
  50% {
    top: 80px;
    height: 40px;
  }
  100% {
    top: 80px;
    height: 40px;
  }
}

@-webkit-keyframes lds-facebook_2 {
  0% {
    top: 20px;
    height: 160px;
  }
  50% {
    top: 80px;
    height: 40px;
  }
  100% {
    top: 80px;
    height: 40px;
  }
}

@keyframes lds-facebook_3 {
  0% {
    top: 40px;
    height: 120px;
  }
  50% {
    top: 80px;
    height: 40px;
  }
  100% {
    top: 80px;
    height: 40px;
  }
}

@-webkit-keyframes lds-facebook_3 {
  0% {
    top: 40px;
    height: 120px;
  }
  50% {
    top: 80px;
    height: 40px;
  }
  100% {
    top: 80px;
    height: 40px;
  }
}

.lds-facebook {
  position: relative;
}

.lds-facebook div {
  position: absolute;
  width: 20px;
}

.lds-facebook div:nth-child(1) {
  left: 40px;
  background: #1d0e0b;
  -webkit-animation: lds-facebook_1 1s cubic-bezier(0, 0.5, 0.5, 1) infinite;
  animation: lds-facebook_1 1s cubic-bezier(0, 0.5, 0.5, 1) infinite;
  -webkit-animation-delay: -0.2s;
  animation-delay: -0.2s;
}

.lds-facebook div:nth-child(2) {
  left: 90px;
  background: #774023;
  -webkit-animation: lds-facebook_2 1s cubic-bezier(0, 0.5, 0.5, 1) infinite;
  animation: lds-facebook_2 1s cubic-bezier(0, 0.5, 0.5, 1) infinite;
  -webkit-animation-delay: -0.1s;
  animation-delay: -0.1s;
}

.lds-facebook div:nth-child(3) {
  left: 140px;
  background: #d88c51;
  -webkit-animation: lds-facebook_3 1s cubic-bezier(0, 0.5, 0.5, 1) infinite;
  animation: lds-facebook_3 1s cubic-bezier(0, 0.5, 0.5, 1) infinite;
}

.lds-facebook {
  width: 90px !important;
  height: 90px !important;
  -webkit-transform: translate(-45px, -45px) scale(0.45) translate(45px, 45px);
  transform: translate(-45px, -45px) scale(0.45) translate(45px, 45px);
}

.iconfont {
  font-size: 15px;
  margin-right: 2px;
}
</style>
