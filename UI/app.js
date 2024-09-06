document.getElementById("priceForm").addEventListener("submit", async function (e) {
   e.preventDefault();

   // Get values from the form
   const bed = document.getElementById("bed").value;
   const bath = document.getElementById("bath").value;
   const acre_lot = document.getElementById("acre_lot").value;
   const house_size = document.getElementById("house_size").value;

   // Basic validation to check if all fields are filled
   if (!bed || !bath || !acre_lot || !house_size) {
       alert("Please fill in all fields.");
       return;
   }

   // Ensure values are numbers and handle potential conversion issues
   const bedNum = parseFloat(bed);
   const bathNum = parseFloat(bath);
   const acreLotNum = parseFloat(acre_lot);
   const houseSizeNum = parseFloat(house_size);

   if (isNaN(bedNum) || isNaN(bathNum) || isNaN(acreLotNum) || isNaN(houseSizeNum)) {
       alert("Please enter valid numbers.");
       return;
   }

   // Make the request to the server
   try {
       const response = await fetch("http://127.0.0.1:5000/predict_price", {
           method: "POST",
           headers: {
               "Content-Type": "application/json",
           },
           body: JSON.stringify({
               bed: bedNum,
               bath: bathNum,
               acre_lot: acreLotNum,
               house_size: houseSizeNum,
           }),
       });

       // Check if the response is ok
       if (!response.ok) {
           throw new Error("Network response was not ok.");
       }

       // Parse the JSON response
       const data = await response.json();

       // Check if the response contains the estimated price
       if (data.estimated_price === undefined) {
           throw new Error("Invalid response from the server.");
       }

       // Display the estimated price
       document.getElementById("estimatedPrice").textContent = `$${data.estimated_price.toFixed(2)}`;

   } catch (error) {
       // Handle any errors that occurred during the fetch operation
       console.error("Error fetching the price:", error);
       alert("There was an error while predicting the price. Please try again.");
   }
});


