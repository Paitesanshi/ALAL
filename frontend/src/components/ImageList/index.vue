<template>
<div class="ImageList">

     <div class="covers" :style="{display:MinDisplay}">
         <div class="cover" v-for="(img,index) in imgs" :key='img'><img :src="img.src" width="90%" class="min" @click="ZoomIn(index)" alt=""></div>
       </div>

       <div class="max" :style="{display:display}">
            <div @click="ZoomOut"  v-for="(img,index) in imgs" :key='img' :class="[index===ShowIndex?'active':'None']" ><img :src="img.src" width="100%"></div>
          
            <div class="small">
                <div :class="[{'smallActive':index===ShowIndex},'cover-small']" v-for="(img,index) in imgs" :key='img' @click="select(index)" ><img :src="img.src" width="90%"></div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: "ImageList",
		props:["imgs"],
        data:function() {
            return {
                ShowIndex:0,
                display: 'none',
                MinDisplay:'flex',
                //Vue模板中使用v-for循环渲染图片时不能直接使用图片文件本地位置
                imgsDefault:[
                    {"src":"http://121.196.111.9:5678/display/img/test.png"},
                    {"src":"http://121.196.111.9:5678/display/img/test.png"},
                    {"src":"http://121.196.111.9:5678/display/img/test.png"},
                    {"src":"https://i.picsum.photos/id/1011/5472/3648.jpg?hmac=Koo9845x2akkVzVFX3xxAc9BCkeGYA9VRVfLE4f0Zzk"},
                    {"src":"https://i.picsum.photos/id/1011/5472/3648.jpg?hmac=Koo9845x2akkVzVFX3xxAc9BCkeGYA9VRVfLE4f0Zzk"},
                    {"src":"https://i.picsum.photos/id/1011/5472/3648.jpg?hmac=Koo9845x2akkVzVFX3xxAc9BCkeGYA9VRVfLE4f0Zzk"},
                    {"src":"https://i.picsum.photos/id/1011/5472/3648.jpg?hmac=Koo9845x2akkVzVFX3xxAc9BCkeGYA9VRVfLE4f0Zzk"},
                    {"src":"https://i.picsum.photos/id/1011/5472/3648.jpg?hmac=Koo9845x2akkVzVFX3xxAc9BCkeGYA9VRVfLE4f0Zzk"},
                    {"src":"https://i.picsum.photos/id/1011/5472/3648.jpg?hmac=Koo9845x2akkVzVFX3xxAc9BCkeGYA9VRVfLE4f0Zzk"},
                ]

            };
        },
		// created(){
		// 	// if (this.imgs!=undefined&&this.imgs!=null&&this.imgs.length>0){
		// 	// 	this.imgs=this.imgs
		// 	// }else{
		// 	// 	this.imgs=this.imgsDefault
		// 	// }
		// 	// console.log(this.imgs)
		// },
        methods:{
            ZoomIn(i){
               this.display='block';
                this.MinDisplay='none';
                this.ShowIndex=i;
            },
            ZoomOut(){
                this.display='none';
                this.MinDisplay='flex';
            },
            select(i){
                this.ShowIndex=i;


            }
        }
    }
</script>

<style scoped>
    .ImageList{
        width: 40%;
    }
    .covers{
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }
    .cover{
        display: flex;
        justify-content: center;
        width: 33%;
        margin: 10px 0;
    }
    .min{
        border-radius: 10px;
        cursor: zoom-in;
    }
    .max{
        cursor: zoom-out;
        width: 100%;

    }
    .small{
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }
    .cover-small{
        display: flex;
        justify-content: center;
        width: 10%;
        margin: 10px 0;
        opacity: 0.6;
        cursor: pointer;
    }
    .cover-small:hover{
        opacity: 1;
    }
    .active{
        display: flex;
    }
    .None{
        display: none;
    }
    .smallActive{
        opacity: 1;
    }

</style>
