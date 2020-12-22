from django.contrib import messages


def referral_middlware(get_response):

	def middleware(request):
		ref = request.GET.get('ref', None)
		if ref and not request.user.is_authenticated:
			request.session['referral'] = ref
			messages.add_message(request, messages.INFO, "your referral is %(ref)s")
			print('Print request session is', request.session['referral'])
		elif request.user.is_authenticated and 'referral' in request.session:
			request.session.pop('referral')
		response = get_response(request)


		return response

	return middleware
