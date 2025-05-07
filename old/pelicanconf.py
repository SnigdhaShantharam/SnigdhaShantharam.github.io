# Pelican configuration settings
AUTHOR = 'Snigdha S.'
SITENAME = 'Snigdha S. | Software Engineer'
SITEURL = 'https://snigdha.github.io'
SITEDESCRIPTION = 'Design-minded back-end software engineer focused on building beautiful interfaces and experiences.'

# # Path to the content directory (you can leave this empty or point to a specific folder for dynamic content)
# PATH = 'content'  # Assuming no dynamic content (you can use markdown for posts if needed)

# # Output path for generated HTML files
# OUTPUT_PATH = 'output/'

# THEME='themes/custom'

# READER={'html':None}

# # Feed settings (RSS feeds)
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
# TRANSLATION_FEED_ATOM = None

# # Timezone settings
# TIMEZONE = 'UTC'

# # Default language
# DEFAULT_LANG = 'en'

# # Date format settings
# DEFAULT_DATE_FORMAT = '%B %d, %Y'
# DATE_FORMAT = '%Y-%m-%d'

# # Exclude specific files from Pelican build
# EXCLUDE = ['node_modules', 'gulpfile.js', 'package.json', 'README.md', '_layouts', '_includes', 'venv', 'build']

# # Static folder settings (your static files like css, js, images, etc.)
# STATIC_PATHS = ['css', 'js', 'imgs', 'fonts', 'scripts']

# # Specify where to find your HTML layouts (use your existing layouts)
# THEME = 'layouts'  # Assuming your layouts are inside the `layouts/` folder

# # Additional files to keep (e.g., .git, .gitignore, etc.)
# KEEP_FILES = ['CNAME', '.git', '.gitignore']

# # Social media links
# SOCIAL = (
#     ('Twitter', 'https://twitter.com/snigdha'),
#     ('GitHub', 'https://github.com/snigdha'),
#     ('LinkedIn', 'https://www.linkedin.com/in/snigdhashantharam'),
# )

# Display pages in the menu
DISPLAY_PAGES_ON_MENU = True

AUTHOR = 'Snigdha S.'
SITENAME = 'Snigdha S. | Software Engineer'
SITEURL = 'https://snigdha.github.io'
SITEDESCRIPTION = 'Design-minded back-end software engineer focused on building beautiful interfaces and experiences.'


PATH = 'content'
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

READERS = {'html': None}  # Allow raw HTML files as pages
OUTPUT_PATH = 'output/'

THEME = 'themes/custom'

# Optional: If using Markdown content later
MARKDOWN = {
    'extensions': ['extra', 'codehilite', 'toc'],
    'output_format': 'html5',
}

STATIC_PATHS = ['css', 'js', 'fonts', 'img']

TEMPLATE_PAGES = {
    'index.html': 'index.html'
}

EXCLUDE = ['node_modules', '_layouts', '_includes', 'venv', 'build']
PLUGINS = ['minify']