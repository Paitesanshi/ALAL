<template>
<div>
    <div class="box">
      <div class="title"  >
        <span class="t1">
          登录
        </span>
        <div class="t2" @click="closeCamera">
          X
        </div>
      </div>

    <el-divider></el-divider>
    <div class="camera_outer">
      <video id="videoCamera" :width="videoWidth" :height="videoHeight" autoplay></video>
      <canvas style="display:none;" id="canvasCamera" :width="videoWidth" :height="videoHeight"></canvas>
      <div v-if="imgSrc" class="img_bg_camera">
        <p>效果预览</p>
        <img :src="imgSrc" alt class="tx_img"/>
      </div>
    </div>
    <div class="button btn-group-vertical">
      <el-row justify="center" type="flex">
        <el-button style="width: 100px;margin: 5px;" @click="getCompetence()">打开摄像头</el-button>
      </el-row>
      <el-row  justify="center" type="flex">
        <el-button style="width: 100px;margin: 5px;" @click="stopNavigator()">关闭摄像头</el-button>
      </el-row>
      <el-row  justify="center" type="flex">
        <el-button style="width: 100px;margin: 5px;" @click="setImage()">拍照</el-button>
      </el-row>
      <el-row  justify="center" type="flex">
      <el-button style="width: 100px;margin: 5px;" @click="change()">本地选择</el-button>
      </el-row>
      <el-row  justify="center" type="flex">
        <el-button style="width: 100px;margin: 5px;" @click="submit()" type="primary">确认</el-button>
      </el-row>

    </div>
    </div>
  <div class="mask"></div>
</div>
</template>
<script>
export default {
  name: 'Camera',
  data () {
    return {
      videoWidth: 200,
      videoHeight: 200,
      imgSrc: '',
      thisCancas: null,
      thisContext: null,
      thisVideo: null,
      openVideo: false
    }
  },
  mounted () {
    // this.getCompetence()//进入页面就调用摄像头
  },
  methods: {
    // 调用权限（打开摄像头功能）
    getCompetence () {
      var _this = this
      _this.thisCancas = document.getElementById('canvasCamera')
      _this.thisContext = this.thisCancas.getContext('2d')
      _this.thisVideo = document.getElementById('videoCamera')
      _this.thisVideo.style.display = 'block'
      // 获取媒体属性，旧版本浏览器可能不支持mediaDevices，我们首先设置一个空对象
      if (navigator.mediaDevices === undefined) {
        navigator.mediaDevices = {}
      }
      // 一些浏览器实现了部分mediaDevices，我们不能只分配一个对象
      // 使用getUserMedia，因为它会覆盖现有的属性。
      // 这里，如果缺少getUserMedia属性，就添加它。
      if (navigator.mediaDevices.getUserMedia === undefined) {
        navigator.mediaDevices.getUserMedia = function (constraints) {
          // 首先获取现存的getUserMedia(如果存在)
          var getUserMedia =
            navigator.webkitGetUserMedia ||
            navigator.mozGetUserMedia ||
            navigator.getUserMedia
          // 有些浏览器不支持，会返回错误信息
          // 保持接口一致
          if (!getUserMedia) { // 不存在则报错
            return Promise.reject(
              new Error('getUserMedia is not implemented in this browser')
            )
          }
          // 否则，使用Promise将调用包装到旧的navigator.getUserMedia
          return new Promise(function (resolve, reject) {
            getUserMedia.call(navigator, constraints, resolve, reject)
          })
        }
      }
      var constraints = {
        audio: false,
        video: {
          width: this.videoWidth,
          height: this.videoHeight,
          transform: 'scaleX(-1)'
        }
      }
      navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function (stream) {
          // 旧的浏览器可能没有srcObject
          if ('srcObject' in _this.thisVideo) {
            _this.thisVideo.srcObject = stream
          } else {
            // 避免在新的浏览器中使用它，因为它正在被弃用。
            _this.thisVideo.src = window.URL.createObjectURL(stream)
          }
          _this.thisVideo.onloadedmetadata = function (e) {
            _this.thisVideo.play()
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    //  绘制图片（拍照功能）
    setImage () {
      var _this = this
      // canvas画图
      _this.thisContext.drawImage(
        _this.thisVideo,
        0,
        0,
        _this.videoWidth,
        _this.videoHeight
      )
      // 获取图片base64链接
      var image = this.thisCancas.toDataURL('image/png')
      _this.imgSrc = image// 赋值并预览图片
    },
    // 关闭摄像头
    stopNavigator () {
      this.thisVideo.srcObject.getTracks()[0].stop()
    },
    submit () {
      this.$emit('crop-upload-success', this.imgSrc)
    },
    change () {
      this.$emit('change')
    },
    // base64转文件，此处没用到
    dataURLtoFile (dataurl, filename) {
      var arr = dataurl.split(',')
      var mime = arr[0].match(/:(.*?);/)[1]
      var bstr = atob(arr[1])
      var n = bstr.length
      var u8arr = new Uint8Array(n)
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n)
      }
      return new File([u8arr], filename, {type: mime})
    },
    closeCamera: function () {
      this.$emit('close', '')
    }
  }
}
</script>
<style>
.box {
  width: 500px;
  height: 500px;
  background: white;
  position: fixed;
  margin: auto;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: 5101; /* 要比遮罩层大 */
}

.img_bg_camera {
  float: right;
}

.camera_outer {
  float: left;
}

.registerBox {
  height: 660px;
}

.box .title {
  height: 48px;
  font-size: 22px;
  font-weight: bold;
  text-align: center;
  line-height: 48px;
}

.box .title .t2 {
  font-size: 16px;
  float: right;
  margin-right: 6px;
  margin-top: -6px;
  cursor: pointer;
}

.box .el-divider--horizontal {
  margin: 12px 0;
}

.box .el-form-item__label {
  margin-left: 10px;
  font-size: 16px;
}

.box .el-input__inner {
  margin-left: 10px;
  width: 90%;
}

.box .btn {
  text-align: center;
}

.box .loginBtn {
  width: 40%;
}

.box .registerBtn {
  width: 40%;
}

.elRow {
  margin-top: 15px;
  text-align: center;
}

.loginTip {
  margin-top: 10px;
  font-size: 14px;
  text-align: center;
  color: #bababa;
}

.remarksBox {
  position: fixed;
  left: 50%;
  margin-left: -100px;
  top: 50%;
  margin-top: -50px;
  border: 1px solid red;
  width: 200px;
  height: 100px;
  text-align: center;
  z-index: 5101; /* 要比遮罩层大 */
}

/* 遮罩层 */
.mask {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 5100;
}
</style>
