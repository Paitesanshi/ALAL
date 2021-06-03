import request from '@/utils/request'

export function editQuestion(params) {
	return request({
		url: process.env.ADMIN_API + '/question/editQuestion',
		method: 'post',
		data: params
	})
}


