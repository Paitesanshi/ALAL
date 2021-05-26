<script>
// import { actions } from '../store';

export default {
	name: 'Card',
    // vuex: {
    //     actions: actions,
    //     getters: {
    //         user: ({ user }) => user,
    //         filterKey: ({ filterKey }) => filterKey
    //     }
    // },
	data(){
		return{
			user: {
				name: 'coffce',
				img: "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"
        	},
			
		}
	},
    methods: {
        onKeyup (e) {
            this.search(e.target.value);
        }
    }
};
</script>

<template>
<div class="card">
    <div>
        <img class="avatar" width="40" height="40" :alt="user.name" :src="user.img">
        <p class="card-name">{{user.name}}</p>
    </div>
    <footer>
        <input class="search" type="text" placeholder="search user..." @keyup="onKeyup">
    </footer>
</div>
</template>

<style scoped lang="less">
.card {
    padding: 12px;
    border-bottom: solid 1px #24272C;

    footer {
        margin-top: 10px;
    }

	header {
 		margin-top: 10px;
	}
    .avatar, .name {
        vertical-align: middle;
    }
    .avatar {
        border-radius: 2px;
    }
    .card-name {
        display: inline-block;
        margin: 0 0 0 15px;
        font-size: 16px;
    }
    .search {
        padding: 0 10px;
        width: 100%;
        font-size: 12px;
        color: #fff;
        height: 30px;
        line-height: 30px;
        border: solid 1px #3a3a3a;
        border-radius: 4px;
        outline: none;
        background-color: #26292E;
    }
}
</style>