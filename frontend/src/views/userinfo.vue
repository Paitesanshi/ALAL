<template>
  <div>
    <div class="wrapper">
      <el-card class="box-card">
        <div>
          <el-upload
            class="avatar-uploader"
            action="/api/v1/user/avatar"
            :headers="head"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload">
            <img v-if="this.list.photoUrl"  :src="getImage(this.list.photoUrl)" class="img">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
          <span class="username">{{list ? list.nickName : ''}}</span>
        </div>
      </el-card>
      <el-tabs type="border-card" tabPosition="left" style="width:1000px;height: 100vh;margin: 14px auto auto auto;position: sticky">
        <el-tab-pane>
          <span slot="label">个人信息</span>
          <user :list="list" :photoUrl="list.photoUrl" class="user"></user>
        </el-tab-pane>
        <el-tab-pane>
          <span slot="label">我的圈子</span>
          <my-resume></my-resume>
        </el-tab-pane>
        <el-tab-pane>
          <span slot="label">消息记录</span>
          <delivery></delivery>
        </el-tab-pane>
        <el-tab-pane>
          <span slot="label">设置账号</span>
          <setting :phone="list.phone"></setting>
        </el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>
<style>
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
</style>

<script>/* eslint-disable indent */
``
import Info from '../components/userInfo/userInfo'
import Resume from '../components/userInfo/resume'
import Delivery from '../components/userInfo/delivery'
import Setting from '../components/userInfo/setting'
export default {
  data () {
    return {
      activeIndex2: '1',
      btnText: '取消',
      list: {
        nickName: '',
        sex: '',
        address: '',
        introduce: '',
        endTime: '',
        education: '',
        school: '',
        intentionCompany: '',
        intentionJob: '',
        photoUrl: '',
        phone:''
      },
      photoUrl: '',
      head: {},
      refresh: 0
    }
  },
  computed: {
    setDefault () {
      return this.list.photoUrl === ''?"./static/default_photo.png":this.list.photoUrl
    }
  },
  mounted () {

    this.head = {
      ContentType: 'application/json',
      'F-RECRUIT-TOKEN': localStorage.getItem('token')
    }
    this.getUserInfo()
    this.refresh = this.$route.params.refresh !== undefined ? this.$route.params.refresh : 0
  },
  watch: {
    refresh () {
      location.reload()
    }
  },
  components: {
    user: Info,
    myResume: Resume,
    delivery: Delivery,
    setting: Setting,
  },

}
</script>
