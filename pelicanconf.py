AUTHOR = 'Snigdha'
SITENAME = 'Snigdha S'
SITEURL = ""

PATH = "content"

TIMEZONE = 'GB'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/snigdhashantharam'),
    # ('linkedin', 'https://linkedin.com/in/yourusername'),
    # ('twitter', 'https://twitter.com/yourusername'),
    # ('instagram', 'https://instagram.com/yourusername'),
    # ('codepen', 'https://codepen.io/yourusername'),
    ('email', 'mailto:snigdhashantharam@outlook.com'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Static paths will be copied to the output directory
STATIC_PATHS = ['images']

# Page-specific settings
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Custom variables for your portfolio
PROFILE_IMAGE = 'images/profile.jpg'  # If you have a profile image
PROJECTS = [
    {
        'title': 'blistabloc',
        'description': 'Custom WordPress theme built with Timber and WooCommerce for blistabloc, the only reactive shoe insert that prevents blisters from forming.',
        'image': 'images/projects/blistabloc.png',
        'tech': ['WordPress', 'Timber', 'WooCommerce'],
        'link': '#'
    },
    {
        'title': 'ScreenTime 2.0',
        'description': 'Starry Station feature that provided users with the ability to easily filter content, pause the internet, and even create custom rules for blocking apps like Facebook and Twitter right from their phones.',
        'image': 'images/projects/screentime.png',
        'tech': ['JavaScript', 'React'],
        'link': '#'
    },
    # Add more projects as needed
]

SKILLS = {
    'LANGUAGES': ['JavaScript (ES6)', 'TypeScript', 'HTML', 'CSS/Sass', 'Python', 'SQL', 'R'],
    'FRAMEWORKS': ['Ember & Glimmer', 'React', 'Jekyll', 'Node', 'D3', 'WordPress', 'Timber'],
    'TOOLS': ['Bash', 'Git & Github', 'Gulp & Grunt', 'Chrome DevTools', 'Postman', 'MongoDB'],
    'DESIGN': ['Sketch', 'InDesign', 'InVision', 'Prototyping', 'Wireframing', 'User Testing']
}

EXPERIENCE = [
    {
        'company': 'Upstatement',
        'position': 'Engineer',
        'period': 'May 2018 - Present',
        'description': 'Building things for the web with some awesome people.'
    },
    {
        'company': 'Scout',
        'position': 'Studio Developer',
        'period': 'Jan - June 2018',
        'description': ''
    },
    {
        'company': 'Apple Music',
        'position': 'UI Engineer Co-op',
        'period': 'July - Dec 2017',
        'description': ''
    },
    {
        'company': 'Scout',
        'position': 'Studio Developer',
        'period': 'Jan - June 2017',
        'description': ''
    },
    {
        'company': 'Starry',
        'position': 'Software Engineer Co-op',
        'period': 'July - Dec 2016',
        'description': ''
    },
    {
        'company': 'Northeastern University',
        'position': 'HCI Teaching Assistant',
        'period': 'Jan - May 2016',
        'description': ''
    }
]

OTHER_PROJECTS = [
    {
        'title': 'Surf Videos',
        'description': 'Small React project created during an interview process to browse and search surf videos via the YouTube API.',
        'tech': ['JavaScript', 'React', 'React Router', 'Axios', 'YouTube API'],
        'link': '#'
    },
    {
        'title': 'Halcyon Theme',
        'description': 'A minimal, dark theme for Sublime Text, Atom, VS Code, and more published to Package Control, Atom Package Manager, Visual Studio Marketplace, and NPM.',
        'tech': ['Gatsby', 'Sublime Text', 'Atom', 'VS Code', 'iTerm2', 'Hyper'],
        'link': '#'
    },
    {
        'title': 'Lonely Planet DBMS',
        'description': 'Final project for my Database Design course at Northeastern. A simple web application that allows users to filter through a database containing Lonely Planet\'s Top 500 Travel Destinations.',
        'tech': ['Python', 'MySQL', 'Flask', 'HTML', 'CSS', 'JavaScript'],
        'link': '#'
    },
    {
        'title': 'myNEU Redesign',
        'description': 'myNEU student portal web prototype for my information science senior project. I conducted a study that aimed to answer the question of how myNEU can be improved to provide students at Northeastern with a better user experience.',
        'tech': ['Jekyll', 'HTML', 'SCSS', 'JavaScript'],
        'link': '#'
    },
    {
        'title': 'JetBlue HumanKinda',
        'description': 'Tumblr site complementing JetBlue\'s HumanKinda campaign and documentary. The site houses the video documentary, many graphics created by Mullen for the campaign, and an interactive quiz to determine how "HumanKinda" you are.',
        'tech': ['HTML', 'CSS', 'JavaScript', 'jQuery'],
        'link': '#'
    }
]

# Education
EDUCATION = [
    {
        'institution': 'Northeastern University',
        'degree': 'Bachelor of Science in Computer Science',
        'graduation': 'May 2018',
        'description': 'Completed three awesome six-month co-ops at MullenLowe U.S., Starry, and Apple Music.'
    }
]

# Background section
BACKGROUND = "I'm currently an Engineer at Upstatement building things for the web with some awesome people. I recently graduated from Northeastern University after completing three awesome six-month co-ops at MullenLowe U.S., Starry, and Apple Music."

# About me section
ABOUT = """As a software engineer, I enjoy bridging the gap between engineering and design — combining my technical knowledge with my keen eye for design to create a beautiful product. My goal is to always build applications that are scalable and efficient under the hood while providing engaging, pixel-perfect user experiences."""

# Personal interests
INTERESTS = "When I'm not in front of a computer screen, I'm probably snowboarding, cruising around on my penny board, or crossing off another item on my bucket list."