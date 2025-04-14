# GlitchString Theme for Micro.blog

This guide will help you implement the custom GlitchString theme on your Micro.blog site.

## Step 1: Prepare Your Theme Files

First, you'll need to organize your theme files in the structure shown below:

```
glitchstring/
├── layouts/
│   ├── _default/
│   │   ├── baseof.html
│   │   ├── list.html
│   │   └── single.html
│   ├── index.html
│   └── partials/
│       ├── footer.html
│       ├── head.html
│       └── header.html
└── static/
    ├── css/
    │   └── style.css
    └── images/
        ├── avatar.png  (Your cartoon avatar)
        ├── banner.png  (Your header background)
        └── r_background.png (Your circuit pattern background)
```

## Step 2: Upload Your Images

You'll need to make sure your images are available:

1. The cartoon avatar with headphones and glasses (as shown in Image 1)
2. A banner image for the header background
3. The circuit board pattern background (as shown in Image 2)

Rename these files to match what's referenced in the CSS:
- avatar.png
- banner.png 
- r_background.png

## Step 3: Implement on Micro.blog

Micro.blog supports custom themes through its plugin system. Here's how to add your theme:

1. Log in to your Micro.blog account
2. Go to Design → Edit Custom Themes
3. Create a new theme named "GlitchString"
4. Upload each of the HTML, CSS and image files to their respective locations
5. Save your theme

Alternatively, you can use the Micro.blog plugin system:

1. Create a zip file of your theme directory
2. Go to Plug-ins in your Micro.blog dashboard
3. Click "Upload a plug-in"
4. Upload your zip file
5. Activate the theme

## Step 4: Configure Your Site

Update your site configuration to match the provided config.toml example. In Micro.blog:

1. Go to Posts → Categories and make sure you have the necessary categories set up
2. Go to Design → Edit Custom Themes
3. Add any custom parameters needed in the theme settings

## Step 5: Customize Content

Update your bio and sections content to match your personal information. The theme uses these parameters:

- `avatar`: Path to your avatar image
- `bio`: Your personal bio with line breaks
- `sections`: Your featured content sections with emoji icons

## Troubleshooting

- If images are not displaying, check the paths in your CSS and HTML files
- For the glitch animation to work properly, make sure your header h1 element has the data-text attribute set with your site name

## Customization

You can further customize the theme by:

- Adjusting colors in the CSS (primary colors are #00ffff and #ff00ff)
- Changing animation timing and effects
- Adding more sections or custom content areas
- Adjusting the responsive breakpoints for different devices

Enjoy your new cyberpunk-themed blog!
