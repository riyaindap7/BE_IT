import 'package:flutter/material.dart';

void main() {
  runApp(BookStoreApp());
}

class BookStoreApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Book Store',
      debugShowCheckedModeBanner: false,
      home: DisplayPage(),
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
            'assets/bookstore.jpg',
            fit: BoxFit.cover,
            height: double.infinity,
            width: double.infinity,
          ),
          Positioned(
            top: 60,
            left: 20,
            child: Text(
              'The Book Burrow',
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
            MaterialPageRoute(builder: (context) => BooksMenuPage()),
          );
        },
        backgroundColor: Colors.purple.shade200,
        child: Icon(Icons.add),
      ),
    );
  }
}

class BooksMenuPage extends StatelessWidget {
  final List<Map<String, String>> books = [
    {'image': 'assets/at_habits.jpg', 'name': 'Atomic Habits', 'price': '₹299'},
    {'image': 'assets/alchemist.jpg', 'name': 'The Alchemist', 'price': '₹349'},
    {'image': 'assets/1984.jpg', 'name': '1984', 'price': '₹250'},
    {'image': 'assets/rich_poor.jpg', 'name': 'Rich Dad Poor Dad', 'price': '₹399'},
    {'image': 'assets/fire.jpeg', 'name': 'Wings of Fire', 'price': '₹199'},
    {'image': 'assets/sapiens.jpg', 'name': 'Sapiens', 'price': '₹449'},
    {'image': 'assets/ikigai.jpeg', 'name': 'Ikigai', 'price': '₹299'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Available Books")),
      body: ListView.builder(
        itemCount: books.length,
        itemBuilder: (context, index) {
          final book = books[index];
          return Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
            child: Container(
              decoration: BoxDecoration(
                border: Border.all(color: Colors.grey.shade300),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Row(
                children: [
                  Container(
                    width: 100,
                    height: 120,
                    child: ClipRRect(
                      borderRadius: BorderRadius.horizontal(left: Radius.circular(10)),
                      child: Image.asset(book['image']!, fit: BoxFit.cover),
                    ),
                  ),
                  Expanded(
                    child: Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 20.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(book['name']!, style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                          SizedBox(height: 10),
                          Text(book['price']!, style: TextStyle(fontSize: 16, color: Colors.grey[700])),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
