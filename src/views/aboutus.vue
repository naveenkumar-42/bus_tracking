<template>
    <div class="about-us">
      <div class="topbar">
        <topbar />
      </div>
      <div class="main">
      <section class="header">
        <h1>About Delhi Transport Corporation</h1>
        <p>Serving the capital city with reliable and efficient transportation since its inception.</p>
      </section>
  
      <section class="content">
        <div class="history">
          <h2>Our History</h2>
          <p>
            Established in May 1948, Delhi Transport Corporation (DTC) is a public transportation provider in Delhi, operating the world's largest eco-friendly CNG fleet. 
            With a focus on sustainable mobility, DTC has played a vital role in connecting the people of Delhi and neighboring areas.
          </p>
        </div>
  
        <div class="services">
          <h2>Our Services</h2>
          <ol>
            <li>Comprehensive bus routes covering Delhi and NCR.</li>
            <li>Eco-friendly buses running on CNG to ensure a sustainable environment.</li>
            <li>Special services for school students, office commuters, and tourists.</li>
            <li>Online and offline ticketing facilities for passenger convenience.</li>
          </ol>
        </div>
  
        <div class="mission">
          <h2>Our Mission</h2>
          <p>
            To provide safe, reliable, and affordable transportation services while minimizing environmental impact. We aim to enhance commuter experiences by constantly improving our services and embracing innovative technologies.
          </p>
        </div>
  
        <div class="contact">
          <h2>Contact Us</h2>
          <p>
            <strong>Address:</strong> BIT <br>
            <strong>Email:</strong> naveenkumarpoff@gmail.com <br>
            <strong>Phone:</strong> +91-1234567890 <br>
          </p>
        </div>
      </section>
      </div>
    </div>
  </template>
  
  <script>
  import topbar from "../components/topbar.vue";
  import '../assets/css/about.css';

  export default {
    name: "AboutUs",
    components: {
      topbar,
    },
  };
  </script>

  