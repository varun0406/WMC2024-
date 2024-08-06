# Epsilon Program Website

Welcome to the Epsilon Program website, an immersive and engaging experience inspired by the satirical Epsilon Program from the GTA V universe.
# Images 
![WhatsApp Image 2024-08-06 at 00 04 29_418ad436](https://github.com/user-attachments/assets/107fc05d-d1c6-44fe-b454-6fa2ed25ce3d)
-
![WhatsApp Image 2024-08-06 at 00 06 07_86ffa815](https://github.com/user-attachments/assets/38ffd63d-175e-45c9-b4ab-10d74019eb14)
-
![WhatsApp Image 2024-08-06 at 00 08 52_6b6aebf2](https://github.com/user-attachments/assets/8b7f5ec1-04c8-46ce-b474-af60bd839f48)
-
![WhatsApp Image 2024-08-06 at 00 09 43_587eed0d](https://github.com/user-attachments/assets/4a14f978-2624-4331-a85a-e6de639e8751)
-
![WhatsApp Image 2024-08-06 at 00 10 27_649f7e83](https://github.com/user-attachments/assets/d302c016-4ab1-4d4d-af18-7e44166794ac)
-
## Video Overview

Watch this video to get an overview of the Epsilon Program Website:
[![Epsilon Program Website Overview](https://img.youtube.com/vi/M5vFXCn9cjw/0.jpg)](https://www.youtube.com/watch?v=M5vFXCn9cjw)

## Features

### Authentication
- **Login/Signup with Role-Based Access**: Users can sign up and log in with roles as either Admin or User. Supports Inserver and Google OAuth.

### Eye-catching Design
- **Thematic Colors and Symbols**: The website uses thematic colors, symbols, and images related to the Epsilon Program to create an immersive experience.

### Membership Tiers
- **Membership Levels**: Various levels of membership from basic to premium, each offering different benefits.
- **Purchase Memberships**: Users can purchase memberships according to their needs using virtual currency (Karma Points).

### Member Stories
- **Live Testimonials**: Users have the option to submit testimonials, which are showcased live on the website, highlighting their positive experiences and personal growth.

### Admin Features
- **Event Management**: Admins can manage event data, including creating, deleting, and modifying events. They can set dynamic ticket prices and apply membership discounts to events, venues, and organizations.
- **User Interaction**: Admins can view and respond to user queries.
- **Quiz Management**: Admins have the capability to create quizzes and manage questions.

### Event Listing and Registration
- **Members-Only Events**: Events are listed for members, who can register to attend.

### Donation Feature
- **Donate to the Program**: Users can make donations to support the program.
- **Total Donations**: The total accumulated donations are visible on the site.

### Virtual Currency
- **Earn and Spend Currency**: Users receive virtual currency on making donations, which can be used in buying memberships.

### Bonus Features
- **Personality Quiz**: A fun quiz to encourage user on upliftment which can be directly created by Admin and user's will recieve karma points against it.
- **Inquiry Form**: Users can ask questions through the inquiry form, Admin can see and answer them from its Dashboard.
- **Interactive Map**: A map showing the locations of Epsilon Program centers and landmarks.

## URL Endpoints

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

## Project Setup

#### 1. Clone the repository:
```bash
git clone https://github.com/varun0406/WMC2024-.git
pip install -r requirements.txt
python manage.py runserver

```
Open your web browser and navigate to http://127.0.0.1:8000
# Admin Credentials
Email id :- epsilon@gmail.com


Password :-Epsilon@123
