<template>
  <div class="survey">
    <div><h1 align="center">请编辑您的问卷</h1></div>
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
          <MyTextArea disabled :textareaName="index" style="margin-bottom: 38px;"  @changeTextarea="changeTextarea"></MyTextArea>
        </template>
      </div>
    </div>
    <el-button @click="handleSubmit" class="surveyBtn">提交问卷</el-button>
  </div>
</template>

<script>
import MyRadio from '../components/MyRadio';
import MyCheckBox from '../components/MyCheckBox';
import MyTextArea from '../components/MyTextArea';
import {editQuestion} from '../api/question'
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
          title: '填空题：请填写你的问题',
          type: 'textarea',
          data: ''
        },
        {
          id: 2,
          title: '填空题：请填写你的问题',
          type: 'textarea',
          data: ''
        },
        {
          id: 3,
          title: '填空题：请填写你的问题',
          type: 'textarea',
          data: ''
        },
        {
          id: 4,
          title: '填空题：请填写你的问题',
          type: 'textarea',
          data: ''
        },
        {
          id: 5,
          title: '填空题：请填写你的问题',
          type: 'textarea',
          data: ''
        },
      ]
    }
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
    handleSubmit() {
      const data = this.questionData;
      const params = {};
      for (let question of data) {
        if (question.type === 'radio') {
          const index = question.data.findIndex(item => item.status);
          if (index !== -1) {
            params[question.id] = question.data[index].value;
          } else {
            params[question.id] = '';
          }
        } else if (question.type === 'checkbox') {
          const arr = [];
          for (let item of question.data) {
            if (item.status) {
              arr.push(item.value);
            }
          }
          params[question.id] = arr;
        } else if (question.type === 'textarea') {
          params[question.id] = question.data;
        }
      }
      // console.log(data[0]);
      console.log(params);
	  var that = this
    let	params2 = new URLSearchParams()
    // if (this.blogUid) {
    //   params.append('uid', this.blogUid)
    // }
    // if (this.blogOid) {
    //   params.append('oid', this.blogOid)
    // }
    params2.append('id', this.$store.state.user.userInfo.uid)
    editQuestion(params2).then(response => {
      if (response.data.code === this.$ECode.SUCCESS) {
        this.blogData = response.data
        console.log(this.blogData)
        // this.blogUid = response.data.uid
        // this.blogOid = response.data.oid\
        this.getCommentDataList()
      } else {

      }
      setTimeout(() => {
        that.blogContent = response.data.content
        that.loadingInstance.close()
      }, 20)
    }).catch(error => {
      console.log(error)
      this.blogData.labels = ['技术', '大数据']
      this.blogData.blogSort = '技术'
      this.blogContent = 'This is a test'
      this.blogData.title = 'test'
      this.blogData.author = 'ptss'
      this.blogData.summary = '概括'
      this.blogData.clickCount = 100
      this.blogData.likeCount = 200
      this.blogData.time = '2020-12-2'
      this.blogData.need = 1
      this.getCommentDataList()
      that.loadingInstance.close()
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
