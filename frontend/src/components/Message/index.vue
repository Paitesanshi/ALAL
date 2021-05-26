<script>
export default {
	name: 'Message',
	data(){
		return{
			session: [
            {
                id: 1,
                user: {
                    name: '示例介绍',
                    img:"@/assets/img/face_logo.png"
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
                    img:"@/assets/img/face_logo.png"
                },
                messages: []
            }
        ],
        // 当前选中的会话
        currentSessionId: 1,
        // 过滤出只包含这个key的会话
        filterKey: '',
		}
	
	},
    // vuex: {
    //     getters: {
    //         user: ({ user }) => user,
    //         session: ({ sessions, currentSessionId }) => sessions.find(session => session.id === currentSessionId)
    //     }
    // },
    // filters: {
    //     // 将日期过滤为 hour:minutes
    //     time (date) {
    //         if (typeof date === 'string') {
    //             date = new Date(date);
    //         }
    //         return date.getHours() + ':' + date.getMinutes();
    //     }
    // },
    directives: {
        // 发送消息后滚动到底部
        'scroll-bottom' () {
			console.log(vm)
            vm.$nextTick(() => {
                vm.$el.scrollTop = vm.$el.scrollHeight - vm.$el.clientHeight;
            });
        }
    }
};
</script>

<template>
<div class="message" v-scroll-bottom="session.messages">
    <ul v-if="session">
        <li v-for="item in session.messages">
            <p class="time">
                <span>{{ item.date | time }}</span>
            </p>
            <div class="main" :class="{ self: item.self }">
                <img class="avatar" width="30" height="30" :src="item.self ? user.img : session.user.img" />
                <div class="text">{{ item.content }}</div>
            </div>
        </li>
    </ul>
</div>
</template>

<style lang="less" scoped>
.message {
    padding: 10px 15px;
    overflow-y: scroll;

    li {
        margin-bottom: 15px;
    }
    .time {
        margin: 7px 0;
        text-align: center;

        > span {
            display: inline-block;
            padding: 0 18px;
            font-size: 12px;
            color: #fff;
            border-radius: 2px;
            background-color: #dcdcdc;
        }
    }
    .avatar {
        float: left;
        margin: 0 10px 0 0;
        border-radius: 3px;
    }
    .text {
        display: inline-block;
        position: relative;
        padding: 0 10px;
        max-width: ~'calc(100% - 40px)';
        min-height: 30px;
        line-height: 2.5;
        font-size: 12px;
        text-align: left;
        word-break: break-all;
        background-color: #fafafa;
        border-radius: 4px;

        &:before {
            content: " ";
            position: absolute;
            top: 9px;
            right: 100%;
            border: 6px solid transparent;
            border-right-color: #fafafa;
        }
    }

    .self {
        text-align: right;

        .avatar {
            float: right;
            margin: 0 0 0 10px;
        }
        .text {
            background-color: #b2e281;

            &:before {
                right: inherit;
                left: 100%;
                border-right-color: transparent;
                border-left-color: #b2e281;
            }
        }
    }
}
</style>