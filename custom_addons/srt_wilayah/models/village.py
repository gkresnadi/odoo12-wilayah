# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SrtVillage(models.Model):
    _name = 'srt_wilayah.village'

    name = fields.Char(string="Kelurahan")
    vill_id = fields.Char(string="Kode Kelurahan")
    dist_id = fields.Char(string="Kode Kecamatan")
