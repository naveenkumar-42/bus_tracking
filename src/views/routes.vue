<template>
  <div>
    <topbar />
    <div class="container">
      <h1>Bus Stops Finder</h1>

      <div class="input-box">
        <label for="routeId">Enter Route ID:</label>
        <input type="number" v-model="routeId" id="routeId" placeholder="Enter route ID" />
        <button @click="fetchStops">Get Stops</button>
      </div>

      <div v-if="loading" class="loading">Loading...</div>

      <div v-if="error" class="error">{{ error }}</div>

      <div v-if="stops.length">
        <h2>Stops for Route ID: {{ routeId }}</h2>
        <div id="map" class="map-container"></div>


        <div class="stops-line">
          <div v-for="(stop, index) in stops" :key="stop.stop_id" class="stop-item">
            <div class="line-connector">
              <div class="dot"></div>
            </div>
            <div class="stop-info">
              <span class="stop-name">{{ stop.stop_name }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import topbar from "../components/topbar.vue";

export default {
  components: {
    topbar
  },
  data() {
    return {
      routeId: null, 
      stops: [], 
      loading: false, 
      error: "", 
      map: null, 
      markers: [], 
      polyline: null, 
    };
  },
  methods: {
    async fetchStops() {
      
      this.error = "";
      this.stops = [];
      if (!this.routeId) {
        this.error = "Please enter a valid route ID.";
        return;
      }

      this.loading = true;
      try {
        
        const response = await axios.get(
          `https://gtfs-7908.onrender.com/api/stops`,
          { params: { route_id: this.routeId } }
        );
        this.stops = response.data;

        
        this.$nextTick(() => {
          this.plotStopsOnMap();
        });
      } catch (err) {
        this.error = err.response?.data?.error || "An error occurred while fetching stops.";
      } finally {
        this.loading = false;
      }
    },

    initializeMap() {
      
      if (!this.map) {
        this.map = L.map("map").setView([28.6139, 77.209], 12); 

        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        }).addTo(this.map);
      }
    },

    plotStopsOnMap() {
      this.initializeMap();

      
      if (this.markers.length) {
        this.markers.forEach((marker) => this.map.removeLayer(marker));
        this.markers = [];
      }
      if (this.polyline) {
        this.map.removeLayer(this.polyline);
      }

      const customIcon = L.icon({
        iconUrl: "/bus.png", 
        iconSize: [18, 18], 
        iconAnchor: [8, 16], 
        popupAnchor: [0, -16], 
      });

      
      const coordinates = [];
      this.stops.forEach((stop) => {
        const marker = L.marker([stop.stop_lat, stop.stop_lon], { icon: customIcon }).addTo(this.map);
        marker.bindPopup(`<strong>${stop.stop_name}</strong><br>ID: ${stop.stop_id}`);
        this.markers.push(marker);
        coordinates.push([stop.stop_lat, stop.stop_lon]);
      });

      
      if (coordinates.length) {
        this.polyline = L.polyline(coordinates, { color: "blue" }).addTo(this.map);
        this.map.fitBounds(this.polyline.getBounds());
      }
    },
  },
};
</script>

<style scoped>
body {
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
  color: #333;
  background-color: #E0F7FA; 
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  margin-top: 70px;
  border-radius: 5px;
  background-color: #9edfe3; 
}

h1 {
  font-size: 2.5em;
  margin-top: 20px;
  text-align: center;
  color: black; 
}

h2 {
  font-size: 1.8em;
  margin-bottom: 15px;
  text-align: center;
  color: black;
}

.input-box {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  margin: 20px auto;
  text-align: center;
}

label {
  font-weight: bold;
  display: block;
  margin-bottom: 8px;
  color: #555;
}

input[type="number"] {
  width: 100%;
  padding: 10px;
  border: 2px solid #ccc;
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.3s ease;
  outline: none;
  max-width: 250px ;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
}

input[type="number"]:focus {
  border-color: #007BFF;
  box-shadow: 0 0 8px rgba(0, 123, 255, 0.3);
}

button {
  background-color: #007BFF;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  margin-top: 10px;
}

button:hover {
  background-color: #0056b3;
  transform: translateY(-2px);
}

.loading {
  text-align: center;
  font-size: 18px;
  color: #666;
  margin: 20px 0;
}

.error {
  text-align: center;
  color: #d9534f;
  font-weight: bold;
  margin-top: 10px;
  padding: 10px;
  background-color: #f2dede;
  border: 1px solid #ebccd1;
  border-radius: 8px;
}

.map-container {
  width: 90%;
  max-width: 1000px;
  height: 400px;
  margin: 20px auto;
  border:#ccc 3px;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.stops-line {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin: 20px auto;
  padding: 0 15px;
  max-width: 600px;
  max-height: 400px; 
  overflow-y: auto; 
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.stop-item {
  display: flex;
  align-items: center;
  position: relative;
  padding: 20px 0;
  margin-left: 20px;
}

.line-connector {
  position: absolute;
  left: -20px;
  top: 0;
  bottom: 0;
  width: 2px; 
  background-color: #007BFF;
  z-index: 1;
}

.dot {
  position: absolute;
  left: -6px;
  top: 50%;
  transform: translateY(-50%);
  width: 12px;
  height: 12px;
  background-color: #fff;
  border: 3px solid #007BFF;
  border-radius: 50%;
  z-index: 2;
}

.stop-info {
  padding-left: 20px;
  display: flex;
  flex-direction: column;
}

.stop-name {
  font-size: 16px;
  font-weight: bold;
  color: #333;
}

.stop-id {
  font-size: 12px;
  color: #555;
}


@media (max-width: 768px) {
  .map-container {
    height: 400px;
  }

  .stops-line {
    max-width: 100%;
  }
}
</style>