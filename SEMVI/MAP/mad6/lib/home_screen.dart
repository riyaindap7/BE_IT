import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class HomeScreen extends StatelessWidget {
  final TextEditingController nameController = TextEditingController();
  final CollectionReference users = FirebaseFirestore.instance.collection('users');

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Firebase UI")),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: nameController,
              decoration: InputDecoration(labelText: "Enter Name"),
            ),
            ElevatedButton(
              onPressed: () {
                users.add({'name': nameController.text});
                nameController.clear();
              },
              child: Text("Add to Firebase"),
            ),
            Expanded(
              child: StreamBuilder(
                stream: users.snapshots(),
                builder: (context, snapshot) {
                  if (!snapshot.hasData) return CircularProgressIndicator();
                  final docs = snapshot.data!.docs;
                  return ListView.builder(
                    itemCount: docs.length,
                    itemBuilder: (context, index) {
                      return ListTile(title: Text(docs[index]['name']));
                    },
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
