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
  
  export default {
    name: "AboutUs",
    components: {
      topbar,
    },
  };
  </script>
  
  <style scoped>
  .about-us {
    /* font-family: Arial, sans-serif; */
    line-height: 1.6;
    color: #333;
    padding: 2rem;
    margin-right: 20px;
    margin-top: 70px;
    margin: 0 auto;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width:100%;
  }
  .main{
    margin-top: 80px;
    max-width: 370px;

  }
  
  .header {
    text-align: center;
    padding: 10px;
    margin-bottom: 3rem;
    margin-left: 25px;
    background-color: #A0C7C9;
  }
  
  .header h1 {
    font-size: 2.5rem;
    color: black;
    font-weight: bold;
  }
  
  .header p {
    font-size: 1.2rem;
    color: whitesmoke;
  }
  
  .content {
    display: flex;
    flex-direction: column;
    gap: 3rem;
  }
  
  .history, .services, .mission, .contact {
    position: relative;
    padding-left: 2.5rem;
  }
  
  .history::before, .services::before, .mission::before, .contact::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
    background-color: black;
  }
  
  h2 {
    font-size: 1.8rem;
    color: black;
    margin-bottom: 1rem;
    position: relative;
  }
  
  h2::after {
    content: "";
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 50px;
    height: 3px;
    background-color: black;
  }
  
  ul {
    list-style-type: none;
    padding-left: 0;
  }
  
  ul li {
    margin-bottom: 0.5rem;
    padding-left: 1.5rem;
    position: relative;
  }
  
  ul li::before {
    content: "\2022";
    color: black;
    font-weight: bold;
    position: absolute;
    left: 0;
  }
  
  .contact p {
    font-size: 1rem;
    color: #555;
  }
  
  strong {
    color: #000;
  }
  
  @media (max-width: 768px) {
    .about-us {
      padding: 1rem;
    }
  
    .header h1 {
      font-size: 2rem;
    }
  
    h2 {
      font-size: 1.5rem;
    }
  
    p, li {
      font-size: 0.9rem;
    }
  }
  </style>
  