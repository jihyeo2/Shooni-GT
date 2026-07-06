import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  base:'./',
  plugins: [vue()],
  // This project lives on a Windows-mounted drive under WSL2 (/mnt/d/...), where
  // Linux inotify often can't see file changes made from the Windows side, so
  // Vite's dev-server cache silently goes stale without polling.
  server: {
    watch: {
      usePolling: true,
    },
  },
})
