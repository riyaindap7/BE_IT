// Define AngularJS module
var app = angular.module("libraryApp", []);


// Define a controller
app.controller("LibraryController", function($scope) {
    // Book data array
    $scope.books = [
        { name: "To Kill a Mockingbird", number: "B001", genre: "Fiction", author: "Harper Lee" },
        { name: "1984", number: "B002", genre: "Dystopian", author: "George Orwell" },
        { name: "Moby-Dick", number: "B003", genre: "Adventure", author: "Herman Melville" },
        { name: "The Great Gatsby", number: "B004", genre: "Classic", author: "F. Scott Fitzgerald" },
    ];
});
