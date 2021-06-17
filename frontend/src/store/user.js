import { SET_USER_INFO, SET_LOGIN_STATE, SET_SINGLE_STATE } from './mutation-types'

const app = {
    // 全局状态
    state: {
        // 用户信息
        userInfo: {
            avatar: 'http://images.zastatic.com/app/seo/randomuser/2_9.jpg',
            name: 'Jackson',
            id: "8",
            sex: '1',
            address: '北下关街道',
            city: '北京',
            job: '程序员',
            birthDate: '1980-09-17',
            emotion: '1',
            ideal_type: '热爱生活，温柔贤惠'
        },
        isLogin: false,
        isSingle: false
    },
    // getters是对数据的包装，例如对数据进行拼接，或者过滤
    getters: {
        // 类似于计算属性
        getUserPhoto(state) {
            if (state.isLogin) {
                if (state.userInfo.photoUrl) {
                    return state.userInfo.photoUrl
                } else {
                    // alert()
                    return 'http://images.zastatic.com/app/seo/randomuser/2_9.jpg'
                }
            } else {
                return '../../static/images/defaultAvatar.png'
            }
        }
    },
    // 如果我们需要更改store中的状态，一定要通过mutations来进行操作
    mutations: {

        // 传入自定义参数
        [SET_USER_INFO](state, userInfo) {
            state.userInfo = userInfo
        },
        [SET_LOGIN_STATE](state, isLogin) {
            state.isLogin = isLogin
        },
        [SET_SINGLE_STATE](state, isSingle) {
            state.isSingle = isSingle
        }
    },

    // actions是我们定义的一些操作，正常情况下，我们很少会直接调用mutation方法来改变state
    actions: {

    }
}
export default app