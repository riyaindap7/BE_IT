import 'package:flutter/material.dart';

class Page1 extends StatefulWidget {
  @override
  _Page1State createState() => _Page1State();
}

class _Page1State extends State<Page1> {
  double _size = 100;
  Color _color = Colors.blue;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Page 1 - Tap & Long Press")),
      body: Center(
        child: GestureDetector(
          onTap: () {
            setState(() {
              _size = 150;
              _color = Colors.green;
            });
          },
          onLongPress: () {
            setState(() {
              _size = 200;
              _color = Colors.red;
            });
          },
          child: AnimatedContainer(
            duration: Duration(milliseconds: 400),
            width: _size,
            height: _size,
            decoration: BoxDecoration(color: _color, borderRadius: BorderRadius.circular(20)),
          ),
        ),
      ),
    );
  }
}
