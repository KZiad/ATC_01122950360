# Ehgz
Ehgz is a full-stack event booking system that allows users to browse and book
events, manage their bookings, and provide an integrated web-based admin panel for event
management.
<h1>📍 Requirements</h1>

<h2>🌍 Frontend</h2>

<h3>🔐 Authentication</h3>

- [x] Users can register and log in.
- [x] The "Forgot Password" functionality is not required.
<h3>🏠 Home Page (Event Listings)</h3>

- [x] Display events using a grid or flexbox layout.
- [x] Events that a user has already booked will show a "Booked" label instead of the "Book
Now" button.
- [x] Each event card includes a "Book Now" button (if not yet booked).
<h3>📄 Event Details Page</h3>

- [ ] Shows full event information:
  -  Event Name, Description, Category, Date, Venue, Price, and Image
- [x] Includes a "Book Now" button (books 1 ticket per click for user)
- [ ] Upon booking, the user is redirected to a Congratulations screen.
- [x] No payment integration is required.
<h3>🧾 Admin Panel</h3>

- [ ] Admin can Create, Read, Update, and Delete events.
- [ ] The admin panel is a separate screen within the same web application.
- [x] User roles are needed (Admin, User).
<h2>🛠 Backend</h2>
<h3>Basic Features:</h3>

- [x] Authentication
- [x] Event Management API (Done through django admin)
- [x] Booking API
<h3>🎯 Optional Enhancements (Nice To Have)</h3>

- [x] Role-based permissions
- [x] Tags and categories for events
- [x] Event image upload functionality (Done through django admin)
- [ ] Pagination or lazy loading
- [x] Responsive design
<h3>🚀 Bonus Features (For Super Heros)</h3>

- [ ] Backend deployment (e.g., on Render, Vercel, or Heroku)
- [ ] Multi-language support (Ex: English - Arabic)
- [ ] Unit testing
- [ ] Dark mode support
