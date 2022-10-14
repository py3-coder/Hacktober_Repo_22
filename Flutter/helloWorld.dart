import 'package:flutter/material.dart';
 
void main() {
  runApp(const Hello());
}
 
class Hello extends StatelessWidget {
  const Hello({Key? key}) : super(key: key);
 
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Center(child: Text('Hello World')),
    );
  }
}
