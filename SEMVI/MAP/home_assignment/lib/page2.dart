import 'package:flutter/material.dart';

class Page2 extends StatefulWidget {
  @override
  _Page2State createState() => _Page2State();
}

class _Page2State extends State<Page2> {
  double _position = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Page 2 - Swipe Animation")),
      body: Center(
        child: GestureDetector(
          onHorizontalDragUpdate: (details) {
            setState(() {
              _position += details.primaryDelta!;
            });
          },
          child: AnimatedContainer(
            duration: Duration(milliseconds: 300),
            transform: Matrix4.translationValues(_position, 0, 0),
            width: 100,
            height: 100,
            color: Colors.orange,
            child: Center(child: Text("Swipe", style: TextStyle(color: Colors.white))),
          ),
        ),
      ),
    );
  }
}
