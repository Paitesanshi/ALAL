<template>
  <div id="ck-editer">
    <ckeditor :editor="editor"
      @ready="onReady"
      v-model="editorData"
      :config="editorConfig">
    </ckeditor>
  </div>
</template>

<script>

import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import CKEditor from "@ckeditor/ckeditor5-vue";
import "@ckeditor/ckeditor5-build-classic/build/translations/zh-cn";
import MyUploadAdapter from "./MyUploadAdapter.js";

export default {
  components: {
    ckeditor: CKEditor.component
  },

  data() {
    return {
      editor: ClassicEditor,
      editorData: "<div>Content of the editor.</div>",
      editorConfig: {
        // The configuration of the editor.
        language: "zh-cn"
        // ckfinder: {
        //   // 后端处理上传逻辑返回json数据, 包括uploaded 上传的字节数 和url两个字段
        //   uploadUrl: process.env.VUE_APP_BASE_URL + `/upload`
        // }
      }
    };
  },
  
  methods: {
    onReady(editor) {
      // 自定义上传图片插件
      editor.plugins.get("FileRepository").createUploadAdapter = loader => {
        return new MyUploadAdapter(loader);
      };
    }
  }
};
</script>

<style lang="scss">
/* 全局修改生效 */
#ck-editer {
  .ck.ck-editor__editable_inline {
    p {
      line-height: 1.5;
    }

    min-height: 400px;
  }
}
</style>

  <!-- <div class="app-container">
    <CKEditor id="editor" rows="10" cols="80"></CKEditor>
   <textarea id="editor" rows="10" cols="80"></textarea>
  </div> -->

// //<script>
// // import { getToken } from '@/utils/auth'
// import CKEditor from 'ckeditor4-vue'
// export default {
//   props: ['content', 'height'],
//   mounted () {
//     var that = this
//     // 使用ckeditor替换textarea，设置代码块风格为 zenburn
//     // 上传时，携带token信息，以便于被feign拦截后传递给mogu-admin获取七牛云相关配置
//     CKEditor.replace('editor',
//       {height: this.height,
//         width: '100%',
//         toolbar: 'toolbar_Full',
//         codeSnippet_theme: 'zenburn',
//         filebrowserImageUploadUrl: process.env.WEB_API + '/file/ckeditorUploadFile?token=' + "1",
// 		extraPlugins='uploadimage',
//         filebrowserUploadUrl: process.env.PICTURE_API + '/file/ckeditorUploadFile?token=' + getToken(),
//      	pasteUploadFileApi: process.env.PICTURE_API + '/file/ckeditorUploadCopyFile?token=' + getToken(),
// 		removeDialogTabs = 'image:advanced;link:advanced',

//       })

//     this.editor = CKEditor.instances.editor
//     this.editor.setData(this.content) // 初始化内容

//     // 一秒钟通知子组件，ckeditor中内容改变
//     that.editor.on('change', function (event) {
//       that.timeout = setTimeout(function () {
//         that.fun()
//       }, 1000)
//     })
//   },
//   created () {
//     this.textData = this.content
//   },
//   watch: {
//     content: function () {
//       this.textData = this.content
//     }
//   },
//   data () {
//     return {
//       editor: null, // 编辑器对象
//       textData: this.content // 初始化内容
//     }
//   },
//   methods: {
//     // 获取data
//     getData: function () {
//       return this.editor.getData()
//     },
//     setData: function (data) {
//       return this.editor.setData(data)
//     },
//     initData: function () {
//       try {
//         this.editor.setData('')
//       } catch (error) {
//         console.log('CKEditor还未加载')
//       }
//     },
//     fun: function () {
//       this.$emit('contentChange', '')
//     }
//   }
// }

// </script>
