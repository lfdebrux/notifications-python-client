from notifications_python_client.base import BaseAPIClient


class NotificationsAPIClient(BaseAPIClient):
    def send_sms_notification(self, phone_number, template_id, personalisation=None, reference=None):
        notification = {
            "phone_number": phone_number,
            "template_id": template_id
        }
        if personalisation:
            notification.update({'personalisation': personalisation})
        if reference:
            notification.update({'reference': reference})
        return self.post(
            '/v2/notifications/sms',
            data=notification)

    def send_email_notification(self, email_address, template_id, personalisation=None, reference=None):
        notification = {
            "email_address": email_address,
            "template_id": template_id
        }
        if personalisation:
            notification.update({'personalisation': personalisation})
        if reference:
            notification.update({'reference': reference})
        return self.post(
            '/v2/notifications/email',
            data=notification)

    def get_notification_by_id(self, id):
        return self.get('/v2/notifications/{}'.format(id))

    def get_all_notifications(self, status=None, template_type=None):
        data = {}
        if status:
            data.update({
                'status': status
            })
        if template_type:
            data.update({
                'template_type': template_type
            })
        return self.get(
            '/notifications',
            params=data
        )

    def get_notification_statistics_for_day(self, day=None):
        data = {}
        if day:
            data.update({'day': day})
        return self.get(
            '/notifications/statistics',
            params=data
        )

    def get_template_preview(self, template_id):
        return self.get('service/{}/template/{}/preview'.format(self.client_id, template_id))

    def get_template(self, template_id):
        return self.get('service/{}/template/{}'.format(self.client_id, template_id))

    def get_all_templates(self):
        return self.get('service/{}/template'.format(self.client_id))

    def get_template_version(self, template_id, version):
        return self.get('service/{}/template/{}/version/{}'.format(self.client_id, template_id, version))

    def get_all_template_versions(self, template_id):
        return self.get('service/{}/template/{}/versions'.format(self.client_id, template_id))
