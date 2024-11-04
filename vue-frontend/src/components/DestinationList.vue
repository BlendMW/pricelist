<template>
    <div>
      <h1>Destinations</h1>
      <ul>
        <li v-for="destination in destinations" :key="destination.id">
          {{ destination.name }} 
          {{ destination.country }}
          {{ destination.description }}
          {{ destination.status }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        destinations: [] 
      };
    },
    mounted() {
      console.log("Component mounted. Attempting to fetch destinations data...");
  
      axios.get('http://localhost:8000/destination/')
        .then(response => {
          console.log("API request successful. Response data:", response.data); // Check if data is returned from API
          this.destinations = response.data;
          console.log("Destinations data assigned:", this.destinations); // Confirm assignment to destinations
        })
        .catch(error => {
          console.error("Error fetching destinations:", error); // Log any errors from the API request
        });
    }
  };
  </script>
  