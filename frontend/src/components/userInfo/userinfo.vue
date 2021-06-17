<template>
  <div>
      <div align="center">
        <el-image
          style="width: 128px; height: 128px; border-radius: 50%;"
          :src="this.list.avatar">
        </el-image>
      </div>
    <div align="center">
      <td><b>ID：</b></td>
      <td>{{list.id}}</td>
      <br>
    </div>
      <!-- <td>头像：</td>
      <td><img style="" src="https://i.picsum.photos/id/1016/3844/2563.jpg?hmac=WEryKFRvTdeae2aUrY-DHscSmZuyYI9jd_-p94stBvc"></td> -->
    <table style="width: 600px">
<!--      <th> 个人信息</th>-->
      <tr>
        <td>姓名：</td>
        <th>{{list.name}}</th>
      </tr>
      <tr>
        <td>性别：</td>
        <th v-if="list.sex=='f'">女</th>
        <th v-if="list.sex=='m'">男</th>
      </tr>
      <tr>
        <td>城市：</td>
        <th>{{list.city}}</th>
      </tr>
      <tr>
        <td>职业：</td>
        <th>{{list.job}}</th>
      </tr>
      <tr>
        <td>情感状况：</td>
        <th v-if="list.emotional_state==2">非单身</th>
        <th v-if="list.emotional_state==1">单身</th>
      </tr>
      <tr>
        <td>出生日期：</td>
        <th>{{list.birthDate}}</th>
      </tr>
      <tr>
<!--      <tr>-->
<!--        <td>学历：</td>-->
<!--        <td v-if="list.education==4">大专</td>-->
<!--        <td v-if="list.education==1">本科</td>-->
<!--        <td v-if="list.education==2">硕士</td>-->
<!--        <td v-if="list.education==3">博士及以上</td>-->
<!--      </tr>-->

        <td>理想型：</td>
        <th>{{list.idealType}}</th>
      </tr>

    </table>
    <el-button class="edit" @click="changeEdit" style="margin-left: 390px">编辑</el-button>
<!--    <el-button style="margin-left: 350px" @click="">编辑</el-button>-->
<!--    <el-dialog class="myDialog">-->
<!--      <el-form  :model="mylist" status-icon :rules="rules2" ref="mylist" label-width="100px" class="formWrap"-->
<!--                v-if="isEdit">-->
<!--        <el-form-item label="ID" prop="nickName">-->
<!--          <el-input v-model="mylist.ID" auto-complete="off"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="姓名" prop="name">-->
<!--          <el-input v-model="mylist.name" auto-complete="off"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="性别" prop="sex">-->
<!--          <el-select v-model="mylist.sex" placeholder="请选择性别" style="width: 100%">-->
<!--            <el-option label="男" :value="1"></el-option>-->
<!--            <el-option label="女" :value="2"></el-option>-->
<!--          </el-select>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="城市" prop="address">-->
<!--          <el-input v-model="mylist.city"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="我的简介" prop="introduce">-->
<!--          <el-input v-model="mylist.introduce"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="情感状况" prop="sex">-->
<!--          <el-select v-model="mylist.emotion" placeholder="请选择性别" style="width: 100%">-->
<!--            <el-option label="单身" :value="1"></el-option>-->
<!--            <el-option label="非单身" :value="2"></el-option>-->
<!--          </el-select>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="学历" prop="education">-->
<!--          <el-select v-model="mylist.education" placeholder="请选择学历" style="width: 100%">-->
<!--            <el-option label="大专" :value="4"></el-option>-->
<!--            <el-option label="本科" :value="1"></el-option>-->
<!--            <el-option label="硕士" :value="2"></el-option>-->
<!--            <el-option label="博士及以上" :value="3"></el-option>-->
<!--          </el-select>-->
<!--        </el-form-item>-->
<!--        <el-form-item>-->
<!--          <el-button class='editor' @click="changeEdit">返回</el-button>-->
<!--          <el-button  @click="submitInfo('mylist')">提交</el-button>-->
<!--        </el-form-item>-->
<!--      </el-form>-->
<!--    </el-dialog>-->
    <el-dialog title="编辑信息" :visible.sync="isEdit" class="myDialog">
         <!-- <el-form :rules="rules" :label-position="labelPosition" :model="registerForm" ref="registerForm">
        <el-form-item label="用户名" prop="userName">
          <el-input v-model="registerForm.userName" placeholder="用户名长度在5~20之间" :disabled="loginType.password"></el-input>
        </el-form-item> -->

        <!-- <el-form-item label="昵称" prop="nickName">
          <el-input v-model="registerForm.nickName" placeholder="昵称长度在1~20之间" :disabled="loginType.password"></el-input>
        </el-form-item> -->
        <!-- <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="registerForm.password" placeholder="密码长度在5~20之间" :disabled="loginType.password"></el-input>
        </el-form-item>

        <el-form-item label="重复密码" prop="password2">
          <el-input type="password" v-model="registerForm.password2" placeholder="请再次输入密码" :disabled="loginType.password"></el-input>
        </el-form-item>
        <el-form-item  label="性别">
          <el-radio
          v-model="registerForm.sex"
          :label="1"
        >男</el-radio>
         <el-radio
          v-model="registerForm.sex"
          :label="0"
        >女</el-radio>
        </el-form-item>
          <el-form-item label="情感状况">
          <el-radio
          v-model="registerForm.emotional_state"
          :label="0"
        >单身</el-radio>
         <el-radio
          v-model="registerForm.emotional_state"
          :label="1"
        >非单身</el-radio>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="registerForm.email" placeholder="请输入正确的邮箱" :disabled="loginType.password"></el-input>
        </el-form-item>

        <el-row class="btn">
          <el-button class="loginBtn" type="primary" @click="startRegister" :disabled="loginType.password">注册</el-button>
          <el-button class="registerBtn" type="info" @click="goLogin" :disabled="loginType.password">返回登录</el-button>
        </el-row> -->

<!--        <div class="loginTip">注册后，需要到邮箱进行邮件认证~</div>-->
      <!-- </el-form> -->
      <el-form :model="mylist" status-icon :rules="rules2"  label-width="100px"
               class="formWrap">
			   <el-form-item label="上传图片" prop="picture" style="width: 800px;">
               <el-upload
			     action=""
                 list-type="picture-card"
                 :on-preview="handlePictureCardPreview"
                 :on-remove="handleRemove"
                 :http-request="uploadPicture"
                 :before-upload="beforeAvatarUpload"
                 :file-list="fileList"
				 :multiple="false"
				 :limit="1"
               >
                 <i class="el-icon-plus"></i>
               </el-upload>
               <el-dialog :visible.sync="dialogVisible">
                 <img width="100%" :src="dialogImageUrl" alt="">
               </el-dialog>
            </el-form-item>
        <el-form-item label="姓名">
          <el-input v-model="mylist.name"></el-input>
        </el-form-item>
        <!-- <el-form-item label="性别" prop="sex">
          <el-select v-model="list.sex" placeholder="请选择性别" style="width: 100%">
            <el-option label="男" :value="1"></el-option>
            <el-option label="女" :value="2"></el-option>
          </el-select>
        </el-form-item> -->
         <el-form-item  label="性别">
          <el-radio
          v-model="this.mylist.sex"
          :label="1"
        >男</el-radio>
         <el-radio
          v-model="this.mylist.sex"
          :label="0"
        >女</el-radio>
        </el-form-item>
          <el-form-item label="情感状况">
          <el-radio
          v-model="this.mylist.emotional_state"
          :label="0"
        >单身</el-radio>
         <el-radio
          v-model="this.mylist.emotional_state"
          :label="1"
        >非单身</el-radio>
        </el-form-item>
        <!--        <el-form-item label="年龄" prop="age">-->
        <!--          <el-input v-model="resumemylist.age"></el-input>-->
        <!--        </el-form-item>-->
        <el-form-item label="城市" prop="address">
          <el-input v-model="mylist.city"></el-input>
        </el-form-item>
        <el-form-item label="职业" prop="career">
          <el-input v-model="mylist.job"></el-input>
        </el-form-item>
        <!-- <el-form-item label="出生日期" prop="birthDate"> -->
          <!--          <el-select v-model="resumeList.birthDate" style="width: 100%">-->
          <!--            <el-option-->
          <!--              v-for="item in options"-->
          <!--              :key="item.value"-->
          <!--              :label="item.label"-->
          <!--              :value="item.value">-->
          <!--            </el-option>-->
          <!--          </el-select>-->
          <!-- <el-input v-model="mylist.birthDate"></el-input> -->

        <!-- </el-form-item> -->
        <el-form-item :label-width="formLabelWidth" label="生日" prop="sort">
         <el-date-picker
           v-model="list.birthDate"
           type="date"
            value-format="yyyy-MM-dd"
            :picker-options="expireTime"
           placeholder="选择日期">
          </el-date-picker>
        </el-form-item>
        <!--        <el-form-item label="学校" prop="school">-->
        <!--          <el-input v-model="resumeList.school"></el-input>-->
        <!--        </el-form-item>-->
<!--        <el-form-item label="手机号" prop="phone">-->
<!--          <el-input v-model="list.phone"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="邮箱" prop="email">-->
<!--          <el-input v-model="list.email"></el-input>-->
<!--        </el-form-item>-->
        <!-- <el-form-item label="情感状况" prop="sex">
          <el-select v-model="list.emotion" placeholder="请选择是否单身" style="width: 100%">
            <el-option label="单身" :value="1"></el-option>
            <el-option label="非单身" :value="2"></el-option>
          </el-select>
        </el-form-item> -->
        <!--        <el-form-item label="技术栈" prop="skills">-->
        <!--          <el-button @click="addSkill()" class="addbtn">添加</el-button>-->
        <!--          <div class="skillContain">-->
        <!--            <div v-for="(item, key) in resumeList.skills" :key="key">-->
        <!--              <input placeholder="技术" class="input" v-model="item.name"/>-->
        <!--              <select class="select" v-model="item.level">-->
        <!--                <option label="了解" value=1></option>-->
        <!--                <option label="熟悉" value=2></option>-->
        <!--                <option label="掌握" value=3></option>-->
        <!--                <option label="精通" value=4></option>-->
        <!--              </select>-->
        <!--              <i class="el-icon-error deleteIt" @click="deleteItem(key)"></i>-->
        <!--            </div>-->
        <!--          </div>-->
        <!--        </el-form-item>-->
        <el-form-item label="理想型" prop="idealType">
          <el-input type="textarea" :autosize="{ minRows: 4, maxRows: 6}" v-model="mylist.idealType "></el-input>
        </el-form-item>
        <!--        <el-form-item label="获奖经历" prop="awards">-->
        <!--          <el-input type="textarea" :autosize="{ minRows: 4, maxRows: 6}" v-model="resumeList.awards"></el-input>-->
        <!--        </el-form-item>-->
        <el-form-item>
          <el-button @click="changeEdit">取消</el-button>
          <el-button type="primary" @click="submitInfo">确定</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>
<style>
table {
  margin: 0 auto;
  font-size: 16px;
  border-collapse: collapse;
  table-layout:fixed;
  word-wrap:break-word;
}
.myDialog {
  width: 1500px;
}
table tr td {
  height: 40px;
  width: 180px;
  text-align: right;
  font-weight: bold;
}
table th{
  padding-left: 60px;
  text-align: left;
}
.formWrap {
  width: 500px;
  font-size: 18px;
}
.edit {
  margin:10px auto auto 40px;
}
</style>

<script>/* eslint-disable indent */
import { editResume} from '@/api/user'
import { uploadPhoto} from '@/api/blog'
export default {
  props: ['lists', 'imageUrl'],
  data () {
    return {
         expireTime: {
        disabledDate (date) {
          return date.getTime() >= Date.now()
        }
      },
    isEdit: false,
	  isEmpty: true,
      // rules2: {
      //   nickName: [{validator: checknickname, trigger: 'blur'}],
      //   name: [{validator: checkname, trigger: 'blur'}],
      //   sex: [{validator: checksex, trigger: 'blur'}],
      //   address: [{validator: checkaddress, trigger: 'blur'}],
      //   introduce: [{validator: checkintroduce, trigger: 'blur'}],
      //   education: [{validator: checkeducation, trigger: 'blur'}],
      //   emotion: [{validator: checkemotion, trigger: 'blur'}]
      //   // intentionCompany: [{validator: checkcompany, trigger: 'blur'}],
      //   // intentionJob: [{validator: checkjob, trigger: 'blur'}]
      // },
      options: [
        {
          value: '2018',
          label: '2018'
        },
        {
          value: '2019',
          label: '2019'
        },
        {
          value: '2020',
          label: '2020'
        },
        {
          value: '2021',
          label: '2021'
        },
        {
          value: '2022',
          label: '2022'
        }
      ],
      list: {
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
      },
        mylist: {
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
      },
      companyOptions: [],
      jobOptions: [],
      intentionCompany: [],
      intentionJob: [],
	  picList: []
    }
  },
  methods: {
	  uploadPicture (item) {
		  this.isEmpty = false
		  console.log(this.isEmpty)
          const formData = new FormData()
          formData.append('file', item.file)
          uploadPhoto(formData).then(res => {
			  console.log(res)
            this.picList.push(res.data.uid)
            this.emptyUpload()
          }).catch(() => {
            this.$message.error('上传失败，请重新上传')
            this.emptyUpload()
          })
        },
        beforeAvatarUpload (file) {
          const isJPG = file.type === 'image/jpeg'
          const isPng = file.type === 'image/png'
          const isLt2M = file.size / 1024 / 1024 < 2

          if (!isJPG && !isPng) {
            this.$message.error('上传图片只能是 JPG或png 格式!')
          }
          if (!isLt2M) {
            this.$message.error('上传图片大小不能超过 2MB!')
          }
          return (isJPG || isPng) && isLt2M
        },
        handleRemove (file, fileList) {
          for (const i in this.picList) {
            if (this.picList[i].key === file.uid) {
              this.picList.splice(i, 1)
            }
          }
		  this.isEmpty = true
        },
        handlePictureCardPreview (file) {
          this.dialogImageUrl = file.url
          this.dialogVisible = true
        },
        /**
         * 清空上传组件
         */
        emptyUpload () {
          const mainImg = this.$refs.upload
          if (mainImg) {
            if (mainImg.length) {
              mainImg.forEach(item => {
                item.clearFiles()
              })
            } else {
              this.$refs.upload.clearFiles()
            }
          }
        },
    changeEdit () {
      this.isEdit = !this.isEdit
    },
    // 提交个人信息
    submitInfo () {
      console.log(this.picList)
      if (this.picList[this.picList.length - 1] != undefined) {
       	this.list.avatar = "http://localhost:5000/display/img/"+this.picList[this.picList.length - 1]
      }
      if(this.list.idealType==undefined){
        this.list.idealType=""
      }
			let params = {}
      params.id = this.$store.state.user.userInfo.id
      params.userInfo = this.list
      console.log('info ', this.list)
      editResume(params).then(response => {
        alert(response.data.code)
      if (response.data.code === this.$ECode.SUCCESS) {
        this.$notify({
          title: '成功',
          message: '修改成功',
          type: 'success',
          offset: 100
        })
        this.changeEdit()
      } else {
        this.$notify({
              title: '失败',
              message: '修改信息失败',
              type: 'error',
              offset: 100
            })
      }
    }).catch(error => {
      console.log(error)
    })
    }
  },
  created () {
    console.log('-------------------------------')
    this.list.id = this.$store.state.user.userInfo.id
		this.list.city = this.$store.state.user.userInfo.city
	  this.list.name = this.$store.state.user.userInfo.name
	  this.list.sex = this.$store.state.user.userInfo.sex
		this.list.emotional_state = this.$store.state.user.userInfo.emotional_state
		this.list.email = this.$store.state.user.userInfo.email
		this.list.birthDate = this.$store.state.user.userInfo.birth
	  this.list.idealType = this.$store.state.user.userInfo.idealType
		this.list.avatar = this.$store.state.user.userInfo.head_portrait
    this.list.job = this.$store.state.user.userInfo.job
    this.mylist = this.list
    console.log(this.mylist)
  }
}
</script>
