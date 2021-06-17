<script>
// import { actions } from '../store';

export default {
	name: 'List',
	data(){
		return{
			sessions: [
            {
                id: 1,
                user: {
                    name: '示例介绍',
                    img: "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
                },
                messages: [
                    {
                        content: 'Hello，这是一个基于Vue + Vuex + Webpack构建的简单chat示例，聊天记录保存在localStorge, 有什么问题可以通过Github Issue问我。',
                        date: new Date()
                    }, {
                        content: '项目地址: https://github.com/coffcer/vue-chat',
                        date: new Date()
                    }
                ]
            },
            {
                id: 2,
                user: {
                    name: 'webpack',
                    img: "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
                },
                messages: []
            }
        ],
        // 当前选中的会话
        currentId: 1,
        // 过滤出只包含这个key的会话
        filterKey: '',
		}
	
	},
	methods:{
        selectSession(id){
            this.currentId=id
        }
    }
    // vuex: {
    //     actions: actions,
    //     getters: {
    //         // 过滤后的会话列表
    //         sessions: ({ sessions, filterKey }) => {
    //             let result = sessions.filter(session => session.user.name.includes(filterKey));
    //             return result;
    //         },
    //         // 当前会话index
    //         currentId: ({ currentSessionId }) => currentSessionId
    //     }
    // }
};
</script>

<template>
<div class="list">
    <ul>
        <li v-for="item in sessions" :class="{ active: item.id === currentId }" @click="selectSession(item.id)">
            <img class="avatar"  width="30" height="30" :alt="item.user.name" :src="item.user.img">
            <p class="name">{{item.user.name}}</p>
        </li>
    </ul>
</div>
</template>

<style scoped lang="less">
.list {
    li {
        padding: 12px 15px;
        border-bottom: 1px solid #292C33;
        cursor: pointer;
        transition: background-color .1s;

        &:hover {
            background-color: rgba(255, 255, 255, 0.03);
        }
        &.active {
            background-color: rgba(255, 255, 255, 0.1);
        }
    }
    .avatar, .name {
        vertical-align: middle;
    }
    .avatar {
        border-radius: 2px;
    }
    .name {
        display: inline-block;
        margin: 0 0 0 15px;
    }
}
</style>