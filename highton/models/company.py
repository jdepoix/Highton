from highton import (
    fields,
    call_mixins,
)
from highton.highton_constants import HightonConstants
from highton.models.contact import Contact


class Company(
    Contact,
    call_mixins.ListCallMixin,
):
    """

    :ivar id: fields.IntegerField(name=HightonConstants.ID)
    :ivar author_id: fields.IntegerField(name=HightonConstants.AUTHOR_ID)
    :ivar background: fields.StringField(name=HightonConstants.BACKGROUND)
    :ivar created_at: fields.DatetimeField(name=HightonConstants.CREATED_AT)
    :ivar group_id: fields.IntegerField(name=HightonConstants.GROUP_ID)
    :ivar owner_id: fields.IntegerField(name=HightonConstants.OWNER_ID)
    :ivar updated_at: fields.DatetimeField(name=HightonConstants.UPDATED_AT)
    :ivar visible_to: fields.StringField(name=HightonConstants.VISIBLE_TO)
    :ivar linkedin_url: fields.StringField(name=HightonConstants.LINKEDIN_URL)
    :ivar avatar_url: fields.StringField(name=HightonConstants.AVATAR_URL)
    :ivar tags: fields.ListField(name=HightonConstants.TAGS, init_class=Tag)
    :ivar contact_data: fields.ObjectField(name=HightonConstants.CONTACT_DATA, init_class=ContactData)
    :ivar subject_datas: fields.ListField(name=HightonConstants.SUBJECT_DATAS, init_class=SubjectData)
    :ivar name: fields.StringField(name=HightonConstants.NAME)
    """
    ENDPOINT = HightonConstants.COMPANIES
    TAG_NAME = HightonConstants.COMPANY

    def __init__(self, **kwargs):
        self.name = fields.StringField(name=HightonConstants.NAME)

        super().__init__(**kwargs)