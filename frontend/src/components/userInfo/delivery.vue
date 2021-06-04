<template>
  <div class="deliveryWrap">
    <div v-if="!show" class="nofind">
      <p>暂时没有记录哦</p>
    </div>
    <div v-show="show" v-for="(item, index) in list" :key="index"  @click="checkDetail(item.recruitId)">
      <el-card shadow="hover" class="deliverycard">
        <div class="resumeBox">
          <p>{{item.title}}</p>
          <p>{{item.content}}</p>
        </div>
      </el-card>
    </div>
  </div>
</template>
<style>
.deliveryWrap {
  height: 1000px;
  overflow: scroll;
}
.deliveryWrap::-webkit-scrollbar {
  display: none;
}
.resumeBox {
  display: flex;
  justify-content: space-between;
}
.deliverycard {
  margin-bottom: 14px;
  width: 100%;
  height: 100px;
  border-left: 5px solid #888;
}
.nofind p {
  font-size: 18px;
  color: #909399;
}
.nofind img {
  width: 350px;
  height: 280px;
  margin: 28px 28px auto auto;
}
</style>

<script>
export default {
  data() {
    return {
      list: [
        {
          title: '有人向你发出好友申请',
          content: 'hihihi，一起交个朋友吧！'
        }
      ],
      show: true
    }
  },
  mounted() {
    this.getList()
  },
  methods: {
    checkDetail(id) {
      localStorage.setItem('jobId', id)
      this.$router.push({name: 'jobInfo'})
    },

  }
}
</script>
