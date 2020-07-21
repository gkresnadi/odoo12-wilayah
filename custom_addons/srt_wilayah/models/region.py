# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SrtRegion(models.Model):
    _name = 'srt_wilayah.region'

    name = fields.Char(string="Kota/Kabupaten")
    prov_id = fields.Char(string="Kode Provinsi")
    reg_id = fields.Char(string="Kode Kota/Kabupaten")
