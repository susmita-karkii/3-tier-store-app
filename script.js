function buy() {
      var firstName = document.getElementById("firstNameInput").value;
      var familyName = document.getElementById("familyNameInput").value;
      var productName = document.getElementById("productNameInput").value;

      // Send an AJAX request to insert the data into the database
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/buy", true);
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
          // Handle the response from the server
          var response = JSON.parse(xhr.responseText);
          // Update the UI or perform any other actions
        }
      };
      var data = JSON.stringify({
        firstName: firstName,
        familyName: familyName,
        productName: productName
      });
      xhr.send(data);
    }

    function show() {
      // Send an AJAX request to retrieve the list of items
      var xhr = new XMLHttpRequest();
      xhr.open("GET", "/show", true);
      xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
          // Handle the response from the server
          var response = JSON.parse(xhr.responseText);
          // Update the UI or perform any other actions
        }
      };
      xhr.send();
    }

    function purchaseHistory() {
      var fullName = document.getElementById("fullNameInput").value;

      // Send an AJAX request to retrieve the purchase history
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/purchaseHistory", true);
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
          // Handle the response from the server
          var response = JSON.parse(xhr.responseText);
          // Update the UI or perform any other actions
        }
      };
      var data = JSON.stringify({ fullName: fullName });
      xhr.send(data);
    }
