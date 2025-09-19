<template>
    <div>
        <topbar />
    <div class="contact-page">
        <h1>Contact Us</h1>
        <form @submit.prevent="submitForm" class="contact-form">
            <div class="form-group">
                <label for="name">Name</label>
                <input v-model="form.name" type="text" id="name" required />
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input v-model="form.email" type="email" id="email" required />
            </div>
            <div class="form-group">
                <label for="subject">Subject</label>
                <input v-model="form.subject" type="text" id="subject" required />
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea v-model="form.message" id="message" rows="5" required></textarea>
            </div>
            <button type="submit">Send Message</button>
            <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
        </form>
        <div class="contact-info">
            <h2>Our Contact Information</h2>
            <ul>
                <li><strong>Email:</strong> info@bustracking.com</li>
                <li><strong>Phone:</strong> +1 234 567 890</li>
                <li><strong>Address:</strong> 123 Main St, City, Country</li>
            </ul>
        </div>
    </div>
    </div>
</template>

<script>
import topbar from '../components/topbar.vue';
import "../assets/css/contact.css";
export default {
    name: "contact",
    components: {
        topbar
    },
    data() {
        return {
            form: {
                name: "",
                email: "",
                subject: "",
                message: "",
            },
            successMessage: "",
        };
    },
    methods: {
        submitForm() {
            // Simulate form submission
            this.successMessage = "Thank you for contacting us! We will get back to you soon.";
            this.form = {
                name: "",
                email: "",
                subject: "",
                message: "",
            };
            setTimeout(() => {
                this.successMessage = "";
            }, 4000);
        },
    },
};
</script>

