<template>
  <div>
    <div class="wrapper">
      <el-tabs type="border-card" tabPosition="left" style="width:1000px;height: 100vh;margin: 60px auto auto auto;position: sticky;">
        <el-tab-pane>
          <span slot="label">个人信息</span>
          <user :lists="list" :photoUrl="list.avatar" class="user"></user>
          <br>
          <setting :phone="list.phone"></setting>
        </el-tab-pane>
<!--        <el-tab-pane>-->
<!--          <span slot="label">我的简历</span>-->
<!--          <myResume></myResume>-->
<!--        </el-tab-pane>-->
        <el-tab-pane>
          <span slot="label">消息记录</span>
          <delivery></delivery>
        </el-tab-pane>
        <el-tab-pane>
          <span slot="label">我的圈子</span>
          <moment></moment>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>

</template>
<style scoped>
html * {
  padding: 0;
  margin: 0;
}
* {
  box-sizing: border-box;
}
.box-card {
  width: 1000px;
  margin: 14px auto auto auto;
}
.img {
  /* border-radius: 50%; */
  width: 72px;
  height: 72px;
}
.el-card .username {
  float: left;
  margin-left: 14px;
  font-size: 21px;
}
.avatar-uploader {
  float: left;
}
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  width: 70px;
  height: 70px;
  margin-bottom: 14px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar {
  width: 5rem;
  height: 5rem;
  display: block;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  margin-top: 35%;

  line-height: 17px;
  text-align: center;
}
/* 遮罩层
  .mask {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 500;
  } */
</style>

<script>/* eslint-disable indent */

import Info from '../components/userInfo/userinfo'
import delivery from '../components/userInfo/delivery'
import Setting from '../components/userInfo/setting'
import moment from '../components/userInfo/moment'
export default {
  data () {
    return {
      activeIndex2: '1',
      btnText: '取消',
      list: {
        id:'',
		    avatar: '',
        name: '',
        sex: '',
        city: '',
        emotional_state:'',
        email:'',
        birthDate:'',
        idealType:'',
        job:'',
      },
      photoUrl: '',
      head: {},
      refresh: 0
    }
  },
  created () {
    this.list.id = this.$store.state.user.userInfo.id
		this.list.city = this.$store.state.user.userInfo.city
	  this.list.name = this.$store.state.user.userInfo.name
	  this.list.sex = this.$store.state.user.userInfo.sex
		this.list.emotional_state = this.$store.state.user.userInfo.emotional_state
		this.list.email = this.$store.state.user.userInfo.email
		this.list.birthDate = this.$store.state.user.userInfo.birth
	  this.list.idealType = this.$store.state.user.userInfo.ideal_type
		this.list.avatar = this.$store.state.user.userInfo.head_portrait
    this.list.job = this.$store.state.user.userInfo.job
			 // this.list.avatar="https://i.picsum.photos/id/1016/3844/2563.jpg?hmac=WEryKFRvTdeae2aUrY-DHscSmZuyYI9jd_-p94stBvc"
  },
  components: {
    user: Info,
    delivery,
    moment,
    setting: Setting
  }
}
</script>
