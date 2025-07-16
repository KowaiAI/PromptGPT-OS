#!/usr/bin/env python3
"""
PromptGBT OS - AI Prompt Generation System
A command-line application for creating comprehensive AI content generation prompts
"""

import os
import sys
import time
from datetime import datetime
from typing import Dict, List, Any

# Try to import colorama for cross-platform colored output
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    HAS_COLORAMA = True
except ImportError:
    HAS_COLORAMA = False
    # Fallback color class
    class Fore:
        MAGENTA = CYAN = YELLOW = GREEN = RED = WHITE = ""
    class Style:
        BRIGHT = RESET_ALL = ""

class PromptGBTOS:
    def __init__(self):
        self.current_screen = 'main_menu'
        self.current_category = ''
        self.current_subcategory = ''
        self.current_question_index = 0
        self.answers = {}
        self.questions = []
        
        # Subcategories for each main category
        self.subcategories = {
            'code': ['Web App', 'Mobile App', 'Script', 'Backend', 'Debug', 'Code Analysis'],
            'image': ['Fantasy', 'Social Media', 'Meme', 'Business', 'Marketing', 'Infographic', 'Character'],
            'music': ['EDM', 'Hip Hop/Rap', 'R&B/Soul', 'Country', 'Experimental', 'Vocal', 'Commercial', 'Voice Over'],
            'text': ['Business', 'Blog', 'Social Media', 'Academic', 'Fiction', 'Non-Fiction', 'Marketing'],
            'video': ['Short Film', 'Commercial', 'Animation', 'Tutorial', 'Music Video', 'Documentary', 'Social Media']
        }
        
        # Comprehensive question templates for all subcategories
        self.question_templates = {
            # CODE CATEGORY
            'Web App': [
                "What is the primary purpose of your web application?",
                "Who is your target audience (age, profession, technical level)?",
                "What main features should the app include?",
                "What programming languages/frameworks do you prefer?",
                "What is the complexity level (simple, moderate, complex)?",
                "What type of user interface style do you want (modern, minimal, colorful)?",
                "Do you need user authentication and registration?",
                "What kind of database functionality is required?",
                "Should it be responsive for mobile devices?",
                "What is your preferred deployment platform?",
                "Do you need real-time features (chat, notifications)?",
                "What security features are important?",
                "Should it integrate with third-party APIs?",
                "What performance requirements do you have?",
                "Do you need offline functionality?",
                "What browser compatibility is required?",
                "Should it support multiple languages?",
                "What accessibility features are needed?",
                "Do you need content management capabilities?",
                "What analytics and tracking features?",
                "Should it have search functionality?",
                "What payment processing needs?",
                "Do you need file upload/download features?",
                "What notification systems are required?",
                "Should it have social media integration?",
                "What admin panel features are needed?",
                "Do you need backup and recovery systems?",
                "What scalability requirements?",
                "Should it have API endpoints?",
                "What caching strategies?",
                "Do you need automated testing?",
                "What monitoring and logging needs?",
                "Should it support webhooks?",
                "What data export/import capabilities?",
                "Do you need rate limiting?",
                "What error handling approaches?",
                "Should it have progressive web app features?",
                "What SEO optimization needs?",
                "Do you need A/B testing capabilities?",
                "What documentation requirements?",
                "Should it have dark/light mode toggle?",
                "What email functionality is needed?",
                "Do you need scheduling features?",
                "What reporting and dashboard needs?",
                "Should it have drag-and-drop functionality?",
                "What keyboard shortcuts are important?",
                "Do you need data visualization components?",
                "What print functionality requirements?",
                "Should it support custom themes?",
                "What specific industry requirements or compliance needs?"
            ],
            'Mobile App': [
                "What platform should the app target (iOS, Android, cross-platform)?",
                "What is the main functionality of your mobile app?",
                "Who is your target user demographic?",
                "What design style do you prefer (Material Design, iOS Human Interface, custom)?",
                "Do you need offline functionality?",
                "What device features should it use (camera, GPS, contacts, etc.)?",
                "Should it support push notifications?",
                "What data storage requirements do you have?",
                "Do you need user accounts and authentication?",
                "Should it integrate with social media platforms?",
                "What monetization model (free, paid, in-app purchases, ads)?",
                "Do you need real-time synchronization with servers?",
                "What performance benchmarks are important?",
                "Should it support multiple screen sizes and orientations?",
                "Do you need accessibility compliance?",
                "What security measures are required?",
                "Should it work with wearable devices?",
                "Do you need analytics and crash reporting?",
                "What app store guidelines must be followed?",
                "Should it support multiple languages?",
                "Do you need background processing capabilities?",
                "What third-party services should it integrate with?",
                "Should it have voice or gesture controls?",
                "Do you need augmented reality features?",
                "What sharing capabilities should be included?",
                "Should it support biometric authentication?",
                "Do you need custom animations and transitions?",
                "What testing requirements do you have?",
                "Should it support widgets or extensions?",
                "Do you need deep linking functionality?",
                "What backup and data recovery features?",
                "Should it have tutorial or onboarding flows?",
                "Do you need custom fonts and branding?",
                "What network connectivity handling is needed?",
                "Should it support dark mode?",
                "Do you need parental controls or content filtering?",
                "What location-based features are required?",
                "Should it integrate with device calendar or contacts?",
                "Do you need barcode or QR code scanning?",
                "What file handling capabilities?",
                "Should it support video or audio streaming?",
                "Do you need custom keyboard or input methods?",
                "What battery optimization considerations?",
                "Should it have split-screen or multi-window support?",
                "Do you need enterprise or MDM compatibility?",
                "What compliance requirements (GDPR, COPPA, etc.)?",
                "Should it support Apple Watch or Android Wear?",
                "What debugging and diagnostic features?",
                "Do you need A/B testing capabilities?",
                "What specific industry regulations must be followed?"
            ],
            'Script': [
                "What is the primary purpose of your script?",
                "What programming language should be used?",
                "What operating system will it run on?",
                "What inputs does the script need to handle?",
                "What outputs should the script produce?",
                "Should it run as a one-time execution or recurring process?",
                "What error handling and logging is needed?",
                "Does it need to interact with databases?",
                "Should it process files or directories?",
                "What performance requirements are there?",
                "Does it need command-line arguments or configuration files?",
                "Should it send notifications or alerts?",
                "What external APIs or services will it connect to?",
                "Does it need to handle large datasets?",
                "Should it support parallel processing or threading?",
                "What security considerations are important?",
                "Does it need to run on a schedule (cron, task scheduler)?",
                "Should it create backups or maintain history?",
                "What dependencies and libraries can be used?",
                "Does it need user interaction or can it be fully automated?",
                "Should it generate reports or summaries?",
                "What data validation and sanitization is needed?",
                "Does it need to handle network requests or file transfers?",
                "Should it support configuration through environment variables?",
                "What monitoring and health checks are required?",
                "Does it need to integrate with existing systems?",
                "Should it support rollback or undo functionality?",
                "What testing and quality assurance approaches?",
                "Does it need to handle different data formats (JSON, XML, CSV)?",
                "Should it support internationalization?",
                "What memory and resource constraints exist?",
                "Does it need to work with cloud services?",
                "Should it support plugins or extensions?",
                "What documentation and help features are needed?",
                "Does it need to handle encryption or sensitive data?",
                "Should it support batch processing?",
                "What retry logic and fault tolerance is required?",
                "Does it need to work offline or with limited connectivity?",
                "Should it support version control or change tracking?",
                "What deployment and distribution methods?",
                "Does it need to integrate with CI/CD pipelines?",
                "Should it support custom filtering or searching?",
                "What data archiving or cleanup processes?",
                "Does it need to handle real-time streaming data?",
                "Should it support custom plugins or modules?",
                "What compliance or audit trail requirements?",
                "Does it need to work with containers or virtualization?",
                "Should it support graceful shutdown and cleanup?",
                "What specific business rules or logic must be implemented?",
                "Does it need to interface with hardware or IoT devices?"
            ],
            'Backend': [
                "What type of backend architecture (REST API, GraphQL, microservices)?",
                "What programming language and framework should be used?",
                "What database technology is preferred (SQL, NoSQL, hybrid)?",
                "What are the expected traffic and load requirements?",
                "What authentication and authorization methods are needed?",
                "Should it support real-time communications (WebSockets, Server-Sent Events)?",
                "What caching strategies should be implemented?",
                "What third-party integrations are required?",
                "What data validation and sanitization rules?",
                "Should it support file uploads and media processing?",
                "What logging and monitoring requirements?",
                "What error handling and recovery mechanisms?",
                "Should it support background job processing?",
                "What API versioning strategy?",
                "What rate limiting and throttling policies?",
                "Should it support multi-tenancy?",
                "What backup and disaster recovery plans?",
                "What security measures (encryption, HTTPS, CORS)?",
                "Should it support horizontal scaling?",
                "What testing strategies (unit, integration, load)?",
                "What documentation and API specification needs?",
                "Should it support webhooks or event streaming?",
                "What data migration and seeding requirements?",
                "What performance optimization priorities?",
                "Should it support search functionality?",
                "What email and notification services?",
                "What payment processing integrations?",
                "Should it support batch operations?",
                "What admin panel or management interface needs?",
                "What analytics and reporting capabilities?",
                "Should it support content delivery networks (CDN)?",
                "What geographic distribution requirements?",
                "What compliance standards (GDPR, HIPAA, SOC2)?",
                "Should it support A/B testing infrastructure?",
                "What message queuing systems are needed?",
                "What container orchestration requirements?",
                "Should it support feature flags or toggles?",
                "What health check and status endpoints?",
                "What data export and import capabilities?",
                "Should it support custom business logic plugins?",
                "What session management strategies?",
                "What database optimization and indexing needs?",
                "Should it support GraphQL subscriptions?",
                "What cross-service communication patterns?",
                "What secrets management and configuration?",
                "Should it support automated deployments?",
                "What performance metrics and KPIs to track?",
                "What disaster recovery and failover mechanisms?",
                "Should it support custom middleware or interceptors?",
                "What specific industry or domain requirements?"
            ],
            'Debug': [
                "What programming language is the code written in?",
                "What type of application or system needs debugging?",
                "What specific error messages or symptoms are occurring?",
                "When does the problem occur (startup, runtime, specific actions)?",
                "What debugging tools are available in your environment?",
                "Can you reproduce the issue consistently?",
                "What was the last working version or state?",
                "What recent changes were made to the codebase?",
                "What error logs or stack traces are available?",
                "What is the expected vs actual behavior?",
                "What operating system and environment details?",
                "What dependencies and library versions are being used?",
                "Are there any performance issues (memory leaks, slow execution)?",
                "What data inputs cause the problem?",
                "Are there any network or connectivity issues?",
                "What database or external service interactions are involved?",
                "Are there any race conditions or concurrency issues?",
                "What security or permission-related problems?",
                "Are there any configuration or environment variable issues?",
                "What testing scenarios reveal the problem?",
                "Are there any browser or client-specific issues?",
                "What API or service integration problems exist?",
                "Are there any deployment or hosting issues?",
                "What monitoring or alerting data is available?",
                "Are there any memory or resource constraint issues?",
                "What user actions trigger the problem?",
                "Are there any timezone or localization issues?",
                "What third-party service failures are occurring?",
                "Are there any SSL/TLS or certificate problems?",
                "What file system or storage issues exist?",
                "Are there any authentication or session problems?",
                "What caching or data consistency issues?",
                "Are there any mobile or device-specific problems?",
                "What load balancing or scaling issues?",
                "Are there any backup or recovery process problems?",
                "What compliance or audit trail issues?",
                "Are there any integration test failures?",
                "What documentation or code comment gaps exist?",
                "Are there any version control or merge conflicts?",
                "What automated deployment or CI/CD issues?",
                "Are there any cross-browser compatibility problems?",
                "What accessibility or usability issues?",
                "Are there any internationalization problems?",
                "What plugin or extension conflicts exist?",
                "Are there any backup or disaster recovery issues?",
                "What specific business logic errors are occurring?",
                "Are there any regulatory compliance problems?",
                "What user experience or interface issues?",
                "Are there any data corruption or integrity problems?",
                "What specific debugging approach or methodology should be used?"
            ],
            'Code Analysis': [
                "What programming language should be analyzed?",
                "What type of analysis is needed (security, performance, quality, style)?",
                "What is the size and scope of the codebase?",
                "What specific metrics or KPIs should be measured?",
                "Are there existing coding standards or guidelines to check against?",
                "What security vulnerabilities should be identified?",
                "Should the analysis include performance bottlenecks?",
                "What code complexity metrics are important?",
                "Should it check for code duplication?",
                "What dependency analysis is needed?",
                "Should it identify dead or unused code?",
                "What documentation coverage analysis is required?",
                "Should it check for design pattern violations?",
                "What test coverage analysis is needed?",
                "Should it identify potential bugs or error-prone code?",
                "What accessibility compliance checks are required?",
                "Should it analyze API usage and compatibility?",
                "What license compliance checks are needed?",
                "Should it identify technical debt indicators?",
                "What maintainability metrics should be calculated?",
                "Should it check for memory leaks or resource issues?",
                "What architectural analysis is required?",
                "Should it identify code smells and anti-patterns?",
                "What performance profiling is needed?",
                "Should it analyze error handling patterns?",
                "What version control history analysis is required?",
                "Should it check for SQL injection or XSS vulnerabilities?",
                "What data flow analysis is needed?",
                "Should it identify race conditions or concurrency issues?",
                "What compliance standard checks (OWASP, CWE, etc.)?",
                "Should it analyze third-party library risks?",
                "What scalability analysis is required?",
                "Should it check for proper logging and monitoring?",
                "What configuration and secrets analysis is needed?",
                "Should it identify business logic flaws?",
                "What cross-platform compatibility analysis?",
                "Should it check for proper exception handling?",
                "What database query optimization analysis?",
                "Should it identify UI/UX code issues?",
                "What mobile app specific analysis (battery, network)?",
                "Should it analyze containerization and deployment code?",
                "What CI/CD pipeline code analysis is needed?",
                "Should it check for proper input validation?",
                "What cloud security analysis is required?",
                "Should it identify GDPR or privacy compliance issues?",
                "What machine learning model code analysis?",
                "Should it check for blockchain or smart contract vulnerabilities?",
                "What IoT device code security analysis?",
                "Should it analyze microservices communication patterns?",
                "What specific industry or domain analysis requirements?"
            ],

            # IMAGE CATEGORY
            'Fantasy': [
                "What type of fantasy setting (medieval, modern, futuristic)?",
                "Who or what is the main subject of the image?",
                "What mood or atmosphere should the image convey?",
                "What art style do you prefer (realistic, cartoon, painterly, digital art)?",
                "What color palette should dominate the image?",
                "What time of day should be depicted?",
                "What kind of lighting (dramatic, soft, magical, natural)?",
                "Should there be any magical elements or effects?",
                "What landscape or environment should be shown?",
                "What clothing or armor style for characters?",
                "Should there be any creatures or monsters?",
                "What weapons or magical items to include?",
                "What architectural style for buildings?",
                "What weather conditions should be present?",
                "Should the image have a specific cultural influence?",
                "What level of detail is desired (highly detailed, minimalist)?",
                "What perspective or viewpoint (close-up, wide shot, aerial)?",
                "Should there be any text or symbols included?",
                "What emotional expression for characters?",
                "What type of vegetation or terrain?",
                "Should there be flying elements (dragons, birds, floating objects)?",
                "What kind of sky (stormy, clear, mystical)?",
                "Should there be water elements (rivers, oceans, rain)?",
                "What type of fantasy race (elves, dwarves, humans, other)?",
                "Should there be any ruins or ancient structures?",
                "What kind of magical aura or energy?",
                "Should there be any celestial elements (moons, stars)?",
                "What type of ground or surface texture?",
                "Should there be any fire or flame elements?",
                "What kind of shadows and contrast?",
                "Should there be any mystical portals or gateways?",
                "What type of fantasy jewelry or accessories?",
                "Should there be any floating islands or structures?",
                "What kind of magical creatures in the background?",
                "Should there be any ancient runes or writing?",
                "What type of crystal or gem elements?",
                "Should there be any mist or fog effects?",
                "What kind of fantasy transportation?",
                "Should there be any enchanted forests or trees?",
                "What type of magical artifacts?",
                "Should there be any elemental magic effects?",
                "What kind of fantasy wildlife?",
                "Should there be any dimensional or reality-bending elements?",
                "What type of fantasy music instruments visible?",
                "Should there be any alchemical elements?",
                "What kind of fantasy food or feast elements?",
                "Should there be any time magic or temporal effects?",
                "What type of fantasy maps or navigation tools?",
                "Should the image suggest any specific fantasy story or legend?",
                "What resolution and aspect ratio do you need for the final image?"
            ],
            'Social Media': [
                "What social media platform is this image for?",
                "What is the main message or call-to-action?",
                "Who is your target audience demographic?",
                "What brand colors and fonts should be used?",
                "What image dimensions and aspect ratio are needed?",
                "Should it include your logo or branding elements?",
                "What style should it be (professional, casual, trendy, minimalist)?",
                "What type of content (announcement, promotion, educational, entertainment)?",
                "Should it include text overlays or quotes?",
                "What mood or emotion should it evoke?",
                "Should it include people, products, or abstract elements?",
                "What photography style (stock photo, lifestyle, product shot)?",
                "Should it follow current design trends?",
                "What color psychology considerations?",
                "Should it include icons or graphic elements?",
                "What contrast and readability requirements?",
                "Should it be part of a series or campaign?",
                "What accessibility considerations (alt text, color contrast)?",
                "Should it include hashtags or social handles?",
                "What engagement strategy (likes, shares, comments)?",
                "Should it be optimized for mobile viewing?",
                "What seasonal or timely elements to include?",
                "Should it include user-generated content elements?",
                "What competition or industry benchmarking?",
                "Should it include pricing or promotional information?",
                "What storytelling elements should be present?",
                "Should it follow platform-specific best practices?",
                "What A/B testing variations to consider?",
                "Should it include interactive elements or polls?",
                "What cross-platform consistency requirements?",
                "Should it include testimonials or reviews?",
                "What urgency or scarcity elements?",
                "Should it be localized for different regions?",
                "What influencer or partnership elements?",
                "Should it include behind-the-scenes content?",
                "What community or user engagement features?",
                "Should it include educational or how-to elements?",
                "What viral or shareable qualities?",
                "Should it include event or announcement details?",
                "What sustainability or social responsibility messaging?",
                "Should it include augmented reality or interactive features?",
                "What analytics and tracking considerations?",
                "Should it include video thumbnail or preview elements?",
                "What cross-generational appeal considerations?",
                "Should it include QR codes or direct links?",
                "What compliance with advertising standards?",
                "Should it include multi-language support?",
                "What brand personality and voice representation?",
                "Should it optimize for different devices and screen sizes?",
                "What specific engagement metrics to optimize for?"
            ],
            'Meme': [
                "What meme format or template should be used?",
                "What's the main joke or punchline?",
                "Who is your target audience (age group, interests)?",
                "What current trends or events to reference?",
                "Should it be text-based or image-based?",
                "What level of humor (clean, edgy, satirical)?",
                "Should it include popular meme characters or figures?",
                "What cultural references to include?",
                "Should it be relatable to specific groups or universal?",
                "What social media platform will it be shared on?",
                "Should it include brand or product placement?",
                "What font style and text placement?",
                "Should it be part of a meme series?",
                "What timing or relevance to current events?",
                "Should it include hashtags or social handles?",
                "What image quality and resolution needed?",
                "Should it be original content or remix existing memes?",
                "What copyright or fair use considerations?",
                "Should it include watermarks or attribution?",
                "What viral potential and shareability factors?",
                "Should it reference internet culture or inside jokes?",
                "What generational humor preferences?",
                "Should it include pop culture references?",
                "What political or social commentary level?",
                "Should it be seasonal or evergreen content?",
                "What engagement encouragement (comments, shares)?",
                "Should it include call-to-action elements?",
                "What accessibility features for different audiences?",
                "Should it be part of marketing or organic content?",
                "What platform-specific optimization (Twitter, Instagram, TikTok)?",
                "Should it include multiple panels or single image?",
                "What emotional response to target (laughter, nostalgia, surprise)?",
                "Should it reference specific fandoms or communities?",
                "What local or regional humor elements?",
                "Should it include reaction GIF potential?",
                "What remix or adaptation potential for users?",
                "Should it include educational or informational elements?",
                "What controversy or sensitive topic avoidance?",
                "Should it include interactive elements or polls?",
                "What cross-platform sharing optimization?",
                "Should it reference workplace or daily life situations?",
                "What celebrity or public figure references?",
                "Should it include gaming or tech culture elements?",
                "What food, travel, or lifestyle themes?",
                "Should it include relationship or friendship humor?",
                "What animal or pet-related content?",
                "Should it reference movies, TV shows, or books?",
                "What sports or competition themes?",
                "Should it include motivational or inspirational twist?",
                "What specific outcome or engagement goal for the meme?"
            ],
            'Business': [
                "What type of business image is needed (presentation, marketing, report)?",
                "What industry or business sector does this represent?",
                "Who is the target audience (executives, employees, customers, investors)?",
                "What is the main message or value proposition?",
                "What brand guidelines and visual identity to follow?",
                "What level of formality is required (corporate, professional, approachable)?",
                "Should it include data visualization or infographics?",
                "What colors align with your brand and industry standards?",
                "Should it include people, products, or conceptual elements?",
                "What image dimensions and format requirements?",
                "Should it include text overlays or headlines?",
                "What photography style (stock, professional headshots, lifestyle)?",
                "Should it convey innovation, reliability, growth, or other values?",
                "What cultural or demographic considerations?",
                "Should it include company logos or partnership logos?",
                "What accessibility and inclusivity requirements?",
                "Should it be optimized for print or digital use?",
                "What seasonal or campaign-specific elements?",
                "Should it include contact information or website details?",
                "What competitive differentiation to highlight?",
                "Should it follow industry-specific visual conventions?",
                "What call-to-action or next steps to include?",
                "Should it include awards, certifications, or credentials?",
                "What geographic or location-specific elements?",
                "Should it include sustainability or social responsibility messaging?",
                "What technology or innovation showcase requirements?",
                "Should it include customer testimonials or case studies?",
                "What urgency or time-sensitive elements?",
                "Should it include pricing or value proposition highlights?",
                "What multi-channel usage requirements (web, print, social)?",
                "Should it include QR codes or interactive elements?",
                "What compliance with advertising and industry regulations?",
                "Should it include diverse representation and inclusion?",
                "What scalability for different sizes and formats?",
                "Should it include partnership or collaboration elements?",
                "What thought leadership or expertise positioning?",
                "Should it include event or announcement details?",
                "What investor or stakeholder communication needs?",
                "Should it include process or methodology illustrations?",
                "What customer journey or experience mapping?",
                "Should it include before/after or transformation elements?",
                "What security, privacy, or trust indicators?",
                "Should it include global or international elements?",
                "What employee or team showcase requirements?",
                "Should it include research or data-backed claims?",
                "What crisis communication or transparency needs?",
                "Should it include mobile-first or responsive design?",
                "What A/B testing or variation requirements?",
                "Should it align with overall marketing campaign themes?",
                "What specific business outcome or KPI optimization goals?"
            ],
            'Marketing': [
                "What marketing channel will this image be used for?",
                "What is the primary marketing objective (awareness, conversion, retention)?",
                "Who is your ideal customer persona?",
                "What stage of the customer journey are you targeting?",
                "What is your unique selling proposition?",
                "What brand personality should the image convey?",
                "What emotional response do you want to trigger?",
                "Should it include a clear call-to-action?",
                "What budget or premium positioning should be reflected?",
                "What seasonal or timely elements to incorporate?",
                "Should it include social proof or testimonials?",
                "What competitive advantages to highlight?",
                "Should it include urgency or scarcity elements?",
                "What color psychology considerations for your audience?",
                "Should it include product features or benefits?",
                "What lifestyle or aspiration elements to show?",
                "Should it be part of an integrated campaign?",
                "What A/B testing variations to consider?",
                "Should it include pricing or promotional offers?",
                "What geographic or cultural customization needs?",
                "Should it include user-generated content elements?",
                "What influencer or partnership integration?",
                "Should it optimize for mobile or desktop viewing?",
                "What accessibility and inclusive design requirements?",
                "Should it include QR codes or trackable elements?",
                "What cross-platform consistency needs?",
                "Should it include video thumbnail or preview elements?",
                "What viral or shareability potential?",
                "Should it include educational or how-to content?",
                "What trust signals or security indicators?",
                "Should it include sustainability or ethical messaging?",
                "What personalization or segmentation elements?",
                "Should it include interactive or gamification features?",
                "What retargeting or remarketing optimization?",
                "Should it include event or launch announcement details?",
                "What omnichannel experience integration?",
                "Should it include augmented reality or virtual try-on elements?",
                "What data privacy or compliance messaging?",
                "Should it include community or social impact elements?",
                "What technological innovation or features to showcase?",
                "Should it include customer success stories or case studies?",
                "What subscription or loyalty program promotion?",
                "Should it include multi-generational appeal elements?",
                "What crisis communication or transparency needs?",
                "Should it include partnership or collaboration highlights?",
                "What thought leadership or expertise positioning?",
                "Should it include research or survey-backed claims?",
                "What customer service or support integration?",
                "Should it optimize for voice search or smart devices?",
                "What specific conversion metric or KPI optimization focus?"
            ],
            'Infographic': [
                "What main topic or subject should the infographic cover?",
                "Who is your target audience and what's their knowledge level?",
                "What key data points or statistics to highlight?",
                "What story or narrative flow should it follow?",
                "Should it be vertical, horizontal, or square format?",
                "What color scheme aligns with your brand or topic?",
                "What level of detail and complexity is appropriate?",
                "Should it include charts, graphs, or data visualizations?",
                "What icons, illustrations, or imagery style?",
                "Should it include sources and citations?",
                "What call-to-action or next steps to include?",
                "Should it be shareable on social media platforms?",
                "What branding elements (logo, website, contact info)?",
                "Should it include interactive or clickable elements?",
                "What accessibility features for different abilities?",
                "Should it be optimized for print or digital distribution?",
                "What font hierarchy and readability requirements?",
                "Should it include QR codes or links to additional resources?",
                "What geographic or demographic customization?",
                "Should it include comparison or before/after elements?",
                "What timeline or chronological information?",
                "Should it include process steps or how-to information?",
                "What industry-specific terminology or jargon level?",
                "Should it include multiple language versions?",
                "What mobile-friendly design considerations?",
                "Should it include embedded videos or animations?",
                "What SEO optimization for web use?",
                "Should it include user-generated content or testimonials?",
                "What seasonal or time-sensitive information?",
                "Should it include contact forms or lead generation?",
                "What compliance with data accuracy and fact-checking?",
                "Should it include downloadable or printable versions?",
                "What white-labeling or customization options?",
                "Should it include social sharing buttons or hashtags?",
                "What analytics or tracking implementation?",
                "Should it include survey or feedback collection elements?",
                "What crisis communication or transparency information?",
                "Should it include partnerships or collaboration credits?",
                "What thought leadership or expertise positioning?",
                "Should it include research methodology or data sources?",
                "What visual hierarchy and scanning patterns?",
                "Should it include myths vs. facts or common misconceptions?",
                "What actionable tips or takeaway recommendations?",
                "Should it include future predictions or trend analysis?",
                "What community or crowdsourced data integration?",
                "Should it include calculator or tool integration?",
                "What gamification or interactive quiz elements?",
                "Should it include augmented reality or AR features?",
                "What voice-over or audio description compatibility?",
                "What specific engagement or sharing goal for the infographic?"
            ],
            'Character': [
                "What type of character (human, animal, fantasy creature, robot)?",
                "What is the character's age, gender, and background?",
                "What personality traits should be visually apparent?",
                "What art style (realistic, cartoon, anime, minimalist, detailed)?",
                "What is the character's role or profession?",
                "What clothing or costume should they wear?",
                "What facial expressions and body language?",
                "What color palette for skin, hair, and clothing?",
                "Should the character have any unique physical features?",
                "What accessories, jewelry, or props to include?",
                "What setting or background environment?",
                "What lighting and mood for the character?",
                "Should the character be in action or static pose?",
                "What cultural or ethnic representation?",
                "What time period or era should they represent?",
                "Should they have any special abilities or powers?",
                "What emotional state should they convey?",
                "What relationship to other characters (if any)?",
                "Should they have any scars, tattoos, or markings?",
                "What body type and physical build?",
                "What hair style, length, and color?",
                "Should they wear makeup or have face paint?",
                "What kind of footwear or shoes?",
                "Should they have any weapons or tools?",
                "What level of detail in facial features?",
                "Should they have any magical or glowing elements?",
                "What perspective or viewing angle?",
                "Should the character be interacting with objects?",
                "What social status or economic background to convey?",
                "Should they have any pets or companion creatures?",
                "What seasonal clothing or environmental adaptation?",
                "Should they show signs of their profession or hobby?",
                "What disabilities or accessibility features to include?",
                "Should they have any technological augmentations?",
                "What family resemblance or genetic traits?",
                "Should they be based on real people or completely original?",
                "What mythology or folklore influences?",
                "Should they have multiple outfit or appearance options?",
                "What aging or life stage representation?",
                "Should they have any symbolic or metaphorical elements?",
                "What voice actor or celebrity inspiration (if any)?",
                "Should they be designed for animation or static art?",
                "What merchandise or commercial use considerations?",
                "Should they appeal to specific demographics?",
                "What character evolution or development potential?",
                "Should they fit within an existing universe or franchise?",
                "What copyright or intellectual property considerations?",
                "Should they be optimized for different media formats?",
                "What brand alignment or marketing message representation?",
                "What specific story or narrative role will they fulfill?"
            ],

            # MUSIC CATEGORY
            'EDM': [
                "What EDM subgenre (house, techno, dubstep, trance, drum & bass)?",
                "What BPM range do you prefer?",
                "What energy level (chill, moderate, high-energy, intense)?",
                "What key or scale should the track be in?",
                "What length should the track be?",
                "What instruments or sounds should be featured?",
                "Should it have vocals or be instrumental?",
                "What mood or emotion should it convey?",
                "What venue or setting is it intended for (club, festival, radio)?",
                "What age group is your target audience?",
                "Should it include classic EDM elements like drops and builds?",
                "What synthesis techniques (analog, digital, hybrid)?",
                "Should it have a memorable hook or melody?",
                "What cultural or regional influences?",
                "Should it include samples from other tracks?",
                "What mastering and production quality level?",
                "Should it be radio-friendly or underground?",
                "What collaboration elements (featuring artists, remixes)?",
                "Should it include live instrument recordings?",
                "What technological innovation or sound design?",
                "Should it follow current trends or be timeless?",
                "What streaming platform optimization?",
                "Should it include storytelling or conceptual elements?",
                "What festival or event performance suitability?",
                "Should it have commercial or artistic focus?",
                "What remix potential and stems availability?",
                "Should it include video game or media sync potential?",
                "What DJ mixing and beatmatching considerations?",
                "Should it appeal to mainstream or niche audiences?",
                "What cross-genre fusion elements?",
                "Should it include environmental or nature sounds?",
                "What nostalgia or retro elements to include?",
                "Should it have danceability and club playability?",
                "What vocal processing and effects techniques?",
                "Should it include experimental or avant-garde elements?",
                "What arrangement structure (intro, breakdown, outro)?",
                "Should it optimize for different sound systems?",
                "What licensing and commercial use intentions?",
                "Should it include cultural or social messaging?",
                "What seasonal or themed content alignment?",
                "Should it have acoustic or organic elements mixed in?",
                "What fan engagement and community building potential?",
                "Should it include interactive or immersive audio features?",
                "What brand partnership or sync licensing goals?",
                "Should it accommodate different listening environments?",
                "What artistic signature or unique producer identity?",
                "Should it include meditation or wellness applications?",
                "What gaming or virtual reality compatibility?",
                "Should it have potential for live performance adaptation?",
                "What specific outcome or impact goal for the track?"
            ],
            'Hip Hop/Rap': [
                "What hip hop subgenre (trap, boom bap, mumble rap, conscious, drill)?",
                "What BPM range fits your style?",
                "Should it have heavy bass or more balanced mix?",
                "What type of drums and percussion?",
                "Should it include samples or original compositions?",
                "What vocal style (melodic, aggressive, laid-back, rapid)?",
                "What topics or themes should the lyrics cover?",
                "Who is your target audience demographic?",
                "Should it have a hook or chorus?",
                "What regional or cultural influences?",
                "Should it include guest features or collaborations?",
                "What length and structure for the track?",
                "Should it be radio-friendly or explicit?",
                "What instrumentation beyond beats (piano, guitar, strings)?",
                "Should it include auto-tune or vocal effects?",
                "What mood or attitude should it convey?",
                "Should it tell a story or be more abstract?",
                "What production style (polished, raw, lo-fi)?",
                "Should it include ad-libs and vocal layers?",
                "What streaming and playlist placement goals?",
                "Should it address social issues or be entertainment-focused?",
                "What generation of hip hop influence?",
                "Should it include singing sections or pure rap?",
                "What geographical or neighborhood representation?",
                "Should it have crossover appeal to other genres?",
                "What seasonal or timely content relevance?",
                "Should it include interpolations from classic tracks?",
                "What record label or independent release strategy?",
                "Should it showcase lyrical complexity or simplicity?",
                "What video and visual content potential?",
                "Should it include live performance elements?",
                "What merchandising and brand building opportunities?",
                "Should it address personal experiences or universal themes?",
                "What collaboration with producers, writers, or artists?",
                "Should it include motivational or inspirational messages?",
                "What controversy or boundary-pushing elements?",
                "Should it optimize for TikTok or social media virality?",
                "What awards show or recognition positioning?",
                "Should it include community or fan engagement elements?",
                "What authenticity and credibility considerations?",
                "Should it blend with R&B, pop, or other genres?",
                "What historical or cultural reference integration?",
                "Should it include family, relationships, or personal growth themes?",
                "What business or entrepreneurship messaging?",
                "Should it have potential for remix or reinterpretation?",
                "What live instrumentation vs. digital production balance?",
                "Should it include educational or consciousness-raising content?",
                "What fan base expansion or retention strategy?",
                "Should it reflect current events or timeless themes?",
                "What specific impact or legacy goal for the track?"
            ],
            'R&B/Soul': [
                "What R&B style (classic soul, contemporary R&B, neo-soul, alternative R&B)?",
                "What vocal range and style should be featured?",
                "Should it be slow and sensual or upbeat and energetic?",
                "What instrumentation (live band, programmed, hybrid)?",
                "What emotional themes (love, heartbreak, empowerment, celebration)?",
                "Should it include gospel or spiritual influences?",
                "What production era influence (vintage, modern, futuristic)?",
                "Should it feature harmonies and background vocals?",
                "What target audience age and demographic?",
                "Should it include rap verses or spoken word sections?",
                "What regional R&B influences (Motown, Philadelphia, Atlanta)?",
                "Should it be radio-friendly or album deep cut?",
                "What tempo and groove feel?",
                "Should it include live instruments or samples?",
                "What vocal effects and processing techniques?",
                "Should it tell a personal story or universal experience?",
                "What collaboration potential with other artists?",
                "Should it have crossover appeal to pop or hip hop?",
                "What length and song structure?",
                "Should it include instrumental solos or breakdowns?",
                "What cultural or social commentary elements?",
                "Should it feature acoustic or electronic elements?",
                "What seasonal or romantic timing considerations?",
                "Should it include interpolations from classic soul tracks?",
                "What streaming platform and playlist targeting?",
                "Should it showcase vocal acrobatics or restraint?",
                "What fashion and visual aesthetic alignment?",
                "Should it include family, community, or heritage themes?",
                "What generational bridge-building or nostalgia elements?",
                "Should it have dance or choreography potential?",
                "What live performance and touring suitability?",
                "Should it include empowerment or self-love messaging?",
                "What relationship dynamics or dating culture reflection?",
                "Should it blend with jazz, funk, or blues influences?",
                "What awards show performance or recognition goals?",
                "Should it include vulnerability and authenticity themes?",
                "What brand partnerships or sync licensing potential?",
                "Should it address mental health or wellness topics?",
                "What fan community building and engagement?",
                "Should it include retro or vintage production elements?",
                "What international or global appeal considerations?",
                "Should it feature emerging technology or innovation in sound?",
                "What social media and viral marketing potential?",
                "Should it include motivational or inspirational content?",
                "What artistic growth or evolution demonstration?",
                "Should it collaborate with producers, songwriters, or musicians?",
                "What legacy or timeless quality aspirations?",
                "Should it address current events or social movements?",
                "What therapeutic or healing music applications?",
                "What specific emotional or spiritual impact goal for listeners?"
            ],
            'Country': [
                "What country subgenre (traditional, modern, pop country, bluegrass, outlaw)?",
                "What instruments should be featured (guitar, banjo, fiddle, steel guitar)?",
                "Should it tell a story or focus on emotions?",
                "What regional influences (Nashville, Texas, Appalachian)?",
                "What themes (rural life, relationships, patriotism, hardship, celebration)?",
                "Should it include traditional country vocals or modern style?",
                "What tempo and energy level?",
                "Should it have crossover appeal to pop or rock?",
                "What age demographic are you targeting?",
                "Should it include harmonies or duet elements?",
                "What production style (acoustic, polished, raw)?",
                "Should it reference specific locations or landmarks?",
                "What seasonal or holiday themes?",
                "Should it include spoken word or dialogue sections?",
                "What cultural or family tradition references?",
                "Should it address current events or timeless themes?",
                "What collaboration with other country artists?",
                "Should it include humor or serious messaging?",
                "What radio format targeting (mainstream, alternative, classic)?",
                "Should it feature live recording or studio production?",
                "What working-class or blue-collar representation?",
                "Should it include military or veteran themes?",
                "What relationship dynamics (marriage, dating, family)?",
                "Should it blend with other genres (rock, folk, blues)?",
                "What awards show or industry recognition goals?",
                "Should it include small town or rural imagery?",
                "What generational storytelling or wisdom sharing?",
                "Should it address social issues or stay apolitical?",
                "What touring and live performance suitability?",
                "Should it include nostalgia or childhood memories?",
                "What outdoor or nature activity themes?",
                "Should it feature truck, farming, or outdoor work references?",
                "What faith or spiritual element inclusion?",
                "Should it have sing-along or anthemic qualities?",
                "What streaming platform and playlist optimization?",
                "Should it include recovery, redemption, or second chance themes?",
                "What community or neighborhood solidarity messaging?",
                "Should it feature traditional country instruments vs. modern production?",
                "What merchandise and brand building opportunities?",
                "Should it include sports or recreation activity themes?",
                "What fan engagement and concert interaction potential?",
                "Should it address economic or financial struggles?",
                "What historical or heritage preservation themes?",
                "Should it include romantic or wedding-appropriate content?",
                "What crisis or disaster community response themes?",
                "Should it feature environmental or conservation messaging?",
                "What intergenerational family relationship dynamics?",
                "Should it include party or celebration atmospheres?",
                "What authentic country lifestyle representation?",
                "What specific cultural impact or message goal for the song?"
            ],
            'Experimental': [
                "What experimental approach (sound design, unconventional structure, genre fusion)?",
                "What traditional music boundaries are you breaking?",
                "Should it challenge listener expectations or comfort zones?",
                "What innovative instruments or technology to use?",
                "What conceptual or philosophical framework?",
                "Should it include field recordings or environmental sounds?",
                "What temporal or rhythmic experimentation?",
                "Should it blend multiple genres or stay within one?",
                "What audience (avant-garde enthusiasts, mainstream, academic)?",
                "Should it include interactive or participatory elements?",
                "What cultural or social commentary through sound?",
                "Should it use extended techniques on traditional instruments?",
                "What digital manipulation or AI-generated elements?",
                "Should it include improvisation or aleatoric elements?",
                "What spatial audio or immersive sound experiences?",
                "Should it challenge conventional song lengths or structures?",
                "What collaboration with other experimental artists?",
                "Should it include microtonal or alternative tuning systems?",
                "What performance art or multimedia integration?",
                "Should it document or archive specific sounds or environments?",
                "What psychological or emotional experimentation?",
                "Should it include chance operations or randomness?",
                "What historical experimental music influences?",
                "Should it use unconventional recording techniques?",
                "What accessibility despite experimental nature?",
                "Should it include spoken word, poetry, or text elements?",
                "What therapeutic or healing experimental approaches?",
                "Should it explore silence, space, or negative space?",
                "What scientific or mathematical concepts in music?",
                "Should it include audience participation or co-creation?",
                "What environmental or ecological sound exploration?",
                "Should it challenge traditional performer-audience relationships?",
                "What technology-human interaction examination?",
                "Should it include elements of other art forms?",
                "What cultural appropriation awareness and respect?",
                "Should it document disappearing or endangered sounds?",
                "What meditation, mindfulness, or consciousness exploration?",
                "Should it include industrial, urban, or machine sounds?",
                "What time-based or durational concepts?",
                "Should it explore memory, nostalgia, or temporal displacement?",
                "What community or collaborative creation processes?",
                "Should it include elements of chance or unpredictability?",
                "What institutional or academic experimental context?",
                "Should it challenge or support existing power structures?",
                "What documentation or archival purposes?",
                "Should it include cross-sensory or synesthetic experiences?",
                "What educational or pedagogical experimental goals?",
                "Should it explore identity, gender, or social construction themes?",
                "What planet or cosmic scale sonic exploration?",
                "What specific experimental music tradition or innovation to contribute to?"
            ],
            'Vocal': [
                "What vocal style (classical, pop, jazz, folk, experimental)?",
                "What vocal range and tessitura to feature?",
                "Should it be solo or include background vocals?",
                "What language or linguistic elements?",
                "Should it showcase technical virtuosity or emotional expression?",
                "What accompaniment (piano, orchestra, a cappella, band)?",
                "What emotional or narrative content?",
                "Should it include extended vocal techniques?",
                "What cultural or traditional vocal influences?",
                "Should it be original composition or interpretation?",
                "What recording environment (studio, live, concert hall)?",
                "Should it include improvisation or scripted elements?",
                "What audience demographic and listening context?",
                "Should it feature multiple vocalists or harmony?",
                "What tempo and rhythmic complexity?",
                "Should it include instrumental interludes or pure vocal?",
                "What microphone technique and production style?",
                "Should it tell a story or express abstract emotions?",
                "What seasonal or themed content?",
                "Should it include vocal effects or processing?",
                "What collaboration with instrumentalists or producers?",
                "Should it feature call-and-response or antiphonal elements?",
                "What regional dialect or accent considerations?",
                "Should it include spoken word or recitative sections?",
                "What breath control and phrasing demonstration?",
                "Should it adapt existing repertoire or create new work?",
                "What therapeutic or healing vocal applications?",
                "Should it include audience participation or sing-along elements?",
                "What historical period or style reference?",
                "Should it feature vocal percussion or beatboxing?",
                "What gender, age, or identity representation through voice?",
                "Should it include environmental or nature sound integration?",
                "What spiritual, religious, or meditative vocal traditions?",
                "Should it showcase vocal coaching or pedagogical elements?",
                "What cross-cultural or world music vocal influences?",
                "Should it include dramatic or theatrical vocal expression?",
                "What technology integration (auto-tune, vocoder, live processing)?",
                "Should it feature community or choir elements?",
                "What awards, competition, or academic assessment preparation?",
                "Should it include vocal warm-ups or exercise demonstrations?",
                "What emotional range and dynamic expression?",
                "Should it feature vocal arrangement or composition skills?",
                "What accessibility for different hearing abilities?",
                "Should it include multilingual or code-switching elements?",
                "What professional development or career showcase goals?",
                "Should it demonstrate vocal health and sustainability practices?",
                "What intergenerational or traditional knowledge transmission?",
                "Should it include innovation in vocal performance or technique?",
                "What community building or social connection through voice?",
                "What specific vocal artistry or technical achievement goal?"
            ],
            'Commercial': [
                "What product, service, or brand is being advertised?",
                "What target demographic and psychographic profile?",
                "What call-to-action or desired consumer behavior?",
                "Should it be jingle, background music, or featured song?",
                "What brand personality and values to convey?",
                "What emotional association or memory creation?",
                "Should it include vocals with product name or slogan?",
                "What length requirements (15, 30, 60 seconds or longer)?",
                "What media placement (TV, radio, online, in-store)?",
                "Should it be original composition or licensed existing music?",
                "What cultural or seasonal relevance?",
                "Should it include sound effects or brand audio signatures?",
                "What genre or style alignment with target audience?",
                "Should it be energetic and upbeat or calm and sophisticated?",
                "What competitive differentiation in sound and message?",
                "Should it include testimonials or user-generated content?",
                "What local or regional customization needs?",
                "Should it appeal to multiple age groups or be age-specific?",
                "What cross-platform consistency and adaptability?",
                "Should it include interactive or social media integration?",
                "What psychological triggers or behavioral economics integration?",
                "Should it feature celebrity endorsements or influencer elements?",
                "What urgency or time-limited offer communication?",
                "Should it include pricing or value proposition highlights?",
                "What storytelling or narrative advertising approach?",
                "Should it align with broader marketing campaign themes?",
                "What accessibility and inclusive advertising practices?",
                "Should it include humor, drama, or straightforward information?",
                "What sustainability or social responsibility messaging?",
                "Should it create viral or shareable content potential?",
                "What data privacy or ethical advertising considerations?",
                "Should it include augmented reality or interactive audio features?",
                "What global or international market adaptation?",
                "Should it feature user experience or customer journey mapping?",
                "What A/B testing or market research optimization?",
                "Should it include crisis communication or brand repair elements?",
                "What loyalty program or repeat customer targeting?",
                "Should it integrate with e-commerce or direct sales platforms?",
                "What influencer marketing or user-generated content integration?",
                "Should it include educational or how-to informational content?",
                "What partnership or collaboration highlighting?",
                "Should it feature innovation, technology, or future-forward messaging?",
                "What community building or brand advocacy encouragement?",
                "Should it include awards, recognition, or credibility indicators?",
                "What customer service or support integration messaging?",
                "Should it optimize for voice search or smart device compatibility?",
                "What measuring success metrics or KPI tracking integration?",
                "Should it include personalization or customization messaging?",
                "What specific business outcome or conversion goal optimization?",
                "What brand legacy or long-term relationship building focus?"
            ],
            'Voice Over': [
                "What type of voice over (commercial, narration, character, educational)?",
                "Who is the target audience demographic?",
                "What tone and personality should the voice convey?",
                "What accent, dialect, or regional speech pattern?",
                "Should it be male, female, or non-binary voice?",
                "What age range should the voice represent?",
                "What pacing and rhythm requirements?",
                "Should it include emotional range or stay consistent?",
                "What industry or subject matter expertise to convey?",
                "Should it be conversational or formal/professional?",
                "What recording quality and technical specifications?",
                "Should it include multiple voices or just one?",
                "What script length and delivery time requirements?",
                "Should it be energetic and enthusiastic or calm and soothing?",
                "What cultural sensitivity and representation considerations?",
                "Should it include character voices or impressions?",
                "What pronunciation and enunciation standards?",
                "Should it adapt for different media formats?",
                "What background music or sound effects integration?",
                "Should it include interactive or responsive elements?",
                "What brand voice consistency with existing materials?",
                "Should it feature storytelling or straightforward information delivery?",
                "What accessibility features for hearing impaired audiences?",
                "Should it include multiple language versions or translations?",
                "What revision and direction feedback incorporation?",
                "Should it optimize for different playback devices and environments?",
                "What copyright and usage rights considerations?",
                "Should it include breath control and natural pause patterns?",
                "What emotional intelligence and empathy demonstration?",
                "Should it feature improvisation or strict script adherence?",
                "What cost and budget considerations for voice talent?",
                "Should it include singing or musical elements?",
                "What deadline and turnaround time requirements?",
                "Should it align with visual content or stand alone?",
                "What competitive analysis and differentiation needs?",
                "Should it include call-to-action or engagement elements?",
                "What testing and focus group feedback integration?",
                "Should it feature authority and credibility establishment?",
                "What seasonal or timely content adaptation?",
                "Should it include humor or entertainment elements?",
                "What technical jargon or specialized terminology handling?",
                "Should it optimize for different age groups or accessibility needs?",
                "What global or international audience considerations?",
                "Should it include emergency or crisis communication elements?",
                "What therapeutic or wellness application voice requirements?",
                "Should it feature education or training content delivery?",
                "What customer service or support voice requirements?",
                "Should it include technology integration (AI, voice assistants)?",
                "What brand personality and marketing message alignment?",
                "What specific communication goal or audience impact objective?"
            ],

            # TEXT CATEGORY
            'Business': [
                "What type of business document (proposal, report, email, presentation)?",
                "Who is your target audience (executives, clients, employees, investors)?",
                "What is the main objective or call-to-action?",
                "What tone should be used (formal, professional, approachable, authoritative)?",
                "What industry or business sector context?",
                "Should it include data, statistics, or research findings?",
                "What length and format requirements?",
                "Should it follow specific corporate style guidelines?",
                "What decision-making or approval process does it support?",
                "Should it include financial information or projections?",
                "What competitive analysis or market research integration?",
                "Should it address risks, challenges, or mitigation strategies?",
                "What timeline or deadline information to include?",
                "Should it feature case studies or success stories?",
                "What compliance or regulatory considerations?",
                "Should it include visual aids or supporting documents?",
                "What collaboration or team input requirements?",
                "Should it address sustainability or social responsibility?",
                "What technology or innovation integration?",
                "Should it include implementation plans or next steps?",
                "What budget or resource allocation information?",
                "Should it feature partnership or vendor information?",
                "What international or global market considerations?",
                "Should it include training or educational components?",
                "What quality assurance or performance metrics?",
                "Should it address customer feedback or market research?",
                "What legal or contractual elements to include?",
                "Should it feature employee or stakeholder communication?",
                "What crisis management or contingency planning?",
                "Should it include brand positioning or marketing strategy?",
                "What operational efficiency or process improvement focus?",
                "Should it address digital transformation or technology adoption?",
                "What supply chain or logistics considerations?",
                "Should it include human resources or talent management?",
                "What intellectual property or competitive advantage discussion?",
                "Should it feature customer acquisition or retention strategies?",
                "What environmental or sustainability impact assessment?",
                "Should it include merger, acquisition, or partnership evaluation?",
                "What governance or organizational structure information?",
                "Should it address cultural change or transformation initiatives?",
                "What performance evaluation or assessment criteria?",
                "Should it include market trends or industry analysis?",
                "What innovation or research and development focus?",
                "Should it address scalability or growth planning?",
                "What stakeholder communication or change management?",
                "Should it include benchmarking or best practices comparison?",
                "What cost-benefit analysis or ROI calculation?",
                "Should it address regulatory compliance or audit preparation?",
                "What strategic planning or vision articulation?",
                "What specific business outcome or success metric to optimize for?"
            ],
            'Blog': [
                "What blog topic or niche area?",
                "Who is your target reader persona?",
                "What blog post type (how-to, listicle, opinion, review, news)?",
                "What tone and writing style (casual, expert, humorous, serious)?",
                "What length target (short-form, long-form, comprehensive)?",
                "Should it be SEO-optimized for specific keywords?",
                "What expertise level to assume in readers?",
                "Should it include personal experiences or stick to facts?",
                "What call-to-action or engagement goal?",
                "Should it include images, videos, or multimedia elements?",
                "What publishing platform and formatting requirements?",
                "Should it be evergreen content or timely/trending?",
                "What research sources and citations to include?",
                "Should it encourage comments, shares, or discussion?",
                "What brand voice and personality to convey?",
                "Should it include affiliate links or monetization elements?",
                "What social media sharing and promotion strategy?",
                "Should it be part of a series or stand-alone piece?",
                "What controversial or sensitive topic handling?",
                "Should it include expert interviews or quotes?",
                "What geographic or cultural considerations?",
                "Should it feature case studies or real examples?",
                "What accessibility and inclusive writing practices?",
                "Should it include interactive elements (polls, quizzes, forms)?",
                "What competitor analysis or differentiation?",
                "Should it address common questions or pain points?",
                "What seasonal or event-based timing relevance?",
                "Should it include actionable tips or takeaways?",
                "What email list building or lead generation integration?",
                "Should it feature guest contributions or collaborations?",
                "What fact-checking and accuracy verification?",
                "Should it include trends, predictions, or future outlook?",
                "What crisis communication or reputation management?",
                "Should it address beginner, intermediate, or advanced audiences?",
                "What visual content or infographic integration?",
                "Should it include product reviews or recommendations?",
                "What community building and reader engagement?",
                "Should it feature behind-the-scenes or personal insights?",
                "What educational or tutorial content elements?",
                "Should it include data analysis or research findings?",
                "What storytelling or narrative structure approach?",
                "Should it address myths, misconceptions, or controversies?",
                "What influencer or thought leader positioning?",
                "Should it include resource lists or curated content?",
                "What cross-promotion with other content or platforms?",
                "Should it feature user-generated content or testimonials?",
                "What local or regional relevance and customization?",
                "Should it include technological innovation or trend analysis?",
                "What specific reader action or behavior change goal?",
                "What long-term content strategy and archive building contribution?"
            ],
            'Social Media': [
                "What social media platform (Facebook, Instagram, Twitter, LinkedIn, TikTok)?",
                "What type of post (text, image, video, story, reel, thread)?",
                "Who is your target audience demographic?",
                "What is the main message or call-to-action?",
                "What tone and personality (professional, casual, humorous, inspirational)?",
                "Should it include hashtags and which ones?",
                "What engagement goal (likes, shares, comments, saves, clicks)?",
                "Should it be promotional, educational, or entertaining?",
                "What brand voice and visual identity consistency?",
                "Should it include user-generated content or mentions?",
                "What timing and posting schedule optimization?",
                "Should it leverage trending topics or current events?",
                "What caption length and format for the platform?",
                "Should it include links to external content or websites?",
                "What community building or conversation starting elements?",
                "Should it feature behind-the-scenes or personal content?",
                "What seasonal or holiday relevance?",
                "Should it include contests, giveaways, or interactive elements?",
                "What crisis communication or reputation management needs?",
                "Should it showcase products, services, or company culture?",
                "What influencer collaboration or partnership integration?",
                "Should it include educational or how-to content?",
                "What local or geographic targeting considerations?",
                "Should it feature customer testimonials or success stories?",
                "What cross-platform content adaptation and consistency?",
                "Should it include live streaming or real-time content?",
                "What accessibility features (alt text, captions, descriptions)?",
                "Should it drive traffic to other platforms or content?",
                "What A/B testing or content optimization strategy?",
                "Should it include social proof or credibility indicators?",
                "What viral or shareability potential maximization?",
                "Should it feature employee advocacy or team members?",
                "What industry thought leadership or expertise demonstration?",
                "Should it include corporate social responsibility or values messaging?",
                "What direct sales or conversion optimization?",
                "Should it feature event promotion or live coverage?",
                "What crisis response or transparent communication?",
                "Should it include research, data, or industry insights?",
                "What community guidelines and platform policy compliance?",
                "Should it feature partnerships, collaborations, or sponsorships?",
                "What content series or campaign integration?",
                "Should it include motivational or inspirational messaging?",
                "What customer service or support integration?",
                "Should it feature innovation, technology, or future trends?",
                "What diversity, inclusion, and representation considerations?",
                "Should it include sustainability or environmental messaging?",
                "What analytics and performance measurement integration?",
                "Should it optimize for algorithm changes and platform updates?",
                "What specific business objective or KPI optimization?",
                "What long-term brand building and community development contribution?"
            ],
            'Academic': [
                "What academic discipline or field of study?",
                "What type of academic writing (essay, research paper, thesis, dissertation)?",
                "What academic level (undergraduate, graduate, doctoral)?",
                "Who is the intended audience (professors, peers, general academic community)?",
                "What citation style (APA, MLA, Chicago, Harvard)?",
                "Should it include original research or literature review?",
                "What thesis statement or research question focus?",
                "Should it follow specific institutional guidelines?",
                "What research methodology or theoretical framework?",
                "Should it include empirical data or qualitative analysis?",
                "What literature review scope and depth?",
                "Should it address current debates or fill knowledge gaps?",
                "What ethical considerations or IRB approval requirements?",
                "Should it include peer review or collaborative elements?",
                "What interdisciplinary or cross-field integration?",
                "Should it feature case studies or applied examples?",
                "What geographic or cultural context considerations?",
                "Should it include policy implications or practical applications?",
                "What historical context or temporal analysis?",
                "Should it feature comparative analysis or cross-case studies?",
                "What statistical analysis or quantitative methods?",
                "Should it address limitations and future research directions?",
                "What theoretical contributions or framework development?",
                "Should it include appendices, supplementary materials, or data?",
                "What conference presentation or publication goals?",
                "Should it feature collaboration with other researchers or institutions?",
                "What funding acknowledgments or grant requirement compliance?",
                "Should it address reproducibility or open science practices?",
                "What technology or digital humanities integration?",
                "Should it include visual aids, charts, or multimedia elements?",
                "What accessibility and inclusive scholarship practices?",
                "Should it feature public engagement or knowledge translation?",
                "What career development or academic advancement goals?",
                "Should it address contemporary social issues or current events?",
                "What international or global perspective integration?",
                "Should it include practitioner or industry perspectives?",
                "What innovation or novel approach demonstration?",
                "Should it feature longitudinal or temporal analysis?",
                "What risk assessment or ethical framework consideration?",
                "Should it include technology transfer or commercialization potential?",
                "What community-based participatory research elements?",
                "Should it address sustainability or environmental considerations?",
                "What health, safety, or public policy implications?",
                "Should it feature digital preservation or archival considerations?",
                "What cultural competency or diverse perspective integration?",
                "Should it include capacity building or educational outreach?",
                "What intellectual property or open access considerations?",
                "Should it address bias, validity, or methodological rigor?",
                "What specific contribution to knowledge or field advancement goal?",
                "What impact measurement or citation potential optimization?"
            ],
            'Fiction': [
                "What genre (fantasy, romance, mystery, sci-fi, literary, horror)?",
                "What target audience age group and demographic?",
                "What length (short story, novella, novel, flash fiction)?",
                "What point of view (first person, third person, omniscient)?",
                "Who are the main characters and their motivations?",
                "What setting (time period, location, world-building details)?",
                "What central conflict or plot structure?",
                "What themes or deeper messages to explore?",
                "Should it be part of a series or standalone work?",
                "What tone and mood (dark, humorous, romantic, suspenseful)?",
                "Should it include diverse characters and representation?",
                "What dialogue style and character voice development?",
                "Should it feature plot twists or surprise elements?",
                "What pacing (fast-paced action, slow burn, varied)?",
                "Should it include romance or relationship subplots?",
                "What level of violence, adult content, or sensitive topics?",
                "Should it incorporate real-world issues or pure escapism?",
                "What research requirements for accuracy and authenticity?",
                "Should it include unique or experimental narrative techniques?",
                "What publication goals (traditional, self-publishing, online)?",
                "Should it feature strong opening hooks and cliffhangers?",
                "What character development arcs and growth?",
                "Should it include detailed descriptions or focus on action?",
                "What cultural or historical accuracy considerations?",
                "Should it appeal to specific fan communities or broad audiences?",
                "What world-building complexity and consistency?",
                "Should it include maps, appendices, or supplementary materials?",
                "What beta reader feedback and revision integration?",
                "Should it feature trigger warnings or content advisories?",
                "What marketing and promotional considerations?",
                "Should it include current technology or social media integration?",
                "What accessibility considerations for different readers?",
                "Should it feature multiple timelines or narrative perspectives?",
                "What environmental or social justice themes?",
                "Should it include elements of other media (film, gaming, music)?",
                "What intellectual property or trademark considerations?",
                "Should it feature fan fiction or derivative work elements?",
                "What educational or informational content integration?",
                "Should it include interactive or multimedia elements?",
                "What translation or international market considerations?",
                "Should it feature collaborative writing or co-authorship?",
                "What adaptation potential for other media formats?",
                "Should it include community building or reader engagement strategies?",
                "What awards or recognition submission considerations?",
                "Should it address mental health or therapeutic themes?",
                "What LGBTQ+ representation or inclusive storytelling?",
                "Should it feature regional dialects or linguistic diversity?",
                "What climate change or futurism themes?",
                "Should it include economic or political commentary?",
                "What specific emotional or inspirational impact goal for readers?"
            ],
            'Non-Fiction': [
                "What non-fiction category (memoir, biography, self-help, history, science)?",
                "Who is your target reader demographic?",
                "What expertise or credentials do you bring to the topic?",
                "Should it be narrative-driven or informational/instructional?",
                "What research methodology and source verification?",
                "Should it include personal experiences or stick to objective facts?",
                "What length and chapter structure organization?",
                "Should it include interviews, case studies, or expert opinions?",
                "What tone (academic, conversational, authoritative, accessible)?",
                "Should it feature actionable advice or theoretical exploration?",
                "What visual aids, charts, or supplementary materials?",
                "Should it address current events or timeless principles?",
                "What fact-checking and accuracy verification processes?",
                "Should it include controversial topics or maintain neutrality?",
                "What publication timeline and market timing considerations?",
                "Should it feature collaboration with experts or co-authors?",
                "What platform building and author platform integration?",
                "Should it include interactive elements or multimedia components?",
                "What accessibility and inclusive writing practices?",
                "Should it address international or global perspectives?",
                "What legal considerations or potential liability issues?",
                "Should it include extensive bibliography and citation?",
                "What peer review or expert validation processes?",
                "Should it feature practical exercises or implementation guides?",
                "What cultural sensitivity and representation considerations?",
                "Should it include personal anecdotes or maintain professional distance?",
                "What current research and cutting-edge information integration?",
                "Should it address myth-busting or misconception correction?",
                "What policy implications or social change advocacy?",
                "Should it include future predictions or trend analysis?",
                "What industry insider knowledge or behind-the-scenes insights?",
                "Should it feature multiple perspectives or maintain single viewpoint?",
                "What environmental or sustainability angle integration?",
                "Should it include technology or digital transformation themes?",
                "What health, wellness, or personal development focus?",
                "Should it address economic or financial literacy topics?",
                "What crisis management or resilience building themes?",
                "Should it include diversity, equity, and inclusion perspectives?",
                "What educational or skill development applications?",
                "Should it feature business or entrepreneurship insights?",
                "What historical context or lessons learned integration?",
                "Should it include psychological or behavioral science elements?",
                "What community building or social connection themes?",
                "Should it address generational differences or age-specific concerns?",
                "What innovation or creative thinking development?",
                "Should it include spiritual or philosophical exploration?",
                "What practical resource lists or directory information?",
                "Should it feature transformation stories or before/after case studies?",
                "What specific knowledge transfer or skill building goal?",
                "What lasting impact or legacy creation objective for readers?"
            ],
            'Marketing': [
                "What marketing channel or medium (email, web, print, social, video)?",
                "What stage of the customer journey (awareness, consideration, decision, retention)?",
                "Who is your ideal customer persona?",
                "What is your unique value proposition or key differentiator?",
                "What action do you want the audience to take?",
                "What tone and brand voice should be used?",
                "Should it include emotional appeals or logical arguments?",
                "What pain points or challenges does it address?",
                "Should it include social proof or testimonials?",
                "What urgency or scarcity elements to incorporate?",
                "Should it be educational or purely promotional?",
                "What competitive advantages to highlight?",
                "Should it include pricing or promotional offers?",
                "What cultural or demographic customization needs?",
                "Should it feature storytelling or straightforward benefits?",
                "What length and format constraints?",
                "Should it include technical specifications or emotional benefits?",
                "What seasonal or event-based timing considerations?",
                "Should it address objections or concerns proactively?",
                "What multi-channel integration and consistency requirements?",
                "Should it include interactive or engaging elements?",
                "What accessibility and inclusive marketing practices?",
                "Should it feature user-generated content or community elements?",
                "What data privacy or ethical marketing considerations?",
                "Should it include partnership or collaboration messaging?",
                "What local or geographic targeting and customization?",
                "Should it address sustainability or social responsibility?",
                "What technology or innovation showcase requirements?",
                "Should it include thought leadership or expertise positioning?",
                "What crisis communication or reputation management needs?",
                "Should it feature employee advocacy or behind-the-scenes content?",
                "What influencer or celebrity endorsement integration?",
                "Should it include educational or how-to content?",
                "What retargeting or remarketing optimization?",
                "Should it address multiple buyer personas or single focus?",
                "What A/B testing or optimization strategy integration?",
                "Should it include cross-selling or upselling opportunities?",
                "What compliance with advertising regulations and standards?",
                "Should it feature case studies or success stories?",
                "What omnichannel experience and touchpoint integration?",
                "Should it include gamification or interactive elements?",
                "What personalization or dynamic content capabilities?",
                "Should it address international or global market expansion?",
                "What loyalty program or repeat customer targeting?",
                "Should it include augmented reality or immersive experiences?",
                "What voice search or smart device optimization?",
                "Should it feature community building or brand advocacy?",
                "What analytics and performance measurement integration?",
                "Should it optimize for mobile-first or multi-device experiences?",
                "What specific conversion metric or business outcome optimization goal?"
            ],

            # VIDEO CATEGORY
            'Short Film': [
                "What genre (drama, comedy, horror, sci-fi, documentary, experimental)?",
                "What is the target length (under 5 min, 5-15 min, 15-30 min)?",
                "Who is your target audience demographic?",
                "What is the central story or message?",
                "What budget range and production constraints?",
                "Should it be dialogue-heavy or visually driven?",
                "What filming locations and settings?",
                "How many characters and what casting requirements?",
                "What visual style and cinematography approach?",
                "Should it include original music or sound design?",
                "What festival submission or distribution goals?",
                "Should it be part of a series or standalone piece?",
                "What social issues or themes to address?",
                "Should it include special effects or practical effects?",
                "What equipment and technical requirements?",
                "Should it feature professional actors or non-actors?",
                "What post-production complexity and timeline?",
                "Should it include voice-over or narration?",
                "What color palette and mood requirements?",
                "Should it be linear narrative or experimental structure?",
                "What cultural or regional representation?",
                "Should it include subtitles or multiple language versions?",
                "What accessibility features for different audiences?",
                "Should it be autobiographical or fictional?",
                "What collaboration with other filmmakers or artists?",
                "Should it address current events or timeless themes?",
                "What educational or social impact goals?",
                "Should it include animation or mixed media elements?",
                "What rights clearance and legal considerations?",
                "Should it be commercial or artistic in focus?",
                "What technology or innovation showcase?",
                "Should it include environmental or sustainability themes?",
                "What community involvement or local talent integration?",
                "Should it feature diverse casting and representation?",
                "What mental health or social awareness messaging?",
                "Should it include historical or period elements?",
                "What interactive or immersive elements?",
                "Should it be optimized for specific platforms (YouTube, Vimeo, festivals)?",
                "What behind-the-scenes or making-of content creation?",
                "Should it include crowdfunding or community support elements?",
                "What awards or recognition submission strategy?",
                "Should it feature emerging technology (VR, AR, 360°)?",
                "What therapeutic or healing storytelling applications?",
                "Should it include fan engagement or community building?",
                "What cross-media adaptation or transmedia potential?",
                "Should it address economic or political themes?",
                "What generational or intergenerational storytelling?",
                "Should it include climate change or environmental advocacy?",
                "What specific emotional or social impact goal?",
                "What legacy or long-term artistic contribution objective?"
            ],
            'Commercial': [
                "What product, service, or brand is being advertised?",
                "What is the target demographic and psychographic profile?",
                "What is the main selling point or value proposition?",
                "What length requirement (15, 30, 60 seconds, longer form)?",
                "What media placement (TV, online, social media, in-store)?",
                "What call-to-action or desired consumer behavior?",
                "What brand personality and tone to convey?",
                "Should it include spokesperson, voice-over, or be visual-only?",
                "What budget constraints and production requirements?",
                "Should it be humorous, emotional, informative, or dramatic?",
                "What competitive differentiation to highlight?",
                "Should it include product demonstrations or lifestyle imagery?",
                "What seasonal or campaign timing considerations?",
                "Should it feature real customers or professional actors?",
                "What filming locations and production complexity?",
                "Should it include music, jingle, or sound effects?",
                "What accessibility and inclusive advertising practices?",
                "Should it address social responsibility or values?",
                "What cross-platform adaptation and consistency?",
                "Should it include interactive or shoppable elements?",
                "What celebrity endorsements or influencer integration?",
                "Should it feature employee or company culture elements?",
                "What local or regional customization needs?",
                "Should it include testimonials or user-generated content?",
                "What crisis communication or reputation management?",
                "Should it feature innovation or technology highlights?",
                "What emotional storytelling or rational benefit focus?",
                "Should it include partnership or collaboration messaging?",
                "What regulatory compliance and advertising standards?",
                "Should it feature urgency or limited-time offer elements?",
                "What premium or luxury vs. value positioning?",
                "Should it include environmental or sustainability messaging?",
                "What multi-generational or age-inclusive appeal?",
                "Should it feature diversity and representation authentically?",
                "What data privacy or transparency messaging?",
                "Should it include educational or how-to content?",
                "What community building or brand advocacy encouragement?",
                "Should it feature awards, recognition, or credibility indicators?",
                "What subscription or loyalty program promotion?",
                "Should it include augmented reality or interactive features?",
                "What voice search or smart device compatibility?",
                "Should it feature customer service or support integration?",
                "What global or international market adaptation?",
                "Should it include cause marketing or social impact themes?",
                "What analytics and performance measurement integration?",
                "Should it optimize for mobile-first viewing?",
                "What A/B testing or creative variation strategy?",
                "Should it include direct response or e-commerce integration?",
                "What specific business KPI or conversion metric optimization?",
                "What long-term brand building vs. immediate sales focus?"
            ],
            'Animation': [
                "What animation style (2D, 3D, stop-motion, mixed media)?",
                "What target audience age group and interests?",
                "What story genre (adventure, comedy, educational, fantasy)?",
                "What length and episode structure (short, series, feature)?",
                "Should it include dialogue or be purely visual?",
                "What art style and visual aesthetic?",
                "Should it feature original characters or existing IP?",
                "What educational or entertainment balance?",
                "Should it include music and sound design?",
                "What production timeline and budget considerations?",
                "Should it be hand-drawn or computer-generated?",
                "What cultural representation and diversity?",
                "Should it include moral lessons or social messages?",
                "What violence or content rating appropriateness?",
                "Should it feature celebrity voice actors or unknowns?",
                "What distribution platform optimization?",
                "Should it include interactive or educational elements?",
                "What merchandising or transmedia potential?",
                "Should it address current social issues or be timeless?",
                "What accessibility features (subtitles, audio description)?",
                "Should it include multiple language versions?",
                "What technological innovation or techniques showcase?",
                "Should it feature environmental or sustainability themes?",
                "What collaboration with educational institutions?",
                "Should it include historical or cultural education?",
                "What mental health or emotional intelligence themes?",
                "Should it feature STEM education or scientific concepts?",
                "What family viewing or cross-generational appeal?",
                "Should it include religious or spiritual themes?",
                "What economic or financial literacy education?",
                "Should it address bullying or social inclusion?",
                "What physical activity or health promotion?",
                "Should it include creativity or artistic expression encouragement?",
                "What critical thinking or problem-solving skills?",
                "Should it feature community service or civic engagement?",
                "What cultural exchange or global awareness?",
                "Should it include career exploration or life skills?",
                "What disability awareness or inclusion themes?",
                "Should it address digital citizenship or online safety?",
                "What emotional regulation or mindfulness concepts?",
                "Should it include cooking, nutrition, or healthy living?",
                "What music, arts, or creative expression integration?",
                "Should it feature animal welfare or conservation themes?",
                "What friendship, family, or relationship dynamics?",
                "Should it include adventure or exploration encouragement?",
                "What reading, literacy, or language learning support?",
                "Should it address change, resilience, or adaptation?",
                "What innovation, invention, or creative thinking?",
                "Should it include therapeutic or healing storytelling?",
                "What specific developmental or educational outcome goal?"
            ],
            'Tutorial': [
                "What skill or topic is being taught?",
                "What is the target audience skill level (beginner, intermediate, advanced)?",
                "What learning objectives should be achieved?",
                "What video length and pacing requirements?",
                "Should it include hands-on practice or theory only?",
                "What equipment or materials are needed for viewers?",
                "Should it be step-by-step or overview approach?",
                "What visual aids or graphics should be included?",
                "Should it feature screen recording or live demonstration?",
                "What voice-over or on-camera presentation style?",
                "Should it include captions or subtitles?",
                "What follow-up resources or materials to provide?",
                "Should it be part of a series or standalone tutorial?",
                "What common mistakes or troubleshooting to address?",
                "Should it include assessment or practice exercises?",
                "What accessibility features for different learning needs?",
                "Should it be platform-specific or general instruction?",
                "What interaction or engagement elements to include?",
                "Should it feature multiple instructors or single presenter?",
                "What cultural or regional adaptation considerations?",
                "Should it include real-world applications or examples?",
                "What safety considerations or warnings to include?",
                "Should it address different learning styles?",
                "What prerequisites or background knowledge assumptions?",
                "Should it include cost breakdowns or budget considerations?",
                "What time requirements and commitment expectations?",
                "Should it feature before/after examples or results?",
                "What tools or software version compatibility?",
                "Should it include community or peer learning elements?",
                "What certification or completion recognition?",
                "Should it address industry standards or best practices?",
                "What legal or compliance considerations to cover?",
                "Should it include alternative methods or approaches?",
                "What quality control or validation checkpoints?",
                "Should it feature guest experts or interviews?",
                "What environmental or workspace setup requirements?",
                "Should it include downloadable resources or templates?",
                "What feedback or questions handling strategy?",
                "Should it address advanced techniques or variations?",
                "What career or professional development integration?",
                "Should it include historical context or background?",
                "What technology updates or future-proofing considerations?",
                "Should it feature collaborative or group learning elements?",
                "What ethical considerations or responsible practice?",
                "Should it include innovation or creative adaptation encouragement?",
                "What maintenance or ongoing skill development?",
                "Should it address different age groups or demographics?",
                "What cross-cultural or international applications?",
                "Should it include sustainability or environmental consciousness?",
                "What specific skill mastery or competency achievement goal?"
            ],
            'Music Video': [
                "What music genre and song characteristics?",
                "Who is the target audience demographic?",
                "What is the song's mood and emotional content?",
                "Should it be performance-based or narrative storytelling?",
                "What budget and production scale requirements?",
                "Should it feature the artist(s) prominently or focus on visuals?",
                "What visual style and aesthetic direction?",
                "Should it include choreography or dance elements?",
                "What locations or sets are needed?",
                "Should it be concept-driven or straightforward performance?",
                "What special effects or post-production needs?",
                "Should it include multiple outfit or look changes?",
                "What color palette and lighting design?",
                "Should it feature guest appearances or collaborations?",
                "What platform optimization (YouTube, MTV, social media)?",
                "Should it include behind-the-scenes or making-of content?",
                "What cultural or social message integration?",
                "Should it be appropriate for radio/TV or uncensored?",
                "What product placement or brand integration?",
                "Should it include fan participation or user-generated content?",
                "What award show or festival submission considerations?",
                "Should it feature diverse representation and inclusion?",
                "What accessibility features (captions, audio description)?",
                "Should it include multiple language or regional versions?",
                "What merchandising or promotional tie-in opportunities?",
                "Should it address current events or social issues?",
                "What interactive or immersive elements (VR, AR)?",
                "Should it feature environmental or sustainability themes?",
                "What collaboration with visual artists or directors?",
                "Should it include animation or mixed media elements?",
                "What historical or period setting requirements?",
                "Should it feature community or local talent?",
                "What charity or cause awareness integration?",
                "Should it include educational or awareness messaging?",
                "What technology or innovation showcase?",
                "Should it feature mental health or wellness themes?",
                "What generational or nostalgic elements?",
                "Should it include sports or competition themes?",
                "What fashion or style trendsetting potential?",
                "Should it feature travel or location showcasing?",
                "What family or relationship dynamics representation?",
                "Should it include empowerment or inspirational messaging?",
                "What artistic or creative expression celebration?",
                "Should it feature cultural heritage or tradition celebration?",
                "What economic or social justice themes?",
                "Should it include comedy or humorous elements?",
                "What seasonal or holiday themed content?",
                "Should it feature innovation in music video format or technology?",
                "What specific emotional or cultural impact goal?",
                "What career milestone or artistic statement objective?"
            ],
            'Documentary': [
                "What subject or topic is the documentary exploring?",
                "What angle or perspective will you take on the topic?",
                "Who is your target audience?",
                "What length format (short, feature-length, series)?",
                "Should it be observational or investigative style?",
                "What research and fact-checking requirements?",
                "Should it include interviews with experts or subjects?",
                "What archival footage or historical material access?",
                "Should it maintain objectivity or advocate for a position?",
                "What sensitive or controversial aspects to handle?",
                "Should it include narrator voice-over or let subjects speak?",
                "What ethical considerations and consent requirements?",
                "Should it feature multiple perspectives or single viewpoint?",
                "What visual style and cinematography approach?",
                "Should it include reenactments or dramatizations?",
                "What distribution and platform goals?",
                "Should it address current events or historical topics?",
                "What legal clearances and rights management?",
                "Should it include data visualization or infographics?",
                "What accessibility features for different audiences?",
                "Should it feature international or global perspectives?",
                "What environmental or location shooting requirements?",
                "Should it include educational or academic collaboration?",
                "What community impact or social change goals?",
                "Should it address underrepresented voices or stories?",
                "What funding sources and budget considerations?",
                "Should it include interactive or transmedia elements?",
                "What follow-up action or engagement strategy?",
                "Should it feature expert analysis or lay perspectives?",
                "What timeline and production schedule constraints?",
                "Should it include personal stories or macro analysis?",
                "What cultural sensitivity and representation accuracy?",
                "Should it address policy implications or solutions?",
                "What technology or innovation documentation?",
                "Should it include crisis communication or urgent issues?",
                "What intergenerational or historical continuity themes?",
                "Should it feature scientific or research-based evidence?",
                "What economic or financial system analysis?",
                "Should it include environmental or climate change focus?",
                "What health, medicine, or public safety topics?",
                "Should it address education or learning system issues?",
                "What criminal justice or legal system examination?",
                "Should it feature arts, culture, or creative expression?",
                "What political or governance system analysis?",
                "Should it include technology impact or digital transformation?",
                "What migration, immigration, or demographic change focus?",
                "Should it address mental health or social wellness?",
                "What corporate or institutional accountability examination?",
                "Should it feature community resilience or adaptation stories?",
                "What specific awareness, education, or action goal for viewers?"
            ],
            'Social Media': [
                "What social media platform (TikTok, Instagram Reels, YouTube Shorts, Facebook)?",
                "What video length constraint (15 sec, 30 sec, 1 min, longer)?",
                "Who is your target audience demographic?",
                "What type of content (entertainment, educational, promotional, behind-the-scenes)?",
                "What is your main message or call-to-action?",
                "Should it be trending topic or evergreen content?",
                "What visual style and aesthetic consistency with brand?",
                "Should it include text overlays or captions?",
                "What music or audio considerations (trending sounds, original)?",
                "Should it be scripted or improvised/authentic?",
                "What hashtag strategy and discoverability optimization?",
                "Should it include product placement or subtle marketing?",
                "What engagement encouragement (likes, shares, comments, saves)?",
                "Should it feature multiple people or solo content?",
                "What location or setting requirements?",
                "Should it include current events or cultural moment references?",
                "What accessibility features (captions, audio descriptions)?",
                "Should it be part of a series or campaign?",
                "What user-generated content or community involvement?",
                "Should it include challenges or interactive elements?",
                "What brand consistency vs. platform-native approach?",
                "Should it feature behind-the-scenes or authentic moments?",
                "What educational or how-to value provision?",
                "Should it include humor or entertainment elements?",
                "What cross-promotion with other platforms or content?",
                "Should it feature collaborations with influencers or creators?",
                "What seasonal or timely content relevance?",
                "Should it include customer testimonials or user stories?",
                "What crisis communication or reputation management?",
                "Should it feature employee advocacy or team content?",
                "What thought leadership or expertise demonstration?",
                "Should it include sustainability or social responsibility messaging?",
                "What diversity and inclusion representation?",
                "Should it feature local or community-specific content?",
                "What technology or innovation showcase?",
                "Should it include live or real-time elements?",
                "What controversial or boundary-pushing content considerations?",
                "Should it feature transformation or before/after content?",
                "What motivational or inspirational messaging?",
                "Should it include contest or giveaway elements?",
                "What platform algorithm optimization strategy?",
                "Should it feature analytics or performance tracking integration?",
                "What cross-generational or age-diverse appeal?",
                "Should it include global or international perspective?",
                "What mental health or wellness messaging?",
                "Should it feature innovation in format or storytelling?",
                "What community building or fan engagement strategy?",
                "Should it include direct sales or conversion optimization?",
                "What specific engagement metric or business outcome optimization?",
                "What long-term brand building vs. viral moment balance?"
            ]
        }

    def clear_screen(self):
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_colored(self, text: str, color: str = 'white'):
        """Prints colored text if colorama is available."""
        if HAS_COLORAMA:
            color_map = {
                'pink': Fore.MAGENTA,
                'blue': Fore.CYAN,
                'yellow': Fore.YELLOW,
                'green': Fore.GREEN,
                'red': Fore.RED,
                'white': Fore.WHITE
            }
            print(f"{color_map.get(color, Fore.WHITE)}{text}")
        else:
            print(text)

    def print_title(self):
        """Prints the main title in Old English style."""
        title_art = """
  ████████   ████████    ██████   ██████████ ████████ █████████ █████████ █████████ █████████
  ████████   ████████   ███████   ██████████ ████████ █████████ █████████ █████████ █████████
  ██    ██   ██    ██  ██    ██   ██  ██  ██ ██   ██      ██        ██        ██       ██   
  ████████   ████████  ██    ██   ██  ██  ██ ████████     ██       ██        ██        ██   
  ██         ██     ██ ██    ██   ██  ██  ██ ██           ██      ██        ██         ██   
  ██         ██     ██  ██████    ██  ██  ██ ██           ██     █████████ █████████   ██   
  ██         ██     ██   ██████   ██  ██  ██ ██           ██     █████████ █████████   ██   

      ██████   █████████    ████████     ██████   █████████
      ██████   █████████    ████████     ██████   █████████
     ██   ██       ██            ██     ██   ██       ██   
     ██   ██       ██            ██     ██   ██       ██   
     ██   ██       ██            ██     ██   ██       ██   
     ███████       ██            ██     ███████       ██   
      ██████       ██            ██      ██████       ██   
        """
        self.print_colored(title_art, 'pink')

    def print_menu_decorations(self):
        """Print decorative elements for the menu."""
        decoration = "╔══════════════════════════════════════════════════════════════════╗"
        self.print_colored(decoration, 'pink')
        center_text = "║                    🚀 AI PROMPT GENERATION SYSTEM 🚀               ║"
        self.print_colored(center_text, 'blue')
        decoration = "╚══════════════════════════════════════════════════════════════════╝"
        self.print_colored(decoration, 'pink')
        print()

    def show_main_menu(self):
        """Display and format the main menu options."""
        self.clear_screen()
        self.print_title()
        print()
        self.print_menu_decorations()
        print()
        
        self.print_colored("⭐ START [Press 1 or type 'start']", 'blue')
        self.print_colored("📖 README [Press 2 or type 'readme']", 'yellow')
        self.print_colored("🚪 QUIT [Press 3 or type 'quit']", 'red')
        print()
        
        separator = "═══════════════════════════════════════════════════════════════════"
        self.print_colored(separator, 'pink')
        self.print_colored("Type command number or name to navigate", 'green')
        print()

    def show_readme(self):
        """Displays README information."""
        self.clear_screen()
        self.print_colored("PromptGBT OS Documentation", 'pink')
        print("=" * 50)
        print()
        
        self.print_colored("🎯 PURPOSE", 'blue')
        print("PromptGBT OS is an advanced AI prompt generation system designed to help you")
        print("create highly effective prompts for AI content generation across multiple categories.")
        print()
        
        self.print_colored("🔧 HOW IT WORKS", 'blue')
        print("1. Select your content category (Code, Image, Music, Text, Video)")
        print("2. Choose a specific subcategory")
        print("3. Answer 50 comprehensive questions about your desired content")
        print("4. Receive a professionally crafted prompt template")
        print()
        
        self.print_colored("💡 BEST TIPS FOR RESULTS", 'blue')
        print("• Be specific and detailed in your answers")
        print("• Include context about your target audience")
        print("• Specify desired style, tone, and functionality")
        print("• Mention any constraints or requirements")
        print("• Provide examples when possible")
        print()
        
        self.print_colored("⌨️ NAVIGATION", 'blue')
        print("• Use number keys for quick navigation")
        print("• Type commands directly (start, readme, quit)")
        print("• Use navigation options at bottom of screens")
        print()
        
        input("\nPress Enter to return to main menu...")

    def show_category_selection(self):
        """Display a menu for selecting content categories."""
        self.clear_screen()
        self.print_colored("Choose Your Content Category", 'pink')
        print("★ ═══════════════════════════════════════════════════════════════════ ★")
        print()
        
        categories = [
            ("💻 CODE", "Apps, Scripts, Debugging"),
            ("🎨 IMAGE", "Art, Graphics, Design"),
            ("🎵 MUSIC", "Beats, Songs, Audio"),
            ("📝 TEXT", "Articles, Stories, Content"),
            ("🎬 VIDEO", "Films, Animations, Clips")
        ]
        
        for i, (cat, desc) in enumerate(categories, 1):
            self.print_colored(f"{i}. {cat}", 'blue')
            self.print_colored(f"   {desc}", 'white')
            print()
        
        print("\nNavigation:")
        self.print_colored("Type category number, name, 'home', or 'quit'", 'green')

    def show_subcategory_selection(self, category: str):
        """Display subcategory selection menu."""
        self.clear_screen()
        self.print_colored(f"Choose {category.upper()} Subcategory", 'pink')
        print("═" * 50)
        print()
        
        subcats = self.subcategories[category.lower()]
        
        for i, subcat in enumerate(subcats, 1):
            self.print_colored(f"{i}. {subcat}", 'blue')
        
        print("\nNavigation:")
        self.print_colored("Type subcategory number, 'back', 'home', or 'quit'", 'green')

    def show_question(self):
        """Display the current question and related information."""
        self.clear_screen()
        
        progress = f"Question {self.current_question_index + 1} of {len(self.questions)}"
        category_info = f"Category: {self.current_category} > {self.current_subcategory}"
        
        self.print_colored(progress, 'yellow')
        self.print_colored(category_info, 'blue')
        print("=" * 60)
        print()
        
        question = self.questions[self.current_question_index]
        self.print_colored(f"Q: {question}", 'white')
        print()
        
        # Show previous answer if exists
        if self.current_question_index in self.answers:
            self.print_colored(f"Current answer: {self.answers[self.current_question_index]}", 'green')
            print()
        
        print("Navigation: 'back', 'next', 'restart', 'home', 'quit'")

    def show_results(self, prompt: str):
        """Displays the generated prompt in a formatted box."""
        self.clear_screen()
        self.print_colored("Your Generated Prompt", 'pink')
        print("=" * 50)
        print()
        
        # Display the prompt in a box
        print("┌" + "─" * 78 + "┐")
        lines = prompt.split('\n')
        for line in lines:
            # Word wrap long lines
            while len(line) > 76:
                print(f"│ {line[:76]} │")
                line = line[76:]
            print(f"│ {line:<76} │")
        print("└" + "─" * 78 + "┘")
        print()
        
        print("Navigation:")
        self.print_colored("'save', 'restart', 'home', 'quit'", 'green')

    def get_user_input(self, prompt: str = "> ") -> str:
        """Get user input with a specified prompt."""
        try:
            return input(prompt).strip()
        except KeyboardInterrupt:
            print("\nExiting PromptGBT OS...")
            sys.exit(0)

    def generate_prompt_template(self) -> str:
        """Generates a project creation prompt based on user answers."""
        prompt = f"Create a {self.current_category.lower()} project with the following specifications:\n\n"
        prompt += f"Type: {self.current_subcategory}\n\n"
        prompt += "Detailed Requirements:\n"
        
        for i, question in enumerate(self.questions):
            if i in self.answers and self.answers[i].strip():
                prompt += f"- {question}\n  Answer: {self.answers[i]}\n\n"
        
        prompt += f"\nPlease generate a {self.current_subcategory.lower()} that incorporates all the above "
        prompt += "requirements and specifications. Ensure the output is professional, functional, "
        prompt += "and meets all stated criteria."
        
        return prompt

    def save_prompt_to_file(self, prompt: str):
        """Saves a generated prompt to a timestamped file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"promptgbt_{self.current_category}_{self.current_subcategory.replace(' ', '_')}_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(prompt)
            self.print_colored(f"✅ Prompt saved to: {filename}", 'green')
        except Exception as e:
            self.print_colored(f"❌ Error saving file: {e}", 'red')

    def handle_navigation(self, user_input: str) -> bool:
        """Handle navigation commands and determine if they are processed."""
        if user_input.lower() in ['quit', 'q', '3']:
            print("\nThanks for using PromptGBT OS! 🚀")
            sys.exit(0)
        elif user_input.lower() in ['home', 'h']:
            self.current_screen = 'main_menu'
            return True
        return False

    def run_questionnaire(self):
        """Executes a questionnaire sequence based on the current subcategory.
        
        The function retrieves questions from the question templates, handles user
        navigation, records answers, and generates a prompt after all questions are
        answered. It also provides options to save the prompt to a file or restart the
        questionnaire.
        
        Args:
            self: The instance of the class containing the method.
        """
        self.questions = self.question_templates.get(self.current_subcategory, [])
        if not self.questions:
            self.print_colored(f"No questions available for {self.current_subcategory}", 'red')
            input("Press Enter to continue...")
            return
        
        self.current_question_index = 0
        self.answers = {}
        
        while self.current_question_index < len(self.questions):
            self.show_question()
            user_input = self.get_user_input("Your answer: ")
            
            if self.handle_navigation(user_input):
                return
            elif user_input.lower() == 'back':
                if self.current_question_index > 0:
                    self.current_question_index -= 1
                continue
            elif user_input.lower() == 'next':
                if self.current_question_index < len(self.questions) - 1:
                    self.current_question_index += 1
                continue
            elif user_input.lower() == 'restart':
                self.current_question_index = 0
                self.answers = {}
                continue
            else:
                # Save the answer
                self.answers[self.current_question_index] = user_input
                self.current_question_index += 1
        
        # All questions answered, generate prompt
        prompt = self.generate_prompt_template()
        
        while True:
            self.show_results(prompt)
            user_input = self.get_user_input()
            
            if self.handle_navigation(user_input):
                return
            elif user_input.lower() == 'save':
                self.save_prompt_to_file(prompt)
                input("Press Enter to continue...")
            elif user_input.lower() == 'restart':
                self.run_questionnaire()
                return

    def run(self):
        """Main application loop that handles user navigation through different screens.
        
        This method continuously runs, processing user input and updating the current
        screen state until the user chooses to quit. It manages transitions between the
        main menu, category selection, and subcategory selection screens, handling
        invalid inputs gracefully.  The loop includes: - Displaying the main menu and
        handling navigation based on user input. - Navigating through category
        selection with a mapping of numeric and named categories. - Selecting
        subcategories by index or name, running a questionnaire if a valid subcategory
        is chosen, and returning to the main menu.
        """
        while True:
            if self.current_screen == 'main_menu':
                self.show_main_menu()
                user_input = self.get_user_input()
                
                if user_input in ['1', 'start', 's']:
                    self.current_screen = 'category_selection'
                elif user_input in ['2', 'readme', 'r']:
                    self.show_readme()
                    self.current_screen = 'main_menu'
                elif user_input in ['3', 'quit', 'q']:
                    print("\nThanks for using PromptGBT OS! 🚀")
                    break
                else:
                    self.print_colored("Invalid option. Please try again.", 'red')
                    time.sleep(1)
            
            elif self.current_screen == 'category_selection':
                self.show_category_selection()
                user_input = self.get_user_input()
                
                if self.handle_navigation(user_input):
                    continue
                
                # Handle category selection
                category_map = {
                    '1': 'code', 'code': 'code',
                    '2': 'image', 'image': 'image',
                    '3': 'music', 'music': 'music',
                    '4': 'text', 'text': 'text',
                    '5': 'video', 'video': 'video'
                }
                
                if user_input.lower() in category_map:
                    self.current_category = category_map[user_input.lower()]
                    self.current_screen = 'subcategory_selection'
                else:
                    self.print_colored("Invalid option. Please try again.", 'red')
                    time.sleep(1)
            
            elif self.current_screen == 'subcategory_selection':
                self.show_subcategory_selection(self.current_category)
                user_input = self.get_user_input()
                
                if self.handle_navigation(user_input):
                    continue
                elif user_input.lower() == 'back':
                    self.current_screen = 'category_selection'
                    continue
                
                # Handle subcategory selection
                try:
                    subcats = self.subcategories[self.current_category]
                    if user_input.isdigit():
                        index = int(user_input) - 1
                        if 0 <= index < len(subcats):
                            self.current_subcategory = subcats[index]
                            self.run_questionnaire()
                            self.current_screen = 'main_menu'
                        else:
                            raise ValueError()
                    else:
                        # Try to match by name
                        for subcat in subcats:
                            if user_input.lower() in subcat.lower():
                                self.current_subcategory = subcat
                                self.run_questionnaire()
                                self.current_screen = 'main_menu'
                                break
                        else:
                            raise ValueError()
                except (ValueError, IndexError):
                    self.print_colored("Invalid option. Please try again.", 'red')
                    time.sleep(1)


def main():
    """Starts the PromptGBTOS application."""
    try:
        app = PromptGBTOS()
        app.run()
    except KeyboardInterrupt:
        print("\n\nThanks for using PromptGBT OS! 🚀")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please restart the application.")


if __name__ == "__main__":
    main()
