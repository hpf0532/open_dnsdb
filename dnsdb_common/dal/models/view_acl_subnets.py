# -*- coding: utf-8 -*-

from . import AuditTimeMixin, JsonMixin
from .. import db


class ViewAclSubnet(db.Model, AuditTimeMixin, JsonMixin):
    __tablename__ = 'tb_view_acl_subnets'
    id = db.Column(db.Integer, primary_key=True)
    subnet = db.Column(db.String(32), nullable=False, unique=True)
    start = db.Column(db.Integer, nullable=False)
    end = db.Column(db.Integer, nullable=False)
    origin_acl = db.Column(db.String(32), nullable=False)
    now_acl = db.Column(db.String(32), nullable=False)
    update_user = db.Column(db.String(64), nullable=False)

    def __str__(self):
        return 'ViewAclSubnet[subnet=%s, now_acl=%s, start=%s, end=%s]' % (
            self.subnet,
            self.now_acl,
            self.start,
            self.end
        )
