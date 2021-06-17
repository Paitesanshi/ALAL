<template>
  <div class="survey">
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
          <MyTextArea disabled :textareaName="index" :value="item.data" style="margin-bottom: 38px;"  @changeTextarea="changeTextarea"></MyTextArea>
        </template>
      </div>
    </div>
	<div><h1 align="center">怎么样？答案符合你的心意吗？</h1></div>
    <div>
      <el-button style="float:right ; margin-right: 400px;margin-bottom: 200px" @click="handleSubmit(true)" class="surveyBtn">同意</el-button>
	   <el-button style="float:left ; margin-left: 400px ;margin-bottom: 200px" @click="handleSubmit(false)" class="surveyBtn">不同意</el-button>
    </div>

  </div>
</template>

<script>
import MyRadio from '../components/MyRadio';
import MyCheckBox from '../components/MyCheckBox';
import MyTextArea from '../components/MyTextAreaDisabled';
import {getQuestions} from '../api/question'
export default {
  name: 'questionsDisabled',
  components: {
    MyRadio, MyCheckBox, MyTextArea
  },
  data () {
    return {
      questionData: []
    }
  },
  created(){
	var that = this
	let	params = new URLSearchParams()
      params.append('id', this.$route.query.id)
      getQuestions(params).then(response => {
        if (response.data.code === this.$ECode.SUCCESS) {
          that.questionData = response.data.data
          console.log(this.questionData)
        }
      }).catch(error => {
        console.log(error)
       that.questionData= [
        {
          id: 1,
          title: '你的最高学历是什么？',
          type: 'textarea',
          data: '北交大研究生'
        },
        {
          id: 2,
          title: '你能接受你的另一半是强迫症吗？',
          type: 'textarea',
          data: '可以，因为我也有一点强迫症'
        },
        {
          id: 3,
          title: '你打算什么时候结婚？',
          type: 'textarea',
          data: '如果情投意合的话什么时候都可以'
        },
        {
          id: 4,
          title: '是否打算要孩子？',
          type: 'textarea',
          data: '要，因为我喜欢小孩'
        },
        {
          id: 5,
          title: '打算要几个孩子？',
          type: 'textarea',
          data: '最多两个吧'
        },
      ]
        that.loadingInstance.close()
      })
  },
  methods: {
    radioChange(data, name) {
      const question = this.questionData[name];
      for (let item of question.data) {
        item.status = data.value === item.value;
      }
    },
    checkboxChange(data, name, isTextarea) {
      const question = this.questionData[name];
      const index = question.data.findIndex(item => item.value === data.value);
      if (isTextarea) {
        question.data[index].status = true;
      } else {
        question.data[index].status = !question.data[index].status;
      }
    },
    changeTextarea(data, name) {
      const question = this.questionData[name];
      question.data = data;
    },
    handleSubmit(info) {
      console.log(info);
      let	params = new URLSearchParams()
      // if (this.blogUid) {
      //   params.append('uid', this.blogUid)
      // }
      // if (this.blogOid) {
      //   params.append('oid', this.blogOid)
      // }
      params.append('id', this.$route.query.id)
	  params.append('accepted', info)
      submitResult(params).then(response => {
        if (response.data.code === this.$ECode.SUCCESS) {
			this.$notify({
				title: '成功',
				message: '申请处理成功',
				type: 'success',
				offset: 100
			})
		}
      }).catch(error => {
      	this.$notify.error({
			title: '失败',
			message: error,
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
