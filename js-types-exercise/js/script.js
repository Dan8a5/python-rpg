function exercise1() {
    // Declare and instantiate a number and return it
    const number = 1;
    return number;
  }
  
  function exercise2() {
    // Declare and instantiate a floating point number that is not a whole number and return it
    const float = 3.14;
    return float;
  }
  
  function exercise3() {
    // Declare and instantiate a string "Hello World!" and return it
    const hello = "Hello World!";
    return hello;
  }
  
  function exercise4() {
    // Declare and instantiate an array containing the string "Hello World!" and the number 4 and return it
    const mixedArray = ["Hello World!", 4];
    return mixedArray;
  }
  
  function exercise5() {
    // Declare and instantiate an object containing the key-value pairs key1 -> "Hello World!" and key2 -> 4, and return it
    const mixedObject = {
      key1: "Hello World!",
      key2: 4
    };
    return mixedObject;
  }
  
  function exercise6() {
    // Declare and instantiate a boolean value 'false' and return it
    const boolean = false;
    return boolean;
  }
  
  console.log('This should be a number:', exercise1());
  console.log('This should be a floating point number:', exercise2());
  console.log('This should be a string saying "Hello World":', exercise3());
  console.log('This should be an array that includes a string, "Hello World," and a number 4:', exercise4());
  console.log('This should be an object that has key-value pairs, key1 -> "Hello World" and key2 -> 4:', exercise5());
  console.log("This should be a boolean value that returns 'false':", exercise6());