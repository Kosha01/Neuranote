import 'dart:convert';
import 'package:http/http.dart' as http;
import 'dart:io';

class ApiService {
  static String backendUrl = "http://localhost:5000";

  static Future addMemory(String userId, String text, String? imagePath) async {
    var uri = Uri.parse('$backendUrl/memories');
    var request = http.MultipartRequest('POST', uri);
    request.fields['user_id'] = userId;
    request.fields['text'] = text;
    if (imagePath != null) {
      request.files.add(await http.MultipartFile.fromPath('image', imagePath));
    }
    var res = await request.send();
    return res.stream.bytesToString();
  }

  static Future searchMemory(String userId, String query) async {
    var res = await http.post(Uri.parse('$backendUrl/search'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'user_id': userId, 'q': query}));
    return jsonDecode(await res.stream.bytesToString());
  }
}

