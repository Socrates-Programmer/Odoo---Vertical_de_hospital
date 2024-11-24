from odoo import http
from odoo.http import request, Response
import json

class PatientController(http.Controller):

    @http.route('/pacientes/consulta/<string:secuencia>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_patient_by_sequence(self, secuencia):
        # Buscar al paciente con la secuencia proporcionada
        patient = request.env['hospital.patient'].sudo().search([('name', '=', secuencia)], limit=1)

        # Si no se encuentra al paciente, devolver un error 404
        if not patient:
            return Response(
                json.dumps({"error": "Paciente no encontrado"}),
                status=404,
                content_type='application/json'
            )

        # Si el paciente se encuentra, devolver los datos en formato JSON
        patient_data = {
            "seq": patient.name,
            "name": f"{patient.full_name} {patient.last_name}",
            "rnc": patient.rnc,
            "state": patient.state,
        }

        # Asegurarse de que se esté devolviendo una respuesta adecuada
        return Response(
            json.dumps(patient_data),
            status=200,
            content_type='application/json'
        )
