import 'package:flutter/material.dart';

void main() {
  runApp(FoodieHubApp());
}

class FoodieHubApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Foodie Hub',
      theme: ThemeData(primarySwatch: Colors.purple),
      home: DisplayPage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class DisplayPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          Image.asset(
            'assets/restaurant.jpeg',
            fit: BoxFit.cover,
            height: double.infinity,
            width: double.infinity,
          ),
          Positioned(
            top: 60,
            left: 20,
            child: Text(
              'Welcome to Foodie Hub',
              style: TextStyle(
                color: Colors.white,
                fontSize: 26,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => MenuPage()),
          );
        },
        backgroundColor: Colors.purple.shade200,
        child: Icon(Icons.add),
      ),
    );
  }
}

class MenuPage extends StatelessWidget {
  final List<Map<String, String>> foodItems = [
    {
      'image': 'assets/burger.jpg',
      'name': 'Burger',
      'price': '₹120',
    },
    {
      'image': 'assets/pasta.jpeg',
      'name': 'Pasta',
      'price': '₹150',
    },
    {
      'image': 'assets/pizza.jpeg',
      'name': 'Pizza',
      'price': '₹200',
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Food Menu")),
      body: Column(
        children: foodItems.map((item) {
          return Expanded(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
              child: Container(
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.grey.shade300),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Row(
                  children: [
                    Container(
                      width: MediaQuery.of(context).size.width * 0.4,
                      height: double.infinity,
                      child: ClipRRect(
                        borderRadius: BorderRadius.only(
                          topLeft: Radius.circular(10),
                          bottomLeft: Radius.circular(10),
                        ),
                        child: Image.asset(
                          item['image']!,
                          fit: BoxFit.cover,
                        ),
                      ),
                    ),
                    Expanded(
                      child: Padding(
                        padding: const EdgeInsets.all(16.0),
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              item['name']!,
                              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                            ),
                            SizedBox(height: 8),
                            Text(
                              item['price']!,
                              style: TextStyle(fontSize: 18, color: Colors.grey[700]),
                            ),
                          ],
                        ),
                      ),
                    )
                  ],
                ),
              ),
            ),
          );
        }).toList(),
      ),
    );
  }
}