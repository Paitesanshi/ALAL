<template>
  <div>
    <table class="container">
<!--      <th> 个人信息</th>-->
 	  <tr>
		<td style="width: 75%;margin:0 auto;text-align:center;">
          <el-image
            style="width: 128px; height: 128px; border-radius: 50%;"
			:src="this.list.avatar">
          </el-image>
        </td>
        <!-- <td>头像：</td>
        <td><img style="" src="https://i.picsum.photos/id/1016/3844/2563.jpg?hmac=WEryKFRvTdeae2aUrY-DHscSmZuyYI9jd_-p94stBvc"></td> -->
      </tr>
      <tr>
        <td>ID：</td>
        <td>{{list.ID}}</td>
      </tr>
      <tr>
        <td>姓名：</td>
        <td>{{list.name}}</td>
      </tr>
      <tr>
        <td>性别：</td>
        <td v-if="list.sex==2">女</td>
        <td v-if="list.sex==1">男</td>
      </tr>
      <tr>
        <td>城市：</td>
        <td>{{list.city}}</td>
      </tr>
      <tr>
        <td>职业：</td>
        <td>{{list.career}}</td>
      </tr>
      <tr>
        <td>情感状况：</td>
        <td v-if="list.emotion==2">非单身</td>
        <td v-if="list.emotion==1">单身</td>
      </tr>
      <tr>
        <td>出生日期：</td>
        <td>{{list.career}}</td>
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
        <td>{{list.career}}</td>
      </tr>
      <el-button class="edit" @click="changeEdit" style="margin-left: 350px">编辑</el-button>
    </table>
<!--    <el-button style="margin-left: 350px" @click="">编辑</el-button>-->
<!--    <el-dialog class="myDialog">-->
<!--      <el-form  :model="list" status-icon :rules="rules2" ref="list" label-width="100px" class="formWrap"-->
<!--                v-if="isEdit">-->
<!--        <el-form-item label="ID" prop="nickName">-->
<!--          <el-input v-model="list.ID" auto-complete="off"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="姓名" prop="name">-->
<!--          <el-input v-model="list.name" auto-complete="off"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="性别" prop="sex">-->
<!--          <el-select v-model="list.sex" placeholder="请选择性别" style="width: 100%">-->
<!--            <el-option label="男" :value="1"></el-option>-->
<!--            <el-option label="女" :value="2"></el-option>-->
<!--          </el-select>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="城市" prop="address">-->
<!--          <el-input v-model="list.city"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="我的简介" prop="introduce">-->
<!--          <el-input v-model="list.introduce"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="情感状况" prop="sex">-->
<!--          <el-select v-model="list.emotion" placeholder="请选择性别" style="width: 100%">-->
<!--            <el-option label="单身" :value="1"></el-option>-->
<!--            <el-option label="非单身" :value="2"></el-option>-->
<!--          </el-select>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="学历" prop="education">-->
<!--          <el-select v-model="list.education" placeholder="请选择学历" style="width: 100%">-->
<!--            <el-option label="大专" :value="4"></el-option>-->
<!--            <el-option label="本科" :value="1"></el-option>-->
<!--            <el-option label="硕士" :value="2"></el-option>-->
<!--            <el-option label="博士及以上" :value="3"></el-option>-->
<!--          </el-select>-->
<!--        </el-form-item>-->
<!--        <el-form-item>-->
<!--          <el-button class='editor' @click="changeEdit">返回</el-button>-->
<!--          <el-button  @click="submitInfo('list')">提交</el-button>-->
<!--        </el-form-item>-->
<!--      </el-form>-->
<!--    </el-dialog>-->
    <el-dialog title="编辑简历" :visible.sync="isEdit" class="myDialog">
      <el-form :model="list" status-icon :rules="rules2" ref="list" label-width="100px"
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
        <el-form-item label="姓名" prop="name">
          <el-input v-model="list.name" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="sex">
          <el-select v-model="list.sex" placeholder="请选择性别" style="width: 100%">
            <el-option label="男" :value="1"></el-option>
            <el-option label="女" :value="2"></el-option>
          </el-select>
        </el-form-item>
        <!--        <el-form-item label="年龄" prop="age">-->
        <!--          <el-input v-model="resumeList.age"></el-input>-->
        <!--        </el-form-item>-->
        <el-form-item label="城市" prop="address">
          <el-input v-model="list.address"></el-input>
        </el-form-item>
        <el-form-item label="职业" prop="career">
          <el-input v-model="list.career"></el-input>
        </el-form-item>
        <el-form-item label="出生日期" prop="birthDate">
          <!--          <el-select v-model="resumeList.birthDate" style="width: 100%">-->
          <!--            <el-option-->
          <!--              v-for="item in options"-->
          <!--              :key="item.value"-->
          <!--              :label="item.label"-->
          <!--              :value="item.value">-->
          <!--            </el-option>-->
          <!--          </el-select>-->
          <el-input v-model="list.birthDate"></el-input>
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
        <el-form-item label="情感状况" prop="sex">
          <el-select v-model="list.emotion" placeholder="请选择是否单身" style="width: 100%">
            <el-option label="单身" :value="1"></el-option>
            <el-option label="非单身" :value="2"></el-option>
          </el-select>
        </el-form-item>
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
          <el-input type="textarea" :autosize="{ minRows: 4, maxRows: 6}" v-model="list.idealType "></el-input>
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
  width: 600px;
  font-size: 16px
}
.myDialog {
  width: 1500px;
}
table tr td {
  padding: 11.2px;
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

export default {
  props: ['list', 'imageUrl'],
  data () {
    var checknickname = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('昵称不能为空'))
      } else {
        callback()
      }
    }
    var checkname = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('姓名不能为空'))
      } else {
        callback()
      }
    }
    var checksex = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('性别不能为空'))
      } else {
        callback()
      }
    }
    var checkemotion = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('情感状况不能为空'))
      } else {
        callback()
      }
    }
    var checkintroduce = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('简介不能为空'))
      } else {
        callback()
      }
    }
    // var checkcompany = (rule, value, callback) => {
    //   if (this.intentionCompany.length === 0) {
    //     return callback(new Error('想去的公司不能为空'))
    //   } else {
    //     callback()
    //   }
    // }
    var checkaddress = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('地址不能为空'))
      } else {
        callback()
      }
    }
    // var checkjob = (rule, value, callback) => {
    //   if (this.intentionJob.length === 0) {
    //     return callback(new Error('感兴趣的工作不能为空'))
    //   } else {
    //     callback()
    //   }
    // }
    var checkeducation = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('学历不能为空'))
      } else {
        callback()
      }
    }
    return {
      isEdit: false,
	  isEmpty:true,
      rules2: {
        nickName: [{validator: checknickname, trigger: 'blur'}],
        name: [{validator: checkname, trigger: 'blur'}],
        sex: [{validator: checksex, trigger: 'blur'}],
        address: [{validator: checkaddress, trigger: 'blur'}],
        introduce: [{validator: checkintroduce, trigger: 'blur'}],
        education: [{validator: checkeducation, trigger: 'blur'}],
        emotion: [{validator: checkemotion, trigger: 'blur'}]
        // intentionCompany: [{validator: checkcompany, trigger: 'blur'}],
        // intentionJob: [{validator: checkjob, trigger: 'blur'}]
      },
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
      companyOptions: [],
      jobOptions: [],
      intentionCompany: [],
      intentionJob: [],
	  picList:[]
    }
  },
  methods: {
	  uploadPicture(item) {
		  this.isEmpty=false
		  console.log(this.isEmpty)
          const formData = new FormData()
          formData.append('file', item.file)
		  formData.append('avatar',true)
          const uid = item.file.uid
          uploadPhoto(formData).then(res => {
			  console.log(res)
            this.picList.push({ key: uid, value: res.data.url })
            this.emptyUpload()
          }).catch(() => {
            this.$message.error('上传失败，请重新上传')
            this.emptyUpload()
          })
        },
        beforeAvatarUpload(file) {
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
        handleRemove(file, fileList) {
          for (const i in this.picList) {
            if (this.picList[i].key === file.uid) {
              this.picList.splice(i, 1)
            }
          }
		  this.isEmpty=true
        },
        handlePictureCardPreview(file) {
          this.dialogImageUrl = file.url
          this.dialogVisible = true
        },
        /**
         * 清空上传组件
         */
        emptyUpload() {
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
      // alert(this.isEdit)
      this.isEdit = !this.isEdit
    },
    // 提交个人信息
    submitInfo (formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
			list.avatar=this.picList[this.picList-1]
			let params=new URLSearchParams()
		params.append("id",this.$store.state.user.userInfo.id)
		params.append("userInfo",list)

				editResume(params).then(response => {
        if (response.data.code === this.$ECode.SUCCESS) {
			this.resumeList=info
			this.$notify({
            title: '成功',
            message: '修改成功',
            type: 'success',
            offset: 100
          })
        }else{
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
        } else {
          console.log('error submit!!')
        }
      })
    },
  }
}
</script>
