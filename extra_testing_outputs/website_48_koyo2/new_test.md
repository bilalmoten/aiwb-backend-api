##

Home Page.html
`` html

<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
     <!--PAID Tailwind CSS CDN -- DO NOT CHANGE -->
    <script src=\"https://cdn.tailwindcss.com\"></script>
    <!-- Font Awesome CDN  -- DO NOT CHANGE  -->
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css\" />
    <script src=https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js></script>
    <script src=\"https://cdn.jsdelivr.net/npm/framer-motion@11.15.0/dist/framer-motion.min.js\"></script>
    <title>Home Page</title>
</head>
<body>
<section>
  <header class=\"bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50\"
    x-data=\"{ isOpen: false, activeDropdown: null }\">
    <div class=\"container mx-auto flex justify-between items-center px-4 sm:px-6 lg:px-8 h-16\">
      <div class=\"flex items-center gap-8\">
        <a href=\"#\" class=\"text-2xl font-bold\" aria-label=\"Startup\">
          <span class=\"flex items-center gap-2\">
            <div class=\"w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center\">
              <i class=\"fas fa-bolt text-white\"></i>
            </div>
            <span class=\"text-gray-900 font-bold\">Startup</span>
          </span>
        </a>

        <nav class=\"hidden lg:flex items-center gap-6\">
          <a href=\"#product\"
            class=\"group relative text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\">
            <i class=\"fas fa-cube text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            Product
            <span
              class=\"absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-600 to-purple-600 group-hover:w-full transition-all duration-300\"></span>
          </a>
          <div class=\"relative\" @mouseleave=\"activeDropdown = null\">
            <button @mouseover=\"activeDropdown = 'solutions'\"
              @click=\"activeDropdown = activeDropdown === 'solutions' ? null : 'solutions'\"
              class=\"group text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\"
              aria-haspopup=\"true\" :aria-expanded=\"activeDropdown === 'solutions'\">
              <i class=\"fas fa-lightbulb text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
              Solutions
              <i class=\"fas fa-chevron-down text-xs transition-transform duration-200\"
                :class=\"{ 'rotate-180': activeDropdown === 'solutions' }\"></i>
            </button>
            <div x-show=\"activeDropdown === 'solutions'\" x-transition:enter=\"transition ease-out duration-200\"
              x-transition:enter-start=\"opacity-0 translate-y-1\" x-transition:enter-end=\"opacity-100 translate-y-0\"
              x-transition:leave=\"transition ease-in duration-150\" x-transition:leave-start=\"opacity-100 translate-y-0\"
              x-transition:leave-end=\"opacity-0 translate-y-1\"
              class=\"absolute left-0  w-80 bg-white rounded-lg shadow-lg ring-1 ring-black ring-opacity-5\">
              <div class=\"p-4 space-y-3\">
                <a href=\"#analytics\"
                  class=\"flex items-center gap-4 p-3 hover:bg-gray-50 rounded-lg group transition-colors duration-200\">
                  <div class=\"flex-shrink-0 w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center\">
                    <i
                      class=\"fas fa-chart-line text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
                  </div>
                  <div>
                    <h3 class=\"text-sm font-medium text-gray-900\">Analytics</h3>
                    <p class=\"text-xs text-gray-600\">Track your performance</p>
                  </div>
                </a>
                <a href=\"#automation\"
                  class=\"flex items-center gap-4 p-3 hover:bg-gray-50 rounded-lg group transition-colors duration-200\">
                  <div class=\"flex-shrink-0 w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center\">
                    <i class=\"fas fa-robot text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
                  </div>
                  <div>
                    <h3 class=\"text-sm font-medium text-gray-900\">Automation</h3>
                    <p class=\"text-xs text-gray-600\">Streamline workflows</p>
                  </div>
                </a>
                <a href=\"#integrations\"
                  class=\"flex items-center gap-4 p-3 hover:bg-gray-50 rounded-lg group transition-colors duration-200\">
                  <div class=\"flex-shrink-0 w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center\">
                    <i class=\"fas fa-plug text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
                  </div>
                  <div>
                    <h3 class=\"text-sm font-medium text-gray-900\">Integrations</h3>
                    <p class=\"text-xs text-gray-600\">Connect your tools</p>
                  </div>
                </a>
              </div>
            </div>
          </div>
          <a href=\"#pricing\"
            class=\"group relative text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\">
            <i class=\"fas fa-tag text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            Pricing
            <span
              class=\"absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-600 to-purple-600 group-hover:w-full transition-all duration-300\"></span>
          </a>
          <a href=\"#resources\"
            class=\"group relative text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\">
            <i class=\"fas fa-book text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            Resources
            <span
              class=\"absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-600 to-purple-600 group-hover:w-full transition-all duration-300\"></span>
          </a>
        </nav>
      </div>

      <div class=\"flex items-center gap-4\">
        <div class=\"hidden lg:flex items-center gap-4\">
          <a href=\"#login\"
            class=\"text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200\">Log in</a>
          <a href=\"#signup\"
            class=\"inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-colors duration-200 group\">
            Start Free Trial
            <i class=\"fas fa-arrow-right ml-2 group-hover:translate-x-1 transition-transform duration-200\"></i>
          </a>
        </div>

        <button type=\"button\" @click=\"isOpen = !isOpen\"
          class=\"lg:hidden p-2 rounded-md text-gray-700 hover:text-gray-900 hover:bg-gray-100 transition-colors duration-200\"
          :aria-expanded=\"isOpen\">
          <span class=\"sr-only\">Toggle menu</span>
          <i class=\"fas\" :class=\"isOpen ? 'fa-times' : 'fa-bars'\"></i>
        </button>
      </div>
    </div>

    <div x-show=\"isOpen\" x-transition:enter=\"transition ease-out duration-200\"
      x-transition:enter-start=\"opacity-0 -translate-y-1\" x-transition:enter-end=\"opacity-100 translate-y-0\"
      x-transition:leave=\"transition ease-in duration-150\" x-transition:leave-start=\"opacity-100 translate-y-0\"
      x-transition:leave-end=\"opacity-0 -translate-y-1\" class=\"lg:hidden\" role=\"dialog\" aria-modal=\"true\"
      style=\"display: none;\">
      <div class=\"fixed inset-0 bg-black bg-opacity-25\" @click=\"isOpen = false\"></div>
      <div class=\"fixed inset-y-0 right-0 w-full max-w-xs bg-white shadow-xl\">
        <div class=\"flex items-center justify-between px-4 py-5 border-b border-gray-200\">
          <span class=\"text-lg font-medium text-gray-900\">Menu</span>
          <button type=\"button\" @click=\"isOpen = false\"
            class=\"p-2 rounded-md text-gray-500 hover:text-gray-700 hover:bg-gray-100 transition-colors duration-200\">
            <i class=\"fas fa-times\"></i>
          </button>
        </div>
        <div class=\"px-2 py-3 space-y-1\">
          <a href=\"#product\"
            class=\"flex items-center gap-3 px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <i class=\"fas fa-cube w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            <span>Product</span>
          </a>
          <button @click=\"activeDropdown = activeDropdown === 'mobile-solutions' ? null : 'mobile-solutions'\"
            class=\"flex items-center justify-between w-full px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <div class=\"flex items-center gap-3\">
              <i
                class=\"fas fa-lightbulb w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
              <span>Solutions</span>
            </div>
            <i class=\"fas fa-chevron-down transition-transform duration-200\"
              :class=\"{ 'rotate-180': activeDropdown === 'mobile-solutions' }\"></i>
          </button>
          <div x-show=\"activeDropdown === 'mobile-solutions'\" class=\"pl-12 space-y-1\" style=\"display: none;\">
            <a href=\"#analytics\"
              class=\"block px-3 py-2 text-base font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150\">Analytics</a>
            <a href=\"#automation\"
              class=\"block px-3 py-2 text-base font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150\">Automation</a>
            <a href=\"#integrations\"
              class=\"block px-3 py-2 text-base font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150\">Integrations</a>
          </div>
          <a href=\"#pricing\"
            class=\"flex items-center gap-3 px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <i class=\"fas fa-tag w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            <span>Pricing</span>
          </a>
          <a href=\"#resources\"
            class=\"flex items-center gap-3 px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <i class=\"fas fa-book w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            <span>Resources</span>
          </a>
        </div>
        <div class=\"mt-auto border-t border-gray-200\">
          <div class=\"px-4 py-5 space-y-4\">
            <a href=\"#login\"
              class=\"block w-full px-4 py-2 text-center text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-200\">
              Sign in
            </a>
            <a href=\"#signup\"
              class=\"flex items-center justify-center px-4 py-2 text-base font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-colors duration-200 group\">
              Start Free Trial
              <i class=\"fas fa-arrow-right ml-2 group-hover:translate-x-1 transition-transform duration-200\"></i>
            </a>
          </div>
        </div>
      </div>
    </div>

  </header>

  <main class=\"container mx-auto grid grid-cols-1 md:grid-cols-3 gap-6 p-4\">
    <article
      class=\"flex flex-col md:flex-row bg-white shadow-md rounded-lg overflow-hidden hover:shadow-lg transition-shadow\">
      <img src=\"https://placehold.co/600x400/EEE/31343C\" alt=\"Article Image\" class=\"w-full md:w-1/3 object-cover\">
      <div class=\"p-4 flex flex-col justify-between\">
        <div>
          <h3 class=\"font-bold text-lg text-gray-800 hover:text-black transition-colors\">Article Title</h3>
          <p class=\"text-gray-600 mt-2\">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
        <a href=\"#\" class=\"mt-4 text-blue-500 hover:underline transition-colors\">Read more</a>
      </div>
    </article>
    <!-- Repeat the above block for more articles -->
  </main>
</section>
<script>
  document.getElementById('menu-button').addEventListener('click', function () {
    const menu = document.getElementById('mobile-menu');
    const expanded = this.getAttribute('aria-expanded') === 'true';
    this.setAttribute('aria-expanded', !expanded);
    menu.classList.toggle('hidden');
  });

document.getElementById('categories-button').addEventListener('click', function () {
const submenu = document.getElementById('categories-menu');
const expanded = this.getAttribute('aria-expanded') === 'true';
this.setAttribute('aria-expanded', !expanded);
submenu.classList.toggle('hidden');
this.querySelector('i').classList.toggle('fa-chevron-up');
this.querySelector('i').classList.toggle('fa-chevron-down');
});
</script>

<!-- Clean Layout Hero -->
<section class=\"relative min-h-screen bg-white\" x-data=\"{ currentSlide: 1, totalSlides: 5 }\">
    <!-- Background -->
    <div class=\"absolute inset-0\">
        <div class=\"absolute inset-0 bg-gradient-to-br from-blue-50 to-white\"></div>
        <div class=\"absolute inset-y-0 right-0 w-1/2 bg-gray-50\"></div>
    </div>

    <!-- Navigation -->
    <nav class=\"relative z-10 py-6\">
        <div class=\"max-w-7xl mx-auto px-8\">
            <div class=\"flex items-center justify-between\">
                <a href=\"#\" class=\"text-xl font-medium text-gray-900\">focus</a>
                <div class=\"hidden md:flex items-center gap-10\">
                    <a href=\"#work\" class=\"text-gray-600 hover:text-gray-900 transition-colors\">Work</a>
                    <a href=\"#services\" class=\"text-gray-600 hover:text-gray-900 transition-colors\">Services</a>
                    <a href=\"#about\" class=\"text-gray-600 hover:text-gray-900 transition-colors\">About</a>
                    <a href=\"#contact\"
                        class=\"inline-flex items-center justify-center h-10 px-6 rounded-full bg-gray-900 text-white hover:bg-gray-800 transition-colors\">
                        Get in Touch
                    </a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class=\"relative\">
        <div class=\"max-w-7xl mx-auto px-8 pt-24 pb-20\">
            <div class=\"grid lg:grid-cols-2 gap-20 items-center\">
                <!-- Left Content -->
                <div class=\"relative max-w-xl\">
                    <!-- Section Label -->
                    <div class=\"inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 mb-8\">
                        <div class=\"w-1 h-1 rounded-full bg-blue-600\"></div>
                        <span class=\"text-sm font-medium text-blue-600\">Design Agency</span>
                    </div>

                    <!-- Main Content -->
                    <div class=\"space-y-10\">
                        <div class=\"space-y-6\">
                            <h1 class=\"text-5xl font-semibold text-gray-900 leading-tight\">
                                Focused on what matters most\u2014your success
                            </h1>
                            <p class=\"text-xl text-gray-600 leading-relaxed\">
                                We help ambitious brands stand out through focused design solutions and strategic
                                thinking.
                            </p>
                        </div>

                        <!-- CTA Section -->
                        <div class=\"flex items-center gap-6\">
                            <a href=\"#projects\"
                                class=\"inline-flex items-center justify-center h-14 px-8 rounded-lg bg-gray-900 text-white hover:bg-gray-800 transition-colors\">
                                View Projects
                            </a>
                            <a href=\"#process\"
                                class=\"group inline-flex items-center text-gray-600 hover:text-gray-900 transition-colors\">
                                <span>Our Process</span>
                                <svg xmlns=\"http://www.w3.org/2000/svg\"
                                    class=\"h-5 w-5 ml-2 transform group-hover:translate-x-1 transition-transform\"
                                    fill=\"none\" viewBox=\"0 0 24 24\" stroke=\"currentColor\">
                                    <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                                        d=\"M17 8l4 4m0 0l-4 4m4-4H3\" />
                                </svg>
                            </a>
                        </div>

                        <!-- Metrics -->
                        <div class=\"grid grid-cols-3 gap-8 pt-8 border-t border-gray-100\">
                            <div>
                                <div class=\"text-3xl font-semibold text-gray-900\">10+</div>
                                <div class=\"text-gray-600 mt-1\">Years Experience</div>
                            </div>
                            <div>
                                <div class=\"text-3xl font-semibold text-gray-900\">200+</div>
                                <div class=\"text-gray-600 mt-1\">Projects Completed</div>
                            </div>
                            <div>
                                <div class=\"text-3xl font-semibold text-gray-900\">50+</div>
                                <div class=\"text-gray-600 mt-1\">Happy Clients</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Content -->
                <div class=\"relative lg:h-[700px]\">
                    <!-- Project Showcase -->
                    <div class=\"relative\">
                        <!-- Project Slides -->
                        <div class=\"relative\">
                            <!-- Slide 1 -->
                            <div x-show=\"currentSlide === 1\"
                                class=\"relative aspect-[4/3] bg-gray-100 rounded-lg overflow-hidden transition-opacity duration-500\">
                                <div class=\"absolute inset-0 bg-gradient-to-br from-gray-100 to-gray-200\"></div>
                                <div
                                    class=\"absolute inset-0 p-8 flex flex-col justify-end bg-gradient-to-t from-gray-900/20 to-transparent\">
                                    <div class=\"relative text-white\">
                                        <div class=\"text-sm font-medium mb-2\">Featured Work</div>
                                        <h3 class=\"text-2xl font-medium mb-2\">Brand Evolution</h3>
                                        <p class=\"text-white/80\">Strategic rebranding and digital presence for modern
                                            businesses.</p>
                                    </div>
                                </div>
                            </div>

                            <!-- Slide 2 -->
                            <div x-show=\"currentSlide === 2\"
                                class=\"relative aspect-[4/3] bg-gray-100 rounded-lg overflow-hidden transition-opacity duration-500\">
                                <div class=\"absolute inset-0 bg-gradient-to-br from-blue-100 to-blue-200\"></div>
                                <div
                                    class=\"absolute inset-0 p-8 flex flex-col justify-end bg-gradient-to-t from-gray-900/20 to-transparent\">
                                    <div class=\"relative text-white\">
                                        <div class=\"text-sm font-medium mb-2\">Latest Project</div>
                                        <h3 class=\"text-2xl font-medium mb-2\">Digital Innovation</h3>
                                        <p class=\"text-white/80\">Creating seamless digital experiences for the modern
                                            web.</p>
                                    </div>
                                </div>
                            </div>

                            <!-- Additional slides can be added here -->
                        </div>

                        <!-- Project Navigation -->
                        <div class=\"absolute -right-8 -bottom-8 flex gap-4 p-4 bg-white rounded-lg shadow-lg\">
                            <button @click=\"currentSlide = currentSlide === 1 ? totalSlides : currentSlide - 1\"
                                class=\"w-10 h-10 rounded-full flex items-center justify-center text-gray-400 hover:text-gray-600 transition-colors\">
                                <svg xmlns=\"http://www.w3.org/2000/svg\" class=\"h-5 w-5\" fill=\"none\" viewBox=\"0 0 24 24\"
                                    stroke=\"currentColor\">
                                    <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                                        d=\"M15 19l-7-7 7-7\" />
                                </svg>
                            </button>
                            <button @click=\"currentSlide = currentSlide === totalSlides ? 1 : currentSlide + 1\"
                                class=\"w-10 h-10 rounded-full flex items-center justify-center text-gray-400 hover:text-gray-600 transition-colors\">
                                <svg xmlns=\"http://www.w3.org/2000/svg\" class=\"h-5 w-5\" fill=\"none\" viewBox=\"0 0 24 24\"
                                    stroke=\"currentColor\">
                                    <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                                        d=\"M9 5l7 7-7 7\" />
                                </svg>
                            </button>
                        </div>

                        <!-- Project Counter -->
                        <div class=\"absolute -left-8 top-1/2 -translate-y-1/2 bg-white p-6 rounded-lg shadow-lg\">
                            <div class=\"space-y-1 text-center\">
                                <div class=\"text-3xl font-semibold text-gray-900\"
                                    x-text=\"String(currentSlide).padStart(2, '0')\">01</div>
                                <div class=\"text-gray-400\" x-text=\"`/${String(totalSlides).padStart(2, '0')}`\">/05</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Bottom Bar -->
    <div class=\"fixed bottom-0 left-0 right-0 bg-white border-t border-gray-100\">
        <div class=\"max-w-7xl mx-auto px-8 py-4\">
            <div class=\"flex items-center justify-between\">
                <!-- Location -->
                <div class=\"flex items-center gap-6\">
                    <div class=\"flex items-center gap-2\">
                        <svg xmlns=\"http://www.w3.org/2000/svg\" class=\"h-5 w-5 text-gray-400\" fill=\"none\"
                            viewBox=\"0 0 24 24\" stroke=\"currentColor\">
                            <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                                d=\"M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z\" />
                            <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                                d=\"M15 11a3 3 0 11-6 0 3 3 0 016 0z\" />
                        </svg>
                        <span class=\"text-gray-600\">New York, USA</span>
                    </div>
                    <div class=\"h-4 w-px bg-gray-200\"></div>
                    <div class=\"text-gray-600\">Available Worldwide</div>
                </div>

                <!-- Social Links -->
                <div class=\"flex items-center gap-6\">
                    <a href=\"#dribbble\" class=\"text-gray-400 hover:text-gray-600 transition-colors\">Dribbble</a>
                    <a href=\"#instagram\" class=\"text-gray-400 hover:text-gray-600 transition-colors\">Instagram</a>
                    <a href=\"#twitter\" class=\"text-gray-400 hover:text-gray-600 transition-colors\">Twitter</a>
                </div>
            </div>
        </div>
    </div>

</section>

<!-- Alpine.js -->
<script src=\"https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js\"></script>
<!DOCTYPE html>
<section class=\"min-h-screen bg-gradient-to-br from-cyan-900 to-blue-900 relative overflow-hidden py-20 font-['Inter']\">
    <!-- Content -->
    <div class=\"max-w-6xl mx-auto px-4\">
        <div class=\"text-center mb-16\">
            <h2 class=\"text-4xl font-bold text-white mb-4\">Compare Features</h2>
            <p class=\"text-cyan-200 max-w-2xl mx-auto\">Find the perfect website package for your needs</p>
        </div>

        <div class=\"bg-white/10 backdrop-blur-sm rounded-2xl p-8\">
            <div class=\"grid grid-cols-4 gap-4\">
                <!-- Headers -->
                <div class=\"col-span-1\"></div>
                <div class=\"text-center\">
                    <h3 class=\"text-xl font-bold text-white mb-2\">Basic</h3>
                    <div class=\"text-2xl font-bold text-cyan-300 mb-4\">$499</div>
                </div>
                <div class=\"text-center\">
                    <h3 class=\"text-xl font-bold text-white mb-2\">Standard</h3>
                    <div class=\"text-2xl font-bold text-cyan-300 mb-4\">$999</div>
                </div>
                <div class=\"text-center\">
                    <h3 class=\"text-xl font-bold text-white mb-2\">Premium</h3>
                    <div class=\"text-2xl font-bold text-cyan-300 mb-4\">$1,499</div>
                </div>

                <!-- Features -->
                <div class=\"col-span-1 py-4 text-cyan-200\">Pages</div>
                <div class=\"text-center py-4 text-white\">1 Page</div>
                <div class=\"text-center py-4 text-white\">5 Pages</div>
                <div class=\"text-center py-4 text-white\">10 Pages</div>

                <div class=\"col-span-1 py-4 text-cyan-200\">Design</div>
                <div class=\"text-center py-4 text-white\">Basic Template</div>
                <div class=\"text-center py-4 text-white\">Custom Design</div>
                <div class=\"text-center py-4 text-white\">Premium Design</div>

                <div class=\"col-span-1 py-4 text-cyan-200\">Responsive</div>
                <div class=\"text-center py-4 text-white\">
                    <svg class=\"w-6 h-6 mx-auto text-cyan-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M5 13l4 4L19 7\"></path>
                    </svg>
                </div>
                <div class=\"text-center py-4 text-white\">
                    <svg class=\"w-6 h-6 mx-auto text-cyan-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M5 13l4 4L19 7\"></path>
                    </svg>
                </div>
                <div class=\"text-center py-4 text-white\">
                    <svg class=\"w-6 h-6 mx-auto text-cyan-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M5 13l4 4L19 7\"></path>
                    </svg>
                </div>

                <div class=\"col-span-1 py-4 text-cyan-200\">SEO Setup</div>
                <div class=\"text-center py-4 text-white\">Basic</div>
                <div class=\"text-center py-4 text-white\">Advanced</div>
                <div class=\"text-center py-4 text-white\">Premium</div>

                <div class=\"col-span-1 py-4 text-cyan-200\">Animations</div>
                <div class=\"text-center py-4 text-white\">
                    <svg class=\"w-6 h-6 mx-auto text-gray-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M6 18L18 6M6 6l12 12\">
                        </path>
                    </svg>
                </div>
                <div class=\"text-center py-4 text-white\">
                    <svg class=\"w-6 h-6 mx-auto text-cyan-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M5 13l4 4L19 7\"></path>
                    </svg>
                </div>
                <div class=\"text-center py-4 text-white\">
                    <svg class=\"w-6 h-6 mx-auto text-cyan-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M5 13l4 4L19 7\"></path>
                    </svg>
                </div>

                <div class=\"col-span-1 py-4 text-cyan-200\">Contact Form</div>
                <div class=\"text-center py-4 text-white\">
                    <svg class=\"w-6 h-6 mx-auto text-cyan-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M5 13l4 4L19 7\"></path>
                    </svg>
                </div>
                <div class=\"text-center py-4 text-white\">
                    <svg class=\"w-6 h-6 mx-auto text-cyan-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M5 13l4 4L19 7\"></path>
                    </svg>
                </div>
                <div class=\"text-center py-4 text-white\">
                    <svg class=\"w-6 h-6 mx-auto text-cyan-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M5 13l4 4L19 7\"></path>
                    </svg>
                </div>

                <!-- Action Buttons -->
                <div class=\"col-span-1 py-4\"></div>
                <div class=\"text-center py-4\">
                    <button class=\"w-full py-3 bg-cyan-600 hover:bg-cyan-700 text-white rounded-xl transition-colors\">
                        Choose Basic
                    </button>
                </div>
                <div class=\"text-center py-4\">
                    <button class=\"w-full py-3 bg-cyan-600 hover:bg-cyan-700 text-white rounded-xl transition-colors\">
                        Choose Standard
                    </button>
                </div>
                <div class=\"text-center py-4\">
                    <button class=\"w-full py-3 bg-cyan-600 hover:bg-cyan-700 text-white rounded-xl transition-colors\">
                        Choose Premium
                    </button>
                </div>
            </div>
        </div>
    </div>

</section>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        // Simple animation for buttons
        const buttons = document.querySelectorAll('button');
        buttons.forEach(button => {
            button.addEventListener('click', () => {
                alert('Thank you for your interest! We will contact you shortly.');
            });
        });
    });
</script>
<section class=\"py-24 bg-gray-50 overflow-hidden\">
    <!-- Decorative Background -->
    <div class=\"absolute inset-0\">
        <div class=\"absolute inset-0 bg-[radial-gradient(circle_800px_at_100%_200px,#f0f9ff,transparent)]\"></div>
    </div>

    <div class=\"container mx-auto px-4 relative\">
        <!-- Header -->
        <div class=\"max-w-3xl mx-auto text-center mb-20 gsap-header\">
            <div class=\"inline-flex items-center gap-2 bg-blue-100 text-blue-600 px-4 py-2 rounded-full mb-8\">
                <i class=\"fas fa-heart\"></i>
                <span class=\"text-sm font-medium\">Life at Our Company</span>
            </div>

            <h2 class=\"text-4xl md:text-5xl font-bold text-gray-900 mb-6\">
                Meet the People Behind<br>Our Success
            </h2>
            <p class=\"text-xl text-gray-600\">
                We're a diverse team of creators, thinkers, and problem solvers, united by our passion for innovation.
            </p>
        </div>

        <!-- Team Grid -->
        <div class=\"grid md:grid-cols-3 gap-8 mb-20 gsap-team\">
            <!-- Team Member 1 -->
            <div class=\"group\">
                <div class=\"relative aspect-[3/4] mb-6 overflow-hidden rounded-2xl\">
                    <img src=\"https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&q=80\"
                        alt=\"Emma Wilson\"
                        class=\"absolute inset-0 w-full h-full object-cover transition duration-500 group-hover:scale-110\">
                    <div class=\"absolute inset-0 bg-gradient-to-t from-gray-900/80 to-transparent\"></div>
                    <div class=\"absolute bottom-0 left-0 right-0 p-6\">
                        <h4 class=\"text-xl font-semibold text-white mb-1\">Emma Wilson</h4>
                        <p class=\"text-gray-300\">Creative Director</p>
                    </div>
                </div>
            </div>
            <!-- Team Member 2 -->
            <div class=\"group\">
                <div class=\"relative aspect-[3/4] mb-6 overflow-hidden rounded-2xl\">
                    <img src=\"https://images.unsplash.com/photo-1556157382-97eda2d62296?auto=format&fit=crop&q=80\"
                        alt=\"David Chen\"
                        class=\"absolute inset-0 w-full h-full object-cover transition duration-500 group-hover:scale-110\">
                    <div class=\"absolute inset-0 bg-gradient-to-t from-gray-900/80 to-transparent\"></div>
                    <div class=\"absolute bottom-0 left-0 right-0 p-6\">
                        <h4 class=\"text-xl font-semibold text-white mb-1\">David Chen</h4>
                        <p class=\"text-gray-300\">Lead Developer</p>
                    </div>
                </div>
            </div>
            <!-- Team Member 3 -->
            <div class=\"group\">
                <div class=\"relative aspect-[3/4] mb-6 overflow-hidden rounded-2xl\">
                    <img src=\"https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&q=80\"
                        alt=\"Sarah Martinez\"
                        class=\"absolute inset-0 w-full h-full object-cover transition duration-500 group-hover:scale-110\">
                    <div class=\"absolute inset-0 bg-gradient-to-t from-gray-900/80 to-transparent\"></div>
                    <div class=\"absolute bottom-0 left-0 right-0 p-6\">
                        <h4 class=\"text-xl font-semibold text-white mb-1\">Sarah Martinez</h4>
                        <p class=\"text-gray-300\">Product Manager</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Culture Grid -->
        <div class=\"grid lg:grid-cols-2 gap-12 mb-20 gsap-culture\">
            <!-- Left Content -->
            <div>
                <h3 class=\"text-2xl font-bold text-gray-900 mb-6\">Our Culture</h3>
                <div class=\"space-y-6 text-gray-600\">
                    <p>
                        We believe in fostering an environment where creativity thrives and innovation is encouraged.
                        Our
                        culture is built on collaboration, continuous learning, and celebrating diverse perspectives.
                    </p>
                    <p>
                        Every team member plays a crucial role in shaping our company's future, and we're committed to
                        supporting their growth and success.
                    </p>
                </div>
            </div>
            <!-- Right Content -->
            <div class=\"grid grid-cols-2 gap-6\">
                <div class=\"bg-white rounded-2xl p-6 shadow-sm\">
                    <div class=\"w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center mb-4\">
                        <i class=\"fas fa-lightbulb text-blue-600 text-xl\"></i>
                    </div>
                    <h4 class=\"font-semibold text-gray-900 mb-2\">Innovation</h4>
                    <p class=\"text-gray-600\">Embracing new ideas and creative solutions</p>
                </div>
                <div class=\"bg-white rounded-2xl p-6 shadow-sm\">
                    <div class=\"w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center mb-4\">
                        <i class=\"fas fa-users text-blue-600 text-xl\"></i>
                    </div>
                    <h4 class=\"font-semibold text-gray-900 mb-2\">Collaboration</h4>
                    <p class=\"text-gray-600\">Working together to achieve excellence</p>
                </div>
                <div class=\"bg-white rounded-2xl p-6 shadow-sm\">
                    <div class=\"w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center mb-4\">
                        <i class=\"fas fa-heart text-blue-600 text-xl\"></i>
                    </div>
                    <h4 class=\"font-semibold text-gray-900 mb-2\">Empathy</h4>
                    <p class=\"text-gray-600\">Understanding and supporting each other</p>
                </div>
                <div class=\"bg-white rounded-2xl p-6 shadow-sm\">
                    <div class=\"w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center mb-4\">
                        <i class=\"fas fa-rocket text-blue-600 text-xl\"></i>
                    </div>
                    <h4 class=\"font-semibold text-gray-900 mb-2\">Growth</h4>
                    <p class=\"text-gray-600\">Continuous learning and development</p>
                </div>
            </div>
        </div>

        <!-- Benefits -->
        <div class=\"text-center gsap-benefits\">
            <h3 class=\"text-2xl font-bold text-gray-900 mb-12\">Life at Our Company</h3>
            <div class=\"grid md:grid-cols-4 gap-8\">
                <div>
                    <div class=\"w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mx-auto mb-6\">
                        <i class=\"fas fa-laptop text-blue-600 text-2xl\"></i>
                    </div>
                    <h4 class=\"font-semibold text-gray-900 mb-2\">Remote First</h4>
                    <p class=\"text-gray-600\">Work from anywhere in the world</p>
                </div>
                <div>
                    <div class=\"w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mx-auto mb-6\">
                        <i class=\"fas fa-book text-blue-600 text-2xl\"></i>
                    </div>
                    <h4 class=\"font-semibold text-gray-900 mb-2\">Learning Budget</h4>
                    <p class=\"text-gray-600\">Resources for your growth</p>
                </div>
                <div>
                    <div class=\"w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mx-auto mb-6\">
                        <i class=\"fas fa-calendar text-blue-600 text-2xl\"></i>
                    </div>
                    <h4 class=\"font-semibold text-gray-900 mb-2\">Flexible Hours</h4>
                    <p class=\"text-gray-600\">Work when you're most productive</p>
                </div>
                <div>
                    <div class=\"w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mx-auto mb-6\">
                        <i class=\"fas fa-hand-holding-heart text-blue-600 text-2xl\"></i>
                    </div>
                    <h4 class=\"font-semibold text-gray-900 mb-2\">Health Benefits</h4>
                    <p class=\"text-gray-600\">Comprehensive healthcare coverage</p>
                </div>
            </div>
        </div>
    </div>

</section>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        gsap.from('.gsap-header', {
            duration: 1,
            y: 30,
            opacity: 0,
            ease: 'power3.out'
        });

        gsap.from('.gsap-team > *', {
            duration: 0.8,
            y: 20,
            opacity: 0,
            stagger: 0.2,
            ease: 'power3.out',
            delay: 0.3
        });

        gsap.from('.gsap-culture', {
            duration: 1,
            y: 30,
            opacity: 0,
            ease: 'power3.out',
            delay: 0.6
        });

        gsap.from('.gsap-benefits > *', {
            duration: 0.8,
            y: 20,
            opacity: 0,
            stagger: 0.2,
            ease: 'power3.out',
            delay: 0.9
        });
    });
</script>
<section class=\"min-h-screen bg-gradient-to-br from-cyan-950 to-blue-950 py-24 overflow-hidden\">
    <!-- Animated Background -->
    <div class=\"absolute inset-0\">
        <div class=\"absolute inset-0 bg-[radial-gradient(circle_800px_at_50%_-30%,rgba(34,211,238,0.15),transparent)]\">
        </div>
        <div class=\"absolute inset-0 bg-[radial-gradient(circle_800px_at_80%_60%,rgba(59,130,246,0.15),transparent)]\">
        </div>
        <!-- Particle Container -->
        <div id=\"particles-js\" class=\"absolute inset-0 opacity-30\"></div>
    </div>

    <div class=\"container mx-auto px-4 relative\">
        <!-- Header -->
        <div class=\"text-center max-w-3xl mx-auto mb-20\">
            <div class=\"relative inline-block\">
                <div
                    class=\"absolute -inset-4 bg-gradient-to-r from-cyan-500 to-blue-500 blur-lg opacity-20 animate-pulse\">
                </div>
                <h2
                    class=\"relative text-4xl md:text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-400 gsap-title\">
                    Success Timeline</h2>
            </div>
            <p class=\"mt-4 text-cyan-200/80\">Journey of growth with our clients</p>
        </div>

        <!-- Timeline Grid -->
        <div class=\"max-w-7xl mx-auto gsap-timeline\">
            <!-- Timeline Item 1 -->
            <div class=\"relative group mb-24\">
                <!-- Timeline Line -->
                <div class=\"absolute left-8 top-8 bottom-0 w-0.5 bg-gradient-to-b from-cyan-500/50 to-transparent\">
                </div>

                <!-- Timeline Dot -->
                <div class=\"absolute left-6 top-8 w-5 h-5\">
                    <div
                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur group-hover:blur-lg transition-all duration-300\">
                    </div>
                    <div class=\"relative w-full h-full bg-cyan-500 rounded-full\"></div>
                </div>

                <!-- Content Card -->
                <div class=\"ml-20 relative\">
                    <div
                        class=\"relative bg-white/5 backdrop-blur-xl rounded-3xl p-8 border border-white/10 transition-all duration-300 hover:bg-white/10\">
                        <!-- Glow Effect -->
                        <div
                            class=\"absolute -inset-px bg-gradient-to-r from-cyan-500 to-blue-500 rounded-3xl opacity-0 group-hover:opacity-20 blur transition-opacity\">
                        </div>
                        <div
                            class=\"absolute -inset-[2px] bg-gradient-to-r from-cyan-500/50 to-blue-500/50 rounded-3xl opacity-0 group-hover:opacity-100 group-hover:blur-sm transition-all duration-300\">
                        </div>

                        <div class=\"relative\">
                            <!-- Year Badge -->
                            <div
                                class=\"inline-flex items-center px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 mb-6\">
                                <span class=\"text-cyan-400 text-sm font-medium\">2024</span>
                            </div>

                            <!-- Content -->
                            <div class=\"mb-8\">
                                <h3 class=\"text-xl font-semibold text-white mb-4\">Revolutionary Impact</h3>
                                <p class=\"text-cyan-100/90 leading-relaxed\">\"The innovative solutions provided by the
                                    team have completely transformed our business operations. Their expertise and
                                    dedication to excellence have helped us achieve unprecedented growth.\"</p>
                            </div>

                            <!-- Metrics -->
                            <div class=\"grid grid-cols-2 md:grid-cols-4 gap-4 mb-8\">
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">300%</div>
                                    <div class=\"text-sm text-cyan-200/80\">Growth</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">95%</div>
                                    <div class=\"text-sm text-cyan-200/80\">Satisfaction</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">24/7</div>
                                    <div class=\"text-sm text-cyan-200/80\">Support</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">50+</div>
                                    <div class=\"text-sm text-cyan-200/80\">Features</div>
                                </div>
                            </div>

                            <!-- Author -->
                            <div class=\"flex items-center\">
                                <div class=\"relative w-12 h-12 mr-4\">
                                    <div
                                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur opacity-50\">
                                    </div>
                                    <img src=\"https://randomuser.me/api/portraits/women/13.jpg\" alt=\"Sarah Chen\"
                                        class=\"relative w-full h-full object-cover rounded-full border-2 border-white/10\">
                                </div>
                                <div>
                                    <h4 class=\"text-white font-semibold\">Sarah Chen</h4>
                                    <p class=\"text-cyan-300/80\">CTO, FutureScale</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Timeline Item 2 -->
            <div class=\"relative group mb-24\">
                <!-- Timeline Line -->
                <div class=\"absolute left-8 top-8 bottom-0 w-0.5 bg-gradient-to-b from-cyan-500/50 to-transparent\">
                </div>

                <!-- Timeline Dot -->
                <div class=\"absolute left-6 top-8 w-5 h-5\">
                    <div
                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur group-hover:blur-lg transition-all duration-300\">
                    </div>
                    <div class=\"relative w-full h-full bg-cyan-500 rounded-full\"></div>
                </div>

                <!-- Content Card -->
                <div class=\"ml-20 relative\">
                    <div
                        class=\"relative bg-white/5 backdrop-blur-xl rounded-3xl p-8 border border-white/10 transition-all duration-300 hover:bg-white/10\">
                        <!-- Glow Effect -->
                        <div
                            class=\"absolute -inset-px bg-gradient-to-r from-cyan-500 to-blue-500 rounded-3xl opacity-0 group-hover:opacity-20 blur transition-opacity\">
                        </div>
                        <div
                            class=\"absolute -inset-[2px] bg-gradient-to-r from-cyan-500/50 to-blue-500/50 rounded-3xl opacity-0 group-hover:opacity-100 group-hover:blur-sm transition-all duration-300\">
                        </div>

                        <div class=\"relative\">
                            <!-- Year Badge -->
                            <div
                                class=\"inline-flex items-center px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 mb-6\">
                                <span class=\"text-cyan-400 text-sm font-medium\">2023</span>
                            </div>

                            <!-- Content -->
                            <div class=\"mb-8\">
                                <h3 class=\"text-xl font-semibold text-white mb-4\">Strategic Partnership</h3>
                                <p class=\"text-cyan-100/90 leading-relaxed\">\"Their strategic insights and technical
                                    expertise have been instrumental in our digital transformation journey. The team's
                                    commitment to innovation has helped us stay ahead of the competition.\"</p>
                            </div>

                            <!-- Metrics -->
                            <div class=\"grid grid-cols-2 md:grid-cols-4 gap-4 mb-8\">
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">200%</div>
                                    <div class=\"text-sm text-cyan-200/80\">ROI</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">98%</div>
                                    <div class=\"text-sm text-cyan-200/80\">Uptime</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">1M+</div>
                                    <div class=\"text-sm text-cyan-200/80\">Users</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">30+</div>
                                    <div class=\"text-sm text-cyan-200/80\">Markets</div>
                                </div>
                            </div>

                            <!-- Author -->
                            <div class=\"flex items-center\">
                                <div class=\"relative w-12 h-12 mr-4\">
                                    <div
                                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur opacity-50\">
                                    </div>
                                    <img src=\"https://randomuser.me/api/portraits/men/14.jpg\" alt=\"David Park\"
                                        class=\"relative w-full h-full object-cover rounded-full border-2 border-white/10\">
                                </div>
                                <div>
                                    <h4 class=\"text-white font-semibold\">David Park</h4>
                                    <p class=\"text-cyan-300/80\">CEO, TechForward</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Timeline Item 3 -->
            <div class=\"relative group\">
                <!-- Timeline Dot -->
                <div class=\"absolute left-6 top-8 w-5 h-5\">
                    <div
                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur group-hover:blur-lg transition-all duration-300\">
                    </div>
                    <div class=\"relative w-full h-full bg-cyan-500 rounded-full\"></div>
                </div>

                <!-- Content Card -->
                <div class=\"ml-20 relative\">
                    <div
                        class=\"relative bg-white/5 backdrop-blur-xl rounded-3xl p-8 border border-white/10 transition-all duration-300 hover:bg-white/10\">
                        <!-- Glow Effect -->
                        <div
                            class=\"absolute -inset-px bg-gradient-to-r from-cyan-500 to-blue-500 rounded-3xl opacity-0 group-hover:opacity-20 blur transition-opacity\">
                        </div>
                        <div
                            class=\"absolute -inset-[2px] bg-gradient-to-r from-cyan-500/50 to-blue-500/50 rounded-3xl opacity-0 group-hover:opacity-100 group-hover:blur-sm transition-all duration-300\">
                        </div>

                        <div class=\"relative\">
                            <!-- Year Badge -->
                            <div
                                class=\"inline-flex items-center px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 mb-6\">
                                <span class=\"text-cyan-400 text-sm font-medium\">2022</span>
                            </div>

                            <!-- Content -->
                            <div class=\"mb-8\">
                                <h3 class=\"text-xl font-semibold text-white mb-4\">Transformative Solutions</h3>
                                <p class=\"text-cyan-100/90 leading-relaxed\">\"The team's ability to understand our unique
                                    challenges and deliver customized solutions has been remarkable. Their innovative
                                    approach has helped us achieve significant operational efficiency.\"</p>
                            </div>

                            <!-- Metrics -->
                            <div class=\"grid grid-cols-2 md:grid-cols-4 gap-4 mb-8\">
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">150%</div>
                                    <div class=\"text-sm text-cyan-200/80\">Efficiency</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">90%</div>
                                    <div class=\"text-sm text-cyan-200/80\">Cost Reduction</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">500K</div>
                                    <div class=\"text-sm text-cyan-200/80\">Transactions</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">20+</div>
                                    <div class=\"text-sm text-cyan-200/80\">Integrations</div>
                                </div>
                            </div>

                            <!-- Author -->
                            <div class=\"flex items-center\">
                                <div class=\"relative w-12 h-12 mr-4\">
                                    <div
                                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur opacity-50\">
                                    </div>
                                    <img src=\"https://randomuser.me/api/portraits/women/15.jpg\" alt=\"Emily Rodriguez\"
                                        class=\"relative w-full h-full object-cover rounded-full border-2 border-white/10\">
                                </div>
                                <div>
                                    <h4 class=\"text-white font-semibold\">Emily Rodriguez</h4>
                                    <p class=\"text-cyan-300/80\">COO, InnovateX</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</section>

<style>
    @keyframes pulse-glow {

        0%,
        100% {
            opacity: 0.2;
        }

        50% {
            opacity: 0.4;
        }
    }

    .animate-pulse-glow {
        animation: pulse-glow 4s ease-in-out infinite;
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        // Initialize Particles.js
        particlesJS('particles-js', {
            particles: {
                number: {
                    value: 50,
                    density: {
                        enable: true,
                        value_area: 800
                    }
                },
                color: {
                    value: '#22d3ee'
                },
                shape: {
                    type: 'circle'
                },
                opacity: {
                    value: 0.5,
                    random: true
                },
                size: {
                    value: 3,
                    random: true
                },
                line_linked: {
                    enable: true,
                    distance: 150,
                    color: '#22d3ee',
                    opacity: 0.2,
                    width: 1
                },
                move: {
                    enable: true,
                    speed: 2,
                    direction: 'none',
                    random: true,
                    straight: false,
                    out_mode: 'out',
                    bounce: false
                }
            },
            interactivity: {
                detect_on: 'canvas',
                events: {
                    onhover: {
                        enable: true,
                        mode: 'grab'
                    },
                    onclick: {
                        enable: true,
                        mode: 'push'
                    },
                    resize: true
                }
            },
            retina_detect: true
        });

        // GSAP Animations
        gsap.from('.gsap-title', {
            duration: 1,
            y: 40,
            opacity: 0,
            ease: 'back.out(1.7)'
        });

        gsap.from('.gsap-timeline > *', {
            duration: 1,
            x: -60,
            opacity: 0,
            stagger: 0.3,
            ease: 'back.out(1.2)'
        });
    });
</script>
<section class=\"relative py-24 bg-gray-50 overflow-hidden\">
    <!-- Decorative Elements -->
    <div class=\"absolute inset-0 bg-[radial-gradient(circle_at_top_right,_#E0F2FE,_transparent_40%)]\"></div>
    <div
        class=\"absolute right-0 top-1/2 -translate-y-1/2 w-1/3 aspect-square bg-gradient-to-br from-blue-500/10 to-purple-500/10 rounded-full blur-3xl\">
    </div>

    <div class=\"container mx-auto px-4 relative\">
        <div class=\"grid md:grid-cols-2 gap-12 items-center\">
            <!-- Left Content -->
            <div class=\"max-w-lg gsap-content\">
                <div class=\"inline-flex items-center gap-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-full mb-8\">
                    <i class=\"fas fa-sparkles text-sm\"></i>
                    <span class=\"text-sm font-medium\">Limited Time Offer</span>
                </div>

                <h2 class=\"text-4xl md:text-5xl font-bold text-gray-900 mb-6 leading-tight\">
                    Start Building Your Next Project Today
                </h2>
                <p class=\"text-xl text-gray-600 mb-8\">
                    Get 50% off on all premium templates and components. Create stunning websites faster than ever.
                </p>

                <div class=\"flex flex-wrap gap-4 mb-12\">
                    <a href=\"#\"
                        class=\"inline-flex items-center gap-2 bg-blue-600 text-white px-8 py-4 rounded-xl font-semibold hover:bg-blue-700 transition-colors duration-300 group\">
                        Get the Deal
                        <i class=\"fas fa-arrow-right transition-transform duration-300 group-hover:translate-x-1\"></i>
                    </a>
                    <a href=\"#\"
                        class=\"inline-flex items-center gap-2 text-gray-600 hover:text-blue-600 px-8 py-4 font-semibold transition-colors duration-300\">
                        Learn More
                    </a>
                </div>

                <!-- Testimonial -->
                <blockquote class=\"p-6 bg-white rounded-2xl shadow-sm border border-gray-100\">
                    <p class=\"text-gray-700 mb-4\">\"This platform has transformed how we build websites. The components
                        are beautiful and easy to customize.\"</p>
                    <footer class=\"flex items-center gap-4\">
                        <div class=\"w-12 h-12 rounded-full bg-gray-200 flex items-center justify-center\">
                            <i class=\"fas fa-user text-gray-500\"></i>
                        </div>
                        <div>
                            <div class=\"font-semibold text-gray-900\">Sarah Chen</div>
                            <div class=\"text-sm text-gray-500\">Lead Designer, Acme Inc</div>
                        </div>
                    </footer>
                </blockquote>
            </div>

            <!-- Right Image/Preview -->
            <div class=\"relative gsap-image\">
                <div class=\"aspect-[4/3] rounded-2xl bg-gradient-to-br from-blue-600 to-purple-600 p-1\">
                    <div class=\"h-full w-full rounded-xl bg-white p-8\">
                        <!-- Preview Content -->
                        <div class=\"grid gap-6\">
                            <div class=\"h-24 rounded-lg bg-gray-100 animate-pulse\"></div>
                            <div class=\"grid grid-cols-2 gap-4\">
                                <div class=\"h-32 rounded-lg bg-gray-100\"></div>
                                <div class=\"h-32 rounded-lg bg-gray-100\"></div>
                            </div>
                            <div class=\"h-12 w-1/2 rounded-lg bg-blue-100\"></div>
                        </div>
                    </div>
                </div>
                <!-- Floating Elements -->
                <div class=\"absolute -top-6 -right-6 w-24 h-24 rounded-xl bg-yellow-400 -rotate-6\"></div>
                <div class=\"absolute -bottom-6 -left-6 w-24 h-24 rounded-xl bg-blue-400 rotate-6\"></div>
            </div>
        </div>
    </div>

</section>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        gsap.from('.gsap-content', {
            duration: 1,
            x: -50,
            opacity: 0,
            ease: 'power3.out'
        });

        gsap.from('.gsap-image', {
            duration: 1,
            x: 50,
            opacity: 0,
            ease: 'power3.out',
            delay: 0.2
        });
    });
</script>

</body>
</html>
 ``

##

Products Page.html
`html

<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
     <!--PAID Tailwind CSS CDN -- DO NOT CHANGE -->
    <script src=\"https://cdn.tailwindcss.com\"></script>
    <!-- Font Awesome CDN  -- DO NOT CHANGE  -->
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css\" />
    <script src=https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js></script>
    <script src=\"https://cdn.jsdelivr.net/npm/framer-motion@11.15.0/dist/framer-motion.min.js\"></script>
    <title>Products Page</title>
</head>
<body>
<section>
  <header class=\"bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50\"
    x-data=\"{ isOpen: false, activeDropdown: null }\">
    <div class=\"container mx-auto flex justify-between items-center px-4 sm:px-6 lg:px-8 h-16\">
      <div class=\"flex items-center gap-8\">
        <a href=\"#\" class=\"text-2xl font-bold\" aria-label=\"Startup\">
          <span class=\"flex items-center gap-2\">
            <div class=\"w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center\">
              <i class=\"fas fa-bolt text-white\"></i>
            </div>
            <span class=\"text-gray-900 font-bold\">Startup</span>
          </span>
        </a>

        <nav class=\"hidden lg:flex items-center gap-6\">
          <a href=\"#product\"
            class=\"group relative text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\">
            <i class=\"fas fa-cube text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            Product
            <span
              class=\"absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-600 to-purple-600 group-hover:w-full transition-all duration-300\"></span>
          </a>
          <div class=\"relative\" @mouseleave=\"activeDropdown = null\">
            <button @mouseover=\"activeDropdown = 'solutions'\"
              @click=\"activeDropdown = activeDropdown === 'solutions' ? null : 'solutions'\"
              class=\"group text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\"
              aria-haspopup=\"true\" :aria-expanded=\"activeDropdown === 'solutions'\">
              <i class=\"fas fa-lightbulb text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
              Solutions
              <i class=\"fas fa-chevron-down text-xs transition-transform duration-200\"
                :class=\"{ 'rotate-180': activeDropdown === 'solutions' }\"></i>
            </button>
            <div x-show=\"activeDropdown === 'solutions'\" x-transition:enter=\"transition ease-out duration-200\"
              x-transition:enter-start=\"opacity-0 translate-y-1\" x-transition:enter-end=\"opacity-100 translate-y-0\"
              x-transition:leave=\"transition ease-in duration-150\" x-transition:leave-start=\"opacity-100 translate-y-0\"
              x-transition:leave-end=\"opacity-0 translate-y-1\"
              class=\"absolute left-0  w-80 bg-white rounded-lg shadow-lg ring-1 ring-black ring-opacity-5\">
              <div class=\"p-4 space-y-3\">
                <a href=\"#analytics\"
                  class=\"flex items-center gap-4 p-3 hover:bg-gray-50 rounded-lg group transition-colors duration-200\">
                  <div class=\"flex-shrink-0 w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center\">
                    <i
                      class=\"fas fa-chart-line text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
                  </div>
                  <div>
                    <h3 class=\"text-sm font-medium text-gray-900\">Analytics</h3>
                    <p class=\"text-xs text-gray-600\">Track your performance</p>
                  </div>
                </a>
                <a href=\"#automation\"
                  class=\"flex items-center gap-4 p-3 hover:bg-gray-50 rounded-lg group transition-colors duration-200\">
                  <div class=\"flex-shrink-0 w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center\">
                    <i class=\"fas fa-robot text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
                  </div>
                  <div>
                    <h3 class=\"text-sm font-medium text-gray-900\">Automation</h3>
                    <p class=\"text-xs text-gray-600\">Streamline workflows</p>
                  </div>
                </a>
                <a href=\"#integrations\"
                  class=\"flex items-center gap-4 p-3 hover:bg-gray-50 rounded-lg group transition-colors duration-200\">
                  <div class=\"flex-shrink-0 w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center\">
                    <i class=\"fas fa-plug text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
                  </div>
                  <div>
                    <h3 class=\"text-sm font-medium text-gray-900\">Integrations</h3>
                    <p class=\"text-xs text-gray-600\">Connect your tools</p>
                  </div>
                </a>
              </div>
            </div>
          </div>
          <a href=\"#pricing\"
            class=\"group relative text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\">
            <i class=\"fas fa-tag text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            Pricing
            <span
              class=\"absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-600 to-purple-600 group-hover:w-full transition-all duration-300\"></span>
          </a>
          <a href=\"#resources\"
            class=\"group relative text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\">
            <i class=\"fas fa-book text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            Resources
            <span
              class=\"absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-600 to-purple-600 group-hover:w-full transition-all duration-300\"></span>
          </a>
        </nav>
      </div>

      <div class=\"flex items-center gap-4\">
        <div class=\"hidden lg:flex items-center gap-4\">
          <a href=\"#login\"
            class=\"text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200\">Log in</a>
          <a href=\"#signup\"
            class=\"inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-colors duration-200 group\">
            Start Free Trial
            <i class=\"fas fa-arrow-right ml-2 group-hover:translate-x-1 transition-transform duration-200\"></i>
          </a>
        </div>

        <button type=\"button\" @click=\"isOpen = !isOpen\"
          class=\"lg:hidden p-2 rounded-md text-gray-700 hover:text-gray-900 hover:bg-gray-100 transition-colors duration-200\"
          :aria-expanded=\"isOpen\">
          <span class=\"sr-only\">Toggle menu</span>
          <i class=\"fas\" :class=\"isOpen ? 'fa-times' : 'fa-bars'\"></i>
        </button>
      </div>
    </div>

    <div x-show=\"isOpen\" x-transition:enter=\"transition ease-out duration-200\"
      x-transition:enter-start=\"opacity-0 -translate-y-1\" x-transition:enter-end=\"opacity-100 translate-y-0\"
      x-transition:leave=\"transition ease-in duration-150\" x-transition:leave-start=\"opacity-100 translate-y-0\"
      x-transition:leave-end=\"opacity-0 -translate-y-1\" class=\"lg:hidden\" role=\"dialog\" aria-modal=\"true\"
      style=\"display: none;\">
      <div class=\"fixed inset-0 bg-black bg-opacity-25\" @click=\"isOpen = false\"></div>
      <div class=\"fixed inset-y-0 right-0 w-full max-w-xs bg-white shadow-xl\">
        <div class=\"flex items-center justify-between px-4 py-5 border-b border-gray-200\">
          <span class=\"text-lg font-medium text-gray-900\">Menu</span>
          <button type=\"button\" @click=\"isOpen = false\"
            class=\"p-2 rounded-md text-gray-500 hover:text-gray-700 hover:bg-gray-100 transition-colors duration-200\">
            <i class=\"fas fa-times\"></i>
          </button>
        </div>
        <div class=\"px-2 py-3 space-y-1\">
          <a href=\"#product\"
            class=\"flex items-center gap-3 px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <i class=\"fas fa-cube w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            <span>Product</span>
          </a>
          <button @click=\"activeDropdown = activeDropdown === 'mobile-solutions' ? null : 'mobile-solutions'\"
            class=\"flex items-center justify-between w-full px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <div class=\"flex items-center gap-3\">
              <i
                class=\"fas fa-lightbulb w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
              <span>Solutions</span>
            </div>
            <i class=\"fas fa-chevron-down transition-transform duration-200\"
              :class=\"{ 'rotate-180': activeDropdown === 'mobile-solutions' }\"></i>
          </button>
          <div x-show=\"activeDropdown === 'mobile-solutions'\" class=\"pl-12 space-y-1\" style=\"display: none;\">
            <a href=\"#analytics\"
              class=\"block px-3 py-2 text-base font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150\">Analytics</a>
            <a href=\"#automation\"
              class=\"block px-3 py-2 text-base font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150\">Automation</a>
            <a href=\"#integrations\"
              class=\"block px-3 py-2 text-base font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150\">Integrations</a>
          </div>
          <a href=\"#pricing\"
            class=\"flex items-center gap-3 px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <i class=\"fas fa-tag w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            <span>Pricing</span>
          </a>
          <a href=\"#resources\"
            class=\"flex items-center gap-3 px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <i class=\"fas fa-book w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            <span>Resources</span>
          </a>
        </div>
        <div class=\"mt-auto border-t border-gray-200\">
          <div class=\"px-4 py-5 space-y-4\">
            <a href=\"#login\"
              class=\"block w-full px-4 py-2 text-center text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-200\">
              Sign in
            </a>
            <a href=\"#signup\"
              class=\"flex items-center justify-center px-4 py-2 text-base font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-colors duration-200 group\">
              Start Free Trial
              <i class=\"fas fa-arrow-right ml-2 group-hover:translate-x-1 transition-transform duration-200\"></i>
            </a>
          </div>
        </div>
      </div>
    </div>

  </header>

  <main class=\"container mx-auto grid grid-cols-1 md:grid-cols-3 gap-6 p-4\">
    <article
      class=\"flex flex-col md:flex-row bg-white shadow-md rounded-lg overflow-hidden hover:shadow-lg transition-shadow\">
      <img src=\"https://placehold.co/600x400/EEE/31343C\" alt=\"Article Image\" class=\"w-full md:w-1/3 object-cover\">
      <div class=\"p-4 flex flex-col justify-between\">
        <div>
          <h3 class=\"font-bold text-lg text-gray-800 hover:text-black transition-colors\">Article Title</h3>
          <p class=\"text-gray-600 mt-2\">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
        <a href=\"#\" class=\"mt-4 text-blue-500 hover:underline transition-colors\">Read more</a>
      </div>
    </article>
    <!-- Repeat the above block for more articles -->
  </main>
</section>
<script>
  document.getElementById('menu-button').addEventListener('click', function () {
    const menu = document.getElementById('mobile-menu');
    const expanded = this.getAttribute('aria-expanded') === 'true';
    this.setAttribute('aria-expanded', !expanded);
    menu.classList.toggle('hidden');
  });

document.getElementById('categories-button').addEventListener('click', function () {
const submenu = document.getElementById('categories-menu');
const expanded = this.getAttribute('aria-expanded') === 'true';
this.setAttribute('aria-expanded', !expanded);
submenu.classList.toggle('hidden');
this.querySelector('i').classList.toggle('fa-chevron-up');
this.querySelector('i').classList.toggle('fa-chevron-down');
});
</script>

<!DOCTYPE html>
<section
    class=\"min-h-screen bg-gradient-to-br from-indigo-900 to-purple-900 relative overflow-hidden py-20 font-['Inter']\">
    <!-- Content -->
    <div class=\"max-w-6xl mx-auto px-4\">
        <div class=\"text-center mb-16\">
            <h2 class=\"text-4xl font-bold text-white mb-4\">Website Solutions</h2>
            <p class=\"text-purple-200 max-w-2xl mx-auto\">Choose from our range of website design packages tailored for
                your online presence</p>
        </div>

        <div class=\"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8\">
            <!-- Basic Package -->
            <div class=\"bg-white/10 backdrop-blur-sm rounded-2xl p-8 hover:scale-105 transition-transform\">
                <div class=\"text-purple-300 mb-4\">
                    <svg class=\"w-12 h-12\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                            d=\"M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z\">
                        </path>
                    </svg>
                </div>
                <h3 class=\"text-2xl font-bold text-white mb-4\">Landing Page</h3>
                <ul class=\"space-y-3 text-purple-200 mb-8\">
                    <li>\u2022 Single page design</li>
                    <li>\u2022 Mobile responsive</li>
                    <li>\u2022 Contact form</li>
                    <li>\u2022 Basic SEO setup</li>
                </ul>
                <div class=\"text-3xl font-bold text-white mb-6\">$499</div>
                <button class=\"w-full py-3 bg-purple-600 hover:bg-purple-700 text-white rounded-xl transition-colors\">
                    Get Started
                </button>
            </div>

            <!-- Professional Package -->
            <div class=\"bg-white/10 backdrop-blur-sm rounded-2xl p-8 hover:scale-105 transition-transform\">
                <div class=\"text-purple-300 mb-4\">
                    <svg class=\"w-12 h-12\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                            d=\"M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10\">
                        </path>
                    </svg>
                </div>
                <h3 class=\"text-2xl font-bold text-white mb-4\">Business Website</h3>
                <ul class=\"space-y-3 text-purple-200 mb-8\">
                    <li>\u2022 Up to 5 pages</li>
                    <li>\u2022 Custom animations</li>
                    <li>\u2022 Image gallery</li>
                    <li>\u2022 Advanced SEO setup</li>
                </ul>
                <div class=\"text-3xl font-bold text-white mb-6\">$999</div>
                <button class=\"w-full py-3 bg-purple-600 hover:bg-purple-700 text-white rounded-xl transition-colors\">
                    Get Started
                </button>
            </div>

            <!-- Premium Package -->
            <div class=\"bg-white/10 backdrop-blur-sm rounded-2xl p-8 hover:scale-105 transition-transform\">
                <div class=\"text-purple-300 mb-4\">
                    <svg class=\"w-12 h-12\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                            d=\"M12 14l9-5-9-5-9 5 9 5z\"></path>
                        <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                            d=\"M12 14l9-5-9-5-9 5 9 5zm0 0L3 9m9 5l9-5\"></path>
                    </svg>
                </div>
                <h3 class=\"text-2xl font-bold text-white mb-4\">Portfolio Pro</h3>
                <ul class=\"space-y-3 text-purple-200 mb-8\">
                    <li>\u2022 Multi-page design</li>
                    <li>\u2022 Project showcases</li>
                    <li>\u2022 Blog section</li>
                    <li>\u2022 Social media integration</li>
                </ul>
                <div class=\"text-3xl font-bold text-white mb-6\">$1,499</div>
                <button class=\"w-full py-3 bg-purple-600 hover:bg-purple-700 text-white rounded-xl transition-colors\">
                    Get Started
                </button>
            </div>
        </div>
    </div>

</section>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        // Simple animation for buttons
        const buttons = document.querySelectorAll('button');
        buttons.forEach(button => {
            button.addEventListener('click', () => {
                alert('Thank you for your interest! We will contact you shortly.');
            });
        });
    });
</script>
<section class=\"py-24 bg-gray-50 relative overflow-hidden\" x-data=\"{ activeFeature: 1 }\">
    <!-- Decorative Background -->
    <div class=\"absolute inset-0\">
        <div class=\"absolute inset-0 bg-gradient-to-br from-gray-100 to-white\"></div>
        <div class=\"absolute inset-y-0 right-0 w-1/2 bg-gradient-to-l from-blue-50 to-transparent\"></div>
    </div>

    <div class=\"container mx-auto px-4 relative\">
        <!-- Section Header -->
        <div class=\"text-center max-w-2xl mx-auto mb-16\">
            <h2 class=\"text-3xl md:text-4xl font-bold text-gray-900 mb-4 gsap-title\">Platform Features</h2>
            <p class=\"text-gray-600 gsap-desc\">Click to explore our comprehensive feature set</p>
        </div>

        <!-- Accordion Features -->
        <div class=\"max-w-3xl mx-auto space-y-4\">
            <!-- Feature 1 -->
            <div class=\"group\" @click=\"activeFeature = activeFeature === 1 ? null : 1\">
                <div class=\"bg-white rounded-2xl shadow-sm hover:shadow-md transition-all duration-300 cursor-pointer\"
                    :class=\"{ 'ring-2 ring-blue-500': activeFeature === 1 }\">
                    <div class=\"p-6 flex items-center gap-4\">
                        <div
                            class=\"w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center flex-shrink-0 transition-transform duration-300 group-hover:scale-110\">
                            <i class=\"fas fa-paint-brush text-blue-600 text-xl\"></i>
                        </div>
                        <div class=\"flex-grow\">
                            <div class=\"flex items-center justify-between\">
                                <h3 class=\"text-lg font-semibold text-gray-900\">Visual Design Tools</h3>
                                <i class=\"fas fa-chevron-down text-gray-400 transform transition-transform duration-300\"
                                    :class=\"{ 'rotate-180': activeFeature === 1 }\"></i>
                            </div>
                            <p class=\"text-gray-600 mt-1\">Create stunning designs with our intuitive tools</p>
                        </div>
                    </div>
                    <div x-show=\"activeFeature === 1\" x-collapse x-cloak class=\"border-t border-gray-100\">
                        <div class=\"p-6 bg-gray-50\">
                            <div class=\"grid md:grid-cols-2 gap-6\">
                                <div class=\"space-y-4\">
                                    <h4 class=\"font-semibold text-gray-900\">Key Features</h4>
                                    <ul class=\"space-y-3\">
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-check text-blue-500\"></i>
                                            <span>Drag-and-drop interface</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-check text-blue-500\"></i>
                                            <span>Pre-built components</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-check text-blue-500\"></i>
                                            <span>Custom styling options</span>
                                        </li>
                                    </ul>
                                </div>
                                <div class=\"space-y-4\">
                                    <h4 class=\"font-semibold text-gray-900\">Benefits</h4>
                                    <ul class=\"space-y-3\">
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-star text-blue-500\"></i>
                                            <span>Save time with templates</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-star text-blue-500\"></i>
                                            <span>Professional results</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-star text-blue-500\"></i>
                                            <span>No coding required</span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Feature 2 -->
            <div class=\"group\" @click=\"activeFeature = activeFeature === 2 ? null : 2\">
                <div class=\"bg-white rounded-2xl shadow-sm hover:shadow-md transition-all duration-300 cursor-pointer\"
                    :class=\"{ 'ring-2 ring-green-500': activeFeature === 2 }\">
                    <div class=\"p-6 flex items-center gap-4\">
                        <div
                            class=\"w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center flex-shrink-0 transition-transform duration-300 group-hover:scale-110\">
                            <i class=\"fas fa-bolt text-green-600 text-xl\"></i>
                        </div>
                        <div class=\"flex-grow\">
                            <div class=\"flex items-center justify-between\">
                                <h3 class=\"text-lg font-semibold text-gray-900\">Performance Optimization</h3>
                                <i class=\"fas fa-chevron-down text-gray-400 transform transition-transform duration-300\"
                                    :class=\"{ 'rotate-180': activeFeature === 2 }\"></i>
                            </div>
                            <p class=\"text-gray-600 mt-1\">Lightning-fast loading speeds and optimization</p>
                        </div>
                    </div>
                    <div x-show=\"activeFeature === 2\" x-collapse x-cloak class=\"border-t border-gray-100\">
                        <div class=\"p-6 bg-gray-50\">
                            <div class=\"grid md:grid-cols-2 gap-6\">
                                <div class=\"space-y-4\">
                                    <h4 class=\"font-semibold text-gray-900\">Optimization Features</h4>
                                    <ul class=\"space-y-3\">
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-check text-green-500\"></i>
                                            <span>Image optimization</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-check text-green-500\"></i>
                                            <span>Code minification</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-check text-green-500\"></i>
                                            <span>Smart caching</span>
                                        </li>
                                    </ul>
                                </div>
                                <div class=\"space-y-4\">
                                    <h4 class=\"font-semibold text-gray-900\">Performance Stats</h4>
                                    <ul class=\"space-y-3\">
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-star text-green-500\"></i>
                                            <span>90+ PageSpeed score</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-star text-green-500\"></i>
                                            <span>50% faster loading</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-star text-green-500\"></i>
                                            <span>Global CDN delivery</span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Feature 3 -->
            <div class=\"group\" @click=\"activeFeature = activeFeature === 3 ? null : 3\">
                <div class=\"bg-white rounded-2xl shadow-sm hover:shadow-md transition-all duration-300 cursor-pointer\"
                    :class=\"{ 'ring-2 ring-purple-500': activeFeature === 3 }\">
                    <div class=\"p-6 flex items-center gap-4\">
                        <div
                            class=\"w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center flex-shrink-0 transition-transform duration-300 group-hover:scale-110\">
                            <i class=\"fas fa-mobile-alt text-purple-600 text-xl\"></i>
                        </div>
                        <div class=\"flex-grow\">
                            <div class=\"flex items-center justify-between\">
                                <h3 class=\"text-lg font-semibold text-gray-900\">Responsive Design</h3>
                                <i class=\"fas fa-chevron-down text-gray-400 transform transition-transform duration-300\"
                                    :class=\"{ 'rotate-180': activeFeature === 3 }\"></i>
                            </div>
                            <p class=\"text-gray-600 mt-1\">Perfect viewing experience on all devices</p>
                        </div>
                    </div>
                    <div x-show=\"activeFeature === 3\" x-collapse x-cloak class=\"border-t border-gray-100\">
                        <div class=\"p-6 bg-gray-50\">
                            <div class=\"grid md:grid-cols-2 gap-6\">
                                <div class=\"space-y-4\">
                                    <h4 class=\"font-semibold text-gray-900\">Design Features</h4>
                                    <ul class=\"space-y-3\">
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-check text-purple-500\"></i>
                                            <span>Mobile-first approach</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-check text-purple-500\"></i>
                                            <span>Flexible layouts</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-check text-purple-500\"></i>
                                            <span>Adaptive images</span>
                                        </li>
                                    </ul>
                                </div>
                                <div class=\"space-y-4\">
                                    <h4 class=\"font-semibold text-gray-900\">Device Support</h4>
                                    <ul class=\"space-y-3\">
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-star text-purple-500\"></i>
                                            <span>Desktop & laptops</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-star text-purple-500\"></i>
                                            <span>Tablets & iPads</span>
                                        </li>
                                        <li class=\"flex items-center gap-3 text-gray-600\">
                                            <i class=\"fas fa-star text-purple-500\"></i>
                                            <span>Mobile devices</span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</section>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        // GSAP Animations
        gsap.from('.gsap-title', {
            duration: 1,
            y: 30,
            opacity: 0,
            ease: 'power3.out'
        });

        gsap.from('.gsap-desc', {
            duration: 1,
            y: 30,
            opacity: 0,
            ease: 'power3.out',
            delay: 0.2
        });
    });
</script>
<section class=\"min-h-screen bg-gradient-to-br from-cyan-950 to-blue-950 py-24 overflow-hidden\">
    <!-- Animated Background -->
    <div class=\"absolute inset-0\">
        <div class=\"absolute inset-0 bg-[radial-gradient(circle_800px_at_50%_-30%,rgba(34,211,238,0.15),transparent)]\">
        </div>
        <div class=\"absolute inset-0 bg-[radial-gradient(circle_800px_at_80%_60%,rgba(59,130,246,0.15),transparent)]\">
        </div>
        <!-- Particle Container -->
        <div id=\"particles-js\" class=\"absolute inset-0 opacity-30\"></div>
    </div>

    <div class=\"container mx-auto px-4 relative\">
        <!-- Header -->
        <div class=\"text-center max-w-3xl mx-auto mb-20\">
            <div class=\"relative inline-block\">
                <div
                    class=\"absolute -inset-4 bg-gradient-to-r from-cyan-500 to-blue-500 blur-lg opacity-20 animate-pulse\">
                </div>
                <h2
                    class=\"relative text-4xl md:text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-400 gsap-title\">
                    Success Timeline</h2>
            </div>
            <p class=\"mt-4 text-cyan-200/80\">Journey of growth with our clients</p>
        </div>

        <!-- Timeline Grid -->
        <div class=\"max-w-7xl mx-auto gsap-timeline\">
            <!-- Timeline Item 1 -->
            <div class=\"relative group mb-24\">
                <!-- Timeline Line -->
                <div class=\"absolute left-8 top-8 bottom-0 w-0.5 bg-gradient-to-b from-cyan-500/50 to-transparent\">
                </div>

                <!-- Timeline Dot -->
                <div class=\"absolute left-6 top-8 w-5 h-5\">
                    <div
                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur group-hover:blur-lg transition-all duration-300\">
                    </div>
                    <div class=\"relative w-full h-full bg-cyan-500 rounded-full\"></div>
                </div>

                <!-- Content Card -->
                <div class=\"ml-20 relative\">
                    <div
                        class=\"relative bg-white/5 backdrop-blur-xl rounded-3xl p-8 border border-white/10 transition-all duration-300 hover:bg-white/10\">
                        <!-- Glow Effect -->
                        <div
                            class=\"absolute -inset-px bg-gradient-to-r from-cyan-500 to-blue-500 rounded-3xl opacity-0 group-hover:opacity-20 blur transition-opacity\">
                        </div>
                        <div
                            class=\"absolute -inset-[2px] bg-gradient-to-r from-cyan-500/50 to-blue-500/50 rounded-3xl opacity-0 group-hover:opacity-100 group-hover:blur-sm transition-all duration-300\">
                        </div>

                        <div class=\"relative\">
                            <!-- Year Badge -->
                            <div
                                class=\"inline-flex items-center px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 mb-6\">
                                <span class=\"text-cyan-400 text-sm font-medium\">2024</span>
                            </div>

                            <!-- Content -->
                            <div class=\"mb-8\">
                                <h3 class=\"text-xl font-semibold text-white mb-4\">Revolutionary Impact</h3>
                                <p class=\"text-cyan-100/90 leading-relaxed\">\"The innovative solutions provided by the
                                    team have completely transformed our business operations. Their expertise and
                                    dedication to excellence have helped us achieve unprecedented growth.\"</p>
                            </div>

                            <!-- Metrics -->
                            <div class=\"grid grid-cols-2 md:grid-cols-4 gap-4 mb-8\">
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">300%</div>
                                    <div class=\"text-sm text-cyan-200/80\">Growth</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">95%</div>
                                    <div class=\"text-sm text-cyan-200/80\">Satisfaction</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">24/7</div>
                                    <div class=\"text-sm text-cyan-200/80\">Support</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">50+</div>
                                    <div class=\"text-sm text-cyan-200/80\">Features</div>
                                </div>
                            </div>

                            <!-- Author -->
                            <div class=\"flex items-center\">
                                <div class=\"relative w-12 h-12 mr-4\">
                                    <div
                                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur opacity-50\">
                                    </div>
                                    <img src=\"https://randomuser.me/api/portraits/women/13.jpg\" alt=\"Sarah Chen\"
                                        class=\"relative w-full h-full object-cover rounded-full border-2 border-white/10\">
                                </div>
                                <div>
                                    <h4 class=\"text-white font-semibold\">Sarah Chen</h4>
                                    <p class=\"text-cyan-300/80\">CTO, FutureScale</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Timeline Item 2 -->
            <div class=\"relative group mb-24\">
                <!-- Timeline Line -->
                <div class=\"absolute left-8 top-8 bottom-0 w-0.5 bg-gradient-to-b from-cyan-500/50 to-transparent\">
                </div>

                <!-- Timeline Dot -->
                <div class=\"absolute left-6 top-8 w-5 h-5\">
                    <div
                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur group-hover:blur-lg transition-all duration-300\">
                    </div>
                    <div class=\"relative w-full h-full bg-cyan-500 rounded-full\"></div>
                </div>

                <!-- Content Card -->
                <div class=\"ml-20 relative\">
                    <div
                        class=\"relative bg-white/5 backdrop-blur-xl rounded-3xl p-8 border border-white/10 transition-all duration-300 hover:bg-white/10\">
                        <!-- Glow Effect -->
                        <div
                            class=\"absolute -inset-px bg-gradient-to-r from-cyan-500 to-blue-500 rounded-3xl opacity-0 group-hover:opacity-20 blur transition-opacity\">
                        </div>
                        <div
                            class=\"absolute -inset-[2px] bg-gradient-to-r from-cyan-500/50 to-blue-500/50 rounded-3xl opacity-0 group-hover:opacity-100 group-hover:blur-sm transition-all duration-300\">
                        </div>

                        <div class=\"relative\">
                            <!-- Year Badge -->
                            <div
                                class=\"inline-flex items-center px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 mb-6\">
                                <span class=\"text-cyan-400 text-sm font-medium\">2023</span>
                            </div>

                            <!-- Content -->
                            <div class=\"mb-8\">
                                <h3 class=\"text-xl font-semibold text-white mb-4\">Strategic Partnership</h3>
                                <p class=\"text-cyan-100/90 leading-relaxed\">\"Their strategic insights and technical
                                    expertise have been instrumental in our digital transformation journey. The team's
                                    commitment to innovation has helped us stay ahead of the competition.\"</p>
                            </div>

                            <!-- Metrics -->
                            <div class=\"grid grid-cols-2 md:grid-cols-4 gap-4 mb-8\">
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">200%</div>
                                    <div class=\"text-sm text-cyan-200/80\">ROI</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">98%</div>
                                    <div class=\"text-sm text-cyan-200/80\">Uptime</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">1M+</div>
                                    <div class=\"text-sm text-cyan-200/80\">Users</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">30+</div>
                                    <div class=\"text-sm text-cyan-200/80\">Markets</div>
                                </div>
                            </div>

                            <!-- Author -->
                            <div class=\"flex items-center\">
                                <div class=\"relative w-12 h-12 mr-4\">
                                    <div
                                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur opacity-50\">
                                    </div>
                                    <img src=\"https://randomuser.me/api/portraits/men/14.jpg\" alt=\"David Park\"
                                        class=\"relative w-full h-full object-cover rounded-full border-2 border-white/10\">
                                </div>
                                <div>
                                    <h4 class=\"text-white font-semibold\">David Park</h4>
                                    <p class=\"text-cyan-300/80\">CEO, TechForward</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Timeline Item 3 -->
            <div class=\"relative group\">
                <!-- Timeline Dot -->
                <div class=\"absolute left-6 top-8 w-5 h-5\">
                    <div
                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur group-hover:blur-lg transition-all duration-300\">
                    </div>
                    <div class=\"relative w-full h-full bg-cyan-500 rounded-full\"></div>
                </div>

                <!-- Content Card -->
                <div class=\"ml-20 relative\">
                    <div
                        class=\"relative bg-white/5 backdrop-blur-xl rounded-3xl p-8 border border-white/10 transition-all duration-300 hover:bg-white/10\">
                        <!-- Glow Effect -->
                        <div
                            class=\"absolute -inset-px bg-gradient-to-r from-cyan-500 to-blue-500 rounded-3xl opacity-0 group-hover:opacity-20 blur transition-opacity\">
                        </div>
                        <div
                            class=\"absolute -inset-[2px] bg-gradient-to-r from-cyan-500/50 to-blue-500/50 rounded-3xl opacity-0 group-hover:opacity-100 group-hover:blur-sm transition-all duration-300\">
                        </div>

                        <div class=\"relative\">
                            <!-- Year Badge -->
                            <div
                                class=\"inline-flex items-center px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 mb-6\">
                                <span class=\"text-cyan-400 text-sm font-medium\">2022</span>
                            </div>

                            <!-- Content -->
                            <div class=\"mb-8\">
                                <h3 class=\"text-xl font-semibold text-white mb-4\">Transformative Solutions</h3>
                                <p class=\"text-cyan-100/90 leading-relaxed\">\"The team's ability to understand our unique
                                    challenges and deliver customized solutions has been remarkable. Their innovative
                                    approach has helped us achieve significant operational efficiency.\"</p>
                            </div>

                            <!-- Metrics -->
                            <div class=\"grid grid-cols-2 md:grid-cols-4 gap-4 mb-8\">
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">150%</div>
                                    <div class=\"text-sm text-cyan-200/80\">Efficiency</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">90%</div>
                                    <div class=\"text-sm text-cyan-200/80\">Cost Reduction</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">500K</div>
                                    <div class=\"text-sm text-cyan-200/80\">Transactions</div>
                                </div>
                                <div class=\"text-center p-4 rounded-2xl bg-white/5\">
                                    <div class=\"text-2xl font-bold text-cyan-400\">20+</div>
                                    <div class=\"text-sm text-cyan-200/80\">Integrations</div>
                                </div>
                            </div>

                            <!-- Author -->
                            <div class=\"flex items-center\">
                                <div class=\"relative w-12 h-12 mr-4\">
                                    <div
                                        class=\"absolute inset-0 bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full blur opacity-50\">
                                    </div>
                                    <img src=\"https://randomuser.me/api/portraits/women/15.jpg\" alt=\"Emily Rodriguez\"
                                        class=\"relative w-full h-full object-cover rounded-full border-2 border-white/10\">
                                </div>
                                <div>
                                    <h4 class=\"text-white font-semibold\">Emily Rodriguez</h4>
                                    <p class=\"text-cyan-300/80\">COO, InnovateX</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</section>

<style>
    @keyframes pulse-glow {

        0%,
        100% {
            opacity: 0.2;
        }

        50% {
            opacity: 0.4;
        }
    }

    .animate-pulse-glow {
        animation: pulse-glow 4s ease-in-out infinite;
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        // Initialize Particles.js
        particlesJS('particles-js', {
            particles: {
                number: {
                    value: 50,
                    density: {
                        enable: true,
                        value_area: 800
                    }
                },
                color: {
                    value: '#22d3ee'
                },
                shape: {
                    type: 'circle'
                },
                opacity: {
                    value: 0.5,
                    random: true
                },
                size: {
                    value: 3,
                    random: true
                },
                line_linked: {
                    enable: true,
                    distance: 150,
                    color: '#22d3ee',
                    opacity: 0.2,
                    width: 1
                },
                move: {
                    enable: true,
                    speed: 2,
                    direction: 'none',
                    random: true,
                    straight: false,
                    out_mode: 'out',
                    bounce: false
                }
            },
            interactivity: {
                detect_on: 'canvas',
                events: {
                    onhover: {
                        enable: true,
                        mode: 'grab'
                    },
                    onclick: {
                        enable: true,
                        mode: 'push'
                    },
                    resize: true
                }
            },
            retina_detect: true
        });

        // GSAP Animations
        gsap.from('.gsap-title', {
            duration: 1,
            y: 40,
            opacity: 0,
            ease: 'back.out(1.7)'
        });

        gsap.from('.gsap-timeline > *', {
            duration: 1,
            x: -60,
            opacity: 0,
            stagger: 0.3,
            ease: 'back.out(1.2)'
        });
    });
</script>
<!DOCTYPE html>
<section
    class=\"min-h-screen bg-gradient-to-br from-violet-900 to-purple-900 relative overflow-hidden py-20 font-['Inter']\">
    <!-- Content -->
    <div class=\"max-w-6xl mx-auto px-4\">
        <div class=\"text-center mb-16\">
            <h2 class=\"text-4xl font-bold text-white mb-4\">Our Services</h2>
            <p class=\"text-violet-200 max-w-2xl mx-auto\">Hover over the cards to discover more details</p>
        </div>

        <div class=\"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8\">
            <!-- Landing Page Card -->
            <div class=\"flip-card h-[400px]\">
                <div class=\"flip-card-inner\">
                    <!-- Front -->
                    <div class=\"flip-card-front bg-white/10 backdrop-blur-sm rounded-2xl p-8\">
                        <div class=\"text-violet-300 mb-6\">
                            <svg class=\"w-16 h-16\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                                <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                                    d=\"M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6z\">
                                </path>
                            </svg>
                        </div>
                        <h3 class=\"text-2xl font-bold text-white mb-4\">Landing Page</h3>
                        <p class=\"text-violet-200 mb-4\">Perfect for showcasing a single product or service</p>
                        <div class=\"text-3xl font-bold text-white\">$499</div>
                    </div>
                    <!-- Back -->
                    <div class=\"flip-card-back bg-white/10 backdrop-blur-sm rounded-2xl p-8\">
                        <h4 class=\"text-xl font-bold text-white mb-6\">What's Included:</h4>
                        <ul class=\"space-y-3 text-violet-200 mb-8\">
                            <li>\u2022 Single page design</li>
                            <li>\u2022 Mobile responsive</li>
                            <li>\u2022 Contact form</li>
                            <li>\u2022 Basic SEO setup</li>
                            <li>\u2022 Fast loading speed</li>
                        </ul>
                        <button
                            class=\"w-full py-3 bg-violet-600 hover:bg-violet-700 text-white rounded-xl transition-colors\">
                            Get Started
                        </button>
                    </div>
                </div>
            </div>

            <!-- Business Website Card -->
            <div class=\"flip-card h-[400px]\">
                <div class=\"flip-card-inner\">
                    <!-- Front -->
                    <div class=\"flip-card-front bg-white/10 backdrop-blur-sm rounded-2xl p-8\">
                        <div class=\"text-violet-300 mb-6\">
                            <svg class=\"w-16 h-16\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                                <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                                    d=\"M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10\">
                                </path>
                            </svg>
                        </div>
                        <h3 class=\"text-2xl font-bold text-white mb-4\">Business Website</h3>
                        <p class=\"text-violet-200 mb-4\">Complete solution for your business presence</p>
                        <div class=\"text-3xl font-bold text-white\">$999</div>
                    </div>
                    <!-- Back -->
                    <div class=\"flip-card-back bg-white/10 backdrop-blur-sm rounded-2xl p-8\">
                        <h4 class=\"text-xl font-bold text-white mb-6\">What's Included:</h4>
                        <ul class=\"space-y-3 text-violet-200 mb-8\">
                            <li>\u2022 Up to 5 pages</li>
                            <li>\u2022 Custom design</li>
                            <li>\u2022 Image gallery</li>
                            <li>\u2022 Blog section</li>
                            <li>\u2022 Advanced SEO</li>
                        </ul>
                        <button
                            class=\"w-full py-3 bg-violet-600 hover:bg-violet-700 text-white rounded-xl transition-colors\">
                            Get Started
                        </button>
                    </div>
                </div>
            </div>

            <!-- Portfolio Website Card -->
            <div class=\"flip-card h-[400px]\">
                <div class=\"flip-card-inner\">
                    <!-- Front -->
                    <div class=\"flip-card-front bg-white/10 backdrop-blur-sm rounded-2xl p-8\">
                        <div class=\"text-violet-300 mb-6\">
                            <svg class=\"w-16 h-16\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                                <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"1.5\"
                                    d=\"M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z\">
                                </path>
                            </svg>
                        </div>
                        <h3 class=\"text-2xl font-bold text-white mb-4\">Portfolio Website</h3>
                        <p class=\"text-violet-200 mb-4\">Showcase your work with style</p>
                        <div class=\"text-3xl font-bold text-white\">$1,499</div>
                    </div>
                    <!-- Back -->
                    <div class=\"flip-card-back bg-white/10 backdrop-blur-sm rounded-2xl p-8\">
                        <h4 class=\"text-xl font-bold text-white mb-6\">What's Included:</h4>
                        <ul class=\"space-y-3 text-violet-200 mb-8\">
                            <li>\u2022 Project showcases</li>
                            <li>\u2022 Animations</li>
                            <li>\u2022 Case studies</li>
                            <li>\u2022 Testimonials</li>
                            <li>\u2022 Contact system</li>
                        </ul>
                        <button
                            class=\"w-full py-3 bg-violet-600 hover:bg-violet-700 text-white rounded-xl transition-colors\">
                            Get Started
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

</section>

<style>
    .flip-card {
        perspective: 1000px;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        transition: transform 0.6s;
        transform-style: preserve-3d;
    }

    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }

    .flip-card-front,
    .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
    }

    .flip-card-back {
        transform: rotateY(180deg);
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        // Simple animation for buttons
        const buttons = document.querySelectorAll('button');
        buttons.forEach(button => {
            button.addEventListener('click', () => {
                alert('Thank you for your interest! We will contact you shortly.');
            });
        });
    });
</script>

</body>
</html>
`

##

About & Contact Page.html
`` html

<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
     <!--PAID Tailwind CSS CDN -- DO NOT CHANGE -->
    <script src=\"https://cdn.tailwindcss.com\"></script>
    <!-- Font Awesome CDN  -- DO NOT CHANGE  -->
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css\" />
    <script src=https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js></script>
    <script src=\"https://cdn.jsdelivr.net/npm/framer-motion@11.15.0/dist/framer-motion.min.js\"></script>
    <title>About & Contact Page</title>
</head>
<body>
<section>
  <header class=\"bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50\"
    x-data=\"{ isOpen: false, activeDropdown: null }\">
    <div class=\"container mx-auto flex justify-between items-center px-4 sm:px-6 lg:px-8 h-16\">
      <div class=\"flex items-center gap-8\">
        <a href=\"#\" class=\"text-2xl font-bold\" aria-label=\"Startup\">
          <span class=\"flex items-center gap-2\">
            <div class=\"w-8 h-8 bg-indigo-600 rounded-lg flex items-center justify-center\">
              <i class=\"fas fa-bolt text-white\"></i>
            </div>
            <span class=\"text-gray-900 font-bold\">Startup</span>
          </span>
        </a>

        <nav class=\"hidden lg:flex items-center gap-6\">
          <a href=\"#product\"
            class=\"group relative text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\">
            <i class=\"fas fa-cube text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            Product
            <span
              class=\"absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-600 to-purple-600 group-hover:w-full transition-all duration-300\"></span>
          </a>
          <div class=\"relative\" @mouseleave=\"activeDropdown = null\">
            <button @mouseover=\"activeDropdown = 'solutions'\"
              @click=\"activeDropdown = activeDropdown === 'solutions' ? null : 'solutions'\"
              class=\"group text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\"
              aria-haspopup=\"true\" :aria-expanded=\"activeDropdown === 'solutions'\">
              <i class=\"fas fa-lightbulb text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
              Solutions
              <i class=\"fas fa-chevron-down text-xs transition-transform duration-200\"
                :class=\"{ 'rotate-180': activeDropdown === 'solutions' }\"></i>
            </button>
            <div x-show=\"activeDropdown === 'solutions'\" x-transition:enter=\"transition ease-out duration-200\"
              x-transition:enter-start=\"opacity-0 translate-y-1\" x-transition:enter-end=\"opacity-100 translate-y-0\"
              x-transition:leave=\"transition ease-in duration-150\" x-transition:leave-start=\"opacity-100 translate-y-0\"
              x-transition:leave-end=\"opacity-0 translate-y-1\"
              class=\"absolute left-0  w-80 bg-white rounded-lg shadow-lg ring-1 ring-black ring-opacity-5\">
              <div class=\"p-4 space-y-3\">
                <a href=\"#analytics\"
                  class=\"flex items-center gap-4 p-3 hover:bg-gray-50 rounded-lg group transition-colors duration-200\">
                  <div class=\"flex-shrink-0 w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center\">
                    <i
                      class=\"fas fa-chart-line text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
                  </div>
                  <div>
                    <h3 class=\"text-sm font-medium text-gray-900\">Analytics</h3>
                    <p class=\"text-xs text-gray-600\">Track your performance</p>
                  </div>
                </a>
                <a href=\"#automation\"
                  class=\"flex items-center gap-4 p-3 hover:bg-gray-50 rounded-lg group transition-colors duration-200\">
                  <div class=\"flex-shrink-0 w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center\">
                    <i class=\"fas fa-robot text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
                  </div>
                  <div>
                    <h3 class=\"text-sm font-medium text-gray-900\">Automation</h3>
                    <p class=\"text-xs text-gray-600\">Streamline workflows</p>
                  </div>
                </a>
                <a href=\"#integrations\"
                  class=\"flex items-center gap-4 p-3 hover:bg-gray-50 rounded-lg group transition-colors duration-200\">
                  <div class=\"flex-shrink-0 w-10 h-10 bg-indigo-100 rounded-lg flex items-center justify-center\">
                    <i class=\"fas fa-plug text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
                  </div>
                  <div>
                    <h3 class=\"text-sm font-medium text-gray-900\">Integrations</h3>
                    <p class=\"text-xs text-gray-600\">Connect your tools</p>
                  </div>
                </a>
              </div>
            </div>
          </div>
          <a href=\"#pricing\"
            class=\"group relative text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\">
            <i class=\"fas fa-tag text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            Pricing
            <span
              class=\"absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-600 to-purple-600 group-hover:w-full transition-all duration-300\"></span>
          </a>
          <a href=\"#resources\"
            class=\"group relative text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200 flex items-center gap-2\">
            <i class=\"fas fa-book text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            Resources
            <span
              class=\"absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-indigo-600 to-purple-600 group-hover:w-full transition-all duration-300\"></span>
          </a>
        </nav>
      </div>

      <div class=\"flex items-center gap-4\">
        <div class=\"hidden lg:flex items-center gap-4\">
          <a href=\"#login\"
            class=\"text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200\">Log in</a>
          <a href=\"#signup\"
            class=\"inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-colors duration-200 group\">
            Start Free Trial
            <i class=\"fas fa-arrow-right ml-2 group-hover:translate-x-1 transition-transform duration-200\"></i>
          </a>
        </div>

        <button type=\"button\" @click=\"isOpen = !isOpen\"
          class=\"lg:hidden p-2 rounded-md text-gray-700 hover:text-gray-900 hover:bg-gray-100 transition-colors duration-200\"
          :aria-expanded=\"isOpen\">
          <span class=\"sr-only\">Toggle menu</span>
          <i class=\"fas\" :class=\"isOpen ? 'fa-times' : 'fa-bars'\"></i>
        </button>
      </div>
    </div>

    <div x-show=\"isOpen\" x-transition:enter=\"transition ease-out duration-200\"
      x-transition:enter-start=\"opacity-0 -translate-y-1\" x-transition:enter-end=\"opacity-100 translate-y-0\"
      x-transition:leave=\"transition ease-in duration-150\" x-transition:leave-start=\"opacity-100 translate-y-0\"
      x-transition:leave-end=\"opacity-0 -translate-y-1\" class=\"lg:hidden\" role=\"dialog\" aria-modal=\"true\"
      style=\"display: none;\">
      <div class=\"fixed inset-0 bg-black bg-opacity-25\" @click=\"isOpen = false\"></div>
      <div class=\"fixed inset-y-0 right-0 w-full max-w-xs bg-white shadow-xl\">
        <div class=\"flex items-center justify-between px-4 py-5 border-b border-gray-200\">
          <span class=\"text-lg font-medium text-gray-900\">Menu</span>
          <button type=\"button\" @click=\"isOpen = false\"
            class=\"p-2 rounded-md text-gray-500 hover:text-gray-700 hover:bg-gray-100 transition-colors duration-200\">
            <i class=\"fas fa-times\"></i>
          </button>
        </div>
        <div class=\"px-2 py-3 space-y-1\">
          <a href=\"#product\"
            class=\"flex items-center gap-3 px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <i class=\"fas fa-cube w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            <span>Product</span>
          </a>
          <button @click=\"activeDropdown = activeDropdown === 'mobile-solutions' ? null : 'mobile-solutions'\"
            class=\"flex items-center justify-between w-full px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <div class=\"flex items-center gap-3\">
              <i
                class=\"fas fa-lightbulb w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
              <span>Solutions</span>
            </div>
            <i class=\"fas fa-chevron-down transition-transform duration-200\"
              :class=\"{ 'rotate-180': activeDropdown === 'mobile-solutions' }\"></i>
          </button>
          <div x-show=\"activeDropdown === 'mobile-solutions'\" class=\"pl-12 space-y-1\" style=\"display: none;\">
            <a href=\"#analytics\"
              class=\"block px-3 py-2 text-base font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150\">Analytics</a>
            <a href=\"#automation\"
              class=\"block px-3 py-2 text-base font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150\">Automation</a>
            <a href=\"#integrations\"
              class=\"block px-3 py-2 text-base font-medium text-gray-600 hover:text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150\">Integrations</a>
          </div>
          <a href=\"#pricing\"
            class=\"flex items-center gap-3 px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <i class=\"fas fa-tag w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            <span>Pricing</span>
          </a>
          <a href=\"#resources\"
            class=\"flex items-center gap-3 px-3 py-2 text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-150 group\">
            <i class=\"fas fa-book w-5 h-5 text-indigo-600 group-hover:scale-110 transition-transform duration-300\"></i>
            <span>Resources</span>
          </a>
        </div>
        <div class=\"mt-auto border-t border-gray-200\">
          <div class=\"px-4 py-5 space-y-4\">
            <a href=\"#login\"
              class=\"block w-full px-4 py-2 text-center text-base font-medium text-gray-900 hover:bg-gray-50 rounded-md transition-colors duration-200\">
              Sign in
            </a>
            <a href=\"#signup\"
              class=\"flex items-center justify-center px-4 py-2 text-base font-medium text-white bg-indigo-600 rounded-lg hover:bg-indigo-700 transition-colors duration-200 group\">
              Start Free Trial
              <i class=\"fas fa-arrow-right ml-2 group-hover:translate-x-1 transition-transform duration-200\"></i>
            </a>
          </div>
        </div>
      </div>
    </div>

  </header>

  <main class=\"container mx-auto grid grid-cols-1 md:grid-cols-3 gap-6 p-4\">
    <article
      class=\"flex flex-col md:flex-row bg-white shadow-md rounded-lg overflow-hidden hover:shadow-lg transition-shadow\">
      <img src=\"https://placehold.co/600x400/EEE/31343C\" alt=\"Article Image\" class=\"w-full md:w-1/3 object-cover\">
      <div class=\"p-4 flex flex-col justify-between\">
        <div>
          <h3 class=\"font-bold text-lg text-gray-800 hover:text-black transition-colors\">Article Title</h3>
          <p class=\"text-gray-600 mt-2\">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
        <a href=\"#\" class=\"mt-4 text-blue-500 hover:underline transition-colors\">Read more</a>
      </div>
    </article>
    <!-- Repeat the above block for more articles -->
  </main>
</section>
<script>
  document.getElementById('menu-button').addEventListener('click', function () {
    const menu = document.getElementById('mobile-menu');
    const expanded = this.getAttribute('aria-expanded') === 'true';
    this.setAttribute('aria-expanded', !expanded);
    menu.classList.toggle('hidden');
  });

document.getElementById('categories-button').addEventListener('click', function () {
const submenu = document.getElementById('categories-menu');
const expanded = this.getAttribute('aria-expanded') === 'true';
this.setAttribute('aria-expanded', !expanded);
submenu.classList.toggle('hidden');
this.querySelector('i').classList.toggle('fa-chevron-up');
this.querySelector('i').classList.toggle('fa-chevron-down');
});
</script>

<section class=\"py-24 bg-gray-900 overflow-hidden\">
    <!-- Decorative Background -->
    <div class=\"absolute inset-0\">
        <div class=\"absolute inset-0 bg-[linear-gradient(to_right,#4f46e5,#0ea5e9)] opacity-10\"></div>
        <div class=\"absolute inset-0 bg-[radial-gradient(circle_800px_at_100%_200px,#4f46e5,transparent)]\"></div>
    </div>

    <div class=\"container mx-auto px-4 relative\">
        <!-- Header -->
        <div class=\"max-w-3xl mx-auto text-center mb-20 gsap-header\">
            <div
                class=\"inline-flex items-center gap-2 bg-gray-800 text-blue-400 px-4 py-2 rounded-full mb-8 border border-gray-700/50\">
                <div class=\"w-2 h-2 rounded-full bg-blue-400 animate-pulse\"></div>
                <span class=\"text-sm font-medium\">Innovating Since 2020</span>
            </div>

            <h2 class=\"text-4xl md:text-6xl font-bold text-white mb-8 leading-tight\">
                Crafting Digital<br>Experiences That Matter
            </h2>
            <p class=\"text-xl text-gray-300\">
                We're a team of passionate creators, developers, and innovators dedicated to pushing the boundaries of
                what's possible in digital design.
            </p>
        </div>

        <!-- Image Grid -->
        <div class=\"grid lg:grid-cols-12 gap-8 mb-20 gsap-images\">
            <div class=\"lg:col-span-5\">
                <div class=\"relative aspect-[4/3]\">
                    <img src=\"https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&q=80\"
                        alt=\"Team Meeting\" class=\"absolute inset-0 w-full h-full object-cover rounded-2xl\">
                    <div class=\"absolute inset-0 rounded-2xl bg-gradient-to-tr from-blue-600/20 to-transparent\"></div>
                </div>
            </div>
            <div class=\"lg:col-span-7\">
                <div class=\"grid grid-cols-2 gap-8 h-full\">
                    <div class=\"relative aspect-[4/3]\">
                        <img src=\"https://images.unsplash.com/photo-1542744094-3a31f272c490?auto=format&fit=crop&q=80\"
                            alt=\"Office Space\" class=\"absolute inset-0 w-full h-full object-cover rounded-2xl\">
                        <div class=\"absolute inset-0 rounded-2xl bg-gradient-to-tr from-purple-600/20 to-transparent\">
                        </div>
                    </div>
                    <div class=\"relative aspect-[4/3]\">
                        <img src=\"https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&q=80\"
                            alt=\"Design Process\" class=\"absolute inset-0 w-full h-full object-cover rounded-2xl\">
                        <div class=\"absolute inset-0 rounded-2xl bg-gradient-to-tr from-cyan-600/20 to-transparent\">
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Values Grid -->
        <div class=\"grid md:grid-cols-3 gap-12 mb-20 gsap-values\">
            <div class=\"text-center\">
                <div class=\"w-16 h-16 bg-gray-800 rounded-2xl flex items-center justify-center mx-auto mb-6\">
                    <i class=\"fas fa-lightbulb text-blue-400 text-2xl\"></i>
                </div>
                <h3 class=\"text-xl font-semibold text-white mb-4\">Innovation</h3>
                <p class=\"text-gray-400\">
                    We're constantly pushing boundaries and exploring new possibilities in digital design and
                    technology.
                </p>
            </div>
            <div class=\"text-center\">
                <div class=\"w-16 h-16 bg-gray-800 rounded-2xl flex items-center justify-center mx-auto mb-6\">
                    <i class=\"fas fa-users text-blue-400 text-2xl\"></i>
                </div>
                <h3 class=\"text-xl font-semibold text-white mb-4\">Collaboration</h3>
                <p class=\"text-gray-400\">
                    Success comes from working together, sharing ideas, and building on each other's strengths.
                </p>
            </div>
            <div class=\"text-center\">
                <div class=\"w-16 h-16 bg-gray-800 rounded-2xl flex items-center justify-center mx-auto mb-6\">
                    <i class=\"fas fa-rocket text-blue-400 text-2xl\"></i>
                </div>
                <h3 class=\"text-xl font-semibold text-white mb-4\">Excellence</h3>
                <p class=\"text-gray-400\">
                    We're committed to delivering exceptional quality in everything we create and build.
                </p>
            </div>
        </div>

        <!-- Stats -->
        <div class=\"grid md:grid-cols-4 gap-8 gsap-stats\">
            <div class=\"bg-gray-800/50 rounded-2xl p-8 text-center backdrop-blur-sm border border-gray-700/50\">
                <div class=\"text-4xl font-bold text-white mb-2\">10K+</div>
                <div class=\"text-gray-400\">Active Users</div>
            </div>
            <div class=\"bg-gray-800/50 rounded-2xl p-8 text-center backdrop-blur-sm border border-gray-700/50\">
                <div class=\"text-4xl font-bold text-white mb-2\">98%</div>
                <div class=\"text-gray-400\">Satisfaction Rate</div>
            </div>
            <div class=\"bg-gray-800/50 rounded-2xl p-8 text-center backdrop-blur-sm border border-gray-700/50\">
                <div class=\"text-4xl font-bold text-white mb-2\">24/7</div>
                <div class=\"text-gray-400\">Expert Support</div>
            </div>
            <div class=\"bg-gray-800/50 rounded-2xl p-8 text-center backdrop-blur-sm border border-gray-700/50\">
                <div class=\"text-4xl font-bold text-white mb-2\">150+</div>
                <div class=\"text-gray-400\">Countries Served</div>
            </div>
        </div>
    </div>

</section>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        gsap.from('.gsap-header', {
            duration: 1,
            y: 30,
            opacity: 0,
            ease: 'power3.out'
        });

        gsap.from('.gsap-images > *', {
            duration: 1,
            y: 30,
            opacity: 0,
            stagger: 0.2,
            ease: 'power3.out',
            delay: 0.3
        });

        gsap.from('.gsap-values > *', {
            duration: 0.8,
            y: 20,
            opacity: 0,
            stagger: 0.2,
            ease: 'power3.out',
            delay: 0.6
        });

        gsap.from('.gsap-stats > *', {
            duration: 0.8,
            y: 20,
            opacity: 0,
            stagger: 0.2,
            ease: 'power3.out',
            delay: 0.9
        });
    });
</script>
<!DOCTYPE html>
<section class=\"py-20 bg-gradient-to-br from-gray-50 to-gray-100 relative overflow-hidden\">
    <!-- Decorative Background Elements -->
    <div class=\"absolute inset-0\">
        <div
            class=\"absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]\">
        </div>
        <div
            class=\"absolute right-0 bottom-0 w-96 h-96 bg-gradient-to-br from-blue-100/20 to-purple-100/20 rounded-full filter blur-3xl\">
        </div>
        <div
            class=\"absolute left-0 top-0 w-96 h-96 bg-gradient-to-br from-pink-100/20 to-indigo-100/20 rounded-full filter blur-3xl\">
        </div>
    </div>

    <!-- Content Container -->
    <div class=\"max-w-7xl mx-auto px-4 relative\">
        <!-- Header -->
        <div class=\"text-center mb-16\">
            <h2 class=\"text-4xl font-bold text-gray-900 mb-4\">Our Achievements</h2>
            <p class=\"text-gray-600 max-w-2xl mx-auto\">Celebrating milestones and recognition in our journey of
                excellence</p>
        </div>

        <!-- Achievement Grid -->
        <div class=\"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8\">
            <!-- Industry Awards -->
            <div class=\"group\" data-aos=\"fade-up\" data-aos-delay=\"100\">
                <div
                    class=\"bg-white rounded-2xl p-8 shadow-lg shadow-gray-200/50 transition-all duration-300 hover:shadow-xl hover:-translate-y-1\">
                    <div class=\"mb-6\">
                        <div class=\"w-12 h-12 bg-blue-500/10 rounded-xl flex items-center justify-center mb-4\">
                            <svg class=\"w-6 h-6 text-blue-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                                <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\"
                                    d=\"M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z\" />
                            </svg>
                        </div>
                        <h3 class=\"text-xl font-bold text-gray-900 mb-2\">Industry Awards</h3>
                        <p class=\"text-gray-600\">Recognized for excellence in innovation and customer satisfaction</p>
                    </div>
                    <div class=\"space-y-4\">
                        <div class=\"flex items-center justify-between\">
                            <span class=\"text-sm text-gray-500\">Best Innovation 2023</span>
                            <span class=\"text-sm font-medium text-blue-600\">Tech Awards</span>
                        </div>
                        <div class=\"flex items-center justify-between\">
                            <span class=\"text-sm text-gray-500\">Excellence in Design</span>
                            <span class=\"text-sm font-medium text-blue-600\">Design Week</span>
                        </div>
                        <div class=\"flex items-center justify-between\">
                            <span class=\"text-sm text-gray-500\">Top 10 Startups</span>
                            <span class=\"text-sm font-medium text-blue-600\">Forbes</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Growth Metrics -->
            <div class=\"group\" data-aos=\"fade-up\" data-aos-delay=\"200\">
                <div
                    class=\"bg-white rounded-2xl p-8 shadow-lg shadow-gray-200/50 transition-all duration-300 hover:shadow-xl hover:-translate-y-1\">
                    <div class=\"mb-6\">
                        <div class=\"w-12 h-12 bg-green-500/10 rounded-xl flex items-center justify-center mb-4\">
                            <svg class=\"w-6 h-6 text-green-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                                <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\"
                                    d=\"M13 7h8m0 0v8m0-8l-8 8-4-4-6 6\" />
                            </svg>
                        </div>
                        <h3 class=\"text-xl font-bold text-gray-900 mb-2\">Growth Metrics</h3>
                        <p class=\"text-gray-600\">Consistent growth and expansion across key metrics</p>
                    </div>
                    <div class=\"space-y-6\">
                        <div>
                            <div class=\"flex items-center justify-between mb-2\">
                                <span class=\"text-sm text-gray-500\">User Growth</span>
                                <span class=\"text-sm font-medium text-green-600\">85%</span>
                            </div>
                            <div class=\"h-2 bg-gray-100 rounded-full overflow-hidden\">
                                <div class=\"h-full bg-green-500 rounded-full\" style=\"width: 85%\"></div>
                            </div>
                        </div>
                        <div>
                            <div class=\"flex items-center justify-between mb-2\">
                                <span class=\"text-sm text-gray-500\">Revenue Growth</span>
                                <span class=\"text-sm font-medium text-green-600\">92%</span>
                            </div>
                            <div class=\"h-2 bg-gray-100 rounded-full overflow-hidden\">
                                <div class=\"h-full bg-green-500 rounded-full\" style=\"width: 92%\"></div>
                            </div>
                        </div>
                        <div>
                            <div class=\"flex items-center justify-between mb-2\">
                                <span class=\"text-sm text-gray-500\">Team Growth</span>
                                <span class=\"text-sm font-medium text-green-600\">78%</span>
                            </div>
                            <div class=\"h-2 bg-gray-100 rounded-full overflow-hidden\">
                                <div class=\"h-full bg-green-500 rounded-full\" style=\"width: 78%\"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Customer Success -->
            <div class=\"group\" data-aos=\"fade-up\" data-aos-delay=\"300\">
                <div
                    class=\"bg-white rounded-2xl p-8 shadow-lg shadow-gray-200/50 transition-all duration-300 hover:shadow-xl hover:-translate-y-1\">
                    <div class=\"mb-6\">
                        <div class=\"w-12 h-12 bg-purple-500/10 rounded-xl flex items-center justify-center mb-4\">
                            <svg class=\"w-6 h-6 text-purple-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                                <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\"
                                    d=\"M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5\" />
                            </svg>
                        </div>
                        <h3 class=\"text-xl font-bold text-gray-900 mb-2\">Customer Success</h3>
                        <p class=\"text-gray-600\">Delivering exceptional value and satisfaction to our clients</p>
                    </div>
                    <div class=\"space-y-4\">
                        <div class=\"flex items-center space-x-4\">
                            <div class=\"flex-1\">
                                <div class=\"text-2xl font-bold text-gray-900 mb-1\">98%</div>
                                <div class=\"text-sm text-gray-500\">Customer Satisfaction</div>
                            </div>
                            <div class=\"flex-1\">
                                <div class=\"text-2xl font-bold text-gray-900 mb-1\">24/7</div>
                                <div class=\"text-sm text-gray-500\">Support</div>
                            </div>
                        </div>
                        <div class=\"pt-4 border-t border-gray-100\">
                            <div class=\"flex items-center space-x-2 text-yellow-400\">
                                <svg class=\"w-5 h-5\" fill=\"currentColor\" viewBox=\"0 0 20 20\">
                                    <path
                                        d=\"M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z\" />
                                </svg>
                                <svg class=\"w-5 h-5\" fill=\"currentColor\" viewBox=\"0 0 20 20\">
                                    <path
                                        d=\"M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z\" />
                                </svg>
                                <svg class=\"w-5 h-5\" fill=\"currentColor\" viewBox=\"0 0 20 20\">
                                    <path
                                        d=\"M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z\" />
                                </svg>
                                <svg class=\"w-5 h-5\" fill=\"currentColor\" viewBox=\"0 0 20 20\">
                                    <path
                                        d=\"M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z\" />
                                </svg>
                                <svg class=\"w-5 h-5\" fill=\"currentColor\" viewBox=\"0 0 20 20\">
                                    <path
                                        d=\"M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z\" />
                                </svg>
                            </div>
                            <div class=\"text-sm text-gray-500 mt-2\">Based on 1,000+ reviews</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Bottom Stats -->
        <div class=\"mt-20 grid grid-cols-2 md:grid-cols-4 gap-8\">
            <div class=\"text-center\" data-aos=\"fade-up\" data-aos-delay=\"100\">
                <div class=\"text-4xl font-bold text-gray-900 mb-2\">50+</div>
                <div class=\"text-gray-600\">Awards Won</div>
            </div>
            <div class=\"text-center\" data-aos=\"fade-up\" data-aos-delay=\"200\">
                <div class=\"text-4xl font-bold text-gray-900 mb-2\">1M+</div>
                <div class=\"text-gray-600\">Happy Users</div>
            </div>
            <div class=\"text-center\" data-aos=\"fade-up\" data-aos-delay=\"300\">
                <div class=\"text-4xl font-bold text-gray-900 mb-2\">$100M+</div>
                <div class=\"text-gray-600\">Revenue Generated</div>
            </div>
            <div class=\"text-center\" data-aos=\"fade-up\" data-aos-delay=\"400\">
                <div class=\"text-4xl font-bold text-gray-900 mb-2\">30+</div>
                <div class=\"text-gray-600\">Countries Reached</div>
            </div>
        </div>
    </div>

</section>

<script src=\"https://unpkg.com/aos@next/dist/aos.js\"></script>
<script>
    document.addEventListener('DOMContentLoaded', function () {
        AOS.init({
            duration: 800,
            easing: 'ease-out',
            once: true
        });

        // Animate progress bars
        const progressBars = document.querySelectorAll('.bg-green-500');
        progressBars.forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0';
            setTimeout(() => {
                bar.style.width = width;
                bar.style.transition = 'width 1s ease-out';
            }, 500);
        });
    });
</script>

<style>
    [data-aos] {
        opacity: 0;
        transform: translateY(20px);
        transition-property: transform, opacity;
    }

    [data-aos].aos-animate {
        opacity: 1;
        transform: translateY(0);
    }

    .bg-green-500 {
        transition: width 1s ease-out;
    }
</style>
<section class=\"min-h-screen bg-gray-950 py-20 overflow-hidden\" x-data=\"{ activeTab: 'form' }\">
    <!-- Geometric Shapes -->
    <div class=\"absolute inset-0\">
        <!-- Neon Lines -->
        <div class=\"absolute inset-0\">
            <div
                class=\"absolute top-0 left-0 w-[1px] h-[300px] bg-gradient-to-b from-blue-500 to-transparent opacity-50\">
            </div>
            <div
                class=\"absolute top-[20%] left-[20%] w-[1px] h-[200px] bg-gradient-to-b from-purple-500 to-transparent opacity-50\">
            </div>
            <div
                class=\"absolute top-[10%] right-[30%] w-[1px] h-[400px] bg-gradient-to-b from-pink-500 to-transparent opacity-50\">
            </div>
        </div>
        <!-- Abstract Shapes -->
        <div class=\"absolute top-20 left-20 w-40 h-40 bg-blue-500/5 rounded-[3rem] rotate-45\"></div>
        <div class=\"absolute bottom-40 right-20 w-60 h-60 bg-purple-500/5 rounded-[4rem] -rotate-12\"></div>
        <div class=\"absolute top-1/2 left-1/3 w-80 h-80 bg-pink-500/5 rounded-full blur-3xl\"></div>
    </div>

    <div class=\"container mx-auto px-4 relative\">
        <!-- Header -->
        <div class=\"max-w-3xl mx-auto text-center mb-20 gsap-header\">
            <div
                class=\"inline-flex items-center gap-2 bg-white/5 text-white/90 px-4 py-2 rounded-full mb-8 backdrop-blur-sm border border-white/10\">
                <i class=\"fas fa-network-wired\"></i>
                <span class=\"text-sm font-medium\">Connect With Us</span>
            </div>
            <h2
                class=\"text-4xl md:text-6xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 mb-6\">
                Let's Build the Future<br>Together
            </h2>
            <p class=\"text-xl text-gray-400\">
                Ready to take the next step? Choose how you'd like to connect with us.
            </p>
        </div>

        <!-- Tab Navigation -->
        <div class=\"max-w-xl mx-auto mb-12\">
            <div class=\"flex items-center justify-center gap-4 gsap-tabs\">
                <button @click=\"activeTab = 'form'\"
                    :class=\"{ 'bg-white/10 border-purple-500': activeTab === 'form', 'bg-white/5 border-transparent hover:bg-white/10': activeTab !== 'form' }\"
                    class=\"flex-1 px-6 py-4 rounded-2xl border-2 transition-all duration-300\">
                    <div class=\"flex items-center justify-center gap-3\">
                        <i class=\"fas fa-paper-plane text-purple-500\"></i>
                        <span class=\"text-white font-medium\">Contact Form</span>
                    </div>
                </button>
                <button @click=\"activeTab = 'chat'\"
                    :class=\"{ 'bg-white/10 border-blue-500': activeTab === 'chat', 'bg-white/5 border-transparent hover:bg-white/10': activeTab !== 'chat' }\"
                    class=\"flex-1 px-6 py-4 rounded-2xl border-2 transition-all duration-300\">
                    <div class=\"flex items-center justify-center gap-3\">
                        <i class=\"fas fa-comments text-blue-500\"></i>
                        <span class=\"text-white font-medium\">Live Chat</span>
                    </div>
                </button>
            </div>
        </div>

        <!-- Content Container -->
        <div class=\"max-w-4xl mx-auto\">
            <!-- Contact Form -->
            <div x-show=\"activeTab === 'form'\" x-transition class=\"gsap-form\">
                <div class=\"relative bg-white/5 backdrop-blur-xl rounded-3xl p-8 border border-white/10\">
                    <div class=\"absolute inset-0 bg-gradient-to-br from-purple-500/5 to-pink-500/5 rounded-3xl\"></div>
                    <div class=\"relative space-y-6\">
                        <div class=\"grid md:grid-cols-2 gap-6\">
                            <div>
                                <label class=\"block text-white text-sm font-medium mb-2\">Name</label>
                                <input type=\"text\"
                                    class=\"w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all\">
                            </div>
                            <div>
                                <label class=\"block text-white text-sm font-medium mb-2\">Email</label>
                                <input type=\"email\"
                                    class=\"w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all\">
                            </div>
                        </div>
                        <div>
                            <label class=\"block text-white text-sm font-medium mb-2\">Subject</label>
                            <input type=\"text\"
                                class=\"w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all\">
                        </div>
                        <div>
                            <label class=\"block text-white text-sm font-medium mb-2\">Message</label>
                            <textarea rows=\"4\"
                                class=\"w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all resize-none\"></textarea>
                        </div>
                        <button
                            class=\"group relative w-full px-8 py-4 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-xl overflow-hidden transition-all hover:scale-105\">
                            <div
                                class=\"absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform\">
                            </div>
                            <span class=\"relative\">Send Message</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Live Chat -->
            <div x-show=\"activeTab === 'chat'\" x-transition class=\"gsap-chat\">
                <div class=\"relative bg-white/5 backdrop-blur-xl rounded-3xl p-8 border border-white/10\">
                    <div class=\"absolute inset-0 bg-gradient-to-br from-blue-500/5 to-purple-500/5 rounded-3xl\"></div>
                    <div class=\"relative\">
                        <div class=\"text-center py-12\">
                            <div
                                class=\"w-20 h-20 bg-blue-500/20 rounded-full flex items-center justify-center mx-auto mb-6\">
                                <i class=\"fas fa-robot text-blue-400 text-3xl\"></i>
                            </div>
                            <h3 class=\"text-2xl font-bold text-white mb-4\">Chat with Our AI Assistant</h3>
                            <p class=\"text-gray-400 mb-8\">
                                Get instant answers to your questions 24/7.<br>
                                Our AI assistant is here to help.
                            </p>
                            <button
                                class=\"group relative px-8 py-4 bg-gradient-to-r from-blue-500 to-purple-500 text-white rounded-xl overflow-hidden transition-all hover:scale-105\">
                                <div
                                    class=\"absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform\">
                                </div>
                                <span class=\"relative\">Start Chat</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Social Links -->
        <div class=\"max-w-2xl mx-auto mt-20\">
            <div class=\"grid grid-cols-4 gap-6 gsap-social\">
                <a href=\"#\" class=\"group\">
                    <div
                        class=\"relative bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10 hover:bg-white/10 transition-all\">
                        <div
                            class=\"absolute inset-0 bg-gradient-to-br from-blue-500/5 to-purple-500/5 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity\">
                        </div>
                        <div class=\"relative flex items-center justify-center\">
                            <i
                                class=\"fab fa-twitter text-2xl text-blue-400 group-hover:scale-125 transition-transform\"></i>
                        </div>
                    </div>
                </a>
                <a href=\"#\" class=\"group\">
                    <div
                        class=\"relative bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10 hover:bg-white/10 transition-all\">
                        <div
                            class=\"absolute inset-0 bg-gradient-to-br from-purple-500/5 to-pink-500/5 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity\">
                        </div>
                        <div class=\"relative flex items-center justify-center\">
                            <i
                                class=\"fab fa-instagram text-2xl text-purple-400 group-hover:scale-125 transition-transform\"></i>
                        </div>
                    </div>
                </a>
                <a href=\"#\" class=\"group\">
                    <div
                        class=\"relative bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10 hover:bg-white/10 transition-all\">
                        <div
                            class=\"absolute inset-0 bg-gradient-to-br from-pink-500/5 to-red-500/5 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity\">
                        </div>
                        <div class=\"relative flex items-center justify-center\">
                            <i
                                class=\"fab fa-linkedin text-2xl text-pink-400 group-hover:scale-125 transition-transform\"></i>
                        </div>
                    </div>
                </a>
                <a href=\"#\" class=\"group\">
                    <div
                        class=\"relative bg-white/5 backdrop-blur-sm rounded-2xl p-6 border border-white/10 hover:bg-white/10 transition-all\">
                        <div
                            class=\"absolute inset-0 bg-gradient-to-br from-red-500/5 to-orange-500/5 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity\">
                        </div>
                        <div class=\"relative flex items-center justify-center\">
                            <i
                                class=\"fab fa-github text-2xl text-red-400 group-hover:scale-125 transition-transform\"></i>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>

</section>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        // GSAP Animations
        gsap.from('.gsap-header', {
            duration: 1,
            y: 30,
            opacity: 0,
            ease: 'power3.out'
        });

        gsap.from('.gsap-tabs', {
            duration: 0.8,
            y: 20,
            opacity: 0,
            ease: 'power3.out',
            delay: 0.3
        });

        gsap.from('.gsap-form, .gsap-chat', {
            duration: 1,
            y: 50,
            opacity: 0,
            ease: 'power3.out',
            delay: 0.5
        });

        gsap.from('.gsap-social > *', {
            duration: 0.6,
            y: 20,
            opacity: 0,
            stagger: 0.1,
            ease: 'power3.out',
            delay: 0.8
        });
    });
</script>
<!DOCTYPE html>
<section class=\"py-20 bg-white relative overflow-hidden\" x-data=\"{ 
    activeFilter: 'all',
    partners: [
        { id: 1, name: 'Partner 1', category: 'technology' },
        { id: 2, name: 'Partner 2', category: 'finance' },
        { id: 3, name: 'Partner 3', category: 'healthcare' },
        { id: 4, name: 'Partner 4', category: 'technology' },
        { id: 5, name: 'Partner 5', category: 'finance' },
        { id: 6, name: 'Partner 6', category: 'healthcare' },
        { id: 7, name: 'Partner 7', category: 'technology' },
        { id: 8, name: 'Partner 8', category: 'finance' },
        { id: 9, name: 'Partner 9', category: 'healthcare' }
    ]
}\">
    <!-- Subtle Background Pattern -->
    <div class=\"absolute inset-0\">
        <div class=\"absolute inset-0 opacity-[0.02]\"
            style=\"background-image: radial-gradient(#000 1px, transparent 1px); background-size: 32px 32px;\"></div>
    </div>

    <!-- Content Container -->
    <div class=\"max-w-7xl mx-auto px-4 relative\">
        <!-- Header -->
        <div class=\"text-center mb-12\">
            <h2 class=\"text-3xl font-bold text-gray-900 mb-4\">Our Global Partners</h2>
            <p class=\"text-gray-600 max-w-2xl mx-auto mb-8\">Discover our network of industry-leading partners across
                various sectors</p>

            <!-- Category Filters -->
            <div class=\"flex flex-wrap justify-center gap-4 mb-12\">
                <button @click=\"activeFilter = 'all'\"
                    :class=\"{ 'bg-gray-900 text-white': activeFilter === 'all', 'bg-gray-100 text-gray-600 hover:bg-gray-200': activeFilter !== 'all' }\"
                    class=\"px-6 py-2 rounded-full text-sm font-medium transition-all duration-300\">
                    All Partners
                </button>
                <button @click=\"activeFilter = 'technology'\"
                    :class=\"{ 'bg-gray-900 text-white': activeFilter === 'technology', 'bg-gray-100 text-gray-600 hover:bg-gray-200': activeFilter !== 'technology' }\"
                    class=\"px-6 py-2 rounded-full text-sm font-medium transition-all duration-300\">
                    Technology
                </button>
                <button @click=\"activeFilter = 'finance'\"
                    :class=\"{ 'bg-gray-900 text-white': activeFilter === 'finance', 'bg-gray-100 text-gray-600 hover:bg-gray-200': activeFilter !== 'finance' }\"
                    class=\"px-6 py-2 rounded-full text-sm font-medium transition-all duration-300\">
                    Finance
                </button>
                <button @click=\"activeFilter = 'healthcare'\"
                    :class=\"{ 'bg-gray-900 text-white': activeFilter === 'healthcare', 'bg-gray-100 text-gray-600 hover:bg-gray-200': activeFilter !== 'healthcare' }\"
                    class=\"px-6 py-2 rounded-full text-sm font-medium transition-all duration-300\">
                    Healthcare
                </button>
            </div>
        </div>

        <!-- Masonry Grid -->
        <div class=\"grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8\">
            <template x-for=\"partner in partners\" :key=\"partner.id\">
                <div x-show=\"activeFilter === 'all' || activeFilter === partner.category\"
                    x-transition:enter=\"transition ease-out duration-300\"
                    x-transition:enter-start=\"opacity-0 transform translate-y-4\"
                    x-transition:enter-end=\"opacity-100 transform translate-y-0\" class=\"group\">
                    <div
                        class=\"relative bg-gray-50 rounded-2xl p-6 transition-all duration-300 hover:shadow-xl hover:-translate-y-1\">
                        <!-- Logo Container -->
                        <div class=\"aspect-[4/3] flex items-center justify-center\">
                            <!-- Replace with actual logo -->
                            <div class=\"text-gray-400 group-hover:text-gray-600 transition-colors\"
                                x-text=\"partner.name\"></div>
                        </div>

                        <!-- Category Badge -->
                        <div class=\"absolute top-4 right-4\">
                            <span class=\"px-3 py-1 text-xs font-medium rounded-full\" :class=\"{
                                    'bg-blue-100 text-blue-600': partner.category === 'technology',
                                    'bg-green-100 text-green-600': partner.category === 'finance',
                                    'bg-purple-100 text-purple-600': partner.category === 'healthcare'
                                }\" x-text=\"partner.category\">
                            </span>
                        </div>

                        <!-- Hover Overlay -->
                        <div
                            class=\"absolute inset-0 rounded-2xl bg-gradient-to-br from-gray-900/5 to-gray-900/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300\">
                        </div>
                    </div>
                </div>
            </template>
        </div>

        <!-- Partner Stats -->
        <div class=\"mt-20 grid grid-cols-1 md:grid-cols-3 gap-8\">
            <div class=\"relative group\">
                <div
                    class=\"bg-gray-50 rounded-2xl p-8 text-center transition-all duration-300 hover:shadow-xl hover:-translate-y-1\">
                    <div class=\"text-4xl font-bold text-gray-900 mb-2\">100+</div>
                    <div class=\"text-gray-600\">Technology Partners</div>
                </div>
            </div>
            <div class=\"relative group\">
                <div
                    class=\"bg-gray-50 rounded-2xl p-8 text-center transition-all duration-300 hover:shadow-xl hover:-translate-y-1\">
                    <div class=\"text-4xl font-bold text-gray-900 mb-2\">50+</div>
                    <div class=\"text-gray-600\">Financial Partners</div>
                </div>
            </div>
            <div class=\"relative group\">
                <div
                    class=\"bg-gray-50 rounded-2xl p-8 text-center transition-all duration-300 hover:shadow-xl hover:-translate-y-1\">
                    <div class=\"text-4xl font-bold text-gray-900 mb-2\">75+</div>
                    <div class=\"text-gray-600\">Healthcare Partners</div>
                </div>
            </div>
        </div>
    </div>

</section>

<style>
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .group {
        animation: fadeInUp 0.6s ease-out forwards;
        opacity: 0;
    }

    .group:nth-child(1) {
        animation-delay: 0.1s;
    }

    .group:nth-child(2) {
        animation-delay: 0.2s;
    }

    .group:nth-child(3) {
        animation-delay: 0.3s;
    }

    .group:nth-child(4) {
        animation-delay: 0.4s;
    }

    .group:nth-child(5) {
        animation-delay: 0.5s;
    }

    .group:nth-child(6) {
        animation-delay: 0.6s;
    }

    .group:nth-child(7) {
        animation-delay: 0.7s;
    }

    .group:nth-child(8) {
        animation-delay: 0.8s;
    }

    .group:nth-child(9) {
        animation-delay: 0.9s;
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        // Add intersection observer for animation on scroll
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.animationPlayState = 'running';
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1
        });

        document.querySelectorAll('.group').forEach(item => {
            item.style.animationPlayState = 'paused';
            observer.observe(item);
        });
    });
</script>
<!DOCTYPE html>
<section class=\"min-h-screen bg-white relative overflow-hidden py-20 font-['Inter']\">
    <!-- Minimal Background Pattern -->
    <div
        class=\"absolute inset-0 bg-[linear-gradient(90deg,#f3f4f6_1px,transparent_1px),linear-gradient(180deg,#f3f4f6_1px,transparent_1px)] bg-[size:48px_48px] opacity-30\">
    </div>

    <!-- Content Container -->
    <div class=\"max-w-3xl mx-auto px-4 relative\">
        <!-- Header -->
        <div class=\"text-center mb-16\">
            <span class=\"text-teal-600 text-sm font-medium tracking-wider uppercase mb-4 block\">Newsletter</span>
            <h2 class=\"text-4xl font-light text-gray-900 mb-6 tracking-tight\">Stay informed with our updates</h2>
            <div class=\"w-20 h-px bg-teal-500 mx-auto\"></div>
        </div>

        <!-- Newsletter Form -->
        <form class=\"space-y-6\" onsubmit=\"handleSubmit(event)\">
            <!-- Email Input -->
            <div class=\"relative group\">
                <label for=\"email\" class=\"block text-sm font-medium text-gray-700 mb-2 ml-1\">Email address</label>
                <input type=\"email\" id=\"email\" required
                    class=\"w-full px-6 py-4 bg-transparent border-2 border-gray-200 rounded-lg text-gray-800 placeholder-gray-400 outline-none transition-all duration-300 hover:border-gray-300 focus:border-teal-500\"
                    placeholder=\"you@example.com\">
            </div>

            <!-- Preferences -->
            <div class=\"flex items-center gap-8\">
                <label class=\"flex items-center gap-2 cursor-pointer group\">
                    <input type=\"checkbox\"
                        class=\"w-5 h-5 border-2 border-gray-200 rounded text-teal-500 focus:ring-teal-500 focus:ring-offset-0 transition-colors group-hover:border-gray-300\">
                    <span class=\"text-sm text-gray-600\">Weekly digest</span>
                </label>
                <label class=\"flex items-center gap-2 cursor-pointer group\">
                    <input type=\"checkbox\"
                        class=\"w-5 h-5 border-2 border-gray-200 rounded text-teal-500 focus:ring-teal-500 focus:ring-offset-0 transition-colors group-hover:border-gray-300\">
                    <span class=\"text-sm text-gray-600\">Breaking news</span>
                </label>
            </div>

            <!-- Submit Button -->
            <button type=\"submit\"
                class=\"w-full px-8 py-4 bg-gray-900 text-white font-medium rounded-lg hover:bg-gray-800 active:bg-gray-950 transition-colors duration-200\">
                Subscribe to newsletter
            </button>

            <!-- Privacy Notice -->
            <p class=\"text-center text-sm text-gray-500\">
                We respect your privacy. Read our <a href=\"#\"
                    class=\"text-teal-600 hover:text-teal-700 transition-colors\">Privacy Policy</a>
            </p>
        </form>

        <!-- Success Message (Hidden by default) -->
        <div id=\"success-message\" class=\"hidden mt-8 text-center\">
            <div class=\"inline-flex items-center justify-center w-16 h-16 rounded-full bg-teal-50 mb-4\">
                <svg class=\"w-8 h-8 text-teal-500\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\">
                    <path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M5 13l4 4L19 7\"></path>
                </svg>
            </div>
            <h3 class=\"text-xl font-medium text-gray-900 mb-2\">Thank you for subscribing!</h3>
            <p class=\"text-gray-600\">Please check your email to confirm your subscription.</p>
        </div>
    </div>

</section>

<script>
    function handleSubmit(event) {
        event.preventDefault();

        // Get form and success message elements
        const form = event.target;
        const successMessage = document.getElementById('success-message');

        // Disable form elements
        const inputs = form.querySelectorAll('input, button');
        inputs.forEach(input => input.disabled = true);

        // Add loading state to button
        const button = form.querySelector('button');
        const originalText = button.textContent;
        button.innerHTML = `
            <svg class=\"animate-spin -ml-1 mr-3 h-5 w-5 text-white inline-block\" xmlns=\"http://www.w3.org/2000/svg\" fill=\"none\" viewBox=\"0 0 24 24\">
                <circle class=\"opacity-25\" cx=\"12\" cy=\"12\" r=\"10\" stroke=\"currentColor\" stroke-width=\"4\"></circle>
                <path class=\"opacity-75\" fill=\"currentColor\" d=\"M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z\"></path>
            </svg>
            Processing...
        `;

        // Simulate API call
        setTimeout(() => {
            // Hide form with fade out
            form.style.opacity = '0';
            form.style.transform = 'translateY(-20px)';
            form.style.transition = 'all 0.5s ease-out';

            // Show success message with fade in
            setTimeout(() => {
                form.style.display = 'none';
                successMessage.style.display = 'block';
                successMessage.style.opacity = '0';
                successMessage.style.transform = 'translateY(20px)';

                requestAnimationFrame(() => {
                    successMessage.style.opacity = '1';
                    successMessage.style.transform = 'translateY(0)';
                    successMessage.style.transition = 'all 0.5s ease-out';
                });
            }, 500);
        }, 1500);
    }
</script>

</body>
</html>
