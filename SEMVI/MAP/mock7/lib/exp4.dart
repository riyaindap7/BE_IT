import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool _showGrid = true;
  bool _showTable = true;
  String _searchQuery = '';
  TextEditingController _searchController = TextEditingController();

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Get screen width to determine how many grid columns we want
    double screenWidth = MediaQuery.of(context).size.width;
    int gridColumns = screenWidth > 600
        ? 4
        : 2; // 4 columns for larger screens, 2 for smaller
    return Scaffold(
      appBar: AppBar(
        title: _searchQuery.isEmpty
            ? Text('Responsive Layout with Widgets')
            : TextField(
                controller: _searchController,
                decoration: InputDecoration(
                  hintText: 'Search...',
                  border: InputBorder.none,
                ),
                onChanged: (value) {
                  setState(() {
                    _searchQuery = value;
                  });
                },
              ),
        actions: [
          IconButton(
            icon: Icon(Icons.search),
            onPressed: () {
              setState(() {
                _searchQuery = '';
                _searchController.clear();
              });
            },
          ),
        ],
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            DrawerHeader(
              decoration: BoxDecoration(
                color: Colors.blueAccent,
              ),
              child: Text(
                'Menu',
                style: TextStyle(color: Colors.white, fontSize: 24),
              ),
            ),
            ListTile(
              title: Text('Home'),
              onTap: () {
                Navigator.pop(context); // Close the drawer
              },
            ),
            ListTile(
              title: Text('Settings'),
              onTap: () {
                Navigator.pop(context); // Close the drawer
              },
            ),
          ],
        ),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header Section using Row
            Container(
              padding: EdgeInsets.all(16.0),
              color: Colors.blueAccent,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Builder(
                    builder: (context) {
                      return IconButton(
                        icon: Icon(Icons.menu, color: Colors.white),
                        onPressed: () {
                          Scaffold.of(context).openDrawer();
                        },
                      );
                    },
                  ),
                  Text('My App',
                      style: TextStyle(color: Colors.white, fontSize: 24)),
                  Icon(Icons.search, color: Colors.white),
                ],
              ),
            ),
            SizedBox(height: 20),

            // Button to toggle visibility of GridView and Table
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      _showGrid = !_showGrid;
                    });
                  },
                  child: Text(_showGrid ? 'Hide Grid' : 'Show Grid'),
                ),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      _showTable = !_showTable;
                    });
                  },
                  child: Text(_showTable ? 'Hide Table' : 'Show Table'),
                ),
              ],
            ),
            SizedBox(height: 20),

            // Show GridView based on the toggle button
            _showGrid
                ? Container(
                    padding: EdgeInsets.all(16.0),
                    child: GridView.builder(
                      shrinkWrap: true,
                      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                        crossAxisCount: gridColumns,
                        crossAxisSpacing: 10,
                        mainAxisSpacing: 10,
                      ),
                      itemCount: 6,
                      itemBuilder: (context, index) {
                        return GestureDetector(
                          onTap: () {
                            ScaffoldMessenger.of(context).showSnackBar(
                              SnackBar(
                                  content: Text('You tapped on Item $index')),
                            );
                          },
                          child: Container(
                            color: Colors.teal,
                            alignment: Alignment.center,
                            child: Text(
                              'Item $index',
                              style:
                                  TextStyle(color: Colors.white, fontSize: 18),
                            ),
                          ),
                        );
                      },
                    ),
                  )
                : SizedBox.shrink(),

            // ListView Section
            SizedBox(height: 20),
            Container(
              height: 200,
              child: ListView.builder(
                itemCount: 10,
                itemBuilder: (context, index) {
                  return ListTile(
                    leading: Icon(Icons.star, color: Colors.amber),
                    title: Text('List Item $index'),
                    subtitle: Text('Subtitle $index'),
                    onTap: () {
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(
                            content: Text('You tapped on List Item $index')),
                      );
                    },
                  );
                },
              ),
            ),
            SizedBox(height: 20),

            // Show Table based on toggle button
            _showTable
                ? Container(
                    padding: EdgeInsets.all(16.0),
                    child: Table(
                      border: TableBorder.all(),
                      children: [
                        TableRow(
                          children: [
                            TableCell(
                                child: Padding(
                                    padding: EdgeInsets.all(8.0),
                                    child: Text('Header 1'))),
                            TableCell(
                                child: Padding(
                                    padding: EdgeInsets.all(8.0),
                                    child: Text('Header 2'))),
                          ],
                        ),
                        TableRow(
                          children: [
                            TableCell(
                                child: Padding(
                                    padding: EdgeInsets.all(8.0),
                                    child: Text('Row 1, Col 1'))),
                            TableCell(
                                child: Padding(
                                    padding: EdgeInsets.all(8.0),
                                    child: Text('Row 1, Col 2'))),
                          ],
                        ),
                        TableRow(
                          children: [
                            TableCell(
                                child: Padding(
                                    padding: EdgeInsets.all(8.0),
                                    child: Text('Row 2, Col 1'))),
                            TableCell(
                                child: Padding(
                                    padding: EdgeInsets.all(8.0),
                                    child: Text('Row 2, Col 2'))),
                          ],
                        ),
                      ],
                    ),
                  )
                : SizedBox.shrink(),
          ],
        ),
      ),
    );
  }
}









