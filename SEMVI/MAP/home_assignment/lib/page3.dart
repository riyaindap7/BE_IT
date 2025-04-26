import 'package:flutter/material.dart';

class Page3 extends StatefulWidget {
  @override
  _Page3State createState() => _Page3State();
}

class _Page3State extends State<Page3> {
  double _x = 0;
  double _y = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Page 3 - Drag Animation")),
      body: Stack(
        children: [
          Positioned(
            left: _x,
            top: _y,
            child: Draggable(
              feedback: Container(
                width: 100,
                height: 100,
                color: Colors.purple.withOpacity(0.5),
                child: Center(child: Text("Dragging", style: TextStyle(color: Colors.white))),
              ),
              childWhenDragging: Container(),
              child: Container(
                width: 100,
                height: 100,
                color: Colors.purple,
                child: Center(child: Text("Drag Me", style: TextStyle(color: Colors.white))),
              ),
              onDragEnd: (details) {
                setState(() {
                  _x = details.offset.dx;
                  _y = details.offset.dy - AppBar().preferredSize.height; // Adjust for AppBar height
                });
              },
            ),
          ),
        ],
      ),
    );
  }
}
