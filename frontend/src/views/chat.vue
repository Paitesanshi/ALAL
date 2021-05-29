<script>
// import { actions } from './store';

// import Card from '../components/card';
// import List from '../components/list';
// import Text from '../components/text';
// import Message from '../components/message';
import Card from '../components/Card';
import List from '../components/List';
import Texts from '../components/Texts';
import Message from '../components/Message';

export default {
    components: { Card, List, Texts, Message },
    // vuex: {
    //     actions: actions
    // },
    // created () {
    //    initData();
    // },
	// methods:{
	// 	initData: function () {
			
	// 	},
	// }
}
</script>

<template>
<div id="chat">
    <div class="chat-sidebar">
        <Card></Card>
        <List></List>
    </div>
    <div class="main">
        <Message></Message>
        <Texts></Texts>
    </div>
</div>
</template>

<style lang="less" scoped>
#chat {
	top:100px;
    margin: 20px auto;
    width: 800px;
    height: 600px;
    overflow: hidden;
    border-radius: 3px;

    .chat-sidebar, .main {
        height: 100%;
    }
    .chat-sidebar {
        float: left;
        width: 200px;
        color: #f4f4f4;
        background-color: #2e3238;
    }
    .main {
        position: relative;
        overflow: hidden;
        background-color: #eee;
    }
    .text {
        position: absolute;
        width: 100%;
        bottom: 0;
        left: 0;
    }
    .message {
        height: ~'calc(100% - 160px)';
    }
}
</style>
