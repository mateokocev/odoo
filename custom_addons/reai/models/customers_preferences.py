from odoo import models, fields, api
import re

class CustomerPreferences(models.Model):
    _inherit = 'res.partner'

    preferred_contact_method = fields.Selection(
        [
            ('phone', 'Phone'),
            ('email', 'Email'),
            ('message', 'Message')
        ],
        string="Preferred Contact Method",
        help="How the client prefers to be contacted"
    )

    client_type = fields.Selection(
        [
            ('buyer', 'Buyer'),
            ('seller', 'Seller'),
            ('investor', 'Investor')
        ],
        string="Client Type",
        help="The type of client"
    )

    preferred_property_type = fields.Selection(
        [
            ('apartment', 'Apartment'),
            ('house', 'House'),
            ('commercial', 'Commercial'),
            ('land', 'Land')
        ],
        string="Preferred Property Type",
        help="The type of property the client is interested in"
    )

    preferred_contact_hours = fields.Float(
        string="Preferred Contact Hours",
        help="Specify the preferred contact time in hours (e.g., 14.30 for 2:30 PM).",
    )