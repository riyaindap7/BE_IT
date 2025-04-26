mport 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Page1(),
    );
  }
}

class Page1 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Page 1",
          style: TextStyle(
            fontSize: 24,  // Bigger font size
            fontWeight: FontWeight.bold, // Bold text
            color: const Color.fromARGB(255, 0, 0, 0),  // White text color
          ),
        ),
        backgroundColor: Color.fromRGBO(243, 168, 125, 0.692),  // AppBar background color
      ),
      body: Container(
        color: Color.fromARGB(65, 155, 63, 10), // Background color for Page 1
        child: Center(
          child: ElevatedButton(
            style: ElevatedButton.styleFrom(
              foregroundColor: Colors.white,
              backgroundColor: Color.fromARGB(255, 252, 127, 11), // Button color
              padding: EdgeInsets.symmetric(horizontal: 30, vertical: 15), // Button padding
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(30), // Rounded corners
              ),
              textStyle: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, ), // Text styling
              elevation: 10,
            ),
            onPressed: () {
              // Navigate to Page2 with fade transition
              Navigator.push(
                context,
                PageRouteBuilder(
                  pageBuilder: (context, animation, secondaryAnimation) => Page2(),
                  transitionsBuilder: (context, animation, secondaryAnimation, child) {
                    var fadeTween = Tween(begin: 0.0, end: 1.0);
                    var fadeAnimation = animation.drive(fadeTween);
                    return FadeTransition(opacity: fadeAnimation, child: child);
                  },
                ),
              );
            },
            child: Text("Go to Page 2"),
          ),
        ),
      ),
    );
  }
}

class Page2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Page 2",
          style: TextStyle(
            fontSize: 24,  // Bigger font size
            fontWeight: FontWeight.bold, // Bold text
            color: Colors.black,  // White text color
          ),
        ),
        backgroundColor: Color.fromARGB(255, 76, 199, 140),  // AppBar background color
      ),
      body: Container(
        color: Color.fromARGB(255, 201, 255, 140), // Background color for Page 2
        child: Center(
          child: ElevatedButton(
            style: ElevatedButton.styleFrom(
              foregroundColor: Colors.white,
              backgroundColor: Color.fromARGB(255, 9, 150, 82), // Button color
              padding: EdgeInsets.symmetric(horizontal: 30, vertical: 15), // Button padding
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(30), // Rounded corners
              ),
              textStyle: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),// Text styling
              elevation: 10,
            ),
            onPressed: () {
              // Navigate back to Page1 with fade transition
              Navigator.pop(context);
            },
            child: Text("Go to Page 1"),
          ),
        ),
      ),
    );
  }
}
