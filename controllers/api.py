# -*- coding: utf-8 -*-

import base64
import json
import logging

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class EmployeeProjectAPI(http.Controller):

    # ---------------------------
    # BASIC AUTH HELPER
    # ---------------------------
    def _authenticate(self):
        auth_header = request.httprequest.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Basic '):
            return None

        try:
            encoded_credentials = auth_header.split(' ')[1]
            decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
            username, password = decoded_credentials.split(':', 1)

            uid = request.session.authenticate(
                request.db,
                username,
                password
            )
            return uid

        except Exception as e:
            _logger.error("Auth error: %s", str(e))
            return None

    # ---------------------------
    # API ENDPOINT
    # ---------------------------
    @http.route(
        '/api/employees/active-projects',
        type='http',
        auth='none',
        methods=['GET'],
        csrf=False
    )
    def get_employees_active_projects(self, **kwargs):

        uid = self._authenticate()
        if not uid:
            return request.make_response(
                json.dumps({
                    "error": "Unauthorized"
                }),
                headers=[('Content-Type', 'application/json')],
                status=401
            )

        employees = request.env['hr.employee'].sudo().search([])

        result = []

        for emp in employees:
            # Active projects (adjust domain if your logic differs)
            projects = request.env['project.project'].sudo().search([
                ('active', '=', True)
            ])

            result.append({
                "employee_id": emp.id,
                "employee_name": emp.name,
                "active_projects": [
                    {
                        "project_id": p.id,
                        "project_name": p.name
                    }
                    for p in projects
                ]
            })

        return request.make_response(
            json.dumps({
                "status": "success",
                "data": result
            }),
            headers=[('Content-Type', 'application/json')]
        )

    @http.route('/test-api', auth='public')
    def test(self):
        return "OK"