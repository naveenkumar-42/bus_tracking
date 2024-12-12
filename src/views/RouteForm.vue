<template>
  <div class = "main">
    <div class="route-form">
      <topbar />
      <h1>Select Your Route</h1>
      <form @submit.prevent="handleSearch">
        <div>
          <label for="source">Source:</label>
          <select id="source" v-model="selectedSource" @change="handleSearch">
            <option value="" disabled>Select a source</option>
            <option v-for="source in sourceOptions" :key="source" :value="source">
              {{ source }}
            </option>
          </select>
        </div>

        <div>
          <label for="destination">Destination:</label>
          <select id="destination" v-model="selectedDestination" @change="handleSearch">
            <option value="" disabled>Select a destination</option>
            <option v-for="destination in destinationOptions" :key="destination" :value="destination">
              {{ destination }}
            </option>
          </select>
        </div>

        <button type="submit">Search Buses</button>
      </form>
    </div>

    <div v-if="Object.keys(groupedSchedules).length > 0" class="schedule-container">
      <h2>Bus Schedules</h2>
      <div class="bus-grid">
        <!-- Loop through the grouped schedules and show only the highlighted ones -->
        <div v-for="(schedule, busId) in groupedSchedules" :key="busId" class="bus-container">
          <h3>Bus ID: {{ busId }}</h3>
          <table>
            <thead>
              <tr>
                <th>Stop Sequence</th>
                <th>Stop Name</th>
                <th>Arrival Time</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(stop, index) in schedule"
                :key="index"
                :class="{
                  'highlight-source': stop.stop_name === selectedSource,
                  'highlight-destination': stop.stop_name === selectedDestination
                }"
              >
                <td>{{ stop.stop_sequence }}</td>
                <td>{{ stop.stop_name }}</td>
                <td>{{ stop.arrival_time }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import Papa from "papaparse";
import topbar from "../components/topbar.vue";


export default {
  name: "RouteForm",
  components: {
     
     topbar
    
   },
  data() {
    return {
      routes: [],
      selectedSource: "",
      selectedDestination: "",
      sourceOptions: [],
      destinationOptions: [],
      selectedSchedule: [],
      groupedSchedules: {}, // New object to hold the grouped schedules by bus_id
    };
  },
  methods: {
  fetchRoutes() {
    const csvUrl = "/final.csv";
    console.log("Fetching CSV data from:", csvUrl);

    Papa.parse(csvUrl, {
      download: true,
      header: true,
      complete: (results) => {
        console.log("Parsing complete:", results.data);
        const data = results.data.filter((row) => row.route_id);

        // Group data by route_id
        const groupedRoutes = data.reduce((acc, row) => {
          if (!acc[row.route_id]) {
            acc[row.route_id] = { route_id: row.route_id, stops: [] };
          }

          if (!acc[row.route_id].stops.some((stop) => stop.stop_name === row.stop_name)) {
            acc[row.route_id].stops.push({
              stop_sequence: parseInt(row.stop_sequence),
              stop_name: row.stop_name,
              arrival_time: row.arrival_time,
              bus_id: row.bus_name,
            });
          }

          return acc;
        }, {});

        // Map the grouped routes
        this.routes = Object.values(groupedRoutes).map((route) => {
          const sortedStops = route.stops.sort((a, b) => a.stop_sequence - b.stop_sequence);
          return {
            route_id: route.route_id,
            schedule: sortedStops,
            stops: sortedStops.map((stop) => stop.stop_name),
          };
        });

        // Populate source and destination options
        const allStops = data.map((row) => row.stop_name);
        this.sourceOptions = [...new Set(allStops)];
        this.destinationOptions = [...new Set(allStops)];
      },
    });
  },

  handleSearch() {
    if (!this.selectedSource || !this.selectedDestination) {
      this.selectedSchedule = [];
      return;
    }

    // Filter routes that include both source and destination
    const matchingRoutes = this.routes.filter((route) => {
      const sourceIndex = route.stops.indexOf(this.selectedSource);
      const destinationIndex = route.stops.indexOf(this.selectedDestination);
      return sourceIndex !== -1 && destinationIndex !== -1 && sourceIndex < destinationIndex;
    });

    // Group stops by bus_id and filter for highlighted schedules
    const groupedSchedules = matchingRoutes.flatMap((route) => {
      return route.schedule
        .filter((stop, index, arr) => {
          const sourceIndex = arr.findIndex((s) => s.stop_name === this.selectedSource);
          const destinationIndex = arr.findIndex((s) => s.stop_name === this.selectedDestination);
          return (
            index >= sourceIndex &&
            index <= destinationIndex &&
            sourceIndex < destinationIndex
          );
        })
        .reduce((acc, stop) => {
          if (!acc[stop.bus_id]) {
            acc[stop.bus_id] = [];
          }
          acc[stop.bus_id].push(stop);
          return acc;
        }, {});
    });

    // Flatten the grouped schedules by bus_id
    this.groupedSchedules = groupedSchedules.reduce((acc, curr) => {
      for (const busId in curr) {
        if (!acc[busId]) {
          acc[busId] = [];
        }
        acc[busId] = acc[busId].concat(curr[busId]);
      }
      return acc;
    }, {});

    console.log("Grouped bus schedules:", this.groupedSchedules);
  },
},



  mounted() {
    this.fetchRoutes();
  },
};
</script>
<style scoped>

.main {
 
  background-size: cover; /* Ensures the image covers the entire viewport */
  background-position: center; /* Center the image */
  background-repeat: no-repeat; /* Prevent repetition */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 50px;
  overflow: auto; /* Allow internal scrolling if content overflows */
  padding: 1rem; /* Add padding for better spacing */
}

.route-form {
  margin-top:60px;
  width: 90%;
  max-width: 600px; /* Limit maximum width */
  margin: 0 auto; /* Centered */
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 12px;
  background-color: #9edfe3;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.route-form h1 {
  text-align: center;
  color: #333;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.route-form select {
  width: 100%;
  padding: 0.7rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.route-form button {
  display: block;
  width: 100%;
  padding: 0.8rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s, transform 0.2s;
}

.schedule-container {
  color: #333;
  margin-top: 2rem;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #9edfe3;
  max-width: 100%;
  max-height: 80vh; /* Restrict height for better alignment */
  overflow-y: auto; /* Enable scrolling for long content */
  overflow-y: auto;
  overflow-x: hidden;
  box-sizing: border-box;
  -ms-overflow-style: none;
}
::-webkit-scrollbar {
  display: none; /* Hide scrollbar */
}
.bus-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}

.bus-container {
  flex: 1 1 calc(100% - 2rem);
  max-width: 100%;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 1rem;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.schedule-container table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.schedule-container th,
.schedule-container td {
  padding: 0.6rem;
  border: 1px solid #ddd;
  text-align: left;
}

.schedule-container th {
  background-color: #f4f4f4;
}

.schedule-container tr:nth-child(even) {
  background-color: #f9f9f9;
}

.schedule-container tr:hover {
  background-color: #e9e9e9;
}

.highlight-source {
  background-color: #d1e7dd;
  font-weight: bold;
  color: #0f5132;
}

.highlight-destination {
  background-color: #f8d7da;
  font-weight: bold;
  color: #842029;
}

@media (max-width: 480px) {
  .route-form {
    margin-top: 60px;
    padding: 1rem;
  }

  .route-form h1 {
    font-size: 1.3rem;
  }

  .route-form button {
    font-size: 0.9rem;
  }

  .bus-container {
    flex: 1 1 100%;
  }

  .schedule-container table {
    font-size: 0.8rem;
  }
}

</style>
