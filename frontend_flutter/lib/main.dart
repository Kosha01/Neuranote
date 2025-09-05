import 'package:flutter/material.dart';
import 'screens/home_screen.dart';
import 'screens/add_memory_screen.dart';
import 'screens/chat_screen.dart';
import 'screens/calendar_screen.dart';

void main() {
  runApp(NeuraNoteApp());
}

class NeuraNoteApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'NeuraNote',
      theme: ThemeData(primarySwatch: Colors.blue),
      initialRoute: '/',
      routes: {
        '/': (context) => HomeScreen(),
        '/add_memory': (context) => AddMemoryScreen(),
        '/chat': (context) => ChatScreen(),
        '/calendar': (context) => CalendarScreen(),
      },
    );
  }
}
