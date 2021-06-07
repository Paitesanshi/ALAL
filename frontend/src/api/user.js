import request from '@/utils/request'
export function authVerify(params) {
	return request({
		url: process.env.WEB_API + '/oauth/verify/' + params,
		method: 'get'
	})
}
export function getFeedbackList(params) {
	return request({
		url: process.env.WEB_API + '/oauth/getFeedbackList',
		method: 'get',
		data: params
	})
}
/**
 * 本地登录
 * @param params
 */
export function localLogin(params) {
	return request({
		url: process.env.WEB_API + '/login/login',
		method: 'post',
		data: params
	})
}

/**
 * 本地注册
 * @param params
 */
export function localRegister(params) {
	return request({
		url: process.env.WEB_API + '/login/register',
		method: 'post',
		data: params
	})
}

export function deleteUserAccessToken(params) {
	return request({
		url: process.env.WEB_API + '/oauth/delete/' + params,
		method: 'post'
	})
}
export function logout() {
	return request({
		url: process.env.WEB_API + '/logout/logout',
		method: 'get'
	})
}
export function editResume(params) {
	return request({
		url: process.env.WEB_API + '/user/editResume',
		method: 'post',
		data: params
	})
}
export function getFriendsRequestList(params) {
	return request({
		url: process.env.WEB_API + '/user/getFriendsRequestList',
		method: 'get',
		params
	})
}
export function editPassword(params) {
	return request({
		url: process.env.WEB_API + '/user/editPassword',
		method: 'post',
		data: params
	})
}
export function getUserInfoByID(params) {
	return request({
		url: process.env.WEB_API + '/user/getUserInfoByID',
		method: 'get',
		params
	})
}