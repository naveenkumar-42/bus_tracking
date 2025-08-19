<template>
  <div class="topbar">
    <div class="logo-container">
      <img src="../assets/dlc.logo.png" alt="DTC Logo" class="topbar-logo" />
      <h1 class="topbar-title">Delhi Transport Corporation</h1>
    </div>

    <!-- Hamburger Icon -->
    <div class="hamburger" @click="toggleMenu">
      <span></span>
      <span></span>
      <span></span>
    </div>

    <!-- Navigation Menu -->
    <nav :class="['menu', { show: isMenuOpen }]">
      <a
        v-for="item in menuItems"
        :key="item.text"
        @click="$router.push(item.route)"
      >
        {{ item.text }}
      </a>
    </nav>
  </div>
</template>

<script>
export default {
  name: "TopBar",
  data() {
    return {
      isMenuOpen: false,
      menuItems: [
        { text: "HOME", route: "/" },
        { text: "ABOUT US", route: "/aboutus" },
        { text: "SEARCH", route: "/routes" },
        { text: "CONTACT US", route: "/contact-us" },
      ],
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
};
</script>

<style scoped>
.topbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 70px;
  background: #9edfe3;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 30px;
  box-shadow: 0 2px 8px rgba(99, 99, 99, 0.2);
  z-index: 1000;
  font-family: Arial, sans-serif;
}

.logo-container {
  display: flex;
  align-items: center;
  gap: 20px;
}

.topbar-logo {
  height: 30px;
  width: 40px;
}

.topbar-title {
  font-size: 20px;
  font-weight: bold;
  color: black;
  margin: 0;
}

.menu {
  display: flex;
  gap: 20px;
}

.menu a {
  text-decoration: none;
  font-size: 14px;
  font-weight: bold;
  color: black;
  padding: 5px 10px;
  border-radius: 5px;
  transition: background 0.3s;
}

.menu a:hover {
  background: #a0c7c9;
}

/* Hamburger Icon */
.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  width: 25px;
  cursor: pointer;
}

.hamburger span {
  height: 3px;
  background: black;
  border-radius: 2px;
}

/* Mobile View */
@media (max-width: 800px) {
  .menu {
    display: none;
    flex-direction: column;
    position: absolute;
    top: 70px;
    left: 0;
    width: 100%;
    background: #a0c7c9;
    box-shadow: 0 4px 8px rgba(99, 99, 99, 0.2);
    padding: 20px;
  }

  .menu.show {
    display: flex;
  }

  .hamburger {
    display: flex;
  }

  .topbar-title {
    font-size: 18px;
  }

  .topbar {
    padding: 0 15px;
  }
}
</style>
