"""
Functionality which could be shared among various serializes.
"""

class InjectUserMixin(object):
    """
    Inject a user to object being created from the logged in user such that the
    Front-end does not need to supply the value
    """
    def __init__(self, *args, **kwargs):
        super(InjectUserMixin, self).__init__(*args, **kwargs)
        self.fields.pop('user')

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        return super(InjectUserMixin, self).create(validated_data)
