from highton.call_mixins import Call
from highton import fields
from highton.models.note import Note


class ListNoteCallMixin(Call):
    """
    A mixin to get all notes of inherited class
    These could be: people || companies || kases || deals

    """

    NOTES_OFFSET = 25

    def notes(self, page=0, since=None):
        """
        Get the notes of current object

        :param page: the page starting at 1 (not 0!!!)
        :type since: int
        :param since: get all notes since a datetime
        :type since: datetime.datetime
        :return: the notes
        :rtype: list
        """
        params = {'page': int(page) * self.NOTES_OFFSET}
        if since:
            params['since'] = since.strftime(self.COLLECTION_DATETIME)

        return fields.ListField(
            name=self.ENDPOINT,
            init_class=Note
        ).decode(
            self.element_from_string(
                self._get_request(
                    endpoint=self.ENDPOINT + '/' + str(self.id) + '/notes',
                    params=params
                ).text
            )
        )
