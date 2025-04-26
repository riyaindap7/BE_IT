import 'package:flutter/material.dart';

void main() {
  runApp(ModernStyledApp());
}

class ModernStyledApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Stylish UI',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        scaffoldBackgroundColor: Colors.grey[100],
        fontFamily: 'Roboto',
      ),
      home: StylishHome(),
    );
  }
}

class StylishHome extends StatefulWidget {
  @override
  _StylishHomeState createState() => _StylishHomeState();
}

class _StylishHomeState extends State<StylishHome> {
  int _counter = 0;
  double _sliderValue = 100;
  bool _showCounter = true;

  void _increaseCounter() {
    setState(() {
      _counter++;
    });
  }

  Color _getFABColor() {
    return Color.lerp(Colors.teal, Colors.pink, _sliderValue / 255)!;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('✨ Stylish Counter'),
        centerTitle: true,
        flexibleSpace: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              colors: [Colors.teal, Colors.pink],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
          ),
        ),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            // Image widget
            Image.network(
              'https://picsum.photos/400/150',
              fit: BoxFit.cover,
              width: double.infinity,
              height: 150,
            ),

            SizedBox(height: 20),

            // Switch widget
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text('Show Counter'),
                Switch(
                  value: _showCounter,
                  onChanged: (value) {
                    setState(() {
                      _showCounter = value;
                    });
                  },
                  activeColor: Colors.pink,
                ),
              ],
            ),

            // Conditionally show the counter
            if (_showCounter)
              Center(
                child: Card(
                  elevation: 10,
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
                  margin: EdgeInsets.symmetric(horizontal: 30, vertical: 10),
                  child: Padding(
                    padding: const EdgeInsets.all(24.0),
                    child: Column(
                      children: [
                        Icon(Icons.favorite, size: 60, color: Colors.teal),
                        SizedBox(height: 20),
                        Text(
                          'Counter',
                          style: TextStyle(
                            fontSize: 30,
                            fontWeight: FontWeight.w600,
                            color: Colors.teal[700],
                          ),
                        ),
                        SizedBox(height: 10),
                        Text(
                          '$_counter',
                          style: TextStyle(
                            fontSize: 48,
                            fontWeight: FontWeight.bold,
                            color: Colors.pink[800],
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),

            // Slider widget
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                children: [
                  Text('Change FAB Color'),
                  Slider(
                    value: _sliderValue,
                    min: 0,
                    max: 255,
                    divisions: 255,
                    onChanged: (value) {
                      setState(() {
                        _sliderValue = value;
                      });
                    },
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: _increaseCounter,
        label: Text("Add"),
        icon: Icon(Icons.add),
        backgroundColor: _getFABColor(),
      ),
    );
  }
}
