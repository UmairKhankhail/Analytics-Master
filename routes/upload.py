from flask import Blueprint, request, jsonify
from file_manager import FileManager

upload_bp = Blueprint('upload', __name__)
file_manager = FileManager()

@upload_bp.route('/', methods=['POST'])
def upload_file():
    data = request.json
    base64_str = data.get('file')
    file_type = data.get('file_type')
    if not base64_str or not file_type:
        return jsonify({'error': 'Missing file or file_type parameter'}), 400

    try:
        message = file_manager.handle_file_upload(base64_str, file_type)
        return jsonify({'message': message}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
