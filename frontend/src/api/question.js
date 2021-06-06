import request from '@/utils/request'

export function editQuestion(params) {
	return request({
		url: process.env.ADMIN_API + '/question/editQuestion',
		method: 'post',
		data: params
	})
}

export function getResumeByID(params) {
	return request({
		url: process.env.ADMIN_API + '/question/getResumeByID',
		method: 'get',
		params
	})
}
export function editResume(params) {
	return request({
		url: process.env.ADMIN_API + '/editResume',
		method: 'post',
		data: params
	})
}
export function getQuestions(params) {
	return request({
		url: process.env.ADMIN_API + '/getQuestions',
		method: 'get',
		params
	})
}
export function submitResult(params) {
	return request({
		url: process.env.ADMIN_API + '/submitResult',
		method: 'post',
		data: params
	})
}