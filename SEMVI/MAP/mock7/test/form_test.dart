import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mock7/registration_form.dart';
import 'package:mock7/login_form.dart';

void main() {
  testWidgets('Registration form validation and submission', (WidgetTester tester) async {
    await tester.pumpWidget(MaterialApp(home: Scaffold(body: RegistrationForm())));

    // Try submitting empty form
    await tester.tap(find.text('Register'));
    await tester.pump();

    expect(find.text('Please enter your name'), findsOneWidget);
    expect(find.text('Please enter your email'), findsOneWidget);
    expect(find.text('Please enter a password'), findsOneWidget);

    // Enter valid data
    await tester.enterText(find.byType(TextFormField).at(0), 'John Doe');
    await tester.enterText(find.byType(TextFormField).at(1), 'john@example.com');
    await tester.enterText(find.byType(TextFormField).at(2), 'password123');
    await tester.enterText(find.byType(TextFormField).at(3), 'password123');

    await tester.tap(find.text('Register'));
    await tester.pump();

    expect(find.text('Registration Successful'), findsOneWidget);
  });

  testWidgets('Login form validation and submission', (WidgetTester tester) async {
    await tester.pumpWidget(MaterialApp(home: Scaffold(body: LoginForm())));

    // Try submitting empty form
    await tester.tap(find.text('Login'));
    await tester.pump();

    expect(find.text('Please enter your email'), findsOneWidget);
    expect(find.text('Please enter your password'), findsOneWidget);

    // Enter valid data
    await tester.enterText(find.byType(TextFormField).at(0), 'john@example.com');
    await tester.enterText(find.byType(TextFormField).at(1), 'password123');

    await tester.tap(find.text('Login'));
    await tester.pump();

    expect(find.text('Login Successful'), findsOneWidget);
  });
}
