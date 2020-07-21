# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SrtProvince(models.Model):
    _name = 'srt_wilayah.province'

    name = fields.Char(string="Provinsi")
    prov_id = fields.Char(string="Kode Provinsi")
