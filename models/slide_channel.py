from odoo import models, fields, api,tools,_

class course_about(models.Model):
    _inherit = "slide.channel"

    long_description = fields.Html(string='Long Description')

