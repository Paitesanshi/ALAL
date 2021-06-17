<template>
  <div class="deliveryWrap">
    <div v-if="!show" class="nofind">
      <p>暂时没有记录哦</p>
    </div>
    <div v-show="show" v-for="(item, index) in list" :key="index"  @click="checkDetail(item.application_id)">
      <el-card shadow="hover" class="deliverycard">
        <div class="resumeBox">
          <p>{{item.applicant}}</p>
          <p>{{item.createdTime}}</p>
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
import { getFriendsRequestList} from '@/api/user'
export default {
  data () {
    return {
      list: [],
      show: true
    }
  },
  created () {
    let that=this
    setTimeout(
      function () {
	      let params = new URLSearchParams()
        params.append('id', that.$store.state.user.userInfo.id)
        console.log("!!!!!!!!!!!!!!")
        getFriendsRequestList(params).then(response => {
          if (response.data.code === that.$ECode.SUCCESS) {
            that.list = response.data.list
          } else {
            that.show = false
          }
        }).catch(error => {
          console.log(error)
		      that.list = [
            {
              id: 1,
              applicant: 'wl',
              createdTime: '2021.05.13'
            }
          ]
        })
      }, 300
    )
  },
  methods: {
    checkDetail (uid) {
      this.$router.push({path: '/questionsDisabled', query: {id: uid}})
    }

  }
}
</script>
