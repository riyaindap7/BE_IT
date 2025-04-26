import 'package:flutter/material.dart';

void main() {
  runApp(CollegeERPApp());
}

class CollegeERPApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'College ERP System',
      home: HomeScreen(),
      theme: ThemeData(
        primarySwatch: Colors.blue,
        appBarTheme: AppBarTheme(
          color: Colors.blue.shade800,
        ),
      ),
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('College ERP System 📚')),
      body: ListView(
        padding: EdgeInsets.all(10),
        children: [
          Text(
            "Departments",
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
          ),
          SizedBox(height: 10),
          DepartmentCard(name: "Computer Science", totalStudents: 300, totalFaculty: 20),
          DepartmentCard(name: "Mechanical Engineering", totalStudents: 250, totalFaculty: 18),
          DepartmentCard(name: "Electrical Engineering", totalStudents: 200, totalFaculty: 15),
          DepartmentCard(name: "Civil Engineering", totalStudents: 220, totalFaculty: 16),
          SizedBox(height: 20),
          Text(
            "College Stats",
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
          ),
          StatsCard(statTitle: "Total Students", value: "970"),
          StatsCard(statTitle: "Total Faculty", value: "69"),
          StatsCard(statTitle: "Pass Percentage", value: "88%"),
          SizedBox(height: 20),
          Text(
            "Recent Activities",
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
          ),
          ListTile(
            leading: Icon(Icons.event, color: Colors.blue),
            title: Text("Guest Lecture on AI - 12th March 2025"),
            subtitle: Text("Department of Computer Science"),
          ),
          ListTile(
            leading: Icon(Icons.event, color: Colors.green),
            title: Text("Robotics Workshop - 15th March 2025"),
            subtitle: Text("Department of Mechanical Engineering"),
          ),
          ListTile(
            leading: Icon(Icons.event, color: Colors.blue),
            title: Text("Civil Engineering Conference - 18th March 2025"),
            subtitle: Text("Department of Civil Engineering"),
          ),
        ],
      ),
    );
  }
}

class DepartmentCard extends StatelessWidget {
  final String name;
  final int totalStudents;
  final int totalFaculty;

  DepartmentCard({required this.name, required this.totalStudents, required this.totalFaculty});

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => DepartmentDetailScreen(name: name)),
        );
      },
      child: Container(
        margin: EdgeInsets.only(bottom: 10),
        padding: EdgeInsets.all(15),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(10),
          boxShadow: [BoxShadow(color: Colors.grey.shade300, blurRadius: 5)],
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(name, style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                Text("Students: $totalStudents, Faculty: $totalFaculty"),
              ],
            ),
            Icon(Icons.arrow_forward, color: Colors.blue),
          ],
        ),
      ),
    );
  }
}

class StatsCard extends StatelessWidget {
  final String statTitle;
  final String value;

  StatsCard({required this.statTitle, required this.value});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.symmetric(vertical: 10),
      padding: EdgeInsets.all(15),
      decoration: BoxDecoration(
        color: Colors.blue.shade100,
        borderRadius: BorderRadius.circular(10),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(statTitle, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
          Text(value, style: TextStyle(fontSize: 16)),
        ],
      ),
    );
  }
}

class DepartmentDetailScreen extends StatelessWidget {
  final String name;

  DepartmentDetailScreen({required this.name});

  TableRow _buildTableRow(String stat, String value, {bool isHeader = false}) {
    return TableRow(
      decoration: BoxDecoration(
        color: isHeader ? Colors.blue.shade100 : Colors.white,
      ),
      children: [
        Padding(
          padding: EdgeInsets.all(8),
          child: Text(
            stat,
            style: TextStyle(
              fontWeight: isHeader ? FontWeight.bold : FontWeight.normal,
            ),
          ),
        ),
        Padding(
          padding: EdgeInsets.all(8),
          child: Text(value),
        ),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('$name Department Details')),
      body: Padding(
        padding: EdgeInsets.all(10),
        child: ListView(
          children: [
            Text(
              "$name Department Stats",
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 10),
            Table(
              border: TableBorder.all(color: Colors.blue),
              children: [
                _buildTableRow("Stat", "Value", isHeader: true),
                _buildTableRow("Total Students", "300"),
                _buildTableRow("Total Faculty", "20"),
                _buildTableRow("Average Marks", "78%"),
                _buildTableRow("Pass Percentage", "92%"),
                _buildTableRow("Research Papers", "15"),
              ],
            ),
            SizedBox(height: 20),
            Text(
              "Recent Department Activities",
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 10),
            ListTile(
              leading: Icon(Icons.event, color: Colors.green),
              title: Text("AI Conference - 10th March 2025"),
              subtitle: Text("$name Department"),
            ),
          ],
        ),
      ),
    );
  }
}