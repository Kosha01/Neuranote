import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import '../services/api.dart';

class AddMemoryScreen extends StatefulWidget {
  @override
  _AddMemoryScreenState createState() => _AddMemoryScreenState();
}

class _AddMemoryScreenState extends State<AddMemoryScreen> {
  final TextEditingController _textController = TextEditingController();
  File? _image;

  Future pickImage() async {
    final picked = await ImagePicker().pickImage(source: ImageSource.gallery);
    if (picked != null) {
      setState(() {
        _image = File(picked.path);
      });
    }
  }

  Future submitMemory() async {
    String text = _textController.text;
    // TODO: send text + image to backend
    await ApiService.addMemory("test_user_id", text, _image?.path);
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text("Memory saved!")));
    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Add Memory")),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(controller: _textController, decoration: InputDecoration(hintText: "Enter memory")),
            SizedBox(height: 20),
            _image == null ? Text("No image selected") : Image.file(_image!, height: 150),
            SizedBox(height: 10),
            ElevatedButton(onPressed: pickImage, child: Text("Pick Image")),
            SizedBox(height: 20),
            ElevatedButton(onPressed: submitMemory, child: Text("Save Memory")),
          ],
        ),
      ),
    );
  }
}
