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
