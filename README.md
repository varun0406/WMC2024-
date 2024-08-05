# Epsilon Program Website

Welcome to the Epsilon Program website, an immersive and engaging experience inspired by the satirical Epsilon Program from the GTA V universe.

## Features

### Authentication
- **Login/Signup with Role-Based Access**: Users can sign up and log in with roles as either Admin or User. Supports Inserver and Google OAuth.

### Eye-catching Design
- **Thematic Colors and Symbols**: The website uses thematic colors, symbols, and images related to the Epsilon Program to create an immersive experience.

### Membership Tiers
- **Membership Levels**: Various levels of membership from basic to premium, each offering different benefits.
- **Purchase Memberships**: Users can purchase memberships according to their needs using virtual currency (Karma Points).

### Member Stories
- **Fake Testimonials**: Showcase testimonials and stories from current members, describing their positive experiences and personal growth.

### Admin Features
- **Post Events**: Admins can post events that are visible only to members.

### Event Listing and Registration
- **Members-Only Events**: Events are listed for members, who can register to attend.

### Donation Feature
- **Donate to the Program**: Users can make donations to support the program.
- **Total Donations**: The total accumulated donations are visible on the site.

### Virtual Currency
- **Earn and Spend Currency**: Users receive virtual currency to purchase memberships and make donations.

### Bonus Features
- **Personality Quiz**: A fun quiz to determine which Epsilon Program character or archetype the user aligns with.
- **Inquiry Form**: Users can ask questions through the inquiry form.
- **Interactive Map**: A map showing the locations of Epsilon Program centers and landmarks in Los Santos.

## URL Endpoints



## URL Endpoints

### Donation Stats
- **Leaderboard**: `/leaderboard/` - View the donation leaderboard.
- **Donaters Dashboard**: `/Donaters_Dashboard/<slug:slug>/` - View the dashboard for a specific donater.
- **Donation**: `/donation` - Make a donation.
- **Qdemo**: `/qdemo` - Demo for queries.


### Donation Stats
- **Leaderboard**: `/leaderboard/` - View the donation leaderboard.
- **Donaters Dashboard**: `/Donaters_Dashboard/<slug:slug>/` - View the dashboard for a specific donater.
- **Donation**: `/donation` - Make a donation.
- **Qdemo**: `/qdemo` - Demo for queries.

### Events
- **Admin Dashboard**: `/administ/` - Access the admin dashboard.
- **Edit Venue**: `/edit_venue/<int:venue_id>` - Edit a specific venue.
- **Delete Venue**: `/delete_venue/<int:venue_id>` - Delete a specific venue.
- **Edit Organization**: `/administ/edit_organization/<int:org_id>/` - Edit a specific organization.
- **Delete Organization**: `/administ/delete_organization/<int:org_id>/` - Delete a specific organization.
- **Edit Event**: `/administ/edit_event/<int:event_id>/` - Edit a specific event.
- **Delete Event**: `/administ/delete_event/<int:event_id>/` - Delete a specific event.
- **Query Details**: `/query/<int:query_id>/` - View details for a specific query.
- **Query Answered**: `/query/answered/<int:query_id>/` - Mark a query as answered.

### Login
- **Home**: `/` - Home page.
- **Profile**: `/profile` - User profile page.
- **Logout**: `/logout` - Logout from the account.
- **Create Profile**: `/Create_Profile` - Create a new profile.
- **About**: `/About` - About page.
- **Membership**: `/Membership` - Membership information.
- **Membership Tier**: `/member` - View and manage membership tiers.
- **Events**: `/Events` - View events.
- **Event Page**: `/Eventpage/<slug:slug>/` - View details for a specific event.
- **Membership Buy**: `/Membership_Buy` - Purchase a membership.
- **Testimonials**: `/Testimonials` - View member testimonials.
- **Review**: `/Review` - Submit a review.
- **Quiz**: `/Quiz` - Take the personality quiz.
- **Quiz Attempt**: `/Quiz/<int:quiz_id>/` - Attempt a specific quiz.
- **Map**: `/map/` - View the interactive map.
- **Ticket Detail**: `/ticket/<int:ticket_id>/` - View details for a specific ticket.
