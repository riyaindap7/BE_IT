const mongoose = require("mongoose");
const userSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: [true, "Name is required"],
    },
    email: {
      type: String,
      required: [true, "Email is required"],
      match: [/\S+@\S+\.\S+/, "Email is invalid"],
      unique: true,
    },
    password: {
      type: String,
      required: [true, "Password is required"],
      minlength: [6, "Password must be at least 6 characters"],
    },
    age: {
      type: Number,
      min: [0, "Age must be a positive number"],
      max: [120, "Age must be realistic"],
    },
  },
  { timestamps: true }
);
module.exports = mongoose.model("User", userSchema);
