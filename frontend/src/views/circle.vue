<template>
  <div>

    <div>
      <div>
        <br>
        <br>
        <br>
        <router-link to="/blog">
          <el-button href="javascript:void(0);" :class="[saveTitle == '/blog' ? 'title' : '']" style="width: 100px;position:fixed;left: 1350px" @click="handleSubmit" class="surveyBtn">发布爱</el-button>
          <!--          <a >发布爱</a>-->
        </router-link></div>
      <!--    <div style="float:right;width: 100px">-->
      <!--      <br>-->
      <!--      <br>-->
      <!--      <br>-->
      <!--    </div>-->
      <!--    <div class="blogsbox">-->
      <div style="width:1000px;float:left;margin-left: 300px">
        <!--      <br>-->
        <!--      <br>-->
        <!--      <br>-->
        <div>
          <div
            v-for="item in newBlogData"
            :key="item.moment_id"
            class="blogs"
            data-scroll-reveal="enter bottom over 1s"
            @click="goToInfo(item)"
          >
            <!-- <h3 class="blogtitle">
              <a href="javascript:void(0);" @click="goToInfo(item)">{{
                item.title
              }}</a>
            </h3> -->

            <!--        <span class="blogpic">-->
            <!--          <a href="javascript:void(0);" @click="goToInfo(item)" title>-->
            <!--            <img v-if="item.photoList" :src="item.photoList[0]" alt>-->
            <!--          </a>-->
            <!--        </span>-->

            <div class="blogtext">{{ item.content }}</div>
            <div class="bloginfo">
              <ul>
                <li class="author">
                  <span class="iconfont">&#xe60f;</span>
                  <a href="javascript:void(0);" @click="goToAuthor(item.id)">{{
                      item.name
                    }}</a>
                </li>
                <!-- <li class="lmname" v-if="item.labels">
                  <span class="iconfont">&#xe603;</span>
                  <a href="javascript:void(0);" @click="goToList(item.labels[0])">{{
                    item.labels[0]
                  }}</a>
                </li> -->
                <!-- <li class="view">
                  <span class="iconfont">&#xe8c7;</span>
                  <span>{{ item.clickCount }}</span>
                </li> -->
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

            <div class="loadContent" @click="loadContent" v-if="!isEnd && !loading">
              点击加载更多
            </div>

            <div class="lds-css ng-scope" v-if="!isEnd && loading">
              <div style="width:100%;height:100%" class="lds-facebook">
                <div></div>
                <div></div>
                <div></div>
              </div>
            </div>

            <span v-if="isEnd">我也是有底线的~</span>
          </div>
        </div>
      </div>

      <!--blogsbox end-->

      <!--    <div class="sidebar">-->
      <!--      &lt;!&ndash;标签云&ndash;&gt;-->
      <!--      <TagCloud></TagCloud>-->

      <!--      &lt;!&ndash;关注我们&ndash;&gt;-->
      <!--&lt;!&ndash;      <FollowUs></FollowUs>&ndash;&gt;-->

      <!--      &lt;!&ndash; 三级推荐 &ndash;&gt;-->
      <!--&lt;!&ndash;      <ThirdRecommend></ThirdRecommend>&ndash;&gt;-->

      <!--&lt;!&ndash;      &lt;!&ndash;四级推荐&ndash;&gt;&ndash;&gt;-->
      <!--&lt;!&ndash;      <FourthRecommend></FourthRecommend>&ndash;&gt;-->

      <!--      &lt;!&ndash;点击排行&ndash;&gt;-->
      <!--&lt;!&ndash;      <HotBlog></HotBlog>&ndash;&gt;-->

      <!--    </div>-->
    </div>
<!--    <div :visible.sync="dialogVisible">-->
<!--      <router-link to="/blog">-->
<!--        <a href="javascript:void(0);" :class="[saveTitle == '/blog' ? 'title' : '']">发布爱</a>-->
<!--      </router-link>-->
<!--    </div>-->
  </div>
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
import { getBlogByLevel, getNewBlog } from '../api/index'
import { Loading } from 'element-ui'
import CameraCapture from '../components/CameraCapture'
import Camera from '../components/Camera'
import PhotoWall from '../components/PhotoWall'

export default {
  name: 'circle',
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
    PhotoWall
  },
  data () {
    return {
      dialogVisible: false,
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
      loading: false // 是否正在加载
    }
  },
  mounted () {
    // 注册scroll事件并监听
    this.loading = false
  },
  created () {
    
    this.newBlogList()
    // alert();
    // var params = new URLSearchParams()
    // params.append('pageName', 'INDEX')
    // recorderVisitPage(params).then(response => {
    // })
  },
  methods: {
    // 跳转到文章详情【或推广链接】
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
      // if (blog.type === '0') {
      //   let routeData = this.$router.resolve({
      //     path: '/info',
      //     query: {blogOid: blog.oid}
      //   })
      //   window.open(routeData.href, '_blank')
      // } else if (blog.type === '1') {
      //   var params = new URLSearchParams()
      //   params.append('uid', blog.uid)
      //   getBlogByUid(params).then(response => {
      //     // 记录一下用户点击日志
      //   })
      //   window.open(blog.outsideLink, '_blank')
      // }
    },
    getResume () {
      let params = new URLSearchParams()
      params.append('id', this.$store.state.user.userInfo.id)
      getResumeByID(params).then(response => {
        if (response.data.code === this.$ECode.SUCCESS) {
          this.blogSortData = response.data.records
        }
      }).catch(error => {
        console.log(error)
        this.blogSortData = [{uid: 1, name: '技术'}, {uid: 2, name: '大数据'}]
      })
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
    newBlogList () {
      var that = this
      that.loadingInstance = Loading.service({
        lock: true,
        text: '正在努力加载中……',
        background: 'rgba(0, 0, 0, 0.7)'
      })

      var params = new URLSearchParams()
      params.append('currentPage', this.currentPage)
      params.append('pageSize', this.pageSize)
      getNewBlog(params)
        .then(response => {
          if (response.data.code === this.$ECode.SUCCESS) {
            that.newBlogData = response.data.records
            console.log(that.newBlogData)
            that.total = response.data.total
            that.pageSize = response.data.size
            that.currentPage = response.data.currentPage
          }
          that.loadingInstance.close()
        })
        .catch(error => {
          // for (let i = 0; i < 5; ++i) {
          //   console.log('error!!!')
            this.newBlogData.push(
            {
              moment_id: '10',
              name: 'Jackson',
              content: '快乐健身，快乐你我！',
              id: '8',
              like_num: '0',
              publish_time: '2021-6-17 03:51:43'
            },
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
            },
            {
              moment_id: '4',
              name: '天使艾米丽',
              content: '亲爱的520快乐！我们以后一直走花路吧',
              id: '5',
              like_num: '5',
              publish_time: '2021-6-15 00:00:00'
            },
            {
              moment_id: '5',
              name: '头上一颗椰',
              content: '昨天跟npy一起去了海南三亚！真是太美了！希望以后还可以去更多地方一起玩~~',
              id: '6',
              like_num: '20',
              publish_time: '2021-6-16 18:43:07'
            },
            {
              moment_id: '6',
              name: 'Jenny',
              content: '今天是我们在一起的第100天了！祝我们100天纪念日快乐呀！嘻嘻',
              id: '7',
              like_num: '78',
              publish_time: '2021-6-16 19:21:45'
            }
          )
          // }
          that.loadingInstance.close()
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
    }
  }
}
</script>

<style scoped>
.el-loading-mask {
  z-index: 2002;
}
.deliverycard {
  margin-bottom: 14px;
  width: 100%;
  height: 100px;
  border-left: 5px solid #888;
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
