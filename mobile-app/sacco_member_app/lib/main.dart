import 'config.dart';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  runApp(SaccoPlusApp());
}

class SaccoPlusApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SaccoPlus',
      theme: ThemeData(primarySwatch: Colors.green),
      home: LoginScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class LoginScreen extends StatefulWidget {
  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final usernameController = TextEditingController();
  final passwordController = TextEditingController();
  String error = '';
  bool isLoading = false;

  Future<void> login() async {
    setState(() {
      isLoading = true;
      error = '';
    });

    final url = Uri.parse('$baseUrl/api/auth/login/');  // Replace with your server IP if not local

    try {
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'username': usernameController.text,
          'password': passwordController.text,
        }),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final prefs = await SharedPreferences.getInstance();
        await prefs.setString('access', data['access']);
        await prefs.setString('refresh', data['refresh']);

        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (_) => DashboardScreen()),
        );
      } else {
        setState(() {
          error = 'Login failed. Check your credentials.';
        });
      }
    } catch (e) {
      setState(() {
        error = 'Error connecting to server.';
      });
    }

    setState(() {
      isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('SaccoPlus Login')),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          children: [
            TextField(
              controller: usernameController,
              decoration: InputDecoration(labelText: 'Username'),
            ),
            TextField(
              controller: passwordController,
              decoration: InputDecoration(labelText: 'Password'),
              obscureText: true,
            ),
            SizedBox(height: 20),
            if (error.isNotEmpty)
              Text(error, style: TextStyle(color: Colors.red)),
            SizedBox(height: 20),
            isLoading
                ? CircularProgressIndicator()
                : ElevatedButton(
                    onPressed: login,
                    child: Text('Login'),
                  ),
          ],
        ),
      ),
    );
  }
}

class DashboardScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('SaccoPlus Dashboard'),
      ),
      body: Center(
        child: Text(
          'Welcome to SaccoPlus!',
          style: TextStyle(fontSize: 24),
        ),
      ),
    );
  }
}
