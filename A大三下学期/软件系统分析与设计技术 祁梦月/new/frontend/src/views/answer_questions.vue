<template>
  <div class="survey">
    <div class="top">
      <el-button style="margin-left: 300px"><a href="click_userInfo.vue>">返回</a></el-button>
      <div><h1 align="center">填写问卷以添加好友</h1></div>
    </div>
    <div v-for="(item, index) in questionData" class="question">
      <div class="num">{{ index + 1 }}</div>
      <div class="question-content">
        <div class="question-title">{{ item.title }}</div>
        <template v-if="item.type === 'radio'">
          <MyRadio :radioData="item.data" :radioName="index" @radioChange="radioChange"></MyRadio>
        </template>
        <template v-else-if="item.type === 'checkbox'">
          <MyCheckBox :checkboxData="item.data" :checkboxName="index" @checkboxChange="checkboxChange"></MyCheckBox>
        </template>
        <template v-else-if="item.type === 'textarea'">
          <MyTextArea :textareaName="index" style="margin-bottom: 38px;" @changeTextarea="changeTextarea">{{item.data}}</MyTextArea>
        </template>
      </div>
    </div>
    <el-button @click="handleSubmit" class="surveyBtn">提交问卷</el-button>
  </div>
</template>

<script>
import MyRadio from '../components/MyRadio'
import MyCheckBox from '../components/MyCheckBox'
import MyTextArea from '../components/MyTextArea'
import {getQuestion,submitQuestion} from '../api/question'
export default {
  name: 'questions',
  components: {
    MyRadio, MyCheckBox, MyTextArea
  },
  data () {
    return {
      questionData: [
        {
          id: 1,
          title: '',
          type: 'textarea',
          data: ''
        },
        {
          id: 2,
          title: '',
          type: 'textarea',
          data: ''
        },
        {
          id: 3,
          title: '',
          type: 'textarea',
          data: ''
        },
        {
          id: 4,
          title: '',
          type: 'textarea',
          data: ''
        },
        {
          id: 5,
          title: '',
          type: 'textarea',
          data: ''
        }
      ]
    }
  },
  created(){
	var that = this
	let	params = new URLSearchParams()
      params.append('id', this.$route.query.id)
      getQuestion(params).then(response => {
        if (response.data.code === this.$ECode.SUCCESS) {
          that.questionData = response.data.questionData
          console.log(this.questionData)
        }
      }).catch(error => {
        console.log(error)
       that.questionData= [
        {
          id: 1,
          title: '你看重另一半的颜值吗？',
          type: 'textarea',
          data: '不是很看重，性格第一位'
        },
        {
          id: 2,
          title: '你有什么爱好？',
          type: 'textarea',
          data: '我喜欢健身，爬山以及美食'
        },
        {
          id: 3,
          title: '你喜欢看什么电影？',
          type: 'textarea',
          data: '《星球大战》等科幻电影是我的最爱'
        },
        {
          id: 4,
          title: '你喜欢听什么音乐？',
          type: 'textarea',
          data: 'Justin Bieber的音乐永不过时'
        },
        {
          id: 5,
          title: '你经常出去旅游吗？',
          type: 'textarea',
          data: '每年国庆、春节有空都会去附近的旅游城市游玩'
        }
      ]
        that.loadingInstance.close()
      })
  },
  methods: {
    radioChange (data, name) {
      const question = this.questionData[name]
      for (let item of question.data) {
        item.status = data.value === item.value
      }
    },
    checkboxChange (data, name, isTextarea) {
      const question = this.questionData[name]
      const index = question.data.findIndex(item => item.value === data.value)
      if (isTextarea) {
        question.data[index].status = true
      } else {
        question.data[index].status = !question.data[index].status
      }
    },
    changeTextarea (data, name) {
      const question = this.questionData[name]
      question.data = data
    },
    handleSubmit () {
      const data = this.questionData
      const params = {}
      for (let question of data) {
        if (question.type === 'radio') {
          const index = question.data.findIndex(item => item.status)
          if (index !== -1) {
            params[question.id] = question.data[index].value
          } else {
            params[question.id] = ''
          }
        } else if (question.type === 'checkbox') {
          const arr = []
          for (let item of question.data) {
            if (item.status) {
              arr.push(item.value)
            }
          }
          params[question.id] = arr
        } else if (question.type === 'textarea') {
          params[question.id] = question.data
        }
      }
      // console.log(data[0]);
      console.log(params)
      var that = this
      let	params2 = new URLSearchParams()
      params2.append('id', this.$store.state.user.userInfo.uid)
	  params2.append('questionData', params)
      submitQuestion(params2).then(response => {
        if (response.data.code === this.$ECode.SUCCESS) {
          console.log(this.blogData)
		  this.$notify({
			title: '成功',
            message: '提交成功',
            type: 'success',
            offset: 100
		  })
        }
      }).catch(error => {
        console.log(error)
		 this.$notify({
			title: '失败',
            message: '网络错误',
            type: 'error',
            offset: 100
		  })
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.survey{
  top:100px;
  position:relative;
}
.surveyBtn{
  display: block;
  margin: 20px auto;
  height: 100px;
  width:300px;
  font-size:30px;
}
.question {
  margin: 20px auto;
  margin-bottom: 20px;
  position: relative;
  display: block;
  width: 720px;
  height: auto;
  background-color: #fffcf0;
  border-radius: 20px;
  z-index: 0;
  .num {
    position: absolute;
    left: 20px;
    top: 0;
    width: 54px;
    height: 66px;
    line-height: 66px;
    font-size: 30px;
    color: #fff;
    background-color: #FCB882;
    text-align: center;
  }
  .question-content {
    margin-left: 40px;
    margin-top: 80px;
    display: inline-block;
    width: 520px;
    .question-title {
      margin-bottom: 38px;
      line-height: 1.5em;
      color: #976e48;
      font-weight: bold;
      font-size: 30px;
      text-align: left;
    }
    /*background: #ff1d5e;*/
  }
}
</style>
