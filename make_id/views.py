from django.http import HttpResponse
import uuid
from django.db import transaction
from make_id.models import uid
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@transaction.atomic
def make_and_record_id(request):
    the_id = str(uuid.uuid4())[25:].upper()
    try:
        uid.objects.get(uid=the_id)
    except ObjectDoesNotExist:
        # exception means id not found in db so we can issue
        uid_model = uid(uid=the_id, origin='tgac')
        uid_model.save()
        return HttpResponse(the_id)
    #else we have a collision so recurse
    return make_and_record_id(request)
