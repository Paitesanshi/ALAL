import request from '@/utils/request'

export function editQuestion(params) {
	return request({
		url: process.env.WEB_API + '/question/editQuestion',
		method: 'post',
		data: params
	})
}

export function getResumeByID(params) {
	return request({
		url: process.env.WEB_API + '/question/getResumeByID',
		method: 'get',
		params
	})
}
export function getQuestions(params) {
	return request({
		url: process.env.WEB_API + '/getQuestions',
		method: 'get',
		params
	})
}
export function submitResult(params) {
	return request({
		url: process.env.WEB_API + '/submitResult',
		method: 'post',
		data: params
	})
}
export function getQuestion(params) {
	return request({
		url: process.env.WEB_API + '/getQuestion',
		method: 'get',
		params
	})
}
export function submitQuestion(params) {
	return request({
		url: process.env.WEB_API + '/submitQuestion',
		method: 'post',
		data: params
	})
}