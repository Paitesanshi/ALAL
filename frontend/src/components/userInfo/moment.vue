<template>
  <div>
    <div v-if="!show" class="nofind">
      <p>暂时没有动态记录哦</p>
    </div>
    <div v-if="show" class="blogsbox">
      <div
        v-for="item in newBlogData"
        :key="item.moment_id"
        class="blogs"
           @click="goToInfo(item)"
        data-scroll-reveal="enter bottom over 1s"
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
</template>

<script>
import FirstRecommend from '../FirstRecommend'
import VideoPlayer from '../VideoPlayer'
import ThirdRecommend from '../ThirdRecommend'
import FourthRecommend from '../FourthRecommend'
import TagCloud from '../TagCloud'
import HotBlog from '../HotBlog'
import FollowUs from '../FollowUs'
import Link from '../Link'
import { getBlogByLevel, getNewBlog, getBlogsByUid } from '../../api/index'
import { Loading } from 'element-ui'
import CameraCapture from '../CameraCapture'
import Camera from '../Camera'
import PhotoWall from '../PhotoWall'

export default {
  name: 'moment',
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
      show:'',
      loadingInstance: null, // loading对象
      VUE_MOGU_WEB: process.env.VUE_MOGU_WEB,
      firstData: [], // ；一级推荐数据
      secondData: [], // ；二级级推荐数据
      newBlogData: [
        // {
        //   moment_id: '10',
        //   name: 'Jackson',
        //   content: '快乐健身，快乐你我！',
        //   id: '8',
        //   like_num: '0',
        //   publish_time: '2021-6-17 03:51:43'
        // }
      ], // 最新文章
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
    // 获取最新博客
    let that=this
    setTimeout(
      function () {
        that.newBlogList()
      }, 500
    )

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
      // params.append('currentPage', this.currentPage)
      // params.append('pageSize', this.pageSize)
      params.append('id', this.$store.state.user.userInfo.id)
      getBlogsByUid(params)
        .then(response => {
          if (response.data.code === this.$ECode.SUCCESS) {
            that.newBlogData = response.data.records
            that.total = response.data.total
            that.pageSize = response.data.size
            that.currentPage = response.data.currentPage
            that.loadingInstance.close()
            that.show=true
          }

          // eslint-disable-next-line handle-callback-err
          // for (let i = 0; i < 5; ++i) {
          //   console.log('error!!!')
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
        })
        .catch(error => {
          // for (let i = 0; i < 5; ++i) {
          //   console.log('error!!!')
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

<style>
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
