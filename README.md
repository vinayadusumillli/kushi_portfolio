# Khushi Deshmukh - Portfolio Website

A modern, premium Django portfolio application for Khushi Deshmukh, Communications Professional specializing in Sports Management and Marketing.

## Features

- **Modern UI/UX**: Premium dark theme with orange accent colors and smooth animations
- **Responsive Design**: Fully responsive across all devices
- **Blog System**: Full-featured blog with Django admin integration
- **Contact Form**: Contact form with message storage in database
- **Portfolio Sections**:
  - Hero section with introduction
  - Professional journey timeline
  - Brands worked with showcase
  - Blog posts
  - Contact information

## Technology Stack

- **Backend**: Django 5.2.9
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Design**: Custom CSS with modern gradients and animations
- **Icons**: Font Awesome 6

## Installation & Setup

1. **Activate Virtual Environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Install Dependencies** (if not already installed):
   ```bash
   pip install django pillow
   ```

3. **Run Migrations** (already completed):
   ```bash
   python manage.py migrate
   ```

4. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   - Website: http://127.0.0.1:8000/
   - Django Admin: http://127.0.0.1:8000/admin/
   
## Django Admin Access

- **Username**: `admin`
- **Password**: `admin123`

Use the Django admin panel to:
- Add new blog posts
- Manage existing blogs
- View contact form submissions
- Manage all content

## Project Structure

```
website/
├── main/                   # Main Django app
│   ├── models.py          # Blog and Contact models
│   ├── views.py           # View functions
│   ├── admin.py           # Admin configurations
│   └── urls.py            # URL patterns
├── portfolio/             # Project settings
│   ├── settings.py        # Django settings
│   └── urls.py            # Main URL configuration
├── templates/main/        # HTML templates
│   ├── base.html          # Base template
│   ├── home.html          # Homepage
│   ├── blog_list.html     # Blog listing
│   ├── blog_detail.html   # Blog detail view
│   └── contact.html       # Contact form
├── static/                # Static files
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   └── images/            # Image assets
├── media/                 # User uploaded files
└── manage.py              # Django management script
```

## Features Details

### Blog Management
- Create, edit, and delete blog posts via Django admin
- Rich text content support
- Image uploads for blog posts
- Slug-based URLs for SEO
- Published/unpublished status
- Automatic timestamps

### Contact System
- Contact form with validation
- Messages stored in database
- Read/unread status tracking
- Email and subject fields
- Timestamp tracking

### Design Highlights
- **Color Scheme**: Dark theme with orange (#D65A31) primary color
- **Typography**: Inter font family
- **Animations**: Smooth scroll animations, hover effects, transitions
- **Layout**: CSS Grid and Flexbox for responsive layouts
- **Components**: Cards, buttons, forms with modern styling

## Adding New Content

### Adding a Blog Post

1. Go to http://127.0.0.1:8000/admin/
2. Log in with the admin credentials
3. Click on "Blogs" → "Add Blog"
4. Fill in:
   - Title (required)
   - Slug (auto-generated from title)
   - Content (required)
   - Excerpt (optional, for preview)
   - Image (optional)
   - Author (defaults to "Khushi Deshmukh")
   - Published status
5. Click "Save"

### Viewing Contact Messages

1. Go to http://127.0.0.1:8000/admin/
2. Click on "Contacts"
3. View all submitted messages
4. Mark as read/unread using the checkbox

## Customization

### Changing Colors
Edit `/static/css/style.css` and modify the CSS variables:
```css
:root {
    --primary-orange: #D65A31;
    --primary-dark: #1A2332;
    /* Add your custom colors */
}
```

### Updating Personal Information
Edit `/templates/main/home.html` to update:
- Journey timeline
- Brands worked with
- Social media links
- Contact information

## Sample Content

The application comes with 3 sample blog posts:
1. "The Rise of Women in Sports Communications"
2. "Behind the Scenes: IPL Social Media Strategy"
3. "Why Sports Management Education Matters"

You can edit or delete these from the Django admin panel.

## Development

To continue development:

1. Activate virtual environment: `source venv/bin/activate`
2. Make changes to code
3. Test locally: `python manage.py runserver`
4. Create migrations if models change: `python manage.py makemigrations`
5. Apply migrations: `python manage.py migrate`

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in settings.py
2. Update `ALLOWED_HOSTS` in settings.py
3. Configure proper database (PostgreSQL recommended)
4. Set up static file serving
5. Configure media file hosting
6. Use environment variables for sensitive data
7. Set up proper SECRET_KEY

## Support

For any issues or questions, please contact through the website contact form.

---

**Built with ❤️ using Django**
