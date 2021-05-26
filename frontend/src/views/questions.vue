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
          <MyTextArea :textareaName="index" style="margin-bottom: 38px;" @changeTextarea="changeTextarea"></MyTextArea>
        </template>
      </div>
    </div>
    <el-button @click="handleSubmit" class="surveyBtn">点击提交</el-button>
  </div>
</template>

<script>
  import MyRadio from '../components/MyRadio';
  import MyCheckBox from '../components/MyCheckBox';
  import MyTextArea from '../components/MyTextArea';
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
            title: '单选题：今年是哪一年？',
            type: 'radio',
            data: [
              {
                type: 1,
                label: '2017年',
                value: 'a',
                status: false
              },
              {
                type: 1,
                label: '2018年',
                value: 'b',
                status: false
              },
              {
                type: 1,
                label: '2019年',
                value: 'c',
                status: false
              },
              {
                type: 1,
                label: '2020年',
                value: 'd',
                status: false
              },
              {
                type: 2,
                label: '其他',
                value: '',
                status: false
              }
            ]
          },
          {
            id: 2,
            title: '单选题：广东省的冬天会下雪吗？',
            type: 'radio',
            data: [
              {
                type: 1,
                label: '会',
                value: 'a',
                status: false
              },
              {
                type: 1,
                label: '不会',
                value: 'b',
                status: false
              }
            ]
          },
          {
            id: 3,
            title: '多选题：你喜欢的季节有？',
            type: 'checkbox',
            data: [
              {
                type: 1,
                label: '春天',
                value: 'a',
                status: false
              },
              {
                type: 1,
                label: '夏天',
                value: 'b',
                status: false
              },
              {
                type: 1,
                label: '秋天',
                value: 'c',
                status: false
              },
              {
                type: 1,
                label: '冬天',
                value: 'd',
                status: false
              }
            ]
          },
          {
            id: 4,
            title: '填空题：请问还有什么疑问吗？',
            type: 'textarea',
            data: ''
          },
          {
            id: 5,
            title: '多选题：你喜欢的水果有？',
            type: 'checkbox',
            data: [
              {
                type: 1,
                label: '苹果',
                value: 'a',
                status: false
              },
              {
                type: 1,
                label: '香蕉',
                value: 'b',
                status: false
              },
              {
                type: 1,
                label: '桃子',
                value: 'c',
                status: false
              },
              {
                type: 1,
                label: '李子',
                value: 'd',
                status: false
              },
              {
                type: 2,
                label: '其他',
                value: '',
                status: false
              }
            ]
          }
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
