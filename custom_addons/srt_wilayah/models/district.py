# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SrtDistrict(models.Model):
    _name = 'srt_wilayah.district'

    name = fields.Char(string="Kecamatan")
    dist_id = fields.Char(string="Kode Kecamatan")
    reg_id = fields.Char(string="Kode Kota/Kabupaten")
