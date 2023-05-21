import { createWebHistory, createRouter } from 'vue-router';
import Home from "../views/Home.vue";
import Rent from "../views/Rent.vue";
import Filter from "../views/Filter.vue";
import Filter0 from "../views/Filter0.vue";
import Filter1 from "../views/Filter1.vue";
import Filter2 from "../views/Filter2.vue";
import FilterReview from "../views/FilterReview.vue";
import Search from "../views/Search.vue";
import About from "../views/About.vue";
import SignUp from '../views/SignUp.vue';
import PageNotFound from "../views/PageNotFound.vue";
import Review from '../views/Review.vue';
import ComingSoon from "../views/ComingSoon.vue";


const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
        meta: {
            title: 'Shooni',
            metaTags: [
                {
                    name: 'description',
                    content: 'The home page of Shooni.'
                  },
                  {
                    property: 'og:description',
                    content: 'The home page of Shooni.'
                  }
            ]
        }
    },
    {
        path: "/rent",
        name: "Rent",
        component: Rent,
        meta: {
            title: 'Rent - Shooni',
            metaTags: [
              {
                name: 'description',
                content: 'The rent page of Shooni.'
              },
              {
                property: 'og:description',
                content: 'The rent page of Shooni.'
              }
            ]
          },
    },
    {
        path: "/filter",
        name: "Filter",
        component: Filter,
        meta: {
            title: 'Filter - Shooni',
            metaTags: [
              {
                name: 'description',
                content: 'The filter page of Shooni.'
              },
              {
                property: 'og:description',
                content: 'The filter page of Shooni.'
              }
            ]
          },
        children: [
            {
              path: '',
              name: "Filter0",
              component: Filter0,
            },
            {
                path: "1",
                name: "Filter1",
                component: Filter1,
            },
            {
                path: "2",
                name: "Filter2",
                component: Filter2,
            },
            {
              path: "review",
              name: "FilterReview",
              component: FilterReview,
            }
        ]
    },
    {
      path: "/roommate",
      name: "Roommate",
      component: ComingSoon,
      meta: {
          title: 'Roommate - Shooni',
          metaTags: [
            {
              name: 'description',
              content: 'The roommate page of Shooni.'
            },
            {
              property: 'og:description',
              content: 'The roommate page of Shooni.'
            }
          ]
        },
    },
    {
        path: "/search",
        name: "Search",
        component: Search,
        meta: {
            title: 'Search - Shooni',
            metaTags: [
              {
                name: 'description',
                content: 'The search page of Shooni.'
              },
              {
                property: 'og:description',
                content: 'The search page of Shooni.'
              }
            ]
          },
    },
    {
        path: "/about",
        name: "About",
        component: About,
        meta: {
            title: 'About - Shooni',
            metaTags: [
              {
                name: 'description',
                content: 'The about page of Shooni.'
              },
              {
                property: 'og:description',
                content: 'The about page of Shooni.'
              }
            ]
          },
    },
    {
      path: "/signup",
      name: "SignUp",
      component: SignUp, 
      meta: {
        title: 'Sign up - Shooni',
        metaTags: [
          {
            name: 'description',
            content: 'The sign up page of Shooni.'
          },
          {
            property: 'og:description',
            content: 'The sign up page of Shooni.'
          }
        ]
      },
    },
    {
      path: "/review",
      name: "Review",
      component: Review, 
      meta: {
        title: 'Review - Shooni',
        metaTags: [
          {
            name: 'description',
            content: 'The review page of Shooni.'
          },
          {
            property: 'og:description',
            content: 'The review page of Shooni.'
          }
        ]
      },
    },
    {
        path:'/:catchAll(.*)*',
        name: "PageNotFound",
        component: PageNotFound,
        meta: {
            title: 'Page Not Found - Shooni',
            metaTags: [
              {
                name: 'description',
                content: 'The pagenotfound page of Shooni.'
              },
              {
                property: 'og:description',
                content: 'The pagenotfound page of Shooni.'
              }
            ]
          },
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});


// Navigation Guard
// referenced from https://www.digitalocean.com/community/tutorials/vuejs-vue-router-modify-head
// This callback runs before every route change, including on page load.
router.beforeEach((to, from, next) => {
    // This goes through the matched routes from last to first, finding the closest route with a title.
    // e.g., if we have `/some/deep/nested/route` and `/some`, `/deep`, and `/nested` have titles,
    // `/nested`'s will be chosen.
    const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);
  
    // Find the nearest route element with meta tags.
    const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);
  
    const previousNearestWithMeta = from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);
  
    // If a route with a title was found, set the document (page) title to that value.
    if(nearestWithTitle) {
      document.title = <string>nearestWithTitle.meta.title;
    } else if(previousNearestWithMeta) {
      document.title = <string>previousNearestWithMeta.meta.title;
    }
  
    // Remove any stale meta tags from the document using the key attribute we set below.
    Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => { if (el.parentNode) el.parentNode.removeChild(el)});
  
    // Skip rendering meta tags if there are none.
    if(!nearestWithMeta) return next();
  
    // Turn the meta tag definitions into actual elements in the head.
    (nearestWithMeta.meta.metaTags as Array<{ [x: string]: string; }>).map((tagDef: { [x: string]: string; }) => {
      const tag = document.createElement('meta');
  
      Object.keys(tagDef).forEach(key => {
        tag.setAttribute(key, tagDef[key]);
      });
  
      // We use this to track which meta tags we create so we don't interfere with other ones.
      tag.setAttribute('data-vue-router-controlled', '');
  
      return tag;
    })
    // Add the meta tags to the document head.
    .forEach((tag: any) => document.head.appendChild(tag));
  
    next();
  });

export default router;
