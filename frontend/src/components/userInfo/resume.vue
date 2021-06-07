<template>
  <div>
<!--    <div class="resumeHead" v-if="!haveResume">-->
<!--      <span>创建简历让'kmm-->
<!--        更多的人发现你</span>-->
<!--      <el-button class="createResume" @click="dialogFormVisible = true">新建简历</el-button>-->
<!--    </div>-->
<!--    <el-card v-if="haveResume" class="resumeCard">-->
<!--      <p>个人简历-{{resumeList.name}}</p>-->
<!--      <el-button class="checkBtn" @click="resumeFormVisible = true">查看简历</el-button>-->
<!--    </el-card>-->
<!--    <el-dialog title="我的简历" :visible="resumeFormVisible" class="myDialog">-->
<!--      <div v-if="!isChange">-->
<!--        <table border="1" cellspacing="0" style="border-color:#ededed" class="mytable">-->
<!--          <tr>-->
<!--            <td>姓名：</td>-->
<!--            <td>{{this.$store.state.user.userInfo.name}}</td>-->
<!--          </tr>-->
<!--&lt;!&ndash;          <tr>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>年龄：</td>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>{{this.$store.state.user.userInfo.age}}</td>&ndash;&gt;-->
<!--&lt;!&ndash;          </tr>&ndash;&gt;-->
<!--          <tr>-->
<!--            <td>性别：</td>-->
<!--            <td v-if="this.$store.state.user.userInfo.sex === 1">男</td>-->
<!--            <td v-else>女</td>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <td>手机号：</td>-->
<!--            <td>{{this.$store.state.user.userInfo.phone}}</td>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <td>邮箱：</td>-->
<!--            <td>{{this.$store.state.user.userInfo.email}}</td>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <td>城市：</td>-->
<!--            <td>{{this.$store.state.user.userInfo.city}}</td>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <td>职业：</td>-->
<!--            <td>{{this.$store.state.user.userInfo.career}}</td>-->
<!--          </tr>-->
<!--&lt;!&ndash;          <tr>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>学校：</td>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>{{this.$store.state.user.userInfo.school}}</td>&ndash;&gt;-->
<!--&lt;!&ndash;          </tr>&ndash;&gt;-->
<!--          <tr>-->
<!--            <td>出生日期：</td>-->
<!--            <td>{{this.$store.state.user.userInfo.birthDate}}</td>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <td>情感状况：</td>-->
<!--            <td v-if="this.$store.state.user.userInfo.sex === 1">单身</td>-->
<!--            <td v-else>非单身</td>-->
<!--          </tr>-->
<!--          <tr>-->
<!--            <td>理想型：</td>-->
<!--            <td>{{this.$store.state.user.userInfo.idealType}}</td>-->
<!--          </tr>-->
<!--&lt;!&ndash;          <tr>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>技术栈：</td>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>&ndash;&gt;-->
<!--&lt;!&ndash;          <tr v-for="(item, key) in this.$store.state.user.userInfo.skills" :key="key">&ndash;&gt;-->
<!--&lt;!&ndash;            <td class="progress">{{item.name}}</td>&ndash;&gt;-->
<!--&lt;!&ndash;            <td class="progress">熟悉程度：&ndash;&gt;-->
<!--&lt;!&ndash;              <el-progress :text-inside="true" :stroke-width="15" :percentage="item.level*25"></el-progress>&ndash;&gt;-->
<!--&lt;!&ndash;            </td>&ndash;&gt;-->
<!--&lt;!&ndash;          </tr>&ndash;&gt;-->
<!--&lt;!&ndash;          </td>&ndash;&gt;-->
<!--&lt;!&ndash;          </tr>&ndash;&gt;-->
<!--&lt;!&ndash;          <tr>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>实习（工作）经历：</td>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>{{this.$store.state.user.userInfo.experience}}</td>&ndash;&gt;-->
<!--&lt;!&ndash;          </tr>&ndash;&gt;-->
<!--&lt;!&ndash;          <tr>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>自我介绍：</td>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>{{this.$store.state.user.userInfo.introduce}}</td>&ndash;&gt;-->
<!--&lt;!&ndash;          </tr>&ndash;&gt;-->
<!--&lt;!&ndash;          <tr>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>获奖经历：</td>&ndash;&gt;-->
<!--&lt;!&ndash;            <td>{{this.$store.state.user.userInfo.awards}}</td>&ndash;&gt;-->
<!--&lt;!&ndash;          </tr>&ndash;&gt;-->
<!--        </table>-->
<!--        <el-button class="modBtn" @click="()=>{isChange = !isChange}">修改简历</el-button>-->
<!--      </div>-->
<!--      <el-form :model="resumeList" status-icon :rules="resumerules" ref="resumeInfo" label-width="100px"-->
<!--               class="resumeInfoForm" v-if="isChange">-->
<!--        <el-input v-if="false" v-model="resumeList.id" auto-complete="off" class="hidden">{{this.resumeList.id}}</el-input>-->
<!--        <el-form-item label="姓名" prop="name">-->
<!--          <el-input v-model="resumeList.name" auto-complete="off"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="性别" prop="sex">-->
<!--          <el-select v-model="resumeList.sex" placeholder="请选择性别" style="width: 100%">-->
<!--            <el-option label="男" :value="1"></el-option>-->
<!--            <el-option label="女" :value="2"></el-option>-->
<!--          </el-select>-->
<!--        </el-form-item>-->
<!--        &lt;!&ndash;        <el-form-item label="年龄" prop="age">&ndash;&gt;-->
<!--        &lt;!&ndash;          <el-input v-model="resumeList.age"></el-input>&ndash;&gt;-->
<!--        &lt;!&ndash;        </el-form-item>&ndash;&gt;-->
<!--        <el-form-item label="城市" prop="city">-->
<!--          <el-input v-model="resumeList.city"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="职业" prop="career">-->
<!--          <el-input v-model="resumeList.career"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="出生日期" prop="birthDate">-->
<!--          &lt;!&ndash;          <el-select v-model="resumeList.birthDate" style="width: 100%">&ndash;&gt;-->
<!--          &lt;!&ndash;            <el-option&ndash;&gt;-->
<!--          &lt;!&ndash;              v-for="item in options"&ndash;&gt;-->
<!--          &lt;!&ndash;              :key="item.value"&ndash;&gt;-->
<!--          &lt;!&ndash;              :label="item.label"&ndash;&gt;-->
<!--          &lt;!&ndash;              :value="item.value">&ndash;&gt;-->
<!--          &lt;!&ndash;            </el-option>&ndash;&gt;-->
<!--          &lt;!&ndash;          </el-select>&ndash;&gt;-->
<!--          <el-input v-model="resumeList.birthDate"></el-input>-->
<!--        </el-form-item>-->
<!--        &lt;!&ndash;        <el-form-item label="学校" prop="school">&ndash;&gt;-->
<!--        &lt;!&ndash;          <el-input v-model="resumeList.school"></el-input>&ndash;&gt;-->
<!--        &lt;!&ndash;        </el-form-item>&ndash;&gt;-->
<!--        <el-form-item label="手机号" prop="phone">-->
<!--          <el-input v-model="resumeList.phone"></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="邮箱" prop="email">-->
<!--          <el-input v-model="resumeList.email"></el-input>-->
<!--        </el-form-item>-->
<!--        &lt;!&ndash;        <el-form-item label="技术栈" prop="skills">&ndash;&gt;-->
<!--        &lt;!&ndash;          <el-button @click="addSkill()" class="addbtn">添加</el-button>&ndash;&gt;-->
<!--        &lt;!&ndash;          <div class="skillContain">&ndash;&gt;-->
<!--        &lt;!&ndash;            <div v-for="(item, key) in resumeList.skills" :key="key">&ndash;&gt;-->
<!--        &lt;!&ndash;              <input placeholder="技术" class="input" v-model="item.name"/>&ndash;&gt;-->
<!--        &lt;!&ndash;              <select class="select" v-model="item.level">&ndash;&gt;-->
<!--        &lt;!&ndash;                <option label="了解" value=1></option>&ndash;&gt;-->
<!--        &lt;!&ndash;                <option label="熟悉" value=2></option>&ndash;&gt;-->
<!--        &lt;!&ndash;                <option label="掌握" value=3></option>&ndash;&gt;-->
<!--        &lt;!&ndash;                <option label="精通" value=4></option>&ndash;&gt;-->
<!--        &lt;!&ndash;              </select>&ndash;&gt;-->
<!--        &lt;!&ndash;              <i class="el-icon-error deleteIt" @click="deleteItem(key)"></i>&ndash;&gt;-->
<!--        &lt;!&ndash;            </div>&ndash;&gt;-->
<!--        &lt;!&ndash;          </div>&ndash;&gt;-->
<!--        &lt;!&ndash;        </el-form-item>&ndash;&gt;-->
<!--        <el-form-item label="情感状况" prop="sex">-->
<!--          <el-select v-model="resumeList.emotion" placeholder="请选择是否单身" style="width: 100%">-->
<!--            <el-option label="单身" :value="1"></el-option>-->
<!--            <el-option label="非单身" :value="2"></el-option>-->
<!--          </el-select>-->
<!--        </el-form-item>-->
<!--        <el-form-item label="理想型" prop="idealType">-->
<!--          <el-input type="textarea" :autosize="{ minRows: 4, maxRows: 6}" v-model="resumeList.idealType "></el-input>-->
<!--        </el-form-item>-->
<!--        <el-form-item>-->
<!--          <el-button @click="cancelChange">取消</el-button>-->
<!--          <el-button type="primary" @click="changeResume('resumeInfo')">确定</el-button>-->
<!--        </el-form-item>-->
<!--      </el-form>-->
<!--    </el-dialog>-->
<!--    <div>-->
<!--      <table class="container">-->
<!--        &lt;!&ndash;      <th> 个人信息</th>&ndash;&gt;-->
<!--        <tr>-->
<!--          <td>ID：</td>-->
<!--          <td>{{list.ID}}</td>-->
<!--        </tr>-->
<!--        <tr>-->
<!--          <td>姓名：</td>-->
<!--          <td>{{list.name}}</td>-->
<!--        </tr>-->
<!--        <tr>-->
<!--          <td>性别：</td>-->
<!--          <td v-if="list.sex==2">女</td>-->
<!--          <td v-if="list.sex==1">男</td>-->
<!--        </tr>-->
<!--        <tr>-->
<!--          <td>城市：</td>-->
<!--          <td>{{list.city}}</td>-->
<!--        </tr>-->
<!--        <tr>-->
<!--          <td>职业：</td>-->
<!--          <td>{{list.career}}</td>-->
<!--        </tr>-->
<!--        &lt;!&ndash;      <tr>&ndash;&gt;-->
<!--        &lt;!&ndash;        <td>学历：</td>&ndash;&gt;-->
<!--        &lt;!&ndash;        <td v-if="list.education==4">大专</td>&ndash;&gt;-->
<!--        &lt;!&ndash;        <td v-if="list.education==1">本科</td>&ndash;&gt;-->
<!--        &lt;!&ndash;        <td v-if="list.education==2">硕士</td>&ndash;&gt;-->
<!--        &lt;!&ndash;        <td v-if="list.education==3">博士及以上</td>&ndash;&gt;-->
<!--        &lt;!&ndash;      </tr>&ndash;&gt;-->
<!--        <tr>-->
<!--          <td>情感状况：</td>-->
<!--          <td v-if="list.emotion==2">非单身</td>-->
<!--          <td v-if="list.emotion==1">单身</td>-->
<!--        </tr>-->
<!--        &lt;!&ndash;      <el-button class="edit" @click="changeEdit">编辑</el-button>&ndash;&gt;-->
<!--      </table>-->
<!--      <el-button style="margin-left: 350px" @click="dialogFormVisible = true">编辑</el-button>-->
<!--    </div>-->
    <el-dialog title="新建简历" :visible="true" class="myDialog">
      <el-form :model="resumeList" status-icon :rules="resumerules" ref="resumeInfo" label-width="100px"
               class="resumeInfoForm">
        <el-form-item label="姓名" prop="name">
          <el-input v-model="resumeList.name" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="sex">
          <el-select v-model="resumeList.sex" placeholder="请选择性别" style="width: 100%">
            <el-option label="男" :value="1"></el-option>
            <el-option label="女" :value="2"></el-option>
          </el-select>
        </el-form-item>
<!--        <el-form-item label="年龄" prop="age">-->
<!--          <el-input v-model="resumeList.age"></el-input>-->
<!--        </el-form-item>-->
        <el-form-item label="城市" prop="address">
          <el-input v-model="resumeList.address"></el-input>
        </el-form-item>
        <el-form-item label="职业" prop="career">
          <el-input v-model="resumeList.career"></el-input>
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
          <el-input v-model="resumeList.birthDate"></el-input>
        </el-form-item>
<!--        <el-form-item label="学校" prop="school">-->
<!--          <el-input v-model="resumeList.school"></el-input>-->
<!--        </el-form-item>-->
        <el-form-item label="手机号" prop="phone">
          <el-input v-model="resumeList.phone"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="resumeList.email"></el-input>
        </el-form-item>
        <el-form-item label="情感状况" prop="sex">
          <el-select v-model="resumeList.emotion" placeholder="请选择是否单身" style="width: 100%">
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
          <el-input type="textarea" :autosize="{ minRows: 4, maxRows: 6}" v-model="resumeList.idealType "></el-input>
        </el-form-item>
<!--        <el-form-item label="获奖经历" prop="awards">-->
<!--          <el-input type="textarea" :autosize="{ minRows: 4, maxRows: 6}" v-model="resumeList.awards"></el-input>-->
<!--        </el-form-item>-->
        <el-form-item>
          <el-button @click="cancelSubmit">取消</el-button>
          <el-button type="primary" @click="changeResume('resumeInfo')">确定</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>
<style>
/*table {*/
/*  width: 600px;*/
/*  font-size: 16px*/
/*}*/
/*table tr td {*/
/*  padding: 11.2px;*/
/*  text-align: left;*/
/*}*/
/*.formWrap {*/
/*  width: 500px;*/
/*  font-size: 18px;*/
/*}*/
/*.edit {*/
/*  margin:10px auto auto 40px;*/
/*}*/
.input {
  width: 45%;
  height: 40px;
  border-radius: 4px;
  border: 1px solid #dcdfe6;
  outline: 0;
  background: #fff;
  padding: 0 15px;
  margin: auto 11.2px 14px auto;
}
.deleteIt {
  color: #dcdfe6;
  position: relative;
}
.deleteIt:hover {
  color: red;
}
.select {
  width: 45%;
  height: 40px;
  border-radius: 4px;
  border: 1px solid #dcdfe6;
  outline: 0;
  background: #fff;
  padding: 0 15px;
  margin: auto 11.2px 14px auto;
}
.mytable {
  width: 100%;
  margin: 0;
}
.progress {
  width: 182px;
  border: 0;
}
.modBtn {
  margin: 14px;
}
.resumeCard {
  width: 830px;
  text-align: left;
  height: 100px;
  border-left: 5px solid #888;
}
.createResume {
  position: relative;
  left: 224px;
}
.resumeHead {
  width: 100%;
  border: 1px solid #ededed;
  background: #f4f4f4;
  padding: 21px;
}
.checkBtn {
  position: relative;
  top: -22.4px;
  left: 680px;
}
.addbtn {
  position: relative;
  top: 40px;
  left: 280px;
}
.resumeInfoForm {
  width: 80%;
}
.myDialog {
  width: 1500px;
}
</style>

<script>/* eslint-disable indent */
import { editResume} from "@/api/user";
export default {
  data () {
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
    var checkideal = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('理想型不能为空'))
      } else {
        callback()
      }
    }
    var checkbirthDate = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('出生日期不能为空'))
      } else {
        callback()
      }
    }
    var checkcareer = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('职业不能为空'))
      } else {
        callback()
      }
    }
    // var checkexperience = (rule, value, callback) => {
    //   if (!value) {
    //     return callback(new Error('经历不能为空'))
    //   } else {
    //     callback()
    //   }
    // }
    var checkcity = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('城市不能为空'))
      } else {
        callback()
      }
    }
    // var checkage = (rule, value, callback) => {
    //   if (!value) {
    //     return callback(new Error('年龄不能为空'))
    //   } else {
    //     callback()
    //   }
    // }
    var checkphone = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('手机号不能为空'))
      } else {
        callback()
      }
    }
    var checkemail = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('邮箱不能为空'))
      } else {
        callback()
      }
    }
    // var checkaward = (rule, value, callback) => {
    //   if (!value) {
    //     return callback(new Error('获奖不能为空'))
    //   } else {
    //     callback()
    //   }
    // }
    return {
      len: 0,
      tip: 0,
      isChange: false,
      dialogFormVisible: false,
      resumeFormVisible: true,
      resumeList: {
        // id:'',
        // userId: sessionStorage.getItem('userId'),
		avatar:'',
        city: '',
        name: '',
        sex: '',
        emotion: '',
        career: '',
        // age: '',
        // avatar: '',
        // awards: '',
        email: '',
        birthDate: '',
        idealType: '',
        phone: '',
        // school: '',
        // skills: [
        //   {
        //     level: 0,
        //     name: ''
        //   }
        // ]
      },
      tableList: [],
      haveResume: true,
      value: '',
      // options: [
      //   {
      //     value: '2018',
      //     label: '2018'
      //   },
      //   {
      //     value: '2019',
      //     label: '2019'
      //   },
      //   {
      //     value: '2020',
      //     label: '2020'
      //   },
      //   {
      //     value: '2021',
      //     label: '2021'
      //   },
      //   {
      //     value: '2022',
      //     label: '2022'
      //   }
      // ],
      resumerules: {
        name: [{validator: checkname, trigger: 'blur'}],
        sex: [{validator: checksex, trigger: 'blur'}],
        career: [{validator: checkcareer, trigger: 'blur'}],
        city: [{validator: checkcity, trigger: 'blur'}],
        // introduce: [{validator: checkintroduce, trigger: 'blur'}],
        birthDate: [{validator: checkbirthDate, trigger: 'blur'}],
        phone: [{validator: checkphone, trigger: 'blur'}],
        // school: [{validator: checkschool, trigger: 'blur'}],
        // age: [{validator: checkage, trigger: 'blur'}],
        email: [{validator: checkemail, trigger: 'blur'}],
        idealType: [{validator: checkideal, trigger: 'blur'}],
        // awards: [{validator: checkaward, trigger: 'blur'}]
      }
    }
  },
  created(){
	  this.resumeList.city=this.$store.state.user.userInfo.city
	   this.resumeList.name=this.$store.state.user.userInfo.name
	    this.resumeList.sex=this.$store.state.user.userInfo.sex
		 this.resumeList.emotion=this.$store.state.user.userInfo.emotion
		  this.resumeList.career=this.$store.state.user.userInfo.career
		   this.resumeList.email=this.$store.state.user.userInfo.email
		    this.resumeList.birthDate=this.$store.state.user.userInfo.birthDate
			 this.resumeList.idealType=this.$store.state.user.userInfo.idealType
			 this.resumeList.avatar=this.$store.state.user.userInfo.avatar
  },
  watch: {
    tip() {
      location.reload()
    }
  },
  methods: {
    cancelChange () {
      this.isChange = !this.isChange
    },
    cancelSubmit () {
      this.dialogFormVisible = false
    },
    deleteItem (key) {
      this.resumeList.skills.splice(key, 1)
    },
	changeResume(info){
		let params=new URLSearchParams()
		params.append("id",this.$store.state.user.userInfo.id)
		params.append("userInfo",info)
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
	},
    addSkill () {
      let newskills = {
        id: 0,
        level: 0,
        name: '',
        resumeId: 0
      }
      this.resumeList.skills.push(newskills)
    },
	// getResume(){
	// 	let params = new URLSearchParams()
    // 	params.append('id',  this.$store.state.user.userInfo.id)
	// 	getResumeByID(params).then(response => {
    //     if (response.data.code === this.$ECode.SUCCESS) {
	// 		this.haveResume=true
    //      	this.resumeList = response.data.records
    //     }else{
	// 		this.haveResume=false
	// 	}
    //   }).catch(error => {
    //     console.log(error)
    //   })

	// }
  }
}
</script>
