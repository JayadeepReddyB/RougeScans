# RougeScans

**RougeScans** is a web-based manga reading platform that allows users to explore, read, and manage manga chapters with a user-friendly interface and admin capabilities.

---

## Features

-  **User Authentication**: Register, login, and manage secure sessions.
-  **Manga & Chapter Management**: Admins can add, update, or delete manga and their chapters.
-  **Chapter Viewer**: Smooth chapter viewing experience with previous/next navigation.
-  **Chapter Image Controls**: Add, edit, or delete images associated with each chapter.
-  **Responsive Design**: Clean layout with animations for buttons, cards, and form fields.
-  **Smart Fallbacks**: Shows “Coming Soon” or a video animation when chapters/images are unavailable.

---

## Tech Stack

- **Frontend**: HTML, CSS, Bootstrap, JavaScript  
- **Backend**: Django  
- **Database**: MySQL  
- **Media Handling**: Django `ImageField` with custom upload paths  
- **Payment Integration**: Razorpay (for donation support if enabled)

---

##  Preview Features

-  Image grid with hover effects  
-  Chapter cards with flip animations  
-  Focus glow for forms and bounce effect on button press  
-  Breadcrumb navigation for easy tracing  
-  Chapter dropdown for fast switching  
-  Staff-only admin actions for editing or deleting content

---

---

## Project Structure

- `urls.py` – URL routes for all major pages and actions  
- `admin.py` – Django admin panel registration for models  
- `chapter_details.html` – Dynamic chapter view page with navigation and fallback behavior  
- `addChapter.html`, `editChapterImage.html`, `delChapterImage.html` – Forms for CRUD operations  
- `base.html` / `index.html` – Base layout and navigation for the site  

---

## Highlights

- Fully functional admin dashboard for manga/chapter/image management  
- Custom form widgets for enhanced UX  
- Video fallback when no chapter images are uploaded  
- Separate flows for regular users and staff (admins)  
- Clean breadcrumb trail for easy site navigation  

---

## Author

Developed by [Jayadeep Reddy](https://github.com/JayadeepReddyB)


