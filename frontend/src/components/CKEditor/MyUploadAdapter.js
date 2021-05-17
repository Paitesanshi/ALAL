import axios from "axios";

/**
 * 自定义上传图片插件
 */
class MyUploadAdapter {
	constructor(loader) {
		this.loader = loader;
	}

	async upload() {
		const data = new FormData();
		data.append("file", await this.loader.file);

		const res = await axios({
			url: process.env.VUE_APP_BASE_URL + `/upload`,
			method: "POST",
			data,
			withCredentials: true, // true 为不允许带 token, false 为允许
		});

		console.log(res.data);
		// 后台返回数据：
		// {"code":0,"msg":"success","data":{"url":"/upload/struts2.jpeg"}}

		// 方法返回数据格式： {default: "url"}
		return {
			default: process.env.VUE_APP_TARGET_URL + res.data.data.url,
		};
	}
}

export default MyUploadAdapter;

