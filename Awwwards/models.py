from sre_parse import CATEGORIES
from django.db import models
from django.contrib.auth.models import User
from django.conf.urls.static import static

COUNTRIES = [ 
    ('Afganistan', ('Afghanistan')),
    ('Albania', ('Albania')),
    ('Algeria', ('Algeria')),
    ('American Samoa', ('American Samoa')),
    ('Andorra', ('Andorra')),
    ('Angola', ('Angola')),
    ('Anguilla', ('Anguilla')),
    ('Antigua & Barbuda', ('Antigua & Barbuda')),
    ('Argentina', ('Argentina')),
    ('Armenia', ('Armenia')),
    ('Aruba', ('Aruba')),
    ('Australia', ('Australia')),
    ('Austria', ('Austria')),
    ('Azerbaijan', ('Azerbaijan')),
    ('Bahamas', ('Bahamas')),
    ('Bahrain', ('Bahrain')),
    ('Bangladesh', ('Bangladesh')),
    ('Barbados', ('Barbados')),
    ('Belarus', ('Belarus')),
    ('Belgium', ('Belgium')),
    ('Belize', ('Belize')),
    ('Benin', ('Benin')),
    ('Bermuda', ('Bermuda')),
    ('Bhutan', ('Bhutan')),
    ('Bolivia', ('Bolivia')),
    ('Bonaire', ('Bonaire')),
    ('Bosnia & Herzegovina', ('Bosnia & Herzegovina')),
    ('Botswana', ('Botswana')),
    ('Brazil', ('Brazil')),
    ('British Indian Ocean Ter', ('British Indian Ocean Ter')),
    ('Brunei', ('Brunei')),
    ('Bulgaria', ('Bulgaria')),
    ('Burkina Faso', ('Burkina Faso')),
    ('Burundi', ('Burundi')),
    ('Cambodia', ('Cambodia')),
    ('Cameroon', ('Cameroon')),
    ('Canada', ('Canada')),
    ('Canary Islands', ('Canary Islands')),
    ('Cape Verde', ('Cape Verde')),
    ('Cayman Islands', ('Cayman Islands')),
    ('Central African Republic', ('Central African Republic')),
    ('Chad', ('Chad')),
    ('Channel Islands', ('Channel Islands')),
    ('Chile', ('Chile')),
    ('China', ('China')),
    ('Christmas Island', ('Christmas Island')),
    ('Cocos Island', ('Cocos Island')),
    ('Colombia', ('Colombia')),
    ('Comoros', ('Comoros')),
    ('Congo', ('Congo')),
    ('Cook Islands', ('Cook Islands')),
    ('Costa Rica', ('Costa Rica')),
    ('Cote DIvoire', ('Cote DIvoire')),
    ('Croatia', ('Croatia')),
    ('Cuba', ('Cuba')),
    ('Curaco', ('Curacao')),
    ('Cyprus', ('Cyprus')),
    ('Czech Republic', ('Czech Republic')),
    ('Denmark', ('Denmark')),
    ('Djibouti', ('Djibouti')),
    ('Dominica', ('Dominica')),
    ('Dominican Republic', ('Dominican Republic')),
    ('East Timor', ('East Timor')),
    ('Ecuador', ('Ecuador')),
    ('Egypt', ('Egypt')),
    ('El Salvador', ('El Salvador')),
    ('Equatorial Guinea', ('Equatorial Guinea')),
    ('Eritrea', ('Eritrea')),
    ('Estonia', ('Estonia')),
    ('Ethiopia', ('Ethiopia')),
    ('Falkland Islands', ('Falkland Islands')),
    ('Faroe Islands', ('Faroe Islands')),
    ('Fiji', ('Fiji')),
    ('Finland', ('Finland')),
    ('France', ('France')),
    ('French Guiana', ('French Guiana')),
    ('French Polynesia', ('French Polynesia')),
    ('French Southern Ter', ('French Southern Ter')),
    ('Gabon', ('Gabon')),
    ('Gambia', ('Gambia')),
    ('Georgia', ('Georgia')),
    ('Germany', ('Germany')),
    ('Ghana', ('Ghana')),
    ('Gibraltar', ('Gibraltar')),
    ('Great Britain', ('Great Britain')),
    ('Greece', ('Greece')),
    ('Greenland', ('Greenland')),
    ('Grenada', ('Grenada')),
    ('Guadeloupe', ('Guadeloupe')),
    ('Guam', ('Guam')),
    ('Guatemala', ('Guatemala')),
    ('Guinea', ('Guinea')),
    ('Guyana', ('Guyana')),
    ('Haiti', ('Haiti')),
    ('Hawaii', ('Hawaii')),
    ('Honduras', ('Honduras')),
    ('Hong Kong', ('Hong Kong')),
    ('Hungary', ('Hungary')),
    ('Iceland', ('Iceland')),
    ('Indonesia', ('Indonesia')),
    ('India', ('India')),
    ('Iran', ('Iran')),
    ('Iraq', ('Iraq')),
    ('Ireland', ('Ireland')),
    ('Isle of Man', ('Isle of Man')),
    ('Israel', ('Israel')),
    ('Italy', ('Italy')),
    ('Jamaica', ('Jamaica')),
    ('Japan', ('Japan')),
    ('Jordan', ('Jordan')),
    ('Kazakhstan', ('Kazakhstan')),
    ('Kenya', ('Kenya')),
    ('Kiribati', ('Kiribati')),
    ('Korea North', ('Korea North')),
    ('Korea Sout', ('Korea South')),
    ('Kuwait', ('Kuwait')),
    ('Kyrgyzstan', ('Kyrgyzstan')),
    ('Laos', ('Laos')),
    ('Latvia', ('Latvia')),
    ('Lebanon', ('Lebanon')),
    ('Lesotho', ('Lesotho')),
    ('Liberia', ('Liberia')),
    ('Libya', ('Libya')),
    ('Liechtenstein', ('Liechtenstein')),
    ('Lithuania', ('Lithuania')),
    ('Luxembourg', ('Luxembourg')),
    ('Macau', ('Macau')),
    ('Macedonia', ('Macedonia')),
    ('Madagascar', ('Madagascar')),
    ('Malaysia', ('Malaysia')),
    ('Malawi', ('Malawi')),
    ('Maldives', ('Maldives')),
    ('Mali', ('Mali')),
    ('Malta', ('Malta')),
    ('Marshall Islands', ('Marshall Islands')),
    ('Martinique', ('Martinique')),
    ('Mauritania', ('Mauritania')),
    ('Mauritius', ('Mauritius')),
    ('Mayotte', ('Mayotte')),
    ('Mexico', ('Mexico')),
    ('Midway Islands', ('Midway Islands')),
    ('Moldova', ('Moldova')),
    ('Monaco', ('Monaco')),
    ('Mongolia', ('Mongolia')),
    ('Montserrat', ('Montserrat')),
    ('Morocco', ('Morocco')),
    ('Mozambique', ('Mozambique')),
    ('Myanmar', ('Myanmar')),
    ('Nambia', ('Nambia')),
    ('Nauru', ('Nauru')),
    ('Nepal', ('Nepal')),
    ('Netherland Antilles', ('Netherland Antilles')),
    ('Netherlands', ('Netherlands (Holland, Europe)')),
    ('Nevis', ('Nevis')),
    ('New Caledonia', ('New Caledonia')),
    ('New Zealand', ('New Zealand')),
    ('Nicaragua', ('Nicaragua')),
    ('Niger', ('Niger')),
    ('Nigeria', ('Nigeria')),
    ('Niue', ('Niue')),
    ('Norfolk Island', ('Norfolk Island')),
    ('Norway', ('Norway')),
    ('Oman', ('Oman')),
    ('Pakistan', ('Pakistan')),
    ('Palau Island', ('Palau Island')),
    ('Palestine', ('Palestine')),
    ('Panama', ('Panama')),
    ('Papua New Guinea', ('Papua New Guinea')),
    ('Paraguay', ('Paraguay')),
    ('Peru', ('Peru')),
    ('Phillipines', ('Philippines')),
    ('Pitcairn Island', ('Pitcairn Island')),
    ('Poland', ('Poland')),
    ('Portugal', ('Portugal')),
    ('Puerto Rico', ('Puerto Rico')),
    ('Qatar', ('Qatar')),
    ('Republic of Montenegro', ('Republic of Montenegro')),
    ('Republic of Serbia', ('Republic of Serbia')),
    ('Reunion', ('Reunion')),
    ('Romania', ('Romania')),
    ('Russia', ('Russia')),
    ('Rwanda', ('Rwanda')),
    ('St Barthelemy', ('St Barthelemy')),
    ('St Eustatius', ('St Eustatius')),
    ('St Helena', ('St Helena')),
    ('St Kitts-Nevis', ('St Kitts-Nevis')),
    ('St Lucia', ('St Lucia')),
    ('St Maarten', ('St Maarten')),
    ('St Pierre & Miquelon', ('St Pierre & Miquelon')),
    ('St Vincent & Grenadines', ('St Vincent & Grenadines')),
    ('Saipan', ('Saipan')),
    ('Samoa', ('Samoa')),
    ('Samoa American', ('Samoa American')),
    ('San Marino', ('San Marino')),
    ('Sao Tome & Principe', ('Sao Tome & Principe')),
    ('Saudi Arabia', ('Saudi Arabia')),
    ('Senegal', ('Senegal')),
    ('Seychelles', ('Seychelles')),
    ('Sierra Leone', ('Sierra Leone')),
    ('Singapore', ('Singapore')),
    ('Slovakia', ('Slovakia')),
    ('Slovenia', ('Slovenia')),
    ('Solomon Islands', ('Solomon Islands')),
    ('Somalia', ('Somalia')),
    ('South Africa', ('South Africa')),
    ('Spain', ('Spain')),
    ('Sri Lanka', ('Sri Lanka')),
    ('Sudan', ('Sudan')),
    ('Suriname', ('Suriname')),
    ('Swaziland', ('Swaziland')),
    ('Sweden', ('Sweden')),
    ('Switzerland', ('Switzerland')),
    ('Syria', ('Syria')),
    ('Tahiti', ('Tahiti')),
    ('Taiwan', ('Taiwan')),
    ('Tajikistan', ('Tajikistan')),
    ('Tanzania', ('Tanzania')),
    ('Thailand', ('Thailand')),
    ('Togo', ('Togo')),
    ('Tokelau', ('Tokelau')),
    ('Tonga', ('Tonga')),
    ('Trinidad & Tobago', ('Trinidad & Tobago')),
    ('Tunisia', ('Tunisia')),
    ('Turkey', ('Turkey')),
    ('Turkmenistan', ('Turkmenistan')),
    ('Turks & Caicos Is', ('Turks & Caicos Is')),
    ('Tuvalu', ('Tuvalu')),
    ('Uganda', ('Uganda')),
    ('United Kingdom', ('United Kingdom')),
    ('Ukraine', ('Ukraine')),
    ('United Arab Erimates', ('United Arab Emirates')),
    ('United States of America', ('United States of America')),
    ('Uraguay', ('Uruguay')),
    ('Uzbekistan', ('Uzbekistan')),
    ('Vanuatu', ('Vanuatu')),
    ('Vatican City State', ('Vatican City State')),
    ('Venezuela', ('Venezuela')),
    ('Vietnam', ('Vietnam')),
    ('Virgin Islands (Brit)', ('Virgin Islands (Brit)')),
    ('Virgin Islands (USA)', ('Virgin Islands (USA)')),
    ('Wake Island', ('Wake Island')),
    ('Wallis & Futana Is', ('Wallis & Futana Is')),
    ('Yemen', ('Yemen')),
    ('Zaire', ('Zaire')),
    ('Zambia', ('Zambia')),
    ('Zimbabwe', ('Zimbabwe')), 
]

CATEGORIES = [
    ('For Practise', ('For Practise')),
    ('Professional', ('Professional')),
]

LANGUAGES = [
    ('C', ('C')), 
    ('C++', ('C++')), 
    ('C#', ('C#')), 
    ('Erlang', ('Erlang')), 
    ('Go', ('Go')), 
    ('Haskell', ('Haskell')), 
    ('HTML', ('HTML')), 
    ('iOS', ('iOS')),
    ('Java', ('Java')), 
    ('Lua', ('Lua')), 
    ('.NET', ('.NET')), 
    ('Node', ('Node')), 
    ('PHP', ('PHP')), 
    ('Python', ('Python')), 
    ('Ruby', ('Ruby')), 
    ('Clojure', ('Clojure')),
    ('Rust', ('Rust')), 
    ('Android', ('Android')), 
    ('Electron', ('Electron')), 
    ('Flutter', ('Flutter')), 
    ('Gatsby', ('Gatsby')), 
    ('JavaScript', ('JavaScript')), 
    ('Kotlin', ('Kotlin')), 
    ('R', ('R')), 
    ('Roku', ('Roku')),
    ('Swift', ('Swift')), 
    ('Xamarin', ('Xamarin')), 
    ('Apex', ('Apex')), 
]

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    profession = models.CharField(max_length=150, verbose_name='Profession', null=True, blank=True)
    bio = models.TextField(max_length=150, verbose_name='Bio', null=True, blank=True)
    profile_image = models.ImageField(upload_to='Profile-Pics', verbose_name='Profile Image', null=True, blank=True)
    country = models.CharField(max_length=100, choices=COUNTRIES, verbose_name="Country", null=True, blank=True)
    personal_website = models.URLField(max_length=500, verbose_name="Personal Website", null=True, blank=True)
    github_link = models.URLField(max_length=500, verbose_name="GitHub Link", null=True, blank=True)
    instagram_link = models.URLField(max_length=500, verbose_name="Instagram Link", null=True, blank=True)
    linkedin_link = models.URLField(max_length=500, verbose_name="LinkedIn Link", null=True, blank=True)
    twitter_link = models.URLField(max_length=500, verbose_name="Twitter Link", null=True, blank=True)
    email_confirmed = models.BooleanField(default=False, verbose_name='Is Confirmed?')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = 'Profiles'

    @property
    def get_avatar(self):
        return self.profile_image.url if self.profile_image else static('assets/img/default.jpg')

class Portfolio(models.Model):
    portfolio_image = models.ImageField(upload_to='Portfolio-Pics', verbose_name='Portfolio  Image', null=False)
    title = models.CharField(max_length=500, verbose_name='Title', null=False)
    caption = models.CharField(max_length=2200, verbose_name='Caption', null=False)
    portfolio_site_url = models.URLField(max_length=500, verbose_name="Webiste Link", null=True, blank=True)
    repo_url = models.URLField(max_length=500, verbose_name="GitHub Repository", null=False)
    primary_language = models.CharField(max_length=100, choices=LANGUAGES, verbose_name="Primary Programming Language", null=False)
    category = models.CharField(max_length=100, choices=CATEGORIES, verbose_name="Category", null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Profile')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = 'Portfolio'

class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2200, verbose_name='Comment', null=False)
    design_rating = models.IntegerField(default=0, null=False)
    usability_rating = models.IntegerField(default=0, null=False)
    content_rating = models.IntegerField(default=0, null=False)
    creativity_rating = models.IntegerField(default=0, null=False)
    experience_rating = models.IntegerField(default=0, null=False)
    avarage_rating = models.IntegerField(default=0, null=False)

    def _str_(self):
        return self.portfolio.title

    class Meta:
        verbose_name_plural = 'Ratings'