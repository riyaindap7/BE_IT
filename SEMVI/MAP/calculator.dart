import 'package:flutter/material.dart';
import 'package:math_expressions/math_expressions.dart';

void main() => runApp(MyCalculator());

class MyCalculator extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: CalculatorPage(),
    );
  }
}

class CalculatorPage extends StatefulWidget {
  @override
  _CalculatorPageState createState() => _CalculatorPageState();
}

class _CalculatorPageState extends State<CalculatorPage> {
  String userInput = '';
  String result = '';

  final List<String> buttons = [
    'C', '=', '-', '+',
    '*', '/', '0', '1',
    '2', '3', '4', '5',
    '6', '7', '8', '9'
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Center(child: Text('Calculator'))),
      backgroundColor: Colors.grey[200],
      body: Column(
        children: [
          Expanded(
            flex: 1,
            child: Container(
              padding: EdgeInsets.all(16),
              alignment: Alignment.centerRight,
              child: Text(
                userInput,
                style: TextStyle(fontSize: 28),
              ),
            ),
          ),
          Divider(thickness: 1),
          Expanded(
            flex: 2,
            child: Container(
              padding: EdgeInsets.all(16),
              alignment: Alignment.centerRight,
              child: Text(
                result,
                style: TextStyle(fontSize: 36, fontWeight: FontWeight.bold),
              ),
            ),
          ),
          Divider(thickness: 1),
          Expanded(
            flex: 6,
            child: GridView.builder(
              itemCount: buttons.length,
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 4),
              itemBuilder: (context, index) {
                return CalculatorButton(
                  text: buttons[index],
                  onTap: () => handleButtonTap(buttons[index]),
                );
              },
            ),
          ),
        ],
      ),
    );
  }

  void handleButtonTap(String value) {
    setState(() {
      if (value == 'C') {
        userInput = '';
        result = '';
      } else if (value == '=') {
        try {
          Parser p = Parser();
          Expression exp = p.parse(userInput.replaceAll('×', '*').replaceAll('÷', '/'));
          ContextModel cm = ContextModel();
          result = exp.evaluate(EvaluationType.REAL, cm).toString();
        } catch (e) {
          result = "Error";
        }
      } else {
        userInput += value;
      }
    });
  }
}

class CalculatorButton extends StatelessWidget {
  final String text;
  final VoidCallback onTap;

  CalculatorButton({required this.text, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        margin: EdgeInsets.all(6),
        decoration: BoxDecoration(
          color: Colors.white,
          border: Border.all(color: Colors.grey.shade400),
          borderRadius: BorderRadius.circular(8),
        ),
        child: Center(
          child: Text(
            text,
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.w600),
          ),
        ),
      ),
    );
  }
}
