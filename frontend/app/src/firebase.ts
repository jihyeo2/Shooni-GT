import { initializeApp } from 'firebase/app'
import { getAuth, onAuthStateChanged } from 'firebase/auth'

const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID,
}

export const firebaseApp = initializeApp(firebaseConfig)
export const auth = getAuth(firebaseApp)

// Resolves once Firebase has reported its initial auth state (logged in or
// not). Firebase Auth persistence is checked asynchronously, so on a hard
// refresh `auth.currentUser` can briefly read `null` even for an already
// logged-in user. Anything that needs to make a redirect decision based on
// auth state (e.g. the router guard) must await this first, rather than
// trusting `auth.currentUser` or the Vuex store immediately.
export const authReadyPromise: Promise<void> = new Promise((resolve) => {
  const unsubscribe = onAuthStateChanged(auth, () => {
    unsubscribe()
    resolve()
  })
})
