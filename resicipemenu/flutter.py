import 'package:flutter/material.dart';

void main() {
 runApp(MyApp());
}

class MyApp extends StatelessWidget {
 @override
 Widget build(BuildContext context) {
   return MaterialApp(
     title: 'New Recipe',
     home: NewRecipePage(),
   );
 }
}

class NewRecipePage extends StatefulWidget {
 @override
 _NewRecipePageState createState() => _NewRecipePageState();
}

class _NewRecipePageState extends State<NewRecipePage> {
 final _formKey = GlobalKey<FormState>();
 final _recipeNameController = TextEditingController();
 final _descriptionController = TextEditingController();
 final _cookingTimeController = TextEditingController();
 final _stepsController = TextEditingController();

 @override
 Widget build(BuildContext context) {
   return Scaffold(
     appBar: AppBar(
       title: Text('NEW RECIPE'),
       centerTitle: true,
       actions: [
          TextButton(
            onPressed: () {},
            child: const Text(
              'Close',
              style: TextStyle(
                  color: Colors.red, fontSize: 15, fontWeight: FontWeight.w500),
            ),
          )
        ],
     ),
     body: Padding(
       padding: const EdgeInsets.all(16.0),
       child: Form(
         key: _formKey,
         child: Column(
           crossAxisAlignment: CrossAxisAlignment.start,
           children: [
             Container(
              color: Colors.red,
               child: Text(
                 'Super Cool you are creating a new recipe Let\'s get started',
                 style: TextStyle(color: Colors.white),
               ),
             ),
             SizedBox(height: 16.0),
             TextFormField(
               controller: _recipeNameController,
               decoration: InputDecoration(
                 labelText: 'Give your a recipe a name',
                 hintText: 'Enter your a recipe name',
               ),
               validator: (value) {
                 if (value!.isEmpty) {
                   return 'Please enter a recipe name';
                 }
                 return null;
               },
             ),
             SizedBox(height: 16.0),
             TextFormField(
               controller: _descriptionController,
               decoration: InputDecoration(
                 labelText: 'Cooking a time (min)',
                 hintText: 'Enter a your cooking time',
               ),
               validator: (value) {
                 if (value!.isEmpty) {
                   return 'Please enter a cooking time';
                 }
                 return null;
               },
             ),
             SizedBox(height: 16.0),
             TextFormField(
               controller: _cookingTimeController,
               decoration: InputDecoration(
                 labelText: 'Description',
                 hintText: 'Enter the Description',
               ),
               validator: (value) {
                 if (value!.isEmpty) {
                   return 'Please enter the Description';
                 }
                 return null;
               },
             ),
             SizedBox(height: 16.0),
             TextFormField(
               controller: _stepsController,
               decoration: InputDecoration(
                 labelText: 'Recipe Ingredients & Steps',
                 hintText: 'Enter the steps & recipe',
               ),
               validator: (value) {
                 if (value!.isEmpty) {
                   return 'Please enter the steps & recipe';
                 }
                 return null;
               },
             ),
             SizedBox(height: 32.0),
             ElevatedButton(
              
               style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.red, minimumSize: Size(1500, 50)),
               onPressed: () {
                 if (_formKey.currentState!.validate()) {
                   // Add code to save the recipe
                   print('Recipe Name: ${_recipeNameController.text}');
                   print('Description: ${_descriptionController.text}');
                   print('Cooking Time: ${_cookingTimeController.text}');
                   print('Steps: ${_stepsController.text}');
                 }
               },
               child: const Text('Add Menu',style: TextStyle(color: Colors.white),),
             ),
           ],
         ),
       ),
     ),
   );
 }

 @override
 void dispose() {
   _recipeNameController.dispose();
   _descriptionController.dispose();
   _cookingTimeController.dispose();
   _stepsController.dispose();
   super.dispose();
 }
}
