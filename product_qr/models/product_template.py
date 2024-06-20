# -*- coding: utf-8 -*-
"""This file provides the While Scan the QR code get the Product Details."""

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)
import base64
import io
try:
    import qrcode
except ImportError:
    _logger.debug('ImportError')


class ProductTemplate(models.Model):
    """
    !!**********@@@ Class representing Product @@@*********!!
    """
    _inherit = 'product.template'

    qr_code = fields.Binary('QR Code', compute="_generate_qr_code")


    @api.depends('name', 'type', 'list_price', 'uom_id')
    def _generate_qr_code(self):
            # """Get the details of Product using compute funtion"""
        for record in self:
            data = f"Product Name: {record.name}.\n" \
                   f"Product Type: {record.type}.\n" \
                   f"Product Price: {record.list_price}.\n" \
                   f"Product UOM: {record.uom_id.name}.\n"
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            qrcode_img = base64.b64encode(buffer.getvalue())
            record.qr_code = qrcode_img
            print(record.qr_code,'qrcode_img')
