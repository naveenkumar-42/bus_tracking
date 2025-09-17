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
import "../assets/css/routesform.css";


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
      groupedSchedules: {},
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

       
        this.routes = Object.values(groupedRoutes).map((route) => {
          const sortedStops = route.stops.sort((a, b) => a.stop_sequence - b.stop_sequence);
          return {
            route_id: route.route_id,
            schedule: sortedStops,
            stops: sortedStops.map((stop) => stop.stop_name),
          };
        });

       
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

   
    const matchingRoutes = this.routes.filter((route) => {
      const sourceIndex = route.stops.indexOf(this.selectedSource);
      const destinationIndex = route.stops.indexOf(this.selectedDestination);
      return sourceIndex !== -1 && destinationIndex !== -1 && sourceIndex < destinationIndex;
    });

   
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